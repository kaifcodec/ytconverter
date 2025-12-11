from ytconverter.utils.styling import apply_style

f1 = r"""
     __   _______ ____                          _
     \ \ / /_   _/ ___|___  _ ____   _____ _ __| |_ ___ _ __
      \ V /  | || |   / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
       | |   | || |__| (_) | | | \ V /  __/ |  | ||  __/ |
       |_|   |_| \____\___/|_| |_|\_/ \___|_|   \__\___|_|"""
f2 = """
      ╔════════════════════════════════════════╗
      ║ ♚ Project Name : YTConverter™          ║
      ║ ♚ Author : Kaif                        ║
      ║ ♚ Github : github.com/kaifcodec        ║
      ║ ♚ Email  : kaifcodec@gmail.com         ║
      ╠═════════════════════════════════════════ """
f3 = """      ╠═▶ [𝗦𝗲𝗹𝗲𝗰𝘁 𝗔n  𝐎𝐩𝐭𝐢𝐨𝐧]  ➳
      ╠═▶ 1. Single Music Mp3 ⏬ 🎶
      ╠═▶ 2. Single Video ⏬ 🎥(detailed quailty & size but slow fetch)
      ╠═▶ 3. Multiple videos ⏬ 🎥
      ╠═▶ 4. Multiple audios ⏬ 🎶
      ╠═▶ 5. Exit YTConverter"""
f4 = "      ╚═:➤ "

des1 = apply_style(f1, "/green/bold")
des2 = apply_style(f2, "/yellow")
des3 = apply_style(f3, "/cyan")
des4 = apply_style(f4, "/cyan")


def print_banner(version: str):
    print(f"{des1}  Version: {version}")
    print(des2)
    print(des3)
