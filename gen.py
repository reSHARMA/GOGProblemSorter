import sys
print(
'''

<!DOCTYPE html>
<html lang="en" >

<head>

  <meta charset="UTF-8">
  <title>GOGOJ</title>
  
  
  
  <link rel='stylesheet prefetch' href='https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.0.0-beta.2/css/bootstrap.css'>
  <link rel='stylesheet prefetch' href='https://cdnjs.cloudflare.com/ajax/libs/bootstrap-table/1.11.1/bootstrap-table.min.css'>

      <style>
      .head {
  padding : 2%;
  font-size : 40px;
  
}
    </style>

  
  
  
  

</head>

<body translate="no" >

  <div class="main container-fluid">
	  <center class = "head"><h1>GeeksForGeeksProblemSorter</h1></center>
  <div class = "table-responsive" id = "table">
 <div class="container">
 '''
 )
print("<h1>" + (sys.argv[1]).upper() + "</h1>")
print(
'''
      <table id="table"
             data-toggle="table"
             data-height="460"
'''
)
print('data-url="./' + sys.argv[1]  + '.json"')
print(
  '''
               data-sort-name="price"
               data-sort-order="desc">
            <thead>
            <tr>
                <th data-field="head" data-sortable="false">Question</th>
                <th data-field="link" data-sortable="false">Link</th>
                <th data-field="rate" data-sortable="true" data-sorter="priceSorter">Difficulty</th>
            </tr>
            </thead>
        </table>
    </div>
  </div>
</div>
<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js'></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js" integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js" integrity="sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVkE+jo0ieGizqPLForn" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-table/1.11.1/bootstrap-table.min.js"  crossorigin="anonymous"></script>


  

    <script >
	function priceSorter(a, b) {
		if (a > b) return 1;
		if (a < b) return -1;
		return 0;
	}
    </script>



  
  

</body>

</html>
 '''
)
