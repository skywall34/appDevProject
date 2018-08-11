#!/bin/bash
#This script starts the django locally as well as deploy the app to gcloud
#for gcloud you might need root access to succeed
#the cloud_sql script must be running in a separate terminal for django to work

echo =============Welcome to Django==========================================
echo Type command: runserver/migrations/restart_server/deploy_app
echo ========================================================================
echo !!Restart the server only if you cant Crtl-C on the terminal, and run it on a different terminal!!
echo =======================================================================


echo "Enter command:" 
read user_input 

case $user_input in
	"runserver")
		python3 manage.py runserver
		;;
	"migrations")
		python3 manage.py makemigrations
		#add error handler
		python3 manage.py migrate
		;;
	"restart_server")
		PID=$! # get the server id
		sleep 2 # w8 for a moment for the server to go down
		kill $PID #kill the server
		python3 manage.py runserver #restart
		;;
	"deploy_app")
		echo Still in the works. Run locally for now!
		;;
	*) echo Wrong input! ;;
esac
