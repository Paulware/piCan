echo "dtparam=spi=on" >> /boot.config.txt
echo "dtoverlay=mcp2515-can0-overlay,oscillator=16000000,interrupt=25" >> /boot.config.txt
echo "dtoverlay=spi-bcm2835-overlay" >> /boot.config.txt

cd python-can
sudo python3 setup.py install

echo "After reboot: " 
echo "sudo /sbin/ip link set can0 up type can bitrate 500000" 

