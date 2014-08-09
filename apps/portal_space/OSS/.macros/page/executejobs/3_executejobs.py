def main(j, args, params, tags, tasklet):

    page = args.page

#     page.addHTML("""
# <iframe src=".files/robot-ui/index.html" frameborder=0 width=100% height=100% scrolling="no"></iframe>

#         """)

    page.addHTMLHeader("""
        <meta charset="utf-8">
        <title>MS1 Robot</title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width">
        <link rel=stylesheet href=".files/robot-ui/lib/codemirror.css">
        <link rel="stylesheet" href=".files/robot-ui/styles/main.css">
        <link rel="icon" 
          type="image/ico" 
          href=".files/robot-ui/favicon.ico" />
        <style type="text/css">
            
        </style>
    """)

    page.addCSS(".files/robot-ui/bootstrap/css/bootstrap.css")
    page.addCSS('.files/robot-ui/css/flat-ui.css')
    page.addCSS(".files/robot-ui/lib/hint/show-hint.css")
    page.addHTML("""
      <div ng-app="robotAngularApp" style="zoom: 0.95;">
  <div id="wrap" ng-controller="mainController" >
    <div class="navbar navbar-default navbar-fixed-top header">
      <div class="container">
        <div class="navbar-header">
          <a href="index.html" class="navbar-brand">MS1 Robot</a>
          
        </div>
        <div class="navbar-collapse collapse" id="navbar-main">
       <ul class="nav navbar-nav">
                <li>
                  <a href="robots" style="padding-top: 10px; font-size: 15px;">Rscripts</a>
                </li>
                <li>
                  <a href="robotjobs" style="padding-top: 10px; font-size: 15px;">Jobs</a>
                </li>
                <li>
                  <a href="ExecuteJobs" style="padding-top: 10px; font-size: 15px;">Execute</a>
                </li>
              </ul>
          </ul>
          <ul class="nav navbar-nav navbar-right">
            <li class="dropdown">
              <a class="dropdown-toggle" data-toggle="dropdown" href="#" style="padding-top: 10px; font-size: 15px;">Hey {{user}} <span class="caret"></span></a>
              <ul class="dropdown-menu" aria-labelledby="ddl1">
                <li><a href="#" data-toggle="modal" data-target="#showSecretModal">secrets</a></li>
                <li><a href="#" ng-click="logout()">logout</a></li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <div class="modal fade" id="showSecretModal" tabindex="-1" role="dialog" aria-labelledby="showSecretModal" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h6 class="modal-title" id="myModalLabel">Secrets</h6>
          </div>
          <div class="modal-body">
            Your secrets are:
            <input ng-model="secretcodes" type="text" placeholder="Enter a secret code.." class="form-control" required>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-primary" ng-click="saveSecret()" style="padding: 5px 10px;">Save</button>
            <button type="button" class="btn btn-default" ng-click="closeModal()" style="padding: 5px 10px;">Cancel</button>
          </div>
        </div>
      </div>
    </div>
    <div id="main" class="container">
        <div class="row" style="margin-top: 25px; margin-left: 0;">
          <div ng-controller="executeController">
          <h1 style="font-size: 24px; font-weight: normal; margin-top: 0; margin-bottom: 0; padding-left: 10px;">Execute</h1>
          <div class="row" style="height: 25px; margin-bottom: 10px;">
            <div class="alert alert-success sample-show-hide" ng-show="executeOnceMsg" role="alert" style="height: 25px;font-size: 14px;line-height: 25px;padding: 10px;padding-top: 0;margin: 0 auto;margin-bottom: 0;width: 400px; text-align: center;">
              {{executeOnceMsg}}
            </div>
          </div>
          <div class="alert alert-danger sample-show-hide" ng-show="errorAlert" role="alert" style="height: 25px;font-size: 14px;line-height: 25px;padding: 10px;padding-top: 0;margin: 0 auto;margin-bottom: 0;width: 580px; text-align: center;">
            <span ng-if="errorAlert.status == 0">0: Internal server error, please try again later.</span>
            <span ng-if="errorAlert.status != 0">{{errorAlert.status}}: {{errorAlert.data}}</span>
          </div>
          <div style="position: relative; margin: 10px 0;" class="clearfix">
              <span spinner-key="spinner" us-spinner="{lines: 9,length: 5, width: 3, radius: 4, corners: 0.6, rotate: 28, direction: 1, color: '#1abc9c', speed: 1.1, trail: 56, shadow: false, hwaccel: false, className: 'spinner', zIndex: 0 , top: '35%', left: '50%'}"></span>
            </div>
          <div class="col-md-6 col-md-offset-3">
            <input type="text" ng-model="SnippetName" placeholder="Enter code snippet name. e.g. machine.youtrack" class="form-control sample-show-hide" style="margin: 15px 0;">
            <select style="border-radius: 5px; height: 35px; padding-left: 5px; margin-bottom: 10px; width: 100%; font-size: 16px;" ng-model="SnippetChannelddl" ng-options="scriptChannel as scriptChannel for scriptChannel in channelsToEnter" class="sample-show-hide">
            </select>
            <div id="executeOncecodeWrap" style="clear: both;">
              <textarea id="executeOncecode" name="executeOncecode" ></textarea>
            </div>
            <input type="checkbox" ng-model="waitFlag" ng-true-value="1" ng-false-value="0" style="float: left; margin-top: 15px; margin-right: 10px;" class="sample-show-hide"><p style="margin-top: 8px; font-size: 16px;" class="sample-show-hide">Wait until rscript get executed?</p>
            <div style="margin-top: 25px; text-align: center;">
              <a href="#" class="btn btn-primary sample-show-hide" style="padding: 5px 10px; margin-top: 5px; margin-right: 10px;" ng-click="rScriptExecuteOnce()">Execute</a>
            </div>
            <div style="min-height: 160px;">
              <div ng-show="jobinfo" class="jobinfo sample-show-hide alert alert-success" style="margin-top: 25px; font-size: 15px; padding: 13px; width: 560px; margin: 25px auto;">
                <strong>Channel: </strong>{{jobinfo.rscript_channel}}
                <br/>
                <strong>Snippet name: </strong>{{jobinfo.rscript_name}}
                <br/>
                <strong>Job start time: </strong> {{jobinfo.start * 1000 | date:'medium'}}
                <br/>
                <strong>Job end time: </strong> {{jobinfo.end * 1000 | date:'medium'}}
                <br/>
                <strong>Result: </strong>{{jobinfo.result}}
                <br/>
                <strong>Status: </strong>{{jobinfo.state}}
              </div>
            </div>
          </div>
            
          </div>
        </div>
    </div>
    </div>
    <footer id="footer">
      <div class="container">
        <div class="row">
          <div class="col-md-3 pull-right">
            <div class="footer-banner">
              <a href="http://Mothership1.com" style="text-decoration: none; font-size: 14px;">Mothership1.com</a>              
            </div>
          </div>
        </div>
      </div>
    </footer>
    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.2.18/angular.min.js"></script>
    <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/angularjs/1.3.0-beta.15/angular-animate.js"></script>
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/angularjs/1.0.3/angular-sanitize.js"></script>
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script> 

    <script src=".files/robot-ui/scripts/app.js"></script>
    <script src=".files/robot-ui/scripts/controllers/main.js"></script>
    <script src=".files/robot-ui/scripts/controllers/executeController.js"></script>
    <script src=".files/robot-ui/lib/codemirror.js"></script>
    <script src=".files/robot-ui/lib/javascript.js"></script>
    <script src=".files/robot-ui/lib/python.js"></script>
    <script src=".files/robot-ui/lib/python-hint.js"></script>
    <script src=".files/robot-ui/lib/show-hint.js"></script>
    <script src=".files/robot-ui/lib/javascript-hint.js"></script>
    <script src=".files/robot-ui/js/bootstrap.min.js"></script>
    <script src=".files/robot-ui/lib/spin.min.js"></script>
    <script src=".files/robot-ui/lib/angular-spinner.min.js"></script>
</div>
        """)

    page.addJS("//ajax.googleapis.com/ajax/libs/angularjs/1.3.0-beta.15/angular.min.js")
    page.addJS("//ajax.googleapis.com/ajax/libs/angularjs/1.3.0-beta.15/angular-animate.js")
    page.addJS("http://ajax.googleapis.com/ajax/libs/angularjs/1.0.3/angular-sanitize.js")
    page.addJS("http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js")
    page.addJS("//cdnjs.cloudflare.com/ajax/libs/underscore.js/1.6.0/underscore-min.js")
    page.addJS(".files/robot-ui/scripts/app.js")
    page.addJS(".files/robot-ui/js/bootstrap-select.js")

    
    params.result = page
    return params


def match(j, args, params, tags, tasklet):
    return True
