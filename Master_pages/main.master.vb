﻿
Partial Class MasterPage
    Inherits System.Web.UI.MasterPage
    Dim _adminObj As New SessionObject.AdminObj

    Private Sub MasterPage_Load(sender As Object, e As EventArgs) Handles Me.Load
        _adminObj = CType(Session.Item("AdminObj"), SessionObject.AdminObj)
        If _adminObj.SessionID IsNot Nothing Then
            btnLogin.Text = "Logout"
        Else
            btnLogin.Text = "Login"
        End If
    End Sub
    
    
End Class
