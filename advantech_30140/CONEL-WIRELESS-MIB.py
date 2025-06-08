# SNMP MIB module (CONEL-WIRELESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/advantech_30140/CONEL-WIRELESS-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:15:06 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Conel_ObjectIdentity = ObjectIdentity
conel = _Conel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140)
)
_Wireless_ObjectIdentity = ObjectIdentity
wireless = _Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 4)
)


class _WirelessStatus_Type(Integer32):
    """Custom type wirelessStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("noService", 0),
          ("availableGPRS", 1),
          ("attachedGPRS", 2),
          ("availableEDGE", 3),
          ("attachedEDGE", 4),
          ("availableUMTS", 5),
          ("attachedUMTS", 6),
          ("availableHSDPA", 7),
          ("attachedHSDPA", 8),
          ("availableHSUPA", 9),
          ("attachedHSUPA", 10),
          ("availableHSPA", 11),
          ("attachedHSPA", 12),
          ("availableLTE", 13),
          ("attachedLTE", 14),
          ("availableCDMA", 15),
          ("attachedCDMA", 16))
    )


_WirelessStatus_Type.__name__ = "Integer32"
_WirelessStatus_Object = MibScalar
wirelessStatus = _WirelessStatus_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 1),
    _WirelessStatus_Type()
)
wirelessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessStatus.setStatus("current")
_WirelessPLMN_Type = OctetString
_WirelessPLMN_Object = MibScalar
wirelessPLMN = _WirelessPLMN_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 2),
    _WirelessPLMN_Type()
)
wirelessPLMN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPLMN.setStatus("current")
_WirelessCell_Type = OctetString
_WirelessCell_Object = MibScalar
wirelessCell = _WirelessCell_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 3),
    _WirelessCell_Type()
)
wirelessCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessCell.setStatus("current")
_WirelessChannel_Type = OctetString
_WirelessChannel_Object = MibScalar
wirelessChannel = _WirelessChannel_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 4),
    _WirelessChannel_Type()
)
wirelessChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessChannel.setStatus("current")
_WirelessLevel_Type = Integer32
_WirelessLevel_Object = MibScalar
wirelessLevel = _WirelessLevel_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 5),
    _WirelessLevel_Type()
)
wirelessLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLevel.setStatus("current")
_WirelessChannelN1_Type = OctetString
_WirelessChannelN1_Object = MibScalar
wirelessChannelN1 = _WirelessChannelN1_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 6),
    _WirelessChannelN1_Type()
)
wirelessChannelN1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessChannelN1.setStatus("current")
_WirelessLevelN1_Type = Integer32
_WirelessLevelN1_Object = MibScalar
wirelessLevelN1 = _WirelessLevelN1_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 7),
    _WirelessLevelN1_Type()
)
wirelessLevelN1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLevelN1.setStatus("current")
_WirelessChannelN2_Type = OctetString
_WirelessChannelN2_Object = MibScalar
wirelessChannelN2 = _WirelessChannelN2_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 8),
    _WirelessChannelN2_Type()
)
wirelessChannelN2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessChannelN2.setStatus("current")
_WirelessLevelN2_Type = Integer32
_WirelessLevelN2_Object = MibScalar
wirelessLevelN2 = _WirelessLevelN2_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 9),
    _WirelessLevelN2_Type()
)
wirelessLevelN2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLevelN2.setStatus("current")
_WirelessChannelN3_Type = OctetString
_WirelessChannelN3_Object = MibScalar
wirelessChannelN3 = _WirelessChannelN3_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 10),
    _WirelessChannelN3_Type()
)
wirelessChannelN3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessChannelN3.setStatus("current")
_WirelessLevelN3_Type = Integer32
_WirelessLevelN3_Object = MibScalar
wirelessLevelN3 = _WirelessLevelN3_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 11),
    _WirelessLevelN3_Type()
)
wirelessLevelN3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLevelN3.setStatus("current")
_WirelessChannelN4_Type = OctetString
_WirelessChannelN4_Object = MibScalar
wirelessChannelN4 = _WirelessChannelN4_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 12),
    _WirelessChannelN4_Type()
)
wirelessChannelN4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessChannelN4.setStatus("current")
_WirelessLevelN4_Type = Integer32
_WirelessLevelN4_Object = MibScalar
wirelessLevelN4 = _WirelessLevelN4_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 13),
    _WirelessLevelN4_Type()
)
wirelessLevelN4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLevelN4.setStatus("current")
_WirelessChannelN5_Type = OctetString
_WirelessChannelN5_Object = MibScalar
wirelessChannelN5 = _WirelessChannelN5_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 14),
    _WirelessChannelN5_Type()
)
wirelessChannelN5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessChannelN5.setStatus("current")
_WirelessLevelN5_Type = Integer32
_WirelessLevelN5_Object = MibScalar
wirelessLevelN5 = _WirelessLevelN5_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 15),
    _WirelessLevelN5_Type()
)
wirelessLevelN5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLevelN5.setStatus("current")
_WirelessUpTime_Type = TimeTicks
_WirelessUpTime_Object = MibScalar
wirelessUpTime = _WirelessUpTime_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 16),
    _WirelessUpTime_Type()
)
wirelessUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessUpTime.setStatus("current")
_WirelessConnect_Type = Counter32
_WirelessConnect_Object = MibScalar
wirelessConnect = _WirelessConnect_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 17),
    _WirelessConnect_Type()
)
wirelessConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessConnect.setStatus("current")
_WirelessDisconnect_Type = Counter32
_WirelessDisconnect_Object = MibScalar
wirelessDisconnect = _WirelessDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 18),
    _WirelessDisconnect_Type()
)
wirelessDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessDisconnect.setStatus("current")


class _WirelessCard_Type(Integer32):
    """Custom type wirelessCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("primary", 0),
          ("secondary", 1))
    )


_WirelessCard_Type.__name__ = "Integer32"
_WirelessCard_Object = MibScalar
wirelessCard = _WirelessCard_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 19),
    _WirelessCard_Type()
)
wirelessCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessCard.setStatus("current")
_WirelessIPAddress_Type = IpAddress
_WirelessIPAddress_Object = MibScalar
wirelessIPAddress = _WirelessIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 20),
    _WirelessIPAddress_Type()
)
wirelessIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessIPAddress.setStatus("current")
_WirelessLatency_Type = Integer32
_WirelessLatency_Object = MibScalar
wirelessLatency = _WirelessLatency_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 21),
    _WirelessLatency_Type()
)
wirelessLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLatency.setStatus("current")
_WirelessReportPeriod_Type = Integer32
_WirelessReportPeriod_Object = MibScalar
wirelessReportPeriod = _WirelessReportPeriod_Object(
    (1, 3, 6, 1, 4, 1, 30140, 4, 22),
    _WirelessReportPeriod_Type()
)
wirelessReportPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessReportPeriod.setStatus("current")
_Wireless_2_ObjectIdentity = ObjectIdentity
wireless_2 = _Wireless_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 5)
)
_WirelessToday_ObjectIdentity = ObjectIdentity
wirelessToday = _WirelessToday_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1)
)
_WirelessTodayRxPri_Type = Counter32
_WirelessTodayRxPri_Object = MibScalar
wirelessTodayRxPri = _WirelessTodayRxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 1),
    _WirelessTodayRxPri_Type()
)
wirelessTodayRxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessTodayRxPri.setStatus("current")
_WirelessTodayRxSec_Type = Counter32
_WirelessTodayRxSec_Object = MibScalar
wirelessTodayRxSec = _WirelessTodayRxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 2),
    _WirelessTodayRxSec_Type()
)
wirelessTodayRxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessTodayRxSec.setStatus("current")
_WirelessTodayTxPri_Type = Counter32
_WirelessTodayTxPri_Object = MibScalar
wirelessTodayTxPri = _WirelessTodayTxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 3),
    _WirelessTodayTxPri_Type()
)
wirelessTodayTxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessTodayTxPri.setStatus("current")
_WirelessTodayTxSec_Type = Counter32
_WirelessTodayTxSec_Object = MibScalar
wirelessTodayTxSec = _WirelessTodayTxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 4),
    _WirelessTodayTxSec_Type()
)
wirelessTodayTxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessTodayTxSec.setStatus("current")
_WirelessTodayConnectionsPri_Type = Counter32
_WirelessTodayConnectionsPri_Object = MibScalar
wirelessTodayConnectionsPri = _WirelessTodayConnectionsPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 5),
    _WirelessTodayConnectionsPri_Type()
)
wirelessTodayConnectionsPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessTodayConnectionsPri.setStatus("current")
_WirelessTodayConnectionsSec_Type = Counter32
_WirelessTodayConnectionsSec_Object = MibScalar
wirelessTodayConnectionsSec = _WirelessTodayConnectionsSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 6),
    _WirelessTodayConnectionsSec_Type()
)
wirelessTodayConnectionsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessTodayConnectionsSec.setStatus("current")
_WirelessTodayOnlinePri_Type = TimeTicks
_WirelessTodayOnlinePri_Object = MibScalar
wirelessTodayOnlinePri = _WirelessTodayOnlinePri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 7),
    _WirelessTodayOnlinePri_Type()
)
wirelessTodayOnlinePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessTodayOnlinePri.setStatus("current")
_WirelessTodayOnlineSec_Type = TimeTicks
_WirelessTodayOnlineSec_Object = MibScalar
wirelessTodayOnlineSec = _WirelessTodayOnlineSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 8),
    _WirelessTodayOnlineSec_Type()
)
wirelessTodayOnlineSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessTodayOnlineSec.setStatus("current")
_WirelessTodayOffline_Type = TimeTicks
_WirelessTodayOffline_Object = MibScalar
wirelessTodayOffline = _WirelessTodayOffline_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 9),
    _WirelessTodayOffline_Type()
)
wirelessTodayOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessTodayOffline.setStatus("current")
_WirelessTodayCells_Type = Counter32
_WirelessTodayCells_Object = MibScalar
wirelessTodayCells = _WirelessTodayCells_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 10),
    _WirelessTodayCells_Type()
)
wirelessTodayCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessTodayCells.setStatus("current")
_WirelessTodayLevelAvg_Type = Integer32
_WirelessTodayLevelAvg_Object = MibScalar
wirelessTodayLevelAvg = _WirelessTodayLevelAvg_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 11),
    _WirelessTodayLevelAvg_Type()
)
wirelessTodayLevelAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessTodayLevelAvg.setStatus("current")
_WirelessTodayLevelMin_Type = Integer32
_WirelessTodayLevelMin_Object = MibScalar
wirelessTodayLevelMin = _WirelessTodayLevelMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 12),
    _WirelessTodayLevelMin_Type()
)
wirelessTodayLevelMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessTodayLevelMin.setStatus("current")
_WirelessTodayLevelMax_Type = Integer32
_WirelessTodayLevelMax_Object = MibScalar
wirelessTodayLevelMax = _WirelessTodayLevelMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 13),
    _WirelessTodayLevelMax_Type()
)
wirelessTodayLevelMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessTodayLevelMax.setStatus("current")
_WirelessTodayDateMin_Type = Counter32
_WirelessTodayDateMin_Object = MibScalar
wirelessTodayDateMin = _WirelessTodayDateMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 14),
    _WirelessTodayDateMin_Type()
)
wirelessTodayDateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessTodayDateMin.setStatus("current")
_WirelessTodayDateMax_Type = Counter32
_WirelessTodayDateMax_Object = MibScalar
wirelessTodayDateMax = _WirelessTodayDateMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 1, 15),
    _WirelessTodayDateMax_Type()
)
wirelessTodayDateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessTodayDateMax.setStatus("current")
_WirelessYesterday_ObjectIdentity = ObjectIdentity
wirelessYesterday = _WirelessYesterday_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2)
)
_WirelessYesterdayRxPri_Type = Counter32
_WirelessYesterdayRxPri_Object = MibScalar
wirelessYesterdayRxPri = _WirelessYesterdayRxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 1),
    _WirelessYesterdayRxPri_Type()
)
wirelessYesterdayRxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessYesterdayRxPri.setStatus("current")
_WirelessYesterdayRxSec_Type = Counter32
_WirelessYesterdayRxSec_Object = MibScalar
wirelessYesterdayRxSec = _WirelessYesterdayRxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 2),
    _WirelessYesterdayRxSec_Type()
)
wirelessYesterdayRxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessYesterdayRxSec.setStatus("current")
_WirelessYesterdayTxPri_Type = Counter32
_WirelessYesterdayTxPri_Object = MibScalar
wirelessYesterdayTxPri = _WirelessYesterdayTxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 3),
    _WirelessYesterdayTxPri_Type()
)
wirelessYesterdayTxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessYesterdayTxPri.setStatus("current")
_WirelessYesterdayTxSec_Type = Counter32
_WirelessYesterdayTxSec_Object = MibScalar
wirelessYesterdayTxSec = _WirelessYesterdayTxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 4),
    _WirelessYesterdayTxSec_Type()
)
wirelessYesterdayTxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessYesterdayTxSec.setStatus("current")
_WirelessYesterdayConnectionsPri_Type = Counter32
_WirelessYesterdayConnectionsPri_Object = MibScalar
wirelessYesterdayConnectionsPri = _WirelessYesterdayConnectionsPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 5),
    _WirelessYesterdayConnectionsPri_Type()
)
wirelessYesterdayConnectionsPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessYesterdayConnectionsPri.setStatus("current")
_WirelessYesterdayConnectionsSec_Type = Counter32
_WirelessYesterdayConnectionsSec_Object = MibScalar
wirelessYesterdayConnectionsSec = _WirelessYesterdayConnectionsSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 6),
    _WirelessYesterdayConnectionsSec_Type()
)
wirelessYesterdayConnectionsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessYesterdayConnectionsSec.setStatus("current")
_WirelessYesterdayOnlinePri_Type = TimeTicks
_WirelessYesterdayOnlinePri_Object = MibScalar
wirelessYesterdayOnlinePri = _WirelessYesterdayOnlinePri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 7),
    _WirelessYesterdayOnlinePri_Type()
)
wirelessYesterdayOnlinePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessYesterdayOnlinePri.setStatus("current")
_WirelessYesterdayOnlineSec_Type = TimeTicks
_WirelessYesterdayOnlineSec_Object = MibScalar
wirelessYesterdayOnlineSec = _WirelessYesterdayOnlineSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 8),
    _WirelessYesterdayOnlineSec_Type()
)
wirelessYesterdayOnlineSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessYesterdayOnlineSec.setStatus("current")
_WirelessYesterdayOffline_Type = TimeTicks
_WirelessYesterdayOffline_Object = MibScalar
wirelessYesterdayOffline = _WirelessYesterdayOffline_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 9),
    _WirelessYesterdayOffline_Type()
)
wirelessYesterdayOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessYesterdayOffline.setStatus("current")
_WirelessYesterdayCells_Type = Counter32
_WirelessYesterdayCells_Object = MibScalar
wirelessYesterdayCells = _WirelessYesterdayCells_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 10),
    _WirelessYesterdayCells_Type()
)
wirelessYesterdayCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessYesterdayCells.setStatus("current")
_WirelessYesterdayLevelAvg_Type = Integer32
_WirelessYesterdayLevelAvg_Object = MibScalar
wirelessYesterdayLevelAvg = _WirelessYesterdayLevelAvg_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 11),
    _WirelessYesterdayLevelAvg_Type()
)
wirelessYesterdayLevelAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessYesterdayLevelAvg.setStatus("current")
_WirelessYesterdayLevelMin_Type = Integer32
_WirelessYesterdayLevelMin_Object = MibScalar
wirelessYesterdayLevelMin = _WirelessYesterdayLevelMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 12),
    _WirelessYesterdayLevelMin_Type()
)
wirelessYesterdayLevelMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessYesterdayLevelMin.setStatus("current")
_WirelessYesterdayLevelMax_Type = Integer32
_WirelessYesterdayLevelMax_Object = MibScalar
wirelessYesterdayLevelMax = _WirelessYesterdayLevelMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 13),
    _WirelessYesterdayLevelMax_Type()
)
wirelessYesterdayLevelMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessYesterdayLevelMax.setStatus("current")
_WirelessYesterdayDateMin_Type = Counter32
_WirelessYesterdayDateMin_Object = MibScalar
wirelessYesterdayDateMin = _WirelessYesterdayDateMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 14),
    _WirelessYesterdayDateMin_Type()
)
wirelessYesterdayDateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessYesterdayDateMin.setStatus("current")
_WirelessYesterdayDateMax_Type = Counter32
_WirelessYesterdayDateMax_Object = MibScalar
wirelessYesterdayDateMax = _WirelessYesterdayDateMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 2, 15),
    _WirelessYesterdayDateMax_Type()
)
wirelessYesterdayDateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessYesterdayDateMax.setStatus("current")
_WirelessThisWeek_ObjectIdentity = ObjectIdentity
wirelessThisWeek = _WirelessThisWeek_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3)
)
_WirelessThisWeekRxPri_Type = Counter32
_WirelessThisWeekRxPri_Object = MibScalar
wirelessThisWeekRxPri = _WirelessThisWeekRxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 1),
    _WirelessThisWeekRxPri_Type()
)
wirelessThisWeekRxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisWeekRxPri.setStatus("current")
_WirelessThisWeekRxSec_Type = Counter32
_WirelessThisWeekRxSec_Object = MibScalar
wirelessThisWeekRxSec = _WirelessThisWeekRxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 2),
    _WirelessThisWeekRxSec_Type()
)
wirelessThisWeekRxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisWeekRxSec.setStatus("current")
_WirelessThisWeekTxPri_Type = Counter32
_WirelessThisWeekTxPri_Object = MibScalar
wirelessThisWeekTxPri = _WirelessThisWeekTxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 3),
    _WirelessThisWeekTxPri_Type()
)
wirelessThisWeekTxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisWeekTxPri.setStatus("current")
_WirelessThisWeekTxSec_Type = Counter32
_WirelessThisWeekTxSec_Object = MibScalar
wirelessThisWeekTxSec = _WirelessThisWeekTxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 4),
    _WirelessThisWeekTxSec_Type()
)
wirelessThisWeekTxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisWeekTxSec.setStatus("current")
_WirelessThisWeekConnectionsPri_Type = Counter32
_WirelessThisWeekConnectionsPri_Object = MibScalar
wirelessThisWeekConnectionsPri = _WirelessThisWeekConnectionsPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 5),
    _WirelessThisWeekConnectionsPri_Type()
)
wirelessThisWeekConnectionsPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisWeekConnectionsPri.setStatus("current")
_WirelessThisWeekConnectionsSec_Type = Counter32
_WirelessThisWeekConnectionsSec_Object = MibScalar
wirelessThisWeekConnectionsSec = _WirelessThisWeekConnectionsSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 6),
    _WirelessThisWeekConnectionsSec_Type()
)
wirelessThisWeekConnectionsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisWeekConnectionsSec.setStatus("current")
_WirelessThisWeekOnlinePri_Type = TimeTicks
_WirelessThisWeekOnlinePri_Object = MibScalar
wirelessThisWeekOnlinePri = _WirelessThisWeekOnlinePri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 7),
    _WirelessThisWeekOnlinePri_Type()
)
wirelessThisWeekOnlinePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisWeekOnlinePri.setStatus("current")
_WirelessThisWeekOnlineSec_Type = TimeTicks
_WirelessThisWeekOnlineSec_Object = MibScalar
wirelessThisWeekOnlineSec = _WirelessThisWeekOnlineSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 8),
    _WirelessThisWeekOnlineSec_Type()
)
wirelessThisWeekOnlineSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisWeekOnlineSec.setStatus("current")
_WirelessThisWeekOffline_Type = TimeTicks
_WirelessThisWeekOffline_Object = MibScalar
wirelessThisWeekOffline = _WirelessThisWeekOffline_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 9),
    _WirelessThisWeekOffline_Type()
)
wirelessThisWeekOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisWeekOffline.setStatus("current")
_WirelessThisWeekCells_Type = Counter32
_WirelessThisWeekCells_Object = MibScalar
wirelessThisWeekCells = _WirelessThisWeekCells_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 10),
    _WirelessThisWeekCells_Type()
)
wirelessThisWeekCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisWeekCells.setStatus("current")
_WirelessThisWeekLevelAvg_Type = Integer32
_WirelessThisWeekLevelAvg_Object = MibScalar
wirelessThisWeekLevelAvg = _WirelessThisWeekLevelAvg_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 11),
    _WirelessThisWeekLevelAvg_Type()
)
wirelessThisWeekLevelAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisWeekLevelAvg.setStatus("current")
_WirelessThisWeekLevelMin_Type = Integer32
_WirelessThisWeekLevelMin_Object = MibScalar
wirelessThisWeekLevelMin = _WirelessThisWeekLevelMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 12),
    _WirelessThisWeekLevelMin_Type()
)
wirelessThisWeekLevelMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisWeekLevelMin.setStatus("current")
_WirelessThisWeekLevelMax_Type = Integer32
_WirelessThisWeekLevelMax_Object = MibScalar
wirelessThisWeekLevelMax = _WirelessThisWeekLevelMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 13),
    _WirelessThisWeekLevelMax_Type()
)
wirelessThisWeekLevelMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisWeekLevelMax.setStatus("current")
_WirelessThisWeekDateMin_Type = Counter32
_WirelessThisWeekDateMin_Object = MibScalar
wirelessThisWeekDateMin = _WirelessThisWeekDateMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 14),
    _WirelessThisWeekDateMin_Type()
)
wirelessThisWeekDateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisWeekDateMin.setStatus("current")
_WirelessThisWeekDateMax_Type = Counter32
_WirelessThisWeekDateMax_Object = MibScalar
wirelessThisWeekDateMax = _WirelessThisWeekDateMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 3, 15),
    _WirelessThisWeekDateMax_Type()
)
wirelessThisWeekDateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisWeekDateMax.setStatus("current")
_WirelessLastWeek_ObjectIdentity = ObjectIdentity
wirelessLastWeek = _WirelessLastWeek_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4)
)
_WirelessLastWeekRxPri_Type = Counter32
_WirelessLastWeekRxPri_Object = MibScalar
wirelessLastWeekRxPri = _WirelessLastWeekRxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 1),
    _WirelessLastWeekRxPri_Type()
)
wirelessLastWeekRxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastWeekRxPri.setStatus("current")
_WirelessLastWeekRxSec_Type = Counter32
_WirelessLastWeekRxSec_Object = MibScalar
wirelessLastWeekRxSec = _WirelessLastWeekRxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 2),
    _WirelessLastWeekRxSec_Type()
)
wirelessLastWeekRxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastWeekRxSec.setStatus("current")
_WirelessLastWeekTxPri_Type = Counter32
_WirelessLastWeekTxPri_Object = MibScalar
wirelessLastWeekTxPri = _WirelessLastWeekTxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 3),
    _WirelessLastWeekTxPri_Type()
)
wirelessLastWeekTxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastWeekTxPri.setStatus("current")
_WirelessLastWeekTxSec_Type = Counter32
_WirelessLastWeekTxSec_Object = MibScalar
wirelessLastWeekTxSec = _WirelessLastWeekTxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 4),
    _WirelessLastWeekTxSec_Type()
)
wirelessLastWeekTxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastWeekTxSec.setStatus("current")
_WirelessLastWeekConnectionsPri_Type = Counter32
_WirelessLastWeekConnectionsPri_Object = MibScalar
wirelessLastWeekConnectionsPri = _WirelessLastWeekConnectionsPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 5),
    _WirelessLastWeekConnectionsPri_Type()
)
wirelessLastWeekConnectionsPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastWeekConnectionsPri.setStatus("current")
_WirelessLastWeekConnectionsSec_Type = Counter32
_WirelessLastWeekConnectionsSec_Object = MibScalar
wirelessLastWeekConnectionsSec = _WirelessLastWeekConnectionsSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 6),
    _WirelessLastWeekConnectionsSec_Type()
)
wirelessLastWeekConnectionsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastWeekConnectionsSec.setStatus("current")
_WirelessLastWeekOnlinePri_Type = TimeTicks
_WirelessLastWeekOnlinePri_Object = MibScalar
wirelessLastWeekOnlinePri = _WirelessLastWeekOnlinePri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 7),
    _WirelessLastWeekOnlinePri_Type()
)
wirelessLastWeekOnlinePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastWeekOnlinePri.setStatus("current")
_WirelessLastWeekOnlineSec_Type = TimeTicks
_WirelessLastWeekOnlineSec_Object = MibScalar
wirelessLastWeekOnlineSec = _WirelessLastWeekOnlineSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 8),
    _WirelessLastWeekOnlineSec_Type()
)
wirelessLastWeekOnlineSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastWeekOnlineSec.setStatus("current")
_WirelessLastWeekOffline_Type = TimeTicks
_WirelessLastWeekOffline_Object = MibScalar
wirelessLastWeekOffline = _WirelessLastWeekOffline_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 9),
    _WirelessLastWeekOffline_Type()
)
wirelessLastWeekOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastWeekOffline.setStatus("current")
_WirelessLastWeekCells_Type = Counter32
_WirelessLastWeekCells_Object = MibScalar
wirelessLastWeekCells = _WirelessLastWeekCells_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 10),
    _WirelessLastWeekCells_Type()
)
wirelessLastWeekCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastWeekCells.setStatus("current")
_WirelessLastWeekLevelAvg_Type = Integer32
_WirelessLastWeekLevelAvg_Object = MibScalar
wirelessLastWeekLevelAvg = _WirelessLastWeekLevelAvg_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 11),
    _WirelessLastWeekLevelAvg_Type()
)
wirelessLastWeekLevelAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastWeekLevelAvg.setStatus("current")
_WirelessLastWeekLevelMin_Type = Integer32
_WirelessLastWeekLevelMin_Object = MibScalar
wirelessLastWeekLevelMin = _WirelessLastWeekLevelMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 12),
    _WirelessLastWeekLevelMin_Type()
)
wirelessLastWeekLevelMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastWeekLevelMin.setStatus("current")
_WirelessLastWeekLevelMax_Type = Integer32
_WirelessLastWeekLevelMax_Object = MibScalar
wirelessLastWeekLevelMax = _WirelessLastWeekLevelMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 13),
    _WirelessLastWeekLevelMax_Type()
)
wirelessLastWeekLevelMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastWeekLevelMax.setStatus("current")
_WirelessLastWeekDateMin_Type = Counter32
_WirelessLastWeekDateMin_Object = MibScalar
wirelessLastWeekDateMin = _WirelessLastWeekDateMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 14),
    _WirelessLastWeekDateMin_Type()
)
wirelessLastWeekDateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastWeekDateMin.setStatus("current")
_WirelessLastWeekDateMax_Type = Counter32
_WirelessLastWeekDateMax_Object = MibScalar
wirelessLastWeekDateMax = _WirelessLastWeekDateMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 4, 15),
    _WirelessLastWeekDateMax_Type()
)
wirelessLastWeekDateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastWeekDateMax.setStatus("current")
_WirelessThisPeriod_ObjectIdentity = ObjectIdentity
wirelessThisPeriod = _WirelessThisPeriod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5)
)
_WirelessThisPeriodRxPri_Type = Counter32
_WirelessThisPeriodRxPri_Object = MibScalar
wirelessThisPeriodRxPri = _WirelessThisPeriodRxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 1),
    _WirelessThisPeriodRxPri_Type()
)
wirelessThisPeriodRxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisPeriodRxPri.setStatus("current")
_WirelessThisPeriodRxSec_Type = Counter32
_WirelessThisPeriodRxSec_Object = MibScalar
wirelessThisPeriodRxSec = _WirelessThisPeriodRxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 2),
    _WirelessThisPeriodRxSec_Type()
)
wirelessThisPeriodRxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisPeriodRxSec.setStatus("current")
_WirelessThisPeriodTxPri_Type = Counter32
_WirelessThisPeriodTxPri_Object = MibScalar
wirelessThisPeriodTxPri = _WirelessThisPeriodTxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 3),
    _WirelessThisPeriodTxPri_Type()
)
wirelessThisPeriodTxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisPeriodTxPri.setStatus("current")
_WirelessThisPeriodTxSec_Type = Counter32
_WirelessThisPeriodTxSec_Object = MibScalar
wirelessThisPeriodTxSec = _WirelessThisPeriodTxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 4),
    _WirelessThisPeriodTxSec_Type()
)
wirelessThisPeriodTxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisPeriodTxSec.setStatus("current")
_WirelessThisPeriodConnectionsPri_Type = Counter32
_WirelessThisPeriodConnectionsPri_Object = MibScalar
wirelessThisPeriodConnectionsPri = _WirelessThisPeriodConnectionsPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 5),
    _WirelessThisPeriodConnectionsPri_Type()
)
wirelessThisPeriodConnectionsPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisPeriodConnectionsPri.setStatus("current")
_WirelessThisPeriodConnectionsSec_Type = Counter32
_WirelessThisPeriodConnectionsSec_Object = MibScalar
wirelessThisPeriodConnectionsSec = _WirelessThisPeriodConnectionsSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 6),
    _WirelessThisPeriodConnectionsSec_Type()
)
wirelessThisPeriodConnectionsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisPeriodConnectionsSec.setStatus("current")
_WirelessThisPeriodOnlinePri_Type = TimeTicks
_WirelessThisPeriodOnlinePri_Object = MibScalar
wirelessThisPeriodOnlinePri = _WirelessThisPeriodOnlinePri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 7),
    _WirelessThisPeriodOnlinePri_Type()
)
wirelessThisPeriodOnlinePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisPeriodOnlinePri.setStatus("current")
_WirelessThisPeriodOnlineSec_Type = TimeTicks
_WirelessThisPeriodOnlineSec_Object = MibScalar
wirelessThisPeriodOnlineSec = _WirelessThisPeriodOnlineSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 8),
    _WirelessThisPeriodOnlineSec_Type()
)
wirelessThisPeriodOnlineSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisPeriodOnlineSec.setStatus("current")
_WirelessThisPeriodOffline_Type = TimeTicks
_WirelessThisPeriodOffline_Object = MibScalar
wirelessThisPeriodOffline = _WirelessThisPeriodOffline_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 9),
    _WirelessThisPeriodOffline_Type()
)
wirelessThisPeriodOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisPeriodOffline.setStatus("current")
_WirelessThisPeriodCells_Type = Counter32
_WirelessThisPeriodCells_Object = MibScalar
wirelessThisPeriodCells = _WirelessThisPeriodCells_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 10),
    _WirelessThisPeriodCells_Type()
)
wirelessThisPeriodCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisPeriodCells.setStatus("current")
_WirelessThisPeriodLevelAvg_Type = Integer32
_WirelessThisPeriodLevelAvg_Object = MibScalar
wirelessThisPeriodLevelAvg = _WirelessThisPeriodLevelAvg_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 11),
    _WirelessThisPeriodLevelAvg_Type()
)
wirelessThisPeriodLevelAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisPeriodLevelAvg.setStatus("current")
_WirelessThisPeriodLevelMin_Type = Integer32
_WirelessThisPeriodLevelMin_Object = MibScalar
wirelessThisPeriodLevelMin = _WirelessThisPeriodLevelMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 12),
    _WirelessThisPeriodLevelMin_Type()
)
wirelessThisPeriodLevelMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisPeriodLevelMin.setStatus("current")
_WirelessThisPeriodLevelMax_Type = Integer32
_WirelessThisPeriodLevelMax_Object = MibScalar
wirelessThisPeriodLevelMax = _WirelessThisPeriodLevelMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 13),
    _WirelessThisPeriodLevelMax_Type()
)
wirelessThisPeriodLevelMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisPeriodLevelMax.setStatus("current")
_WirelessThisPeriodDateMin_Type = Counter32
_WirelessThisPeriodDateMin_Object = MibScalar
wirelessThisPeriodDateMin = _WirelessThisPeriodDateMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 14),
    _WirelessThisPeriodDateMin_Type()
)
wirelessThisPeriodDateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisPeriodDateMin.setStatus("current")
_WirelessThisPeriodDateMax_Type = Counter32
_WirelessThisPeriodDateMax_Object = MibScalar
wirelessThisPeriodDateMax = _WirelessThisPeriodDateMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 5, 15),
    _WirelessThisPeriodDateMax_Type()
)
wirelessThisPeriodDateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessThisPeriodDateMax.setStatus("current")
_WirelessLastPeriod_ObjectIdentity = ObjectIdentity
wirelessLastPeriod = _WirelessLastPeriod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6)
)
_WirelessLastPeriodRxPri_Type = Counter32
_WirelessLastPeriodRxPri_Object = MibScalar
wirelessLastPeriodRxPri = _WirelessLastPeriodRxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 1),
    _WirelessLastPeriodRxPri_Type()
)
wirelessLastPeriodRxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastPeriodRxPri.setStatus("current")
_WirelessLastPeriodRxSec_Type = Counter32
_WirelessLastPeriodRxSec_Object = MibScalar
wirelessLastPeriodRxSec = _WirelessLastPeriodRxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 2),
    _WirelessLastPeriodRxSec_Type()
)
wirelessLastPeriodRxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastPeriodRxSec.setStatus("current")
_WirelessLastPeriodTxPri_Type = Counter32
_WirelessLastPeriodTxPri_Object = MibScalar
wirelessLastPeriodTxPri = _WirelessLastPeriodTxPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 3),
    _WirelessLastPeriodTxPri_Type()
)
wirelessLastPeriodTxPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastPeriodTxPri.setStatus("current")
_WirelessLastPeriodTxSec_Type = Counter32
_WirelessLastPeriodTxSec_Object = MibScalar
wirelessLastPeriodTxSec = _WirelessLastPeriodTxSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 4),
    _WirelessLastPeriodTxSec_Type()
)
wirelessLastPeriodTxSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastPeriodTxSec.setStatus("current")
_WirelessLastPeriodConnectionsPri_Type = Counter32
_WirelessLastPeriodConnectionsPri_Object = MibScalar
wirelessLastPeriodConnectionsPri = _WirelessLastPeriodConnectionsPri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 5),
    _WirelessLastPeriodConnectionsPri_Type()
)
wirelessLastPeriodConnectionsPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastPeriodConnectionsPri.setStatus("current")
_WirelessLastPeriodConnectionsSec_Type = Counter32
_WirelessLastPeriodConnectionsSec_Object = MibScalar
wirelessLastPeriodConnectionsSec = _WirelessLastPeriodConnectionsSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 6),
    _WirelessLastPeriodConnectionsSec_Type()
)
wirelessLastPeriodConnectionsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastPeriodConnectionsSec.setStatus("current")
_WirelessLastPeriodOnlinePri_Type = TimeTicks
_WirelessLastPeriodOnlinePri_Object = MibScalar
wirelessLastPeriodOnlinePri = _WirelessLastPeriodOnlinePri_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 7),
    _WirelessLastPeriodOnlinePri_Type()
)
wirelessLastPeriodOnlinePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastPeriodOnlinePri.setStatus("current")
_WirelessLastPeriodOnlineSec_Type = TimeTicks
_WirelessLastPeriodOnlineSec_Object = MibScalar
wirelessLastPeriodOnlineSec = _WirelessLastPeriodOnlineSec_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 8),
    _WirelessLastPeriodOnlineSec_Type()
)
wirelessLastPeriodOnlineSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastPeriodOnlineSec.setStatus("current")
_WirelessLastPeriodOffline_Type = TimeTicks
_WirelessLastPeriodOffline_Object = MibScalar
wirelessLastPeriodOffline = _WirelessLastPeriodOffline_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 9),
    _WirelessLastPeriodOffline_Type()
)
wirelessLastPeriodOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastPeriodOffline.setStatus("current")
_WirelessLastPeriodCells_Type = Counter32
_WirelessLastPeriodCells_Object = MibScalar
wirelessLastPeriodCells = _WirelessLastPeriodCells_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 10),
    _WirelessLastPeriodCells_Type()
)
wirelessLastPeriodCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastPeriodCells.setStatus("current")
_WirelessLastPeriodLevelAvg_Type = Integer32
_WirelessLastPeriodLevelAvg_Object = MibScalar
wirelessLastPeriodLevelAvg = _WirelessLastPeriodLevelAvg_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 11),
    _WirelessLastPeriodLevelAvg_Type()
)
wirelessLastPeriodLevelAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastPeriodLevelAvg.setStatus("current")
_WirelessLastPeriodLevelMin_Type = Integer32
_WirelessLastPeriodLevelMin_Object = MibScalar
wirelessLastPeriodLevelMin = _WirelessLastPeriodLevelMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 12),
    _WirelessLastPeriodLevelMin_Type()
)
wirelessLastPeriodLevelMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastPeriodLevelMin.setStatus("current")
_WirelessLastPeriodLevelMax_Type = Integer32
_WirelessLastPeriodLevelMax_Object = MibScalar
wirelessLastPeriodLevelMax = _WirelessLastPeriodLevelMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 13),
    _WirelessLastPeriodLevelMax_Type()
)
wirelessLastPeriodLevelMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastPeriodLevelMax.setStatus("current")
_WirelessLastPeriodDateMin_Type = Counter32
_WirelessLastPeriodDateMin_Object = MibScalar
wirelessLastPeriodDateMin = _WirelessLastPeriodDateMin_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 14),
    _WirelessLastPeriodDateMin_Type()
)
wirelessLastPeriodDateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastPeriodDateMin.setStatus("current")
_WirelessLastPeriodDateMax_Type = Counter32
_WirelessLastPeriodDateMax_Object = MibScalar
wirelessLastPeriodDateMax = _WirelessLastPeriodDateMax_Object(
    (1, 3, 6, 1, 4, 1, 30140, 5, 6, 15),
    _WirelessLastPeriodDateMax_Type()
)
wirelessLastPeriodDateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLastPeriodDateMax.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CONEL-WIRELESS-MIB",
    **{"conel": conel,
       "wireless": wireless,
       "wirelessStatus": wirelessStatus,
       "wirelessPLMN": wirelessPLMN,
       "wirelessCell": wirelessCell,
       "wirelessChannel": wirelessChannel,
       "wirelessLevel": wirelessLevel,
       "wirelessChannelN1": wirelessChannelN1,
       "wirelessLevelN1": wirelessLevelN1,
       "wirelessChannelN2": wirelessChannelN2,
       "wirelessLevelN2": wirelessLevelN2,
       "wirelessChannelN3": wirelessChannelN3,
       "wirelessLevelN3": wirelessLevelN3,
       "wirelessChannelN4": wirelessChannelN4,
       "wirelessLevelN4": wirelessLevelN4,
       "wirelessChannelN5": wirelessChannelN5,
       "wirelessLevelN5": wirelessLevelN5,
       "wirelessUpTime": wirelessUpTime,
       "wirelessConnect": wirelessConnect,
       "wirelessDisconnect": wirelessDisconnect,
       "wirelessCard": wirelessCard,
       "wirelessIPAddress": wirelessIPAddress,
       "wirelessLatency": wirelessLatency,
       "wirelessReportPeriod": wirelessReportPeriod,
       "wireless-2": wireless_2,
       "wirelessToday": wirelessToday,
       "wirelessTodayRxPri": wirelessTodayRxPri,
       "wirelessTodayRxSec": wirelessTodayRxSec,
       "wirelessTodayTxPri": wirelessTodayTxPri,
       "wirelessTodayTxSec": wirelessTodayTxSec,
       "wirelessTodayConnectionsPri": wirelessTodayConnectionsPri,
       "wirelessTodayConnectionsSec": wirelessTodayConnectionsSec,
       "wirelessTodayOnlinePri": wirelessTodayOnlinePri,
       "wirelessTodayOnlineSec": wirelessTodayOnlineSec,
       "wirelessTodayOffline": wirelessTodayOffline,
       "wirelessTodayCells": wirelessTodayCells,
       "wirelessTodayLevelAvg": wirelessTodayLevelAvg,
       "wirelessTodayLevelMin": wirelessTodayLevelMin,
       "wirelessTodayLevelMax": wirelessTodayLevelMax,
       "wirelessTodayDateMin": wirelessTodayDateMin,
       "wirelessTodayDateMax": wirelessTodayDateMax,
       "wirelessYesterday": wirelessYesterday,
       "wirelessYesterdayRxPri": wirelessYesterdayRxPri,
       "wirelessYesterdayRxSec": wirelessYesterdayRxSec,
       "wirelessYesterdayTxPri": wirelessYesterdayTxPri,
       "wirelessYesterdayTxSec": wirelessYesterdayTxSec,
       "wirelessYesterdayConnectionsPri": wirelessYesterdayConnectionsPri,
       "wirelessYesterdayConnectionsSec": wirelessYesterdayConnectionsSec,
       "wirelessYesterdayOnlinePri": wirelessYesterdayOnlinePri,
       "wirelessYesterdayOnlineSec": wirelessYesterdayOnlineSec,
       "wirelessYesterdayOffline": wirelessYesterdayOffline,
       "wirelessYesterdayCells": wirelessYesterdayCells,
       "wirelessYesterdayLevelAvg": wirelessYesterdayLevelAvg,
       "wirelessYesterdayLevelMin": wirelessYesterdayLevelMin,
       "wirelessYesterdayLevelMax": wirelessYesterdayLevelMax,
       "wirelessYesterdayDateMin": wirelessYesterdayDateMin,
       "wirelessYesterdayDateMax": wirelessYesterdayDateMax,
       "wirelessThisWeek": wirelessThisWeek,
       "wirelessThisWeekRxPri": wirelessThisWeekRxPri,
       "wirelessThisWeekRxSec": wirelessThisWeekRxSec,
       "wirelessThisWeekTxPri": wirelessThisWeekTxPri,
       "wirelessThisWeekTxSec": wirelessThisWeekTxSec,
       "wirelessThisWeekConnectionsPri": wirelessThisWeekConnectionsPri,
       "wirelessThisWeekConnectionsSec": wirelessThisWeekConnectionsSec,
       "wirelessThisWeekOnlinePri": wirelessThisWeekOnlinePri,
       "wirelessThisWeekOnlineSec": wirelessThisWeekOnlineSec,
       "wirelessThisWeekOffline": wirelessThisWeekOffline,
       "wirelessThisWeekCells": wirelessThisWeekCells,
       "wirelessThisWeekLevelAvg": wirelessThisWeekLevelAvg,
       "wirelessThisWeekLevelMin": wirelessThisWeekLevelMin,
       "wirelessThisWeekLevelMax": wirelessThisWeekLevelMax,
       "wirelessThisWeekDateMin": wirelessThisWeekDateMin,
       "wirelessThisWeekDateMax": wirelessThisWeekDateMax,
       "wirelessLastWeek": wirelessLastWeek,
       "wirelessLastWeekRxPri": wirelessLastWeekRxPri,
       "wirelessLastWeekRxSec": wirelessLastWeekRxSec,
       "wirelessLastWeekTxPri": wirelessLastWeekTxPri,
       "wirelessLastWeekTxSec": wirelessLastWeekTxSec,
       "wirelessLastWeekConnectionsPri": wirelessLastWeekConnectionsPri,
       "wirelessLastWeekConnectionsSec": wirelessLastWeekConnectionsSec,
       "wirelessLastWeekOnlinePri": wirelessLastWeekOnlinePri,
       "wirelessLastWeekOnlineSec": wirelessLastWeekOnlineSec,
       "wirelessLastWeekOffline": wirelessLastWeekOffline,
       "wirelessLastWeekCells": wirelessLastWeekCells,
       "wirelessLastWeekLevelAvg": wirelessLastWeekLevelAvg,
       "wirelessLastWeekLevelMin": wirelessLastWeekLevelMin,
       "wirelessLastWeekLevelMax": wirelessLastWeekLevelMax,
       "wirelessLastWeekDateMin": wirelessLastWeekDateMin,
       "wirelessLastWeekDateMax": wirelessLastWeekDateMax,
       "wirelessThisPeriod": wirelessThisPeriod,
       "wirelessThisPeriodRxPri": wirelessThisPeriodRxPri,
       "wirelessThisPeriodRxSec": wirelessThisPeriodRxSec,
       "wirelessThisPeriodTxPri": wirelessThisPeriodTxPri,
       "wirelessThisPeriodTxSec": wirelessThisPeriodTxSec,
       "wirelessThisPeriodConnectionsPri": wirelessThisPeriodConnectionsPri,
       "wirelessThisPeriodConnectionsSec": wirelessThisPeriodConnectionsSec,
       "wirelessThisPeriodOnlinePri": wirelessThisPeriodOnlinePri,
       "wirelessThisPeriodOnlineSec": wirelessThisPeriodOnlineSec,
       "wirelessThisPeriodOffline": wirelessThisPeriodOffline,
       "wirelessThisPeriodCells": wirelessThisPeriodCells,
       "wirelessThisPeriodLevelAvg": wirelessThisPeriodLevelAvg,
       "wirelessThisPeriodLevelMin": wirelessThisPeriodLevelMin,
       "wirelessThisPeriodLevelMax": wirelessThisPeriodLevelMax,
       "wirelessThisPeriodDateMin": wirelessThisPeriodDateMin,
       "wirelessThisPeriodDateMax": wirelessThisPeriodDateMax,
       "wirelessLastPeriod": wirelessLastPeriod,
       "wirelessLastPeriodRxPri": wirelessLastPeriodRxPri,
       "wirelessLastPeriodRxSec": wirelessLastPeriodRxSec,
       "wirelessLastPeriodTxPri": wirelessLastPeriodTxPri,
       "wirelessLastPeriodTxSec": wirelessLastPeriodTxSec,
       "wirelessLastPeriodConnectionsPri": wirelessLastPeriodConnectionsPri,
       "wirelessLastPeriodConnectionsSec": wirelessLastPeriodConnectionsSec,
       "wirelessLastPeriodOnlinePri": wirelessLastPeriodOnlinePri,
       "wirelessLastPeriodOnlineSec": wirelessLastPeriodOnlineSec,
       "wirelessLastPeriodOffline": wirelessLastPeriodOffline,
       "wirelessLastPeriodCells": wirelessLastPeriodCells,
       "wirelessLastPeriodLevelAvg": wirelessLastPeriodLevelAvg,
       "wirelessLastPeriodLevelMin": wirelessLastPeriodLevelMin,
       "wirelessLastPeriodLevelMax": wirelessLastPeriodLevelMax,
       "wirelessLastPeriodDateMin": wirelessLastPeriodDateMin,
       "wirelessLastPeriodDateMax": wirelessLastPeriodDateMax}
)
