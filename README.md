# FoxyDriver

**FoxyDriver** is a Python toolkit for remotely operating the Foxy R1 and R2 fraction collectors from Teledyne Technologies. While these instruments support remote control, Teledyne doesn’t provide the necessary utilities—**FoxyDriver** bridges that gap.

## Usage

### Foxy Terminal

1. After installation, place the batch file in your preferred directory.
2. Ensure Python and Foxy Terminal are installed correctly.
3. Launch the terminal via the batch file.

The terminal will prompt you to input the Foxy’s IP address and port. The port is always 23 (as per the Foxy R1/R2 manual). The IP address may vary depending on your setup.

Once you’ve entered the IP and port, the terminal will attempt to connect. A successful connection enables direct control over your Foxy device. 

### Built-In Commands

In addition to the commands listed in the Foxy R1/R2 manual, the terminal includes these hard-coded commands:

- **Exit**: Closes the connection and exits the terminal.
- **Download**: Downloads a program from the Foxy.
- **Upload**: Uploads a program to the Foxy.

## License

This project is licensed under the GNU GPL v3 license.
