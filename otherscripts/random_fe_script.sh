#!/bin/bash
echo "inicio do script, execucao do for para listar o ip pv dos FE servers" $(date +"%d-%m-%y")
for FE_IP in $(/usr/local/bin/aws ec2 describe-instances --filter Name=tag:Roles,Values=frontend | grep PrivateIpAddress | awk '{print $2}' | tr -d '[' | tr -d '"' | tr -d ',' | tr -d ' ' | awk 'NF > 0' | sort | uniq ); do
    UPTIME_RESULT=`ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no ubuntu@$FE_IP 'uptime' | cut -d " " -f4`
    if [ $UPTIME_RESULT -ge 7 ];
        then
          echo "The frontend server with the ip address:" $FE_IP "will be restarted" $(date +"%d-%m-%y")
          ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no ubuntu@$FE_IP 'sudo reboot'
          echo "Aguardando alguns minutos para o FES ser reiniciado"
          sleep 200
          echo "Agora o servico do nginx sera reiniciado"
          ssh ubuntu@$FE_IP 'sudo service nginx start'
          echo "o servico do nginx ja foi reiniciado"
          echo "############ FIM DA EXECUCAO DO SCRIPT ############" $(date +"%d-%m-%y")
          exit 0
    else
        echo "The frontend server with the ip address" $FE_IP "is less than 7 days old and will not be restarted"
    fi

done