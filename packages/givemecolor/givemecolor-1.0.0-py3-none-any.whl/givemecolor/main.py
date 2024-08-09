import random
import sys
import subprocess


def givemecolor():
    # Generate random values for red, green, and blue components
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    # Convert decimal to hexadecimal format
    red_hex = f"{red:02x}"
    green_hex = f"{green:02x}"
    blue_hex = f"{blue:02x}"

    # Calculate luminance
    luminance = (0.299 * red + 0.587 * green + 0.114 * blue) / 255

    # Determine luminance color
    lum_color = "0;0;0" if luminance > 0.5 else "255;255;255"

    # Concatenate the components to form the color code
    color = f"#{red_hex}{green_hex}{blue_hex}"

    # Copy to clipboard
    copy_to_clipboard(color)

    # Print the color
    print(f"\033[48;2;{red};{green};{blue}m\033[38;2;{lum_color}m{color}\033[0m")


def copy_to_clipboard(color):
    # Determine the platform
    if sys.platform == "win32":
        # Windows
        subprocess.run(f"echo {color.strip()} | clip", shell=True)
    else:
        # macOS and Linux
        subprocess.run(f"echo -n {color.strip()} | pbcopy", shell=True)


if __name__ == "__main__":
    givemecolor()
