<h3>Lint</h3>
<div>
<table class="listing lint scroll scrollable" id="nosebitten_lint">
  <thead>
    <tr>
      <th>Type</th>
      <th>Class/File</th>
      <th>Line</th>
      <th>Message</th>
    </tr>
  </thead>
  <tbody>
  <?cs each:item = data ?>
  <tr class="<?cs var:item.cat ?>">
    <td><?cs var:item.type ?></td>
    <td ><a href="<?cs var:item.href ?>#L<?cs var:item.line ?>"<?cs if:item.tag ?>
    class="tooltip" title="Module/Class/Function - <?cs var:item.tag ?>"
    <?cs /if ?>><?cs var:item.file ?></a>
    </td>
    <td><?cs var:item.line ?></td>
    <td><?cs var:item.msg ?></td>
  </tr><?cs /each ?>
  </tbody>
</table>
<h3>Messages Totals</h3>
<table class="listing lint_totals" id="nosebitten_lint_totals">
  <thead>
    <tr>
      <th>Convention</th>
      <th>Refactor</th>
      <th>Warning</th>
      <th>Failure</th>
      <th>Error</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="convention"><?cs var:totals.convention ?></td>
      <td class="refactor"><?cs var:totals.refactor ?></td>
      <td class="warning"><?cs var:totals.warning ?></td>
      <td class="failure"><?cs var:totals.failure ?></td>
      <td class="error"><?cs var:totals.error ?></td>
    </tr>
  </tbody>
</table>
<div id="sorting_lint" class="sorting">
  <div>Sorting tables, please hold on...</div>
</div>
</div>
<script>
$(document).ready(function() {
    $("#nosebitten_lint").tableSorter({
        sortColumn: 'Class/File',         // Integer or String of the name of the column to sort by.
        sortClassAsc: 'sortUp',       // class name for ascending sorting action to header
        sortClassDesc: 'sortDown',    // class name for descending sorting action to header
        headerClass: 'largeHeaders',           // class name for headers (th's)
        rowLimit: 5,
        minRowsForWaitingMsg: 2,
    }).tableScroller();
    $(document).sortStart(function(){
        $("div#sorting_lint").show();
    }).sortStop(function(){
        $("div#sorting_lint").hide();
    });
    $('a.tooltip').Tooltip({track: true, delay: 0, showBody: true, showURL: false, showBody: " - "});
});
</script>
