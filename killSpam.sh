#! /bin/sh
#
# A script to read the To, From, Subject, and Date of files in the SpamAssassin
# / Amavisd Quarantine directory and allow the adminstrator to release the
# email to the user mailbox or delete the email from the system.
#
# Chris J
# @rattis
#
# version 1.0
###############################################################################


for quarfile in $(ls -1);
do
        # list number of remaining emails
        ls -1 | wc -l
        echo "---"

        ## start email block
        echo "$quarfile:"
        # is it zipped or unzipped, and display
        testFile=$(file --mime-type -b $quarfile)
        if [ "$testFile" = 'application/gzip' ];
        then
                zgrep -E '^(To|From|Subject|Date)\: ' $quarfile
                echo ''
        else
                egrep '^(To|From|Subject|Date)\: ' $quarfile
                echo ''
        fi

        # relase to mailbox or delete file
        read -p "Do you want to Release or Delete the file? (r/d): " RorD
        cRorD=$(echo -n $RorD | tr A-Z a-z)
        if [ X"$cRorD" = X"r" ];
        # release the file to the recipient
        then
                amavisd-release $quarfile
                echo "email released to user "
        elif [ X"$cRorD" = X"d" ];
        # delete the file
        then
                rm $quarfile
                echo "email deleted "
        else
        # do nothing and go to next file.
        echo 'nothing done to email, moving to next one'
        fi
        echo ''
done
