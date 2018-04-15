// // Sends a new request to update the to-do list
// function getPost() {
//     var itemTextElement = $("#pagename");
//     var itemTextValue   = itemTextElement.val();
//     console.log(itemTextValue);
//     $.ajax({
//         url: "/socialnetwork/get-list-json",
//         dataType: "json",
//         type: "GET",
//         data: "pagename="+itemTextValue,
//         success: updatePost
//     });
// }

// function getComment() {
//     $.ajax({
//         url: "/socialnetwork/get-comment-json",
//         dataType: "json",
//         type: "GET",
//         success: updateComment
//     });
// }


// function updatePost(posts) {

//     $(posts).each(function () {
//         var id = this.pk;
//         var lastPost = "#postId_" + id;
//         console.log(this.fields.updated_by);
//         $("#postcontent:not(:has(" + lastPost + "))").prepend(
//             '<div class="list" id="postId_' + id + '"><p class="post"><i>Post by <a href="/socialnetwork/profile/' + this.fields.userid+'">' + this.fields.username + '</a>-</i>' + this.fields.text + ' <i>-{{' + this.fields.update_time + '}}</i></p>' +
//             '<div><p class="post_comment"><label for="form2">Comment: </label><input type="text" name="comment_text" id="form2"><button id="commemt-button" onclick=add_comment('+id+')>Submit</button></p></div></div>');
//     });
// }

// function updateComment(comments) {
//     $(comments).each(function () {
//         var post_id = "#postId_" + String(this.fields.post);
//         // console.log(post_id);
//         var comment_id = "#commentId_" + String(this.pk);
//         // console.log(comment_id);
//         console.log("updated_by: "+this.fields.updated_by);
//         $(post_id + ":not(:has(" + comment_id + "))").append(
//             '<div class="comment" id="commentId_' + String(this.pk) + '"><p class="info"> by <a href="/socialnetwork/profile/' + this.fields.userid + '">' + this.fields.username + '</a>' + this.fields.text + '<i>-' + this.fields.update_time + '</i></p></div>');
//     });
// }


// function add_comment(id) {
//     var itemTextElement = $("#form2_"+id);
//     var itemTextValue   = itemTextElement.val();
//     console.log(itemTextValue);
//     // Clear input box and old error message (if any)
//     itemTextElement.val('');
//     displayError('');

//     $.ajax({
//         url: "/socialnetwork/add-comment/"+id,
//         type: "POST",
//         data: "comment_text="+itemTextValue+"&csrfmiddlewaretoken="+getCSRFToken(),
//         dataType : "json",
//         success: function(response) {
//             if (Array.isArray(response)) {
//                 updateComment(response);
//             } else {
//                 displayError(response.error);
//             }
//         }
//     });
// }

function displayError(message) {
    $("#error").html(message);
}

function getCSRFToken() {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
        if (cookies[i].startsWith("csrftoken=")) {
            return cookies[i].substring("csrftoken=".length, cookies[i].length);
        }
    }
    return "unknown";
}


function yesnoCheck() {
    if (document.getElementById('yesCheck_military').checked) {
        document.getElementById('ifYes').style.visibility = 'visible';
        document.getElementById('yesCheck_veteran').style.visibility = 'visible';
    } else {
        document.getElementById('ifYes').style.visibility = 'hidden';
        document.getElementById('yesCheck_veteran').style.visibility = 'hidden';
    }
    if (document.getElementById('yesCheck_veteran').checked) {
        document.getElementById('ifYes_veteran').style.visibility = 'visible';
    }
    else document.getElementById('ifYes_veteran').style.visibility = 'hidden';
}