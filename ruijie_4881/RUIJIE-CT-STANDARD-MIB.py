# SNMP MIB module (RUIJIE-CT-STANDARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-CT-STANDARD-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:05:39 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ruijieApgWlanId,) = mibBuilder.importSymbols(
    "RUIJIE-AC-MGMT-MIB",
    "ruijieApgWlanId")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ctStandardmibmodule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71)
)
if mibBuilder.loadTexts:
    ctStandardmibmodule.setRevisions(
        ("2010-02-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtStandardMIBObjects_ObjectIdentity = ObjectIdentity
ctStandardMIBObjects = _CtStandardMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2)
)
_CtStandardSystemConfigTable_Object = MibTable
ctStandardSystemConfigTable = _CtStandardSystemConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 1)
)
if mibBuilder.loadTexts:
    ctStandardSystemConfigTable.setStatus("current")
_CtStandardSystemConfigEntry_Object = MibTableRow
ctStandardSystemConfigEntry = _CtStandardSystemConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 1, 1)
)
ctStandardSystemConfigEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgWlanId"),
)
if mibBuilder.loadTexts:
    ctStandardSystemConfigEntry.setStatus("current")
_CtStandardAPConfigurationFileUpdate_Type = TruthValue
_CtStandardAPConfigurationFileUpdate_Object = MibTableColumn
ctStandardAPConfigurationFileUpdate = _CtStandardAPConfigurationFileUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 1, 1, 1),
    _CtStandardAPConfigurationFileUpdate_Type()
)
ctStandardAPConfigurationFileUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctStandardAPConfigurationFileUpdate.setStatus("current")
_CtStandardAPVersionFileUpdate_Type = TruthValue
_CtStandardAPVersionFileUpdate_Object = MibTableColumn
ctStandardAPVersionFileUpdate = _CtStandardAPVersionFileUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 1, 1, 2),
    _CtStandardAPVersionFileUpdate_Type()
)
ctStandardAPVersionFileUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctStandardAPVersionFileUpdate.setStatus("current")
_CtStandardMomentSTAConnected_Type = TimeTicks
_CtStandardMomentSTAConnected_Object = MibTableColumn
ctStandardMomentSTAConnected = _CtStandardMomentSTAConnected_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 1, 1, 3),
    _CtStandardMomentSTAConnected_Type()
)
ctStandardMomentSTAConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctStandardMomentSTAConnected.setStatus("current")
_ApCableInterfaceStatisticsTable_Object = MibTable
apCableInterfaceStatisticsTable = _ApCableInterfaceStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 2)
)
if mibBuilder.loadTexts:
    apCableInterfaceStatisticsTable.setStatus("current")
_ApCableInterfaceStatisticsEntry_Object = MibTableRow
apCableInterfaceStatisticsEntry = _ApCableInterfaceStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 2, 1)
)
apCableInterfaceStatisticsEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgWlanId"),
)
if mibBuilder.loadTexts:
    apCableInterfaceStatisticsEntry.setStatus("current")
_ApIntfaceUnicastPacketsNumReceived_Type = Integer32
_ApIntfaceUnicastPacketsNumReceived_Object = MibTableColumn
apIntfaceUnicastPacketsNumReceived = _ApIntfaceUnicastPacketsNumReceived_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 2, 1, 1),
    _ApIntfaceUnicastPacketsNumReceived_Type()
)
apIntfaceUnicastPacketsNumReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIntfaceUnicastPacketsNumReceived.setStatus("current")
_ApIntfacebroadcastPacketsNumReceived_Type = Integer32
_ApIntfacebroadcastPacketsNumReceived_Object = MibTableColumn
apIntfacebroadcastPacketsNumReceived = _ApIntfacebroadcastPacketsNumReceived_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 2, 1, 2),
    _ApIntfacebroadcastPacketsNumReceived_Type()
)
apIntfacebroadcastPacketsNumReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIntfacebroadcastPacketsNumReceived.setStatus("current")
_ApIntfaceMuticastPacketsNumReceived_Type = Integer32
_ApIntfaceMuticastPacketsNumReceived_Object = MibTableColumn
apIntfaceMuticastPacketsNumReceived = _ApIntfaceMuticastPacketsNumReceived_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 2, 1, 3),
    _ApIntfaceMuticastPacketsNumReceived_Type()
)
apIntfaceMuticastPacketsNumReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIntfaceMuticastPacketsNumReceived.setStatus("current")
_ApIntfacePacketsNumDiscarded_Type = Integer32
_ApIntfacePacketsNumDiscarded_Object = MibTableColumn
apIntfacePacketsNumDiscarded = _ApIntfacePacketsNumDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 2, 1, 4),
    _ApIntfacePacketsNumDiscarded_Type()
)
apIntfacePacketsNumDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIntfacePacketsNumDiscarded.setStatus("current")
_ApIntfaceUnicastPacketsNumTransmitted_Type = Integer32
_ApIntfaceUnicastPacketsNumTransmitted_Object = MibTableColumn
apIntfaceUnicastPacketsNumTransmitted = _ApIntfaceUnicastPacketsNumTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 2, 1, 5),
    _ApIntfaceUnicastPacketsNumTransmitted_Type()
)
apIntfaceUnicastPacketsNumTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIntfaceUnicastPacketsNumTransmitted.setStatus("current")
_ApIntfacebroadcastPacketsNumTransmitted_Type = Integer32
_ApIntfacebroadcastPacketsNumTransmitted_Object = MibTableColumn
apIntfacebroadcastPacketsNumTransmitted = _ApIntfacebroadcastPacketsNumTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 2, 1, 6),
    _ApIntfacebroadcastPacketsNumTransmitted_Type()
)
apIntfacebroadcastPacketsNumTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIntfacebroadcastPacketsNumTransmitted.setStatus("current")
_ApIntfaceMuticastPacketsNumTransmitted_Type = Integer32
_ApIntfaceMuticastPacketsNumTransmitted_Object = MibTableColumn
apIntfaceMuticastPacketsNumTransmitted = _ApIntfaceMuticastPacketsNumTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 2, 1, 7),
    _ApIntfaceMuticastPacketsNumTransmitted_Type()
)
apIntfaceMuticastPacketsNumTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIntfaceMuticastPacketsNumTransmitted.setStatus("current")
_Ac8023CableInterfaceStatisticsTable_Object = MibTable
ac8023CableInterfaceStatisticsTable = _Ac8023CableInterfaceStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 3)
)
if mibBuilder.loadTexts:
    ac8023CableInterfaceStatisticsTable.setStatus("current")
_Ac8023CableInterfaceStatisticsEntry_Object = MibTableRow
ac8023CableInterfaceStatisticsEntry = _Ac8023CableInterfaceStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 3, 1)
)
ac8023CableInterfaceStatisticsEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgWlanId"),
)
if mibBuilder.loadTexts:
    ac8023CableInterfaceStatisticsEntry.setStatus("current")
_Ac8023IntfaceUnicastPacketsNumReceived_Type = Integer32
_Ac8023IntfaceUnicastPacketsNumReceived_Object = MibTableColumn
ac8023IntfaceUnicastPacketsNumReceived = _Ac8023IntfaceUnicastPacketsNumReceived_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 3, 1, 1),
    _Ac8023IntfaceUnicastPacketsNumReceived_Type()
)
ac8023IntfaceUnicastPacketsNumReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ac8023IntfaceUnicastPacketsNumReceived.setStatus("current")
_Ac8023IntfacebroadcastPacketsNumReceived_Type = Integer32
_Ac8023IntfacebroadcastPacketsNumReceived_Object = MibTableColumn
ac8023IntfacebroadcastPacketsNumReceived = _Ac8023IntfacebroadcastPacketsNumReceived_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 3, 1, 2),
    _Ac8023IntfacebroadcastPacketsNumReceived_Type()
)
ac8023IntfacebroadcastPacketsNumReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ac8023IntfacebroadcastPacketsNumReceived.setStatus("current")
_Ac8023IntfaceMuticastPacketsNumReceived_Type = Integer32
_Ac8023IntfaceMuticastPacketsNumReceived_Object = MibTableColumn
ac8023IntfaceMuticastPacketsNumReceived = _Ac8023IntfaceMuticastPacketsNumReceived_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 3, 1, 3),
    _Ac8023IntfaceMuticastPacketsNumReceived_Type()
)
ac8023IntfaceMuticastPacketsNumReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ac8023IntfaceMuticastPacketsNumReceived.setStatus("current")
_Ac8023IntfacePacketsNumDiscarded_Type = Integer32
_Ac8023IntfacePacketsNumDiscarded_Object = MibTableColumn
ac8023IntfacePacketsNumDiscarded = _Ac8023IntfacePacketsNumDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 3, 1, 4),
    _Ac8023IntfacePacketsNumDiscarded_Type()
)
ac8023IntfacePacketsNumDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ac8023IntfacePacketsNumDiscarded.setStatus("current")
_Ac8023IntfaceUnicastPacketsNumTransmitted_Type = Integer32
_Ac8023IntfaceUnicastPacketsNumTransmitted_Object = MibTableColumn
ac8023IntfaceUnicastPacketsNumTransmitted = _Ac8023IntfaceUnicastPacketsNumTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 3, 1, 5),
    _Ac8023IntfaceUnicastPacketsNumTransmitted_Type()
)
ac8023IntfaceUnicastPacketsNumTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ac8023IntfaceUnicastPacketsNumTransmitted.setStatus("current")
_Ac8023IntfacebroadcastPacketsNumTransmitted_Type = Integer32
_Ac8023IntfacebroadcastPacketsNumTransmitted_Object = MibTableColumn
ac8023IntfacebroadcastPacketsNumTransmitted = _Ac8023IntfacebroadcastPacketsNumTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 3, 1, 6),
    _Ac8023IntfacebroadcastPacketsNumTransmitted_Type()
)
ac8023IntfacebroadcastPacketsNumTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ac8023IntfacebroadcastPacketsNumTransmitted.setStatus("current")
_Ac8023IntfaceMuticastPacketsNumTransmitted_Type = Integer32
_Ac8023IntfaceMuticastPacketsNumTransmitted_Object = MibTableColumn
ac8023IntfaceMuticastPacketsNumTransmitted = _Ac8023IntfaceMuticastPacketsNumTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 3, 1, 7),
    _Ac8023IntfaceMuticastPacketsNumTransmitted_Type()
)
ac8023IntfaceMuticastPacketsNumTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ac8023IntfaceMuticastPacketsNumTransmitted.setStatus("current")
_Ac80211WirelessInterfaceStatisticsTable_Object = MibTable
ac80211WirelessInterfaceStatisticsTable = _Ac80211WirelessInterfaceStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 4)
)
if mibBuilder.loadTexts:
    ac80211WirelessInterfaceStatisticsTable.setStatus("current")
_Ac80211WirelessInterfaceStatisticsEntry_Object = MibTableRow
ac80211WirelessInterfaceStatisticsEntry = _Ac80211WirelessInterfaceStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 4, 1)
)
ac80211WirelessInterfaceStatisticsEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgWlanId"),
)
if mibBuilder.loadTexts:
    ac80211WirelessInterfaceStatisticsEntry.setStatus("current")
_Ac80211UplinkPortTraffic_Type = Integer32
_Ac80211UplinkPortTraffic_Object = MibTableColumn
ac80211UplinkPortTraffic = _Ac80211UplinkPortTraffic_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 4, 1, 1),
    _Ac80211UplinkPortTraffic_Type()
)
ac80211UplinkPortTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ac80211UplinkPortTraffic.setStatus("current")
_Ac80211DownlinkPortTraffic_Type = Integer32
_Ac80211DownlinkPortTraffic_Object = MibTableColumn
ac80211DownlinkPortTraffic = _Ac80211DownlinkPortTraffic_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 4, 1, 2),
    _Ac80211DownlinkPortTraffic_Type()
)
ac80211DownlinkPortTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ac80211DownlinkPortTraffic.setStatus("current")
_Ac80211UplinkChannelFrameNummissed_Type = Integer32
_Ac80211UplinkChannelFrameNummissed_Object = MibTableColumn
ac80211UplinkChannelFrameNummissed = _Ac80211UplinkChannelFrameNummissed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 4, 1, 3),
    _Ac80211UplinkChannelFrameNummissed_Type()
)
ac80211UplinkChannelFrameNummissed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ac80211UplinkChannelFrameNummissed.setStatus("current")
_Ac80211UplinkChannelFrameNumRetrans_Type = Integer32
_Ac80211UplinkChannelFrameNumRetrans_Object = MibTableColumn
ac80211UplinkChannelFrameNumRetrans = _Ac80211UplinkChannelFrameNumRetrans_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 4, 1, 4),
    _Ac80211UplinkChannelFrameNumRetrans_Type()
)
ac80211UplinkChannelFrameNumRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ac80211UplinkChannelFrameNumRetrans.setStatus("current")
_Ac80211UplinkChannelTotalFrameNum_Type = Integer32
_Ac80211UplinkChannelTotalFrameNum_Object = MibTableColumn
ac80211UplinkChannelTotalFrameNum = _Ac80211UplinkChannelTotalFrameNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 4, 1, 5),
    _Ac80211UplinkChannelTotalFrameNum_Type()
)
ac80211UplinkChannelTotalFrameNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ac80211UplinkChannelTotalFrameNum.setStatus("current")
_Ac80211DownlinkChannelTotalFrameNum_Type = Integer32
_Ac80211DownlinkChannelTotalFrameNum_Object = MibTableColumn
ac80211DownlinkChannelTotalFrameNum = _Ac80211DownlinkChannelTotalFrameNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 4, 1, 6),
    _Ac80211DownlinkChannelTotalFrameNum_Type()
)
ac80211DownlinkChannelTotalFrameNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ac80211DownlinkChannelTotalFrameNum.setStatus("current")
_Ac80211DownlinkChannelWrongFrameNum_Type = Integer32
_Ac80211DownlinkChannelWrongFrameNum_Object = MibTableColumn
ac80211DownlinkChannelWrongFrameNum = _Ac80211DownlinkChannelWrongFrameNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 4, 1, 7),
    _Ac80211DownlinkChannelWrongFrameNum_Type()
)
ac80211DownlinkChannelWrongFrameNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ac80211DownlinkChannelWrongFrameNum.setStatus("current")
_Ac80211DownlinkChannelFrameNummissed_Type = Integer32
_Ac80211DownlinkChannelFrameNummissed_Object = MibTableColumn
ac80211DownlinkChannelFrameNummissed = _Ac80211DownlinkChannelFrameNummissed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 4, 1, 8),
    _Ac80211DownlinkChannelFrameNummissed_Type()
)
ac80211DownlinkChannelFrameNummissed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ac80211DownlinkChannelFrameNummissed.setStatus("current")
_Ac80211DownlinkChannelFrameNumRetrans_Type = Integer32
_Ac80211DownlinkChannelFrameNumRetrans_Object = MibTableColumn
ac80211DownlinkChannelFrameNumRetrans = _Ac80211DownlinkChannelFrameNumRetrans_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 4, 1, 9),
    _Ac80211DownlinkChannelFrameNumRetrans_Type()
)
ac80211DownlinkChannelFrameNumRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ac80211DownlinkChannelFrameNumRetrans.setStatus("current")
_Ac80211DataFrameBytesCountReceived_Type = Integer32
_Ac80211DataFrameBytesCountReceived_Object = MibTableColumn
ac80211DataFrameBytesCountReceived = _Ac80211DataFrameBytesCountReceived_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 4, 1, 10),
    _Ac80211DataFrameBytesCountReceived_Type()
)
ac80211DataFrameBytesCountReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ac80211DataFrameBytesCountReceived.setStatus("current")
_Ac80211DataFrameBytesCountTransmitted_Type = Integer32
_Ac80211DataFrameBytesCountTransmitted_Object = MibTableColumn
ac80211DataFrameBytesCountTransmitted = _Ac80211DataFrameBytesCountTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 4, 1, 11),
    _Ac80211DataFrameBytesCountTransmitted_Type()
)
ac80211DataFrameBytesCountTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ac80211DataFrameBytesCountTransmitted.setStatus("current")
_Ac80211AssociatedFramesCount_Type = Integer32
_Ac80211AssociatedFramesCount_Object = MibTableColumn
ac80211AssociatedFramesCount = _Ac80211AssociatedFramesCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 2, 4, 1, 12),
    _Ac80211AssociatedFramesCount_Type()
)
ac80211AssociatedFramesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ac80211AssociatedFramesCount.setStatus("current")
_CtStandardCompliances_ObjectIdentity = ObjectIdentity
ctStandardCompliances = _CtStandardCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 3)
)
_CtStandardGroup_ObjectIdentity = ObjectIdentity
ctStandardGroup = _CtStandardGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 4)
)

# Managed Objects groups

ctStandardBase = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 4, 1)
)
ctStandardBase.setObjects(
      *(("RUIJIE-CT-STANDARD-MIB", "ctStandardAPConfigurationFileUpdate"),
        ("RUIJIE-CT-STANDARD-MIB", "ctStandardAPVersionFileUpdate"),
        ("RUIJIE-CT-STANDARD-MIB", "ctStandardMomentSTAConnected"),
        ("RUIJIE-CT-STANDARD-MIB", "apIntfaceUnicastPacketsNumReceived"),
        ("RUIJIE-CT-STANDARD-MIB", "apIntfacebroadcastPacketsNumReceived"),
        ("RUIJIE-CT-STANDARD-MIB", "apIntfaceMuticastPacketsNumReceived"),
        ("RUIJIE-CT-STANDARD-MIB", "apIntfacePacketsNumDiscarded"),
        ("RUIJIE-CT-STANDARD-MIB", "apIntfaceUnicastPacketsNumTransmitted"),
        ("RUIJIE-CT-STANDARD-MIB", "apIntfacebroadcastPacketsNumTransmitted"),
        ("RUIJIE-CT-STANDARD-MIB", "apIntfaceMuticastPacketsNumTransmitted"),
        ("RUIJIE-CT-STANDARD-MIB", "ac8023IntfaceUnicastPacketsNumReceived"),
        ("RUIJIE-CT-STANDARD-MIB", "ac8023IntfacebroadcastPacketsNumReceived"),
        ("RUIJIE-CT-STANDARD-MIB", "ac8023IntfaceMuticastPacketsNumReceived"),
        ("RUIJIE-CT-STANDARD-MIB", "ac8023IntfacePacketsNumDiscarded"),
        ("RUIJIE-CT-STANDARD-MIB", "ac8023IntfaceUnicastPacketsNumTransmitted"),
        ("RUIJIE-CT-STANDARD-MIB", "ac8023IntfacebroadcastPacketsNumTransmitted"),
        ("RUIJIE-CT-STANDARD-MIB", "ac8023IntfaceMuticastPacketsNumTransmitted"),
        ("RUIJIE-CT-STANDARD-MIB", "ac80211UplinkPortTraffic"),
        ("RUIJIE-CT-STANDARD-MIB", "ac80211DownlinkPortTraffic"),
        ("RUIJIE-CT-STANDARD-MIB", "ac80211UplinkChannelFrameNummissed"),
        ("RUIJIE-CT-STANDARD-MIB", "ac80211UplinkChannelFrameNumRetrans"),
        ("RUIJIE-CT-STANDARD-MIB", "ac80211UplinkChannelTotalFrameNum"),
        ("RUIJIE-CT-STANDARD-MIB", "ac80211DownlinkChannelTotalFrameNum"),
        ("RUIJIE-CT-STANDARD-MIB", "ac80211DownlinkChannelWrongFrameNum"),
        ("RUIJIE-CT-STANDARD-MIB", "ac80211DownlinkChannelFrameNummissed"),
        ("RUIJIE-CT-STANDARD-MIB", "ac80211DownlinkChannelFrameNumRetrans"),
        ("RUIJIE-CT-STANDARD-MIB", "ac80211DataFrameBytesCountReceived"),
        ("RUIJIE-CT-STANDARD-MIB", "ac80211DataFrameBytesCountTransmitted"),
        ("RUIJIE-CT-STANDARD-MIB", "ac80211AssociatedFramesCount"))
)
if mibBuilder.loadTexts:
    ctStandardBase.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ctStandardCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 71, 3, 2)
)
ctStandardCompliance.setObjects(
    ("RUIJIE-CT-STANDARD-MIB", "ctStandardBase")
)
if mibBuilder.loadTexts:
    ctStandardCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-CT-STANDARD-MIB",
    **{"ctStandardmibmodule": ctStandardmibmodule,
       "ctStandardMIBObjects": ctStandardMIBObjects,
       "ctStandardSystemConfigTable": ctStandardSystemConfigTable,
       "ctStandardSystemConfigEntry": ctStandardSystemConfigEntry,
       "ctStandardAPConfigurationFileUpdate": ctStandardAPConfigurationFileUpdate,
       "ctStandardAPVersionFileUpdate": ctStandardAPVersionFileUpdate,
       "ctStandardMomentSTAConnected": ctStandardMomentSTAConnected,
       "apCableInterfaceStatisticsTable": apCableInterfaceStatisticsTable,
       "apCableInterfaceStatisticsEntry": apCableInterfaceStatisticsEntry,
       "apIntfaceUnicastPacketsNumReceived": apIntfaceUnicastPacketsNumReceived,
       "apIntfacebroadcastPacketsNumReceived": apIntfacebroadcastPacketsNumReceived,
       "apIntfaceMuticastPacketsNumReceived": apIntfaceMuticastPacketsNumReceived,
       "apIntfacePacketsNumDiscarded": apIntfacePacketsNumDiscarded,
       "apIntfaceUnicastPacketsNumTransmitted": apIntfaceUnicastPacketsNumTransmitted,
       "apIntfacebroadcastPacketsNumTransmitted": apIntfacebroadcastPacketsNumTransmitted,
       "apIntfaceMuticastPacketsNumTransmitted": apIntfaceMuticastPacketsNumTransmitted,
       "ac8023CableInterfaceStatisticsTable": ac8023CableInterfaceStatisticsTable,
       "ac8023CableInterfaceStatisticsEntry": ac8023CableInterfaceStatisticsEntry,
       "ac8023IntfaceUnicastPacketsNumReceived": ac8023IntfaceUnicastPacketsNumReceived,
       "ac8023IntfacebroadcastPacketsNumReceived": ac8023IntfacebroadcastPacketsNumReceived,
       "ac8023IntfaceMuticastPacketsNumReceived": ac8023IntfaceMuticastPacketsNumReceived,
       "ac8023IntfacePacketsNumDiscarded": ac8023IntfacePacketsNumDiscarded,
       "ac8023IntfaceUnicastPacketsNumTransmitted": ac8023IntfaceUnicastPacketsNumTransmitted,
       "ac8023IntfacebroadcastPacketsNumTransmitted": ac8023IntfacebroadcastPacketsNumTransmitted,
       "ac8023IntfaceMuticastPacketsNumTransmitted": ac8023IntfaceMuticastPacketsNumTransmitted,
       "ac80211WirelessInterfaceStatisticsTable": ac80211WirelessInterfaceStatisticsTable,
       "ac80211WirelessInterfaceStatisticsEntry": ac80211WirelessInterfaceStatisticsEntry,
       "ac80211UplinkPortTraffic": ac80211UplinkPortTraffic,
       "ac80211DownlinkPortTraffic": ac80211DownlinkPortTraffic,
       "ac80211UplinkChannelFrameNummissed": ac80211UplinkChannelFrameNummissed,
       "ac80211UplinkChannelFrameNumRetrans": ac80211UplinkChannelFrameNumRetrans,
       "ac80211UplinkChannelTotalFrameNum": ac80211UplinkChannelTotalFrameNum,
       "ac80211DownlinkChannelTotalFrameNum": ac80211DownlinkChannelTotalFrameNum,
       "ac80211DownlinkChannelWrongFrameNum": ac80211DownlinkChannelWrongFrameNum,
       "ac80211DownlinkChannelFrameNummissed": ac80211DownlinkChannelFrameNummissed,
       "ac80211DownlinkChannelFrameNumRetrans": ac80211DownlinkChannelFrameNumRetrans,
       "ac80211DataFrameBytesCountReceived": ac80211DataFrameBytesCountReceived,
       "ac80211DataFrameBytesCountTransmitted": ac80211DataFrameBytesCountTransmitted,
       "ac80211AssociatedFramesCount": ac80211AssociatedFramesCount,
       "ctStandardCompliances": ctStandardCompliances,
       "ctStandardCompliance": ctStandardCompliance,
       "ctStandardGroup": ctStandardGroup,
       "ctStandardBase": ctStandardBase}
)
