import pandas as pd

from typing import Dict, Self
from .sds import SDS
from .search import Search
from .plot import Plot
from .utilities import (
    validate_date,
)
from .database import *


class Convert(Search):
    def __init__(self, input_dir: str, directory_structure: str, network: str = 'VG', station: str = '*',
                 channel: str = '*', location: str = '*', output_directory: str = None,
                 min_completeness: float = 70, save_to_database: bool = True, plot_seismogram: bool = True,
                 plot_type: str = 'normal'):
        """Seismic convert class

        Convert CVGHM various seismic data structure into Seiscomp Data Structure (SDS)

        Args:
            input_dir (str): input directory path
            directory_structure (str): input directory structure
            network (str): input network name
            station (str): input station name
            channel (str): input channel name
            min_completeness (float): minimum data completeness
            location (str): input location name
            save_to_database (bool, optional): if to save to database. Defaults to True.
            plot_seismogram (bool, optional): if to plot the seismogram plots. Defaults to True.
            plot_type (str, optional): type of plot. Defaults to 'normal'.
        """

        super().__init__(
            input_dir=input_dir,
            directory_structure=directory_structure,
            network=network,
            station=station,
            channel=channel,
            location=location,
        )

        self.min_completeness = min_completeness
        self.output_dir = output_directory
        self.new_channel: str | None = None
        self.success: list[Dict[str, Any]] = []
        self.failed: list[Dict[str, Any]] = []

        self.dates: pd.DatetimeIndex | None = None

        self.save_to_database = save_to_database
        self.database: Database | None = None
        if save_to_database is True:
            db.connect(reuse_if_open=True)
            db.create_tables([Station, Sds])
            db.close()

        self.plot_seismogram = plot_seismogram
        self.plot_type = plot_type

    def between_dates(self, start_date: str, end_date: str) -> Self:
        """Convert seismic between two range of dates.

        Args:
            start_date (str): start date in yyyy-mm-dd
            end_date (str): end date in yyyy-mm-dd

        Returns:
            Self
        """
        validate_date(start_date)
        validate_date(end_date)

        self.dates: pd.DatetimeIndex = pd.date_range(start_date, end_date)

        return self

    def run(self) -> Self:
        """Run converter.

        Returns:
            Self
        """
        assert isinstance(self.dates, pd.DatetimeIndex), "Please set start and end date using between_dates() method."

        for _date in self.dates:
            date_str: str = _date.strftime('%Y-%m-%d')
            self._run(date_str)

        # Save to database
        if self.save_to_database is True:
            print(f"\n💽⌛ Update database..")
            if len(self.success) > 0:
                self.database = Database(sds_results=self.success).update()
                print(f"💽✅ Finish updating database!")
            else:
                print(f"⚠️ Nothing to update in database.")

        return self

    def _run(self, date_str: str, **kwargs) -> None:
        """Convert for specific date.

        Args:
            date_str (str): Date format in yyyy-mm-dd
            **kwargs (dict): Keyword arguments save in Obspy

        Returns:
            None
        """
        min_completeness = self.min_completeness
        stream = self.search(date_str)
        for trace in stream:

            if trace.stats.channel[0] not in ['M', 'O']:
                sds: SDS = SDS(
                    output_dir=self.output_dir,
                    directory_structure=self.directory_structure,
                    trace=trace,
                    date_str=date_str,
                    channel=self.channel,
                    station=self.station,
                    location=self.location,
                    network=self.network,
                )

                if sds.save(min_completeness=min_completeness, **kwargs) is True:
                    self.success.append(sds.results)

                    if self.plot_seismogram is True:
                        Plot(
                            sds=sds,
                            plot_type=self.plot_type
                        ).save()

                else:
                    self.failed.append(sds.results)

    def fix_channel_to(self, new_channel: str) -> Self:
        """Fix channel name

        Args:
            new_channel (str): new channel name

        Returns:
            Self: Convert class
        """
        self.new_channel = new_channel
        return self
