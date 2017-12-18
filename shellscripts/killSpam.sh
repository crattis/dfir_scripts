#! /bin/sh
#
# A script to read the To, From, Subject, and Date of files in the SpamAssassin
# / Amavisd Quarantine directory and allow the adminstrator to release the
# email to the user mailbox or delete the email from the system.
#
# Chris J
# [@]rattis
#
# version 1.001
###############################################################################

echo ''
workDir=$(basename `pwd`)
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
                zgrep -E '^(To|From|Subject|Date)\: ' $quarFile
                echo ''
        else
                egrep '^(To|From|Subject|Date)\: ' $quarFile
                echo ''
        fi

        # relase to mailbox or delete file
        read -p "[*] Do you want to Release or Delete the file? (r/d): " RorD
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
        else
        # do nothing and go to next file.
        echo '[-] nothing done to email, moving to next one'
        fi
        echo ''
done

