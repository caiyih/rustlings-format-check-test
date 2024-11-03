## Rustlings 作业

如果还没有接受作业，在 [作业列表](https://github.com/Loongson-neuq) 中找到 rustlings 作业的链接，打开并接受作业。网页会给你创建一个仓库，以及这个仓库的链接。点击链接打开仓库页面。

1. 在网络浏览器中用自己的 github id 登录 github.com。
2. 本仓库已经自动建立好，可以直接看到你要完成的实验了：
* 本地环境：
  1. **安装Linux的环境**。对于windows的用户，推荐使用wsl2安装Ubuntu 22.04，也可以使用vmware等虚拟机进行安装。如果在这一步存在问题，请联系助教。
  2. **本地安装rust**。进入linux环境下，参考 [第二周 Slides](https://loongson-neuq.pages.dev/p/os-week2-get-started-with-rust/) 中，找到Rust 开发环境配置的章节，相应配置即可，你可以同时将后续需要的环境也配置好.
  3. **clone实验仓库到本地**。在前面点击链接生成的仓库中，同样点击醒目的 `code` 绿色按钮，复制下面的链接。随后回到本地linux环境下，使用`git clone 复制的链接`的方式，将目标仓库clone到本地。随后，使用`ls`命令查看自己clone下来的文件夹，再使用`cd`命令进入到该文件夹下，使用  `cargo install --force --path .`  安装rustlings。
  4. **练习rustlings**。使用VSCode等编辑器，进入clone下来的目录中，执行`rustlings watch`依次查看完成情况，并依次完成对应的练习。 执行`rustlings run 练习名称`去运行对应练习，也可以使用`rustlings hint 练习名称`查看题解。
  5. **提交完成情况**。当做完部分或所有练习之后，在rustlings目录下执行 `git add .; git commit -m "update"; git push` 命令，把更新提交到GithubClassroom的CI进行自动评测。你可以在github仓库页面的actions分页看到你的CI评测过程。

**评测过程大约需要消耗 2 分钟，在评测结束后，你可以在 commit 的评论里或者 `grading-result` 分支的 `README.md` 内看到评测结果。**

3. 上述步骤有任何问题都可以找助教。

4. 下面是官方的Rustlings的布置，可以参考，**请务必不要拉取下面的仓库！**

 Rustlings 是长期作业，没有要求一周内完成。最慢根据每周要求完成对应的内容即可。如果你已经完成过，建议再做一遍，尽量争取 2 小时内能够完成前 101 个练习。

# rustlings 🦀❤️

</div>

Greetings and welcome to `rustlings`. This project contains small exercises to get you used to reading and writing Rust code. This includes reading and responding to compiler messages!

_...looking for the old, web-based version of Rustlings? Try [here](https://github.com/rust-lang/rustlings/tree/rustlings-1)_

Alternatively, for a first-time Rust learner, there are several other resources:

- [The Book](https://doc.rust-lang.org/book/index.html) - The most comprehensive resource for learning Rust, but a bit theoretical sometimes. You will be using this along with Rustlings!
- [Rust By Example](https://doc.rust-lang.org/rust-by-example/index.html) - Learn Rust by solving little exercises! It's almost like `rustlings`, but online

## Getting Started

_Note: If you're on MacOS, make sure you've installed Xcode and its developer tools by typing `xcode-select --install`._
_Note: If you're on Linux, make sure you've installed gcc. Deb: `sudo apt install gcc`. Yum: `sudo yum -y install gcc`._

You will need to have Rust installed. You can get it by visiting https://rustup.rs. This'll also install Cargo, Rust's package/project manager.

## MacOS/Linux

Just run:

```bash
curl -L https://raw.githubusercontent.com/rust-lang/rustlings/main/install.sh | bash
```
Or if you want it to be installed to a different path:

```bash
curl -L https://raw.githubusercontent.com/rust-lang/rustlings/main/install.sh | bash -s mypath/
```

This will install Rustlings and give you access to the `rustlings` command. Run it to get started!

### Nix

Basically: Clone the repository at the latest tag, finally run `nix develop` or `nix-shell`.

```bash
# find out the latest version at https://github.com/rust-lang/rustlings/releases/latest (on edit 5.5.1)
git clone -b 5.5.1 --depth 1 https://github.com/rust-lang/rustlings
cd rustlings
# if nix version > 2.3
nix develop
# if nix version <= 2.3
nix-shell
```

## Windows

In PowerShell (Run as Administrator), set `ExecutionPolicy` to `RemoteSigned`:

```ps1
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then, you can run:

```ps1
Start-BitsTransfer -Source https://raw.githubusercontent.com/rust-lang/rustlings/main/install.ps1 -Destination $env:TMP/install_rustlings.ps1; Unblock-File $env:TMP/install_rustlings.ps1; Invoke-Expression $env:TMP/install_rustlings.ps1
```

To install Rustlings. Same as on MacOS/Linux, you will have access to the `rustlings` command after it. Keep in mind that this works best in PowerShell, and any other terminals may give you errors.

If you get a permission denied message, you might have to exclude the directory where you cloned Rustlings in your antivirus.

## Browser

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/rust-lang/rustlings)

[![Open Rustlings On Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new/?repo=rust-lang%2Frustlings&ref=main)

## Manually

Basically: Clone the repository at the latest tag, run `cargo install --path .`.

```bash
# find out the latest version at https://github.com/rust-lang/rustlings/releases/latest (on edit 5.5.1)
git clone -b 5.5.1 --depth 1 https://github.com/rust-lang/rustlings
cd rustlings
cargo install --force --path .
```

If there are installation errors, ensure that your toolchain is up to date. For the latest, run:

```bash
rustup update
```

Then, same as above, run `rustlings` to get started.

## Doing exercises

The exercises are sorted by topic and can be found in the subdirectory `rustlings/exercises/<topic>`. For every topic there is an additional README file with some resources to get you started on the topic. We really recommend that you have a look at them before you start.

The task is simple. Most exercises contain an error that keeps them from compiling, and it's up to you to fix it! Some exercises are also run as tests, but rustlings handles them all the same. To run the exercises in the recommended order, execute:

```bash
rustlings watch
```

This will try to verify the completion of every exercise in a predetermined order (what we think is best for newcomers). It will also rerun automatically every time you change a file in the `exercises/` directory. If you want to only run it once, you can use:

```bash
rustlings verify
```

This will do the same as watch, but it'll quit after running.

In case you want to go by your own order, or want to only verify a single exercise, you can run:

```bash
rustlings run myExercise1
```

Or simply use the following command to run the next unsolved exercise in the course:

```bash
rustlings run next
```

In case you get stuck, you can run the following command to get a hint for your
exercise:

```bash
rustlings hint myExercise1
```

You can also get the hint for the next unsolved exercise with the following command:

```bash
rustlings hint next
```

To check your progress, you can run the following command:

```bash
rustlings list
```

## Testing yourself

After every couple of sections, there will be a quiz that'll test your knowledge on a bunch of sections at once. These quizzes are found in `exercises/quizN.rs`.

## Enabling `rust-analyzer`

Run the command `rustlings lsp` which will generate a `rust-project.json` at the root of the project, this allows [rust-analyzer](https://rust-analyzer.github.io/) to parse each exercise.

## Continuing On

Once you've completed Rustlings, put your new knowledge to good use! Continue practicing your Rust skills by building your own projects, contributing to Rustlings, or finding other open-source projects to contribute to.

## Uninstalling Rustlings

If you want to remove Rustlings from your system, there are two steps. First, you'll need to remove the exercises folder that the install script created
for you:

```bash
rm -rf rustlings # or your custom folder name, if you chose and or renamed it
```

Second, run `cargo uninstall` to remove the `rustlings` binary:

```bash
cargo uninstall rustlings
```

Now you should be done!

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md).

Development-focused discussion about Rustlings happens in the [**rustlings** stream](https://rust-lang.zulipchat.com/#narrow/stream/334454-rustlings)
on the [Rust Project Zulip](https://rust-lang.zulipchat.com). Feel free to start a new thread there
if you have ideas or suggestions!

## Contributors ✨

Thanks goes to the wonderful people listed in [AUTHORS.md](./AUTHORS.md) 🎉
