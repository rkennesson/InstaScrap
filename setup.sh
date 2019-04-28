# The only setup here is installing Instagram's API and making the InstaScrap directory
echo "--------------------------------------------------------------------------------"
echo "*Installing Instagram's API for Python 3\n"
pip3 install git+https://git@github.com/ping/instagram_private_api.git@1.6.0
echo "--------------------------------------------------------------------------------"

if [ ! -d "/home/$USER/Pictures/InstaScrap" ]; then
    mkdir ~/Pictures/InstaScrap
fi
    echo 'Directory already created!'
    echo "--------------------------------------------------------------------------------"
