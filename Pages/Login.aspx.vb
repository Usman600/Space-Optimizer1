Imports System.Text.RegularExpressions

Partial Class Pages_Login
    Inherits System.Web.UI.Page
    Dim model As New Model

#Region "Page Events"
    Private Sub Pages_Login_Load(sender As Object, e As EventArgs) Handles Me.Load
        If Not Page.IsPostBack Then
            Session.RemoveAll()
            ClearFields()
        End If
    End Sub

    Public Sub ClearFields()
        txtEmail.Text = ""
        txtLoginEmail.Text = ""
        txtLoginPassword.Text = ""
        txtName.Text = ""
        txtPassword.Text = ""
        txtPasswordF.Text = ""
        txtEmailF.Text = ""
        txtCodeF.Text = ""
    End Sub
#End Region



End Class
