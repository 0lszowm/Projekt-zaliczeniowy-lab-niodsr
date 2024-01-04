# Projekt-zaliczeniowy-lab-niodsr

## Wymagania:
- [ROS 2 Humble Hawksbill](https://docs.ros.org/en/humble/Installation.html) on [Ubuntu Linux - Jammy Jellyfish (22.04)](https://releases.ubuntu.com/jammy/)

## Budowanie środowiska:
1. Należy stworzyć folder `ROS2_WS` który będzie traktowany jako ROS2 workspace.
    ```bash
    $ mkdir -p ~/ROS2_WS/src/
    ```
2. Należy sklonować to repozytorium:
    ```bash
    $ git clone https://github.com/0lszowm/Projekt-zaliczeniowy-lab-niodsr.git
    ```
3. Przenieś paczke `solution` do katalogu (`src`) znajdującego się w środowisku `ROS2_WS`.
    ```bash
    $ mv ~/Projekt-zaliczeniowy-lab-niodsr/solution/ ~/ROS2_WS/src/
    
4. Należy zbudować całe środowisko.
    ```bash
    $ cd ~/ROS2_WS
    $ colcon build
    ```
5. Teraz trzeba zsource'owac `setup.bash` ze środowiska `ROS2_WS`.
    ```bash
    $ echo "source ~/ROS2_WS/install/setup.bash" >> ~/.bashrc
    $ source ~/.bashrc
    ```

## Uruchomienie rozwiązania:
1. Aby uruchomić rozwiązanie należy we wcześniej uruchomionej konsoli wykonać poniższe polecenie :
    ```bash
    $ ros2 launch solution control.launch.py
    ```
