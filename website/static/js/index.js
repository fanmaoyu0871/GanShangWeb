// v-0.01
// xuxiang
// 2017-03-20
// 

var myWeb = angular.module("myweb",[]);
// 头部导航数据
	myWeb.controller('init', function ($scope, $http, $interval) {
	// 页面初始化数据
	    $scope.showFlag = false
		$scope.projectData = {};
		$scope.bananaNavData = {};
		$http({
			'method':'get',
			'url':'../json/navlist.json'
		}).then(function successcallback (res){
	        $scope.navdata = res.data;
	        for(var i in $scope.navdata){
	            $scope.projectData[$scope.navdata[i].projectid] = $scope.navdata[i].projectData;
			}
	    },function errorcallback(res){
			console.error(res)
		})
		$scope.mouseoverNavList = function(e){
			var id = e.navitem.projectid;
	        $scope.resData = $scope.projectData[id];
	        $scope.showFlag = true
		}
		
		$scope.mouseleave = function(){
	        $scope.showFlag = false;
	    }
	    // 产品内容数据
		$http({
			'method':'get',
			'url':'../json/projectindex.json'
			// "cache": true
		}).then(function successcallback (res){
			// console.log(res);
	        $scope.projectArray = res.data;
	    },function errorcallback(res){
			console.error(res)
		})
		// 页脚foot数据绑定
		$http({
			'method':'get',
			'url':'../json/foot.json'
			// "cache": true
		}).then(function successcallback (res){
			console.log(res);
	        $scope.footArray = res.data;
	    },function errorcallback(res){
			console.error(res)
		})
	});
// banana位轮播
	myWeb.controller('moveSlide',function($scope){
		$scope.moveNode = function(){
			return new mySlider("slideList");
		}
		function mySlider(obj){
			this.init(obj);
		};
		mySlider.prototype={
			init:function(obj){
				if(document.getElementById(obj) == null || document.getElementById(obj) === undefined) return;
				this.box=document.getElementById(obj),
				this.winW=1200,
				this.winH=460,
				this.section=this.box.children,
				this.len=this.section.length,
				lenN = this.len;
				document.getElementById('wrapBanner').style.width=this.winW+'px';
				this.box.style.cssText='width:'+this.winW*this.len+'px; height:'+this.winH+'px;-webkit-transform:translate3d(0,0,0); transform:translate3d(0,0,0);';
				var oIconul=document.createElement("ul"),nextEle=document.createElement("span"),prevEle=document.createElement("span");
					nextEle.id="nextBtn";
					prevEle.id="prevBtn";
					oIconul.id="icon";
					document.getElementById('wrapBanner').appendChild(oIconul);
					document.getElementById('wrapBanner').appendChild(nextEle);
					document.getElementById('wrapBanner').appendChild(prevEle);
				for (var i = 0; i < lenN; i++) {
					var myDiv=this.section[i];
						myDiv.index = i;
					var oul=document.getElementById("icon"),oli=document.createElement("li");
						oul.appendChild(oli);
						document.getElementById("icon").getElementsByTagName('li')[0].style.backgroundColor = "#f00";
					
					myDiv.style.cssText='width:'+this.winW+'px;height:100%;float:left;';
					// this.slider(myDiv);
				};
				this.slider(this.box);
			},
			slider:function(myObj){
				var nextBtn = document.getElementById('nextBtn'),prevBtn = document.getElementById('prevBtn');
				var timer,self=this,n=0,speed=5000;
			// 检点图切换效果
				var animateFn = function(k){
					var btnIcon = document.getElementById("icon").children;
						for (var j = 0; j < btnIcon.length; j++) {
							btnIcon[j].style.backgroundColor = "#FFF";
						}
						btnIcon[k].style.backgroundColor = "#f00";
					var t=(-k*1200);
					self.box.style.cssText = 'width:'+self.winW*lenN+'px;-webkit-transition:-webkit-transform 1s;transition:transform 1s;-webkit-transform:translate3d('+t+'px,0,0);transform:translate3d('+t+'px,0,0)';
				};
				var timeFn = function(){
					n+=1;
					if (n>lenN-1) {
						self.box.style.cssText = 'width:'+self.winW*lenN+'px;-webkit-transition:-webkit-transform 1s;transition:transform 1s;-webkit-transform:translate3d(0,0,0);transform:translate3d(0,0,0)';
						n = 0;
						for (var jj = 0; jj < document.getElementById("icon").children.length; jj++) {
							document.getElementById("icon").children[jj].style.backgroundColor = "#FFF";
						}
						document.getElementById("icon").children[0].style.backgroundColor = "#f00";
					} else {
						animateFn(n);
					}
				};
				timer = setInterval(timeFn,speed),
				nextFn = function(){
					// 下一张
					n+=1;
					if (n>lenN-1) {
						n = lenN-1;
						alert("已经是最后一张了");
						return false
					} else {
						animateFn(n);
					}
				},
				prevFn = function(){
					// 上一张
					n-=1;
					if (n<0) {
						n = 0;
						alert("已经是第一张了");
						return false
					} else {
						animateFn(n);
					}
				},
				mouseoverFn = function(e){
					nextBtn.style.cssText="display:block;opacity:1;-webkit-opacity:1;-moz-opacity:1;-ms-opacity:1;"
					prevBtn.style.cssText="display:block;opacity:1;-webkit-opacity:1;-moz-opacity:1;-ms-opacity:1;"
					clearInterval(timer);
				},
				mouseleaveFn = function(e){
					nextBtn.style.cssText="display:none;opacity:0;-webkit-opacity:0;-moz-opacity:0;-ms-opacity:0;"
					prevBtn.style.cssText="display:none;opacity:0;-webkit-opacity:0;-moz-opacity:0;-ms-opacity:0;";
					timer = setInterval(timeFn,speed);
				}
			self.box.parentNode.addEventListener("mouseover",mouseoverFn,false);
			self.box.parentNode.addEventListener("mouseleave",mouseleaveFn,false);
			nextBtn.addEventListener("click",nextFn,false);
			prevBtn.addEventListener("click",prevFn,false);
			}
		}
		$scope.moveNode();
	});
// 作品列表
	myWeb.controller('proCtr',function($scope,$http){
	// 优秀作品
		$scope.switchProductNice = function(){
			return new productnice("productNiceScorll");
		}
		function productnice(obj){
			this.inits(obj);
		};
		productnice.prototype={
			inits:function(obj){
				if(document.getElementById(obj) == null || document.getElementById(obj) === undefined) return;
				this.box=document.getElementById(obj),
				this.wid = parseInt(267),
				this.marLeft = parseInt(44),
				this.child=this.box.children,
				pN=this.child.length;
				this.box.style.cssText='width:'+(this.wid*pN + this.marLeft*(pN-1))+'px;-webkit-transform:translate3d(0,0,0); transform:translate3d(0,0,0);';
				this.productniceFn();
			},
			productniceFn:function(){
				var prevN = 0,_this = this;
				var switchProductNiceFn =function(b){
					var tb=(-b*(_this.wid+_this.marLeft));
						_this.box.style.cssText = 'width:'+(_this.wid*pN + _this.marLeft*(pN-1))+'px;-webkit-transition:-webkit-transform 1s;transition:transform 1s;-webkit-transform:translate3d('+tb+'px,0,0);transform:translate3d('+tb+'px,0,0)';
				}
				$scope.prevProduct = function(objp){
					console.log(objp);
					prevN -= 1;
					if (prevN < 0) {
						prevN = 0;
						alert("没有更多产品了！");
						return false
					} else {
						switchProductNiceFn(prevN);
					}
				}
				$scope.nextProduct = function(objp){
					prevN += 1;
					if (prevN + 4 > pN) {
						prevN -= 1;
						alert("没有更多产品了！");
						return false
					} else {
						switchProductNiceFn(prevN);
					}
				}
			}
		}
		$scope.switchProductNice();
	})
