import tkinter as tk
from tkinter import ttk
import json


def display_results(api_response):
    root = tk.Tk()
    root.title("API Response Table")

    tree = ttk.Treeview(root)
    tree["columns"] = (
        "timestamp", "logs", "posting_instruction_batches", "balances", "account_notes",
        "instantiate_workflow_requests",
        "derived_params", "contract_notification_events", "hook_execution_logs")

    tree.heading("timestamp", text="Timestamp")
    tree.heading("logs", text="Logs")
    tree.heading("posting_instruction_batches", text="Posting Instruction Batches")
    tree.heading("balances", text="Balances")
    tree.heading("account_notes", text="Account Notes")
    tree.heading("instantiate_workflow_requests", text="Instantiate Workflow Requests")
    tree.heading("derived_params", text="Derived Params")
    tree.heading("contract_notification_events", text="Contract Notification Events")
    tree.heading("hook_execution_logs", text="Hook Execution Logs")

    for idx, item in enumerate(api_response):
        result = item['result']
        tree.insert("", "end", iid=idx, values=(
            result["timestamp"],
            len(result["logs"]),
            len(result["posting_instruction_batches"]),
            len(result["balances"]),
            len(result["account_notes"]),
            len(result["instantiate_workflow_requests"]),
            len(result["derived_params"]),
            len(result["contract_notification_events"]),
            len(result["hook_execution_logs"])
        ))

    def show_details(event):
        selected_item = tree.focus()
        item_details = tree.item(selected_item, "values")
        details_window = tk.Toplevel(root)
        details_window.title("Details")

        timestamp_label = tk.Label(details_window, text=f"Timestamp: {item_details[0]}")
        timestamp_label.pack()

        arrays = [
            "logs", "posting_instruction_batches", "balances", "account_notes",
            "instantiate_workflow_requests", "derived_params", "contract_notification_events", "hook_execution_logs"
        ]

        for i, array in enumerate(arrays, 1):
            if int(item_details[i]) > 0:
                btn = tk.Button(details_window, text=f"Show {array} details",
                                command=lambda arr=array: show_array_details(
                                    api_response[int(selected_item)]['result'][arr]))
                btn.pack()

    def show_array_details(array_data):
        array_window = tk.Toplevel(root)
        array_window.title("Array Details")
        text = tk.Text(array_window)
        text.insert(tk.END, json.dumps(array_data, indent=2))
        text.pack(expand=True, fill=tk.BOTH)

    tree.bind("<Double-1>", show_details)
    tree.pack(expand=True, fill=tk.BOTH)

    root.mainloop()