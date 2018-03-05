#! /bin/sh
#
# A script to read the To, From, Subject, and Date of files in the SpamAssassin
# / Amavisd Quarantine directory and allow the adminstrator to release the
# email to the user mailbox or delete the email from the system.
#
# Chris J
# [@]rattis
#
# version 1.002
###############################################################################

echo ''
for workDir in $(ls -1)
do
        cd $workDir
        echo "----"
        echo $workDir
        echo "----"
        #workDir=$(basename `pwd`)
        for quarFile in $(ls -1);
        do
                # list number of remaining emails
                echo "---"
                ls -1 | wc -l
                echo "---"

                ## start email block
                echo "$quarFile:"
                # is it zipped or unzipped, and display
                testFile=$(file --mime-type -b $quarFile)
                if [ "$testFile" = 'application/gzip' ];
                then
                        zgrep -E '^To\: ' $quarFile
                        zgrep -E '^Date\: ' $quarFile
                        zgrep -E '^From\: ' $quarFile
                        zgrep -E '^Subject\: ' $quarFile
                        echo ''
                else
                        egrep '^To\: ' $quarFile
                        egrep '^Date\: ' $quarFile
                        egrep '^From\: ' $quarFile
                        egrep '^Subject\: ' $quarFile
                        echo ''
                fi

                # relase to mailbox or delete file
                read -p "[*] Do you want to Release the email, Delete the email, or Quit?? (r/d/q): " RorD
                cRorD=$(echo -n $RorD | tr A-Z a-z)
                if [ X"$cRorD" = X"r" ];
                # release the file to the recipient
                then
                        releaseFile="$workDir/$quarFile"
                        amavisd-release $releaseFile
                        echo "[+] email released to user and removed from quarantine "
                        rm $quarFile
                elif [ X"$cRorD" = X"d" ];
                # delete the file
                then
                        rm $quarFile
                        echo "[+] email deleted "
                elif [ X"$cRorD" = X"q" ] ;
                then
                        echo "[-] User chose to quit"
                        echo ''
                        exit 0
                else
                # do nothing and go to next file.
                echo '[-] nothing done to email, moving to next one'
                fi
                echo ''
        done
        cd ..
done
echo ''
echo '[***] All emails reviewed, nothing left to process.'
echo ''
