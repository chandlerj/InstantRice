# Features I *could* add to `InstantRice` during HackUSU
*number after item indicates anticipated level of difficulty out of 5*
- [x] Using a central config file instead of a python dictionary | 2
- [ ] Completing the TUI | 4
    - [ ] Creating classes that store configuration settings and persist changes made to config | 2
    - [ ] Class will need to grab initial state of configuration files | 2
- [ ] Add support for compiling dmenu with predetermined list of plugins | 5
- [ ] Add support for `dwm` | 5
- [ ] Add support for `sway` (*should* be trivial) | 1
- [ ] Rewrite K-means clustering algorithm using builtins instead of `scikit-learn` | 4
    - Im not doing this lol
- [ ] Implement native terminal image viewer (or find python lib that covers functionality) | 5
- [ ] Minimize number of `sys` package usage | 5
- [ ] add features to randomized color selector | 5
    - [ ] preview what colors will be used for what aspects of the system color scheme | 1
    - [ ] Add ability to customize what colors are used for different aspects of the system | 3
    - [X] Detection of when colors do not have enough contrast from one another and generate new scheme | 3
        - Instead of automatically generating new colors, constrast value is provided with a given color pair
          and the user is given the ability to choose which color pairs they want to use.
    - [ ] Provide ability to save color schemes to use independent of wallpaper | 2
    - [ ] Ability to load preset color scheme | 1
    - [ ] Provide ability to pass in separate image to provide colors than image being used for background | 1
- [ ] Put program in a state to publish on AUR/pip | 2
    - [ ] Create build process using `PKGBUILD` or `PyInstaller` | 2
