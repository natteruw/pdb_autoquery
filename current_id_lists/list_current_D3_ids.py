#14.08.21 used rcsb.org's RESTful web services python script example to construct this
#reports number of PDB entries found that fit the requirements listed below
#contact: Una <natteruw@uw.edu>


import urllib2


url = 'http://www.rcsb.org/pdb/rest/search'

queryText = """

<?xml version="1.0" encoding="UTF-8"?>

<orgPdbCompositeQuery version="1.0">     <resultCount>5132</resultCount>
<queryId>7057EF69</queryId>  <queryRefinement>   <queryRefinementLevel>0</queryRefinementLevel>

<orgPdbQuery>
<version>head</version>
<queryType>org.pdb.query.simple.PointGroupQuery</queryType>
<description>Finds PDB entries based on symmetry: Protein Symmetry is D3 and RMSD is between the default min 0.0 and the default max 7.0</description>
<queryId>669312BE</queryId>
<resultCount>5132</resultCount>
<runtimeStart>2014-08-21T23:24:12Z</runtimeStart>
<runtimeMilliseconds>1366</runtimeMilliseconds>
<pointGroup>D3</pointGroup>
<rMSDComparator>between</rMSDComparator>
</orgPdbQuery>

</queryRefinement>
<queryRefinement>
<queryRefinementLevel>1
</queryRefinementLevel>
<conjunctionType>and</conjunctionType>

<orgPdbQuery>
<version>head</version> 
<queryType>org.pdb.query.simple.SequenceLengthQuery</queryType>
<description>Sequence Length is between 75 and 500 </description>
<queryId>2F136164</queryId>
<resultCount>87937</resultCount>
<runtimeStart>2014-08-21T23:24:14Z</runtimeStart>
<runtimeMilliseconds>11824</runtimeMilliseconds>
<v_sequence.chainLength.min>75</v_sequence.chainLength.min>
<v_sequence.chainLength.max>500</v_sequence.chainLength.max>
</orgPdbQuery>

</queryRefinement>
<queryRefinement>
<queryRefinementLevel>2</queryRefinementLevel>
<conjunctionType>and</conjunctionType>

<orgPdbQuery>
<version>head</version>
<queryType>org.pdb.query.simple.ResolutionQuery</queryType>
<description>Resolution is between 0.5 and 3.0 </description>
<queryId>2E44619D</queryId>
<resultCount>85748</resultCount>
<runtimeStart>2014-08-21T23:24:26Z</runtimeStart>
<runtimeMilliseconds>763</runtimeMilliseconds>
<refine.ls_d_res_high.comparator>between</refine.ls_d_res_high.comparator>
<refine.ls_d_res_high.min>0.5</refine.ls_d_res_high.min>
<refine.ls_d_res_high.max>3.0</refine.ls_d_res_high.max>
</orgPdbQuery>

</queryRefinement>
<queryRefinement>
<queryRefinementLevel>3</queryRefinementLevel>
<conjunctionType>and</conjunctionType> 
<orgPdbQuery>
<version>head</version>     
<queryType>org.pdb.query.simple.ExpressionOrganismQuery</queryType>     
<description>ExpressionOrganismQuery: entity_src_gen.pdbx_host_org_scientific_name.comparator=equals entity_src_gen.pdbx_host_org_scientific_name.value=Escherichia coli </description>     
<queryId>7E4847AF</queryId>     
<resultCount>64931</resultCount>     
<runtimeStart>2014-08-21T23:24:26Z</runtimeStart>     
<runtimeMilliseconds>1800</runtimeMilliseconds>     
<entity_src_gen.pdbx_host_org_scientific_name.comparator>equals</entity_src_gen.pdbx_host_org_scientific_name.comparator>     
<entity_src_gen.pdbx_host_org_scientific_name.value>Escherichia coli</entity_src_gen.pdbx_host_org_scientific_name.value>   
</orgPdbQuery>  

</queryRefinement>
</orgPdbCompositeQuery>

"""


print "query:\n", queryText

print "querying PDB...\n"

req = urllib2.Request(url, data=queryText)

f = urllib2.urlopen(req)

result = f.read()


if result:

	    print "Found number of PDB entries:", result.count('\n')
	    print result
            temp=open('./updated_temp_id_lists/tempD3', 'w+')
	    temp.write(result)
else:

	    print "Failed to retrieve results" 
