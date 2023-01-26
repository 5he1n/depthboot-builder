import build


def print_header(message: str) -> None:
    print("\033[95m" + message + "\033[0m", flush=True)


def print_error(message: str) -> None:
    print("\033[91m" + message + "\033[0m", flush=True)


if __name__ == "__main__":
    print_header("Starting Debian tests")

    testing_dict = {
        "distro_name": "debian",
        "distro_version": "",
        "de_name": "",
        "username": "localuser",
        "password": "test",
        "device": "image",
        "kernel_type": "mainline"
    }
    available_des = ["gnome", "kde", "xfce", "lxqt", "budgie", "cli"]
    failed_distros = []

    # Start testing
    for version in ["stable", "testing"]:
        testing_dict["distro_version"] = version
        for de_name in available_des:
            testing_dict["de_name"] = de_name
            print_header(f"Testing Debian + {de_name}")
            try:
                build.start_build(verbose=True, local_path=None, dev_release=False, build_options=testing_dict,
                                  no_download_progress=True, no_shrink=True)
            except Exception as e:
                print_error(str(e))
                print_error(f"Failed to build Debian + {de_name}")
                failed_distros.append(de_name)

        with open("results.txt", "w") as f:
            f.write(str(failed_distros))
