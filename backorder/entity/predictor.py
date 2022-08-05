from backorder.exception import BackorderPredictionException
from backorder.util.util import load_object
import pandas as pd
import sys
import os


class BackorderData:

    def __init__(self,
                sku : int,
                national_inv: int,
                lead_time: int,
                in_transit_qty: int,
                forecast_3_month: int,
                forecast_6_month: int,
                forecast_9_month: int,
                sales_1_month: int,
                sales_3_month: int,
                sales_6_month: int,
                sales_9_month: int,
                min_bank: int,
                potential_issue: object,
                pieces_past_due: int,
                perf_6_month_avg: float,
                perf_12_month_avg: float,
                local_bo_qty: int,
                deck_risk: object,
                oe_constraint: object,
                ppap_risk: object,
                stop_auto_buy: object,
                rev_stop: object,
                went_on_backorder: object):

        try:
            self.sku = sku
            self.national_inv = national_inv
            self.lead_time = lead_time
            self.in_transit_qty = in_transit_qty
            self.forecast_3_month = forecast_3_month
            self.forecast_6_month =  forecast_6_month
            self. forecast_9_month =  forecast_9_month
            self.sales_1_month = sales_1_month
            self.sales_3_month = sales_3_month
            self.sales_6_month = sales_6_month
            self.sales_9_month = sales_9_month
            self.min_bank = min_bank
            self.potential_issue = potential_issue
            self.pieces_past_due = pieces_past_due
            self.perf_6_month_avg = perf_6_month_avg
            self.perf_12_month_avg = perf_12_month_avg
            self.local_bo_qty = local_bo_qty
            self.deck_risk = deck_risk
            self.oe_constraint = oe_constraint
            self.ppap_risk = ppap_risk
            self.stop_auto_buy = stop_auto_buy
            self.rev_stop = rev_stop
            self.went_on_backorder = went_on_backorder
        except Exception as e:
            raise BackorderPredictionException(e, sys) from e

    def get_backorder_input_data_frame(self):

        try:
            backorder_input_dict = self.get_backorder_data_as_dict()
            return pd.DataFrame(backorder_input_dict)
        except Exception as e:
            raise BackorderPredictionException(e, sys) from e

    def get_backorder_data_as_dict(self):
        try:
            input_data = {
                "sku": [self.sku], 
                "national_inv": [self.national_inv],
                "lead_time": [self.lead_time], 
                "in_transit_qty": [self.in_transit_qty], 
                "forecast_3_month": [self.forecast_3_month], 
                "forecast_6_month": [self.forecast_6_month], 
                "forecast_9_month": [self. forecast_9_month], 
                "sales_1_month": [self.sales_1_month], 
                "sales_3_month": [self.sales_3_month], 
                "sales_6_month": [self.sales_6_month], 
                "sales_9_month": [self.sales_9_month], 
                "min_bank": [self.min_bank],
                "potential_issue": [self.potential_issue], 
                "pieces_past_due": [self.pieces_past_due], 
                "perf_6_month_avg": [self.perf_6_month_avg], 
                "perf_12_month_avg": [self.perf_12_month_avg], 
                "local_bo_qty": [self.local_bo_qty], 
                "deck_risk": [self.deck_risk], 
                "oe_constraint": [self.oe_constraint], 
                "ppap_risk": [self.ppap_risk], 
                "stop_auto_buy": [self.stop_auto_buy], 
                "rev_stop": [self.rev_stop], 
                "went_on_backorder": [self.went_on_backorder]}
            return input_data
        except Exception as e:
            raise BackorderPredictionException(e, sys)


class BackorderPredictor:

    def __init__(self, model_dir: str):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise BackorderPredictionException(e, sys) from e

    def get_latest_model_path(self):
        try:
            folder_name = list(map(int, os.listdir(self.model_dir)))
            latest_model_dir = os.path.join(self.model_dir, f"{max(folder_name)}")
            file_name = os.listdir(latest_model_dir)[0]
            latest_model_path = os.path.join(latest_model_dir, file_name)
            return latest_model_path
        except Exception as e:
            raise BackorderPredictionException(e, sys) from e

    def predict(self, X):
        try:
            model_path = self.get_latest_model_path()
            model = load_object(file_path=model_path)
            backorder = model.predict(X)
            return backorder
        except Exception as e:
            raise BackorderPredictionException(e, sys) from e