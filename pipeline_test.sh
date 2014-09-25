for f in `cat /work/natteruw/pdb_autoquery/diff_list_D*`
do
dir=`echo $f | cut -c 2-3`
cp /lab/databases/biounits/$dir/${f}* .
done
