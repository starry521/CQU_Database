# START-DB Package Tutorial

## For Linux users

**Linux distribution: Ubuntu 22.04 LTS**

Operations may differ on different distributions.

1. Install **maven**.

   `sudo apt install maven`

   > If you are the root user, `sudo` is not necessary:
   >
   > `apt install maven`

   _Get the system updated before you install a new package to avoid other problems:_

   `sudo apt update && sudo apt upgrade`

2. Download **OracleJDK 1.8 (JAVA 8)** and install it.

   > Here is the official link: [OracleJDK](https://www.oracle.com/java/technologies/downloads/#java8-linux)

   1. We should choose "x86 Compressed Archive" or "x64 Compressed Archive" instead of "x86 RPM Package" or "x64 RPM Package".

   2. Make a directory for the JDK:

      `sudo mkdir -p /usr/lib/jvm`

   3. Extract the file and install the JDK:

      `sudo tar zxvf jdk-8u351-linux-x64.tar.gz -C /usr/lib/jvm`

   4. Tell the system that there's a new Java version available:

      `sudo update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/jdk1.8.0_351/bin/java" 1`

   5. Set the new JDK as the default:

      `sudo update-alternatives --set java /usr/lib/jvm/jdk1.8.0_351/bin/java`

   6. Verify the version of the JRE or JDK:

      `java -version`

      The output message should be like:

      ```
      java version "1.8.0_351"
      Java(TM) SE Runtime Environment (build 1.8.0_351-b10)
      Java HotSpot(TM) 64-Bit Server VM (build 25.351-b10, mixed mode)
      ```

3. Install **docker.io** & **docker-compose**.

   `sudo apt install docker.io && sudo apt install docker-compose`

   Then run a command for test:

   `sudo docker run hello-world`

   If Docker Engine is installed, the output message should be like:

   ```
   ......
   Hello from Docker!
   This message shows that your installation appears to be working correctly.

   ......
   ```

4. If you do not have a local copy of **START-DB** 's source code, clone it or download the zip file of it.

5. Now change the working directory into start-db.

6. Run the following command to run containers as dependency.

   `sudo docker-compose -f docker/local/docker-compose.yml up -d`

7. Set MySQL host

   `echo "127.0.0.1 mysql-local" | sudo tee -a /etc/hosts`

8. Set GeoMesa HBase host

   `echo "127.0.0.1 geomesa-hbase-local" | sudo tee -a /etc/hosts`

9. Compile and package

   `mvn package`

## For Windows/MacOS users

1. Download and install **Docker Desktop**

   > Here is the official link: [Docker Desktop](https://www.docker.com/products/docker-desktop/)

   On macOS, it is easy to install **Docker Desktop**. Just drag and drop, and you got it.

   <img src="./START-DB Package Tutorial.assets/docker.png" alt="docker" style="zoom:50%;" />

   On Windows, it might be a little different.

   <img src="./START-DB Package Tutorial.assets/docker-2.png" alt="docker-2" style="zoom:50%;" />

   If the installWizard tells you to enable WSL, please click "Yes" and continue.

   > About how to enable WSL manually: [Windows Subsystem for Linux Documentation](https://learn.microsoft.com/en-US/windows/wsl/)

2. Install the latest version of **IntelliJ IDEA**

   > Here is the official link: [IntelliJ IDEA](https://www.jetbrains.com/idea/)

   On macOS, You need just one step to finish it.

   <img src="./START-DB Package Tutorial.assets/idea.png" alt="idea" style="zoom:50%;" />

   On Windows, what you need is 4 clicks on "Next"

   <img src="./START-DB Package Tutorial.assets/idea-2.png" alt="idea-2" style="zoom:50%;" />

3. Download and install **OracleJDK 1.8 (JAVA 8)**

   > Here is the official link: [OracleJDK](https://www.oracle.com/java/technologies/downloads/)

   On macOS, open the dmg file and click "JDK 8 Update 351.pkg", the installer will guide you to finish it.

   <img src="./START-DB Package Tutorial.assets/jdk.png" alt="jdk" style="zoom:50%;" />

   On Windows, there is no special steps, just click "Next" and wait for it to be done.

   <img src="./START-DB Package Tutorial.assets/jdk-2.png" alt="jdk-2" style="zoom:50%;" />

   Take down the path surrounded by the red rectangle, and this might help when the PATH adding job is manual.

   <img src="./START-DB Package Tutorial.assets/jdk-3.png" alt="jdk-3" style="zoom:50%;" />

   Sometimes, the installer will not add JDK to PATH variables automatically due to certain reasons, which means you have to do it by yourself.

   If you are not sure whether the installer had done that, open the Command Prompt and input: `java -version`

   The output message should be like:

   ```
   java version "1.8.0_351"
   Java(TM) SE Runtime Environment (build 1.8.0_351-b10)
   Java HotSpot(TM) 64-Bit Server VM (build 25.351-b10, mixed mode)
   ```

   If not, go to the Advanced system settings and click "Environment Varables" to add the JDK to PATH variables.

   <img src="./START-DB Package Tutorial.assets/path.png" alt="path" style="zoom:50%;" />

4. If you do not have a local copy of **START-DB** 's source code, clone it or download the zip file of it.

5. Open **START-DB** as a project using **IntelliJ IDEA**.

   _Please click "Trust Project" if there is a safety-notice dialog._

   <img src="./START-DB Package Tutorial.assets/dialog.png" alt="dialog" style="zoom:50%;" />

6. Open the terminal in **IntelliJ IDEA** and run the following command:

   `docker-compose -f docker/local/docker-compose.yml up -d`

   <img src="./START-DB Package Tutorial.assets/ter.png" alt="ter" style="zoom:50%;" />

7. Add two lines in your hosts file:

   ```
   127.0.0.1 mysql-local
   127.0.0.1 geomesa-hbase-local
   ```

8. Click "Maven > start-db > Lifecycle > package"in **IntelliJ IDEA** and packaging will begin.

   <img src="./START-DB Package Tutorial.assets/maven.png" alt="maven" style="zoom:50%;" />

## TIPS

1. It is recommended to drop all containers and restart them before every test.
2. If there is any network problem during synchronization of maven repositories or docker images, please delete the cache and retry.
3. Administrator privilege is needed for editing the hosts file.
4. If an error raised by module 'start-db-server' occurred, please try to disable your network proxy tool.
