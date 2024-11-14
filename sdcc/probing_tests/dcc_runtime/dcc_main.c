//
// C code to intercept runtime errors and run this program
//

#undef _exit
#undef close
#undef execvp
#undef getpid
#undef lseek
#undef pipe
#undef read
#undef sleep
#undef unlink
#undef write

#define ADDRESS 1
#define MEMORY 2
#define VALGRIND 3

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#ifdef __linux__
#include <sys/prctl.h>
#endif

#if __has_attribute(no_sanitize)
#ifdef __clang__
#define NO_SANITIZE                                                            \
  __attribute__((no_sanitize("address", "memory", "undefined")))
#else
#define NO_SANITIZE __attribute__((no_sanitize("address", "undefined")))
#endif
#else
#define NO_SANITIZE
#endif

int main(int argc, char *argv[], char *envp[]) NO_SANITIZE;
int __real_main(int argc, char *argv[]);

// static void __dcc_start(void) __attribute__((constructor)) NO_SANITIZE;
static void __dcc_start(void) NO_SANITIZE;
void __dcc_error_exit(void) NO_SANITIZE;
static void __dcc_signal_handler(int signum) NO_SANITIZE;
static void set_signals_default(void) NO_SANITIZE;
static void launch_valgrind(int argc, char *argv[]) NO_SANITIZE;
static void setenvd_int(const char *n, int v) NO_SANITIZE;
static void setenvd(const char *n, const char *v) NO_SANITIZE;
static void putenvd(const char *s) NO_SANITIZE;
static void _explain_error(void) NO_SANITIZE;
static void clear_stack(void) NO_SANITIZE;
static void quick_clear_stack(void) NO_SANITIZE;
static int __dcc_run_sanitizer1(int argc, char *argv[]);

#undef main

//
// any function which might appear in a user call stack
// should be prefaced with __dcc_ so it won't displayed in explanations
//

int main(int argc, char *argv[], char *envp[]) {
  __dcc_start();
  (void)envp; // avoid unused parameter warning
  char *mypath = realpath(argv[0], NULL);
  if (mypath) {
    setenvd("DCC_BINARY", mypath);
    free(mypath);
  }
  return __dcc_run_sanitizer1(argc, argv);
}

static int __dcc_run_sanitizer1(int argc, char *argv[]) {
  printf("__real_main is about to run\n");
  int r = __real_main(argc, argv);
  printf("__real_main returning %d\n", r);
  return r;
}

static void __dcc_start(void) {
  setenvd("DCC_SANITIZER", "__SANITIZER__");
  setenvd("DCC_PATH", "__PATH__");
  setenvd_int("DCC_PID", getpid());

  signal(SIGABRT, __dcc_signal_handler);
  signal(SIGSEGV, __dcc_signal_handler);
  signal(SIGINT, __dcc_signal_handler);
  signal(SIGXCPU, __dcc_signal_handler);
  signal(SIGXFSZ, __dcc_signal_handler);
  signal(SIGFPE, __dcc_signal_handler);
  signal(SIGILL, __dcc_signal_handler);
}

static void __dcc_signal_handler(int signum) {
  printf("received signal %d\n", signum);
  set_signals_default();

  char signum_buffer[64];
  snprintf(signum_buffer, sizeof signum_buffer, "DCC_SIGNAL=%d", (int)signum);
  putenvd(signum_buffer); // less likely? to trigger another error than direct
                          // setenv

  // _explain_error();

  // not reached
}

static void setenvd(const char *n, const char *v) {
  setenv(n, v, 1);
  printf("setenv %s=%s\n", n, v);
}

static void setenvd_int(const char *n, int v) {
  char buffer[64] = {0};
  snprintf(buffer, sizeof buffer, "%d", v);
  setenvd(n, buffer);
}

static void putenvd(const char *s) {
  putenv((char *)s);
  printf("putenv '%s'\n", s);
}

static void set_signals_default(void) {
  printf("set_signals_default()\n");
  signal(SIGABRT, SIG_DFL);
  signal(SIGSEGV, SIG_DFL);
  signal(SIGINT, SIG_DFL);
  signal(SIGXCPU, SIG_DFL);
  signal(SIGXFSZ, SIG_DFL);
  signal(SIGFPE, SIG_DFL);
  signal(SIGILL, SIG_DFL);
}

// static const char *run_tar_file =
//     "PATH=$PATH:/bin:/usr/bin:/usr/local/bin exec python3 -B -E -c \"import
//     io,os,sys,tarfile,tempfile\n \
// with tempfile.TemporaryDirectory() as temp_dir:\n\
//   buffer = io.BytesIO(sys.stdin.buffer.raw.read())\n\
//   buffer_length = len(buffer.getbuffer())\n\
//   if not buffer_length:\n\
//     sys.exit(1)\n\
//   k = {'filter':'data'} if hasattr(tarfile, 'data_filter') else {}\n\
//   tarfile.open(fileobj=buffer, bufsize=buffer_length,
//   mode='r|xz').extractall(temp_dir, **k)\n\
//   os.environ['DCC_PWD'] = os.getcwd()\n\
//   os.chdir(temp_dir)\n\
//   exec(open('start_gdb.py').read())\n\
// \"";
//
// static void _explain_error(void) {
//     // if a program has exhausted file descriptors then we need to close some
//     to run gdb etc,
//     // so as a precaution we close a pile of file descriptors which may or
//     may not be open for (int i = 4; i < 32; i++) {
//         close(i);
//     }
//
// #ifdef __linux__
//     // ensure gdb can ptrace binary
//     // https://www.kernel.org/doc/Documentation/security/Yama.txt
//     prctl(PR_SET_PTRACER, PR_SET_PTRACER_ANY);
// #endif
//
//     debug_printf(2, "running %s\n", run_tar_file);
//     FILE *python_pipe = popen(run_tar_file, "w");
//     size_t n_items = sizeof tar_data / sizeof tar_data[0];
//     size_t items_written =
//         fwrite(tar_data, sizeof tar_data[0], n_items, python_pipe);
//     if (items_written != n_items) {
//         debug_printf(1, "fwrite bad return %d returned %d expected\n",
//                      (int)items_written, (int)n_items);
//     }
//     pclose(python_pipe);
//     __dcc_error_exit();
// }
//
// void __dcc_error_exit(void) {
//     debug_printf(2, "__dcc_error_exit()\n");
//
//     // use kill instead of exit or _exit because
//     // exit or _exit keeps executing sanitizer code - including perhaps
//     superfluous output
//     // but not with valgrind which will catch signal and start gdb
//     // SIGPIPE avoids killed message from bash
//     // signal(SIGPIPE, SIG_DFL);
//     // kill(getpid(), SIGPIPE);
//
//     _exit(1);
// }
