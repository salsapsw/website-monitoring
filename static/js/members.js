document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".delete-btn").forEach(function (btn) {
    btn.addEventListener("click", function (event) {
      event.preventDefault();
      if (confirm("Are you sure to delete this user?")) {
        window.location.href = btn.getAttribute("href");
      }
    });
  });
});

function openEditModal(username, email, role) {
  $("#editUsername").val(username);
  $("#editEmail").val(email);
  $("#editRole").val(role);
  $("#editModal").modal("show");
}

function saveChanges() {
  // Implementasi penyimpanan perubahan di sini
  // Misalnya, Anda dapat menggunakan Ajax untuk mengirim data ke server.
  // Setelah menyimpan, Anda mungkin ingin memperbarui tampilan tabel.
  // Anda juga dapat menutup modal setelah penyimpanan berhasil.
  $("#editModal").modal("hide");
}

$(".btn-edit-role").click(function () {
  var userId = $(this).data("user-id");
  var modalSelector = "#editRoleModal" + userId;

  // Retrieve form data or perform any other actions before submitting the form

  // Submit form using Ajax
  $.ajax({
    type: "POST",
    url: "/path/to/edit_role/" + userId + "/",
    data: $("#editRoleForm" + userId).serialize(),
    success: function (data) {
      if (data.success) {
        // If the server responds with success, close the modal
        $(modalSelector).modal("hide");
        // Optionally, you can update the UI as needed
      } else {
        // If there are errors, display them or handle them appropriately
        console.error(data.errors);
      }
    },
    error: function (error) {
      console.error("Error:", error);
    },
  });
});

document.addEventListener("DOMContentLoaded", function () {
  var searchInput = document.getElementById("searchInput");
  var searchForm = document.getElementById("searchForm");

  searchInput.addEventListener("input", function () {
    if (searchInput.value === "") {
      // Jika input dikosongkan, kirim formulir secara otomatis
      searchForm.submit();
    }
  });
});

document.addEventListener("DOMContentLoaded", function () {
  var editRoleModal = new bootstrap.Modal(document.getElementById("editRoleModal"));
  var editRoleForm = document.getElementById("editRoleForm");
  var editRoleBtns = document.querySelectorAll(".edit-role-btn");

  editRoleBtns.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var userId = btn.getAttribute("data-user-id");
      editRoleForm.action = "/setting/edit_role/" + userId + "/";
      editRoleModal.show();
    });
  });
});
