# SNMP MIB module (ME1200-LACP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-LACP-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:30 2025
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

(me1200SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCOME1200-MIB",
    "me1200SwitchMgmt")

(ME1200InterfaceIndex,
 ME1200Unsigned16,
 ME1200Unsigned8) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200InterfaceIndex",
    "ME1200Unsigned16",
    "ME1200Unsigned8")

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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

me1200LacpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35)
)
if mibBuilder.loadTexts:
    me1200LacpMib.setRevisions(
        ("2014-03-11 00:00",
         "2014-02-18 00:00",
         "2014-01-29 00:00",
         "2014-01-22 00:00",
         "2013-10-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Me1200LacpMibObjects_ObjectIdentity = ObjectIdentity
me1200LacpMibObjects = _Me1200LacpMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1)
)
_Me1200LacpConfig_ObjectIdentity = ObjectIdentity
me1200LacpConfig = _Me1200LacpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 2)
)
_Me1200LacpPortConfigTable_Object = MibTable
me1200LacpPortConfigTable = _Me1200LacpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 2, 1)
)
if mibBuilder.loadTexts:
    me1200LacpPortConfigTable.setStatus("current")
_Me1200LacpPortConfigEntry_Object = MibTableRow
me1200LacpPortConfigEntry = _Me1200LacpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 2, 1, 1)
)
me1200LacpPortConfigEntry.setIndexNames(
    (0, "ME1200-LACP-MIB", "me1200LacpPortConfigInterfaceNo"),
)
if mibBuilder.loadTexts:
    me1200LacpPortConfigEntry.setStatus("current")
_Me1200LacpPortConfigInterfaceNo_Type = ME1200InterfaceIndex
_Me1200LacpPortConfigInterfaceNo_Object = MibTableColumn
me1200LacpPortConfigInterfaceNo = _Me1200LacpPortConfigInterfaceNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 2, 1, 1, 1),
    _Me1200LacpPortConfigInterfaceNo_Type()
)
me1200LacpPortConfigInterfaceNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200LacpPortConfigInterfaceNo.setStatus("current")
_Me1200LacpPortConfigDot3adAggrActorAdminMode_Type = TruthValue
_Me1200LacpPortConfigDot3adAggrActorAdminMode_Object = MibTableColumn
me1200LacpPortConfigDot3adAggrActorAdminMode = _Me1200LacpPortConfigDot3adAggrActorAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 2, 1, 1, 2),
    _Me1200LacpPortConfigDot3adAggrActorAdminMode_Type()
)
me1200LacpPortConfigDot3adAggrActorAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LacpPortConfigDot3adAggrActorAdminMode.setStatus("current")
_Me1200LacpPortConfigDot3adAggrActorAdminKey_Type = ME1200Unsigned16
_Me1200LacpPortConfigDot3adAggrActorAdminKey_Object = MibTableColumn
me1200LacpPortConfigDot3adAggrActorAdminKey = _Me1200LacpPortConfigDot3adAggrActorAdminKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 2, 1, 1, 3),
    _Me1200LacpPortConfigDot3adAggrActorAdminKey_Type()
)
me1200LacpPortConfigDot3adAggrActorAdminKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LacpPortConfigDot3adAggrActorAdminKey.setStatus("current")
_Me1200LacpPortConfigDot3adAggrRole_Type = TruthValue
_Me1200LacpPortConfigDot3adAggrRole_Object = MibTableColumn
me1200LacpPortConfigDot3adAggrRole = _Me1200LacpPortConfigDot3adAggrRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 2, 1, 1, 4),
    _Me1200LacpPortConfigDot3adAggrRole_Type()
)
me1200LacpPortConfigDot3adAggrRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LacpPortConfigDot3adAggrRole.setStatus("current")
_Me1200LacpPortConfigDot3adAggrTimeout_Type = TruthValue
_Me1200LacpPortConfigDot3adAggrTimeout_Object = MibTableColumn
me1200LacpPortConfigDot3adAggrTimeout = _Me1200LacpPortConfigDot3adAggrTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 2, 1, 1, 5),
    _Me1200LacpPortConfigDot3adAggrTimeout_Type()
)
me1200LacpPortConfigDot3adAggrTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LacpPortConfigDot3adAggrTimeout.setStatus("current")
_Me1200LacpPortConfigDot3adAggrPortPriority_Type = ME1200Unsigned16
_Me1200LacpPortConfigDot3adAggrPortPriority_Object = MibTableColumn
me1200LacpPortConfigDot3adAggrPortPriority = _Me1200LacpPortConfigDot3adAggrPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 2, 1, 1, 6),
    _Me1200LacpPortConfigDot3adAggrPortPriority_Type()
)
me1200LacpPortConfigDot3adAggrPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LacpPortConfigDot3adAggrPortPriority.setStatus("current")
_Me1200LacpStatus_ObjectIdentity = ObjectIdentity
me1200LacpStatus = _Me1200LacpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 3)
)
_Me1200LacpSystemStatusTable_Object = MibTable
me1200LacpSystemStatusTable = _Me1200LacpSystemStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 3, 1)
)
if mibBuilder.loadTexts:
    me1200LacpSystemStatusTable.setStatus("current")
_Me1200LacpSystemStatusEntry_Object = MibTableRow
me1200LacpSystemStatusEntry = _Me1200LacpSystemStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 3, 1, 1)
)
me1200LacpSystemStatusEntry.setIndexNames(
    (0, "ME1200-LACP-MIB", "me1200LacpSystemStatusInterfaceNo"),
)
if mibBuilder.loadTexts:
    me1200LacpSystemStatusEntry.setStatus("current")
_Me1200LacpSystemStatusInterfaceNo_Type = ME1200InterfaceIndex
_Me1200LacpSystemStatusInterfaceNo_Object = MibTableColumn
me1200LacpSystemStatusInterfaceNo = _Me1200LacpSystemStatusInterfaceNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 3, 1, 1, 1),
    _Me1200LacpSystemStatusInterfaceNo_Type()
)
me1200LacpSystemStatusInterfaceNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200LacpSystemStatusInterfaceNo.setStatus("current")
_Me1200LacpSystemStatusDot3adAggrID_Type = ME1200Unsigned16
_Me1200LacpSystemStatusDot3adAggrID_Object = MibTableColumn
me1200LacpSystemStatusDot3adAggrID = _Me1200LacpSystemStatusDot3adAggrID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 3, 1, 1, 2),
    _Me1200LacpSystemStatusDot3adAggrID_Type()
)
me1200LacpSystemStatusDot3adAggrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LacpSystemStatusDot3adAggrID.setStatus("current")


class _Me1200LacpSystemStatusDot3adAggrPartnerSystemID_Type(OctetString):
    """Custom type me1200LacpSystemStatusDot3adAggrPartnerSystemID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6


_Me1200LacpSystemStatusDot3adAggrPartnerSystemID_Type.__name__ = "OctetString"
_Me1200LacpSystemStatusDot3adAggrPartnerSystemID_Object = MibTableColumn
me1200LacpSystemStatusDot3adAggrPartnerSystemID = _Me1200LacpSystemStatusDot3adAggrPartnerSystemID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 3, 1, 1, 3),
    _Me1200LacpSystemStatusDot3adAggrPartnerSystemID_Type()
)
me1200LacpSystemStatusDot3adAggrPartnerSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LacpSystemStatusDot3adAggrPartnerSystemID.setStatus("current")
_Me1200LacpSystemStatusDot3adAggrPartnerOperKey_Type = ME1200Unsigned16
_Me1200LacpSystemStatusDot3adAggrPartnerOperKey_Object = MibTableColumn
me1200LacpSystemStatusDot3adAggrPartnerOperKey = _Me1200LacpSystemStatusDot3adAggrPartnerOperKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 3, 1, 1, 4),
    _Me1200LacpSystemStatusDot3adAggrPartnerOperKey_Type()
)
me1200LacpSystemStatusDot3adAggrPartnerOperKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LacpSystemStatusDot3adAggrPartnerOperKey.setStatus("current")
_Me1200LacpSystemStatusDot3adAggrPartnerOperSystemPriority_Type = ME1200Unsigned16
_Me1200LacpSystemStatusDot3adAggrPartnerOperSystemPriority_Object = MibTableColumn
me1200LacpSystemStatusDot3adAggrPartnerOperSystemPriority = _Me1200LacpSystemStatusDot3adAggrPartnerOperSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 3, 1, 1, 5),
    _Me1200LacpSystemStatusDot3adAggrPartnerOperSystemPriority_Type()
)
me1200LacpSystemStatusDot3adAggrPartnerOperSystemPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LacpSystemStatusDot3adAggrPartnerOperSystemPriority.setStatus("current")
_Me1200LacpSystemStatusDot3adAggrPartnerStateLastChanged_Type = Unsigned32
_Me1200LacpSystemStatusDot3adAggrPartnerStateLastChanged_Object = MibTableColumn
me1200LacpSystemStatusDot3adAggrPartnerStateLastChanged = _Me1200LacpSystemStatusDot3adAggrPartnerStateLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 3, 1, 1, 6),
    _Me1200LacpSystemStatusDot3adAggrPartnerStateLastChanged_Type()
)
me1200LacpSystemStatusDot3adAggrPartnerStateLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LacpSystemStatusDot3adAggrPartnerStateLastChanged.setStatus("current")


class _Me1200LacpSystemStatusDot3adAggrLocalPorts_Type(OctetString):
    """Custom type me1200LacpSystemStatusDot3adAggrLocalPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_Me1200LacpSystemStatusDot3adAggrLocalPorts_Type.__name__ = "OctetString"
_Me1200LacpSystemStatusDot3adAggrLocalPorts_Object = MibTableColumn
me1200LacpSystemStatusDot3adAggrLocalPorts = _Me1200LacpSystemStatusDot3adAggrLocalPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 3, 1, 1, 7),
    _Me1200LacpSystemStatusDot3adAggrLocalPorts_Type()
)
me1200LacpSystemStatusDot3adAggrLocalPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LacpSystemStatusDot3adAggrLocalPorts.setStatus("current")
_Me1200LacpPortStatusTable_Object = MibTable
me1200LacpPortStatusTable = _Me1200LacpPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 3, 2)
)
if mibBuilder.loadTexts:
    me1200LacpPortStatusTable.setStatus("current")
_Me1200LacpPortStatusEntry_Object = MibTableRow
me1200LacpPortStatusEntry = _Me1200LacpPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 3, 2, 1)
)
me1200LacpPortStatusEntry.setIndexNames(
    (0, "ME1200-LACP-MIB", "me1200LacpPortStatusInterfaceNo"),
)
if mibBuilder.loadTexts:
    me1200LacpPortStatusEntry.setStatus("current")
_Me1200LacpPortStatusInterfaceNo_Type = ME1200InterfaceIndex
_Me1200LacpPortStatusInterfaceNo_Object = MibTableColumn
me1200LacpPortStatusInterfaceNo = _Me1200LacpPortStatusInterfaceNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 3, 2, 1, 1),
    _Me1200LacpPortStatusInterfaceNo_Type()
)
me1200LacpPortStatusInterfaceNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200LacpPortStatusInterfaceNo.setStatus("current")
_Me1200LacpPortStatusDot3adAggrActorAdminMode_Type = TruthValue
_Me1200LacpPortStatusDot3adAggrActorAdminMode_Object = MibTableColumn
me1200LacpPortStatusDot3adAggrActorAdminMode = _Me1200LacpPortStatusDot3adAggrActorAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 3, 2, 1, 2),
    _Me1200LacpPortStatusDot3adAggrActorAdminMode_Type()
)
me1200LacpPortStatusDot3adAggrActorAdminMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LacpPortStatusDot3adAggrActorAdminMode.setStatus("current")
_Me1200LacpPortStatusDot3adAggrActorAdminKey_Type = ME1200Unsigned16
_Me1200LacpPortStatusDot3adAggrActorAdminKey_Object = MibTableColumn
me1200LacpPortStatusDot3adAggrActorAdminKey = _Me1200LacpPortStatusDot3adAggrActorAdminKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 3, 2, 1, 3),
    _Me1200LacpPortStatusDot3adAggrActorAdminKey_Type()
)
me1200LacpPortStatusDot3adAggrActorAdminKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LacpPortStatusDot3adAggrActorAdminKey.setStatus("current")
_Me1200LacpPortStatusDot3adAggrPartnerOperPortIndex_Type = ME1200Unsigned8
_Me1200LacpPortStatusDot3adAggrPartnerOperPortIndex_Object = MibTableColumn
me1200LacpPortStatusDot3adAggrPartnerOperPortIndex = _Me1200LacpPortStatusDot3adAggrPartnerOperPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 3, 2, 1, 4),
    _Me1200LacpPortStatusDot3adAggrPartnerOperPortIndex_Type()
)
me1200LacpPortStatusDot3adAggrPartnerOperPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LacpPortStatusDot3adAggrPartnerOperPortIndex.setStatus("current")
_Me1200LacpPortStatusDot3adAggrPartnerOperPortPriority_Type = ME1200Unsigned16
_Me1200LacpPortStatusDot3adAggrPartnerOperPortPriority_Object = MibTableColumn
me1200LacpPortStatusDot3adAggrPartnerOperPortPriority = _Me1200LacpPortStatusDot3adAggrPartnerOperPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 3, 2, 1, 5),
    _Me1200LacpPortStatusDot3adAggrPartnerOperPortPriority_Type()
)
me1200LacpPortStatusDot3adAggrPartnerOperPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LacpPortStatusDot3adAggrPartnerOperPortPriority.setStatus("current")
_Me1200LacpPortStatisticsTable_Object = MibTable
me1200LacpPortStatisticsTable = _Me1200LacpPortStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 3, 3)
)
if mibBuilder.loadTexts:
    me1200LacpPortStatisticsTable.setStatus("current")
_Me1200LacpPortStatisticsEntry_Object = MibTableRow
me1200LacpPortStatisticsEntry = _Me1200LacpPortStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 3, 3, 1)
)
me1200LacpPortStatisticsEntry.setIndexNames(
    (0, "ME1200-LACP-MIB", "me1200LacpPortStatisticsInterfaceNo"),
)
if mibBuilder.loadTexts:
    me1200LacpPortStatisticsEntry.setStatus("current")
_Me1200LacpPortStatisticsInterfaceNo_Type = ME1200InterfaceIndex
_Me1200LacpPortStatisticsInterfaceNo_Object = MibTableColumn
me1200LacpPortStatisticsInterfaceNo = _Me1200LacpPortStatisticsInterfaceNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 3, 3, 1, 1),
    _Me1200LacpPortStatisticsInterfaceNo_Type()
)
me1200LacpPortStatisticsInterfaceNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200LacpPortStatisticsInterfaceNo.setStatus("current")
_Me1200LacpPortStatisticsDot3adAggrRxFrames_Type = Counter64
_Me1200LacpPortStatisticsDot3adAggrRxFrames_Object = MibTableColumn
me1200LacpPortStatisticsDot3adAggrRxFrames = _Me1200LacpPortStatisticsDot3adAggrRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 3, 3, 1, 2),
    _Me1200LacpPortStatisticsDot3adAggrRxFrames_Type()
)
me1200LacpPortStatisticsDot3adAggrRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LacpPortStatisticsDot3adAggrRxFrames.setStatus("current")
_Me1200LacpPortStatisticsDot3adAggrTxFrames_Type = Counter64
_Me1200LacpPortStatisticsDot3adAggrTxFrames_Object = MibTableColumn
me1200LacpPortStatisticsDot3adAggrTxFrames = _Me1200LacpPortStatisticsDot3adAggrTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 3, 3, 1, 3),
    _Me1200LacpPortStatisticsDot3adAggrTxFrames_Type()
)
me1200LacpPortStatisticsDot3adAggrTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LacpPortStatisticsDot3adAggrTxFrames.setStatus("current")
_Me1200LacpPortStatisticsDot3adAggrRxIllegalFrames_Type = Counter64
_Me1200LacpPortStatisticsDot3adAggrRxIllegalFrames_Object = MibTableColumn
me1200LacpPortStatisticsDot3adAggrRxIllegalFrames = _Me1200LacpPortStatisticsDot3adAggrRxIllegalFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 3, 3, 1, 4),
    _Me1200LacpPortStatisticsDot3adAggrRxIllegalFrames_Type()
)
me1200LacpPortStatisticsDot3adAggrRxIllegalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LacpPortStatisticsDot3adAggrRxIllegalFrames.setStatus("current")
_Me1200LacpPortStatisticsDot3adAggrRxUnknownFrames_Type = Counter64
_Me1200LacpPortStatisticsDot3adAggrRxUnknownFrames_Object = MibTableColumn
me1200LacpPortStatisticsDot3adAggrRxUnknownFrames = _Me1200LacpPortStatisticsDot3adAggrRxUnknownFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 3, 3, 1, 5),
    _Me1200LacpPortStatisticsDot3adAggrRxUnknownFrames_Type()
)
me1200LacpPortStatisticsDot3adAggrRxUnknownFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200LacpPortStatisticsDot3adAggrRxUnknownFrames.setStatus("current")
_Me1200LacpControl_ObjectIdentity = ObjectIdentity
me1200LacpControl = _Me1200LacpControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 4)
)
_Me1200LacpPortStatsClearTable_Object = MibTable
me1200LacpPortStatsClearTable = _Me1200LacpPortStatsClearTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 4, 1)
)
if mibBuilder.loadTexts:
    me1200LacpPortStatsClearTable.setStatus("current")
_Me1200LacpPortStatsClearEntry_Object = MibTableRow
me1200LacpPortStatsClearEntry = _Me1200LacpPortStatsClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 4, 1, 1)
)
me1200LacpPortStatsClearEntry.setIndexNames(
    (0, "ME1200-LACP-MIB", "me1200LacpPortStatsClearInterfaceNo"),
)
if mibBuilder.loadTexts:
    me1200LacpPortStatsClearEntry.setStatus("current")
_Me1200LacpPortStatsClearInterfaceNo_Type = ME1200InterfaceIndex
_Me1200LacpPortStatsClearInterfaceNo_Object = MibTableColumn
me1200LacpPortStatsClearInterfaceNo = _Me1200LacpPortStatsClearInterfaceNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 4, 1, 1, 1),
    _Me1200LacpPortStatsClearInterfaceNo_Type()
)
me1200LacpPortStatsClearInterfaceNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200LacpPortStatsClearInterfaceNo.setStatus("current")
_Me1200LacpPortStatsClearPortStatisticsClear_Type = TruthValue
_Me1200LacpPortStatsClearPortStatisticsClear_Object = MibTableColumn
me1200LacpPortStatsClearPortStatisticsClear = _Me1200LacpPortStatsClearPortStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 1, 4, 1, 1, 2),
    _Me1200LacpPortStatsClearPortStatisticsClear_Type()
)
me1200LacpPortStatsClearPortStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200LacpPortStatsClearPortStatisticsClear.setStatus("current")
_Me1200LacpMibConformance_ObjectIdentity = ObjectIdentity
me1200LacpMibConformance = _Me1200LacpMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 2)
)
_Me1200LacpMibCompliances_ObjectIdentity = ObjectIdentity
me1200LacpMibCompliances = _Me1200LacpMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 2, 1)
)
_Me1200LacpMibGroups_ObjectIdentity = ObjectIdentity
me1200LacpMibGroups = _Me1200LacpMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 2, 2)
)

# Managed Objects groups

me1200LacpPortConfigTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 2, 2, 1)
)
me1200LacpPortConfigTableInfoGroup.setObjects(
      *(("ME1200-LACP-MIB", "me1200LacpPortConfigDot3adAggrActorAdminMode"),
        ("ME1200-LACP-MIB", "me1200LacpPortConfigDot3adAggrActorAdminKey"),
        ("ME1200-LACP-MIB", "me1200LacpPortConfigDot3adAggrRole"),
        ("ME1200-LACP-MIB", "me1200LacpPortConfigDot3adAggrTimeout"),
        ("ME1200-LACP-MIB", "me1200LacpPortConfigDot3adAggrPortPriority"))
)
if mibBuilder.loadTexts:
    me1200LacpPortConfigTableInfoGroup.setStatus("current")

me1200LacpSystemStatusTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 2, 2, 2)
)
me1200LacpSystemStatusTableInfoGroup.setObjects(
      *(("ME1200-LACP-MIB", "me1200LacpSystemStatusDot3adAggrID"),
        ("ME1200-LACP-MIB", "me1200LacpSystemStatusDot3adAggrPartnerSystemID"),
        ("ME1200-LACP-MIB", "me1200LacpSystemStatusDot3adAggrPartnerOperKey"),
        ("ME1200-LACP-MIB", "me1200LacpSystemStatusDot3adAggrPartnerOperSystemPriority"),
        ("ME1200-LACP-MIB", "me1200LacpSystemStatusDot3adAggrPartnerStateLastChanged"),
        ("ME1200-LACP-MIB", "me1200LacpSystemStatusDot3adAggrLocalPorts"))
)
if mibBuilder.loadTexts:
    me1200LacpSystemStatusTableInfoGroup.setStatus("current")

me1200LacpPortStatusTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 2, 2, 3)
)
me1200LacpPortStatusTableInfoGroup.setObjects(
      *(("ME1200-LACP-MIB", "me1200LacpPortStatusDot3adAggrActorAdminMode"),
        ("ME1200-LACP-MIB", "me1200LacpPortStatusDot3adAggrActorAdminKey"),
        ("ME1200-LACP-MIB", "me1200LacpPortStatusDot3adAggrPartnerOperPortIndex"),
        ("ME1200-LACP-MIB", "me1200LacpPortStatusDot3adAggrPartnerOperPortPriority"))
)
if mibBuilder.loadTexts:
    me1200LacpPortStatusTableInfoGroup.setStatus("current")

me1200LacpPortStatisticsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 2, 2, 4)
)
me1200LacpPortStatisticsTableInfoGroup.setObjects(
      *(("ME1200-LACP-MIB", "me1200LacpPortStatisticsDot3adAggrRxFrames"),
        ("ME1200-LACP-MIB", "me1200LacpPortStatisticsDot3adAggrTxFrames"),
        ("ME1200-LACP-MIB", "me1200LacpPortStatisticsDot3adAggrRxIllegalFrames"),
        ("ME1200-LACP-MIB", "me1200LacpPortStatisticsDot3adAggrRxUnknownFrames"))
)
if mibBuilder.loadTexts:
    me1200LacpPortStatisticsTableInfoGroup.setStatus("current")

me1200LacpPortStatsClearTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 2, 2, 5)
)
me1200LacpPortStatsClearTableInfoGroup.setObjects(
    ("ME1200-LACP-MIB", "me1200LacpPortStatsClearPortStatisticsClear")
)
if mibBuilder.loadTexts:
    me1200LacpPortStatsClearTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200LacpMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 35, 2, 1, 1)
)
me1200LacpMibCompliance.setObjects(
      *(("ME1200-LACP-MIB", "me1200LacpPortConfigTableInfoGroup"),
        ("ME1200-LACP-MIB", "me1200LacpSystemStatusTableInfoGroup"),
        ("ME1200-LACP-MIB", "me1200LacpPortStatusTableInfoGroup"),
        ("ME1200-LACP-MIB", "me1200LacpPortStatisticsTableInfoGroup"),
        ("ME1200-LACP-MIB", "me1200LacpPortStatsClearTableInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200LacpMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-LACP-MIB",
    **{"me1200LacpMib": me1200LacpMib,
       "me1200LacpMibObjects": me1200LacpMibObjects,
       "me1200LacpConfig": me1200LacpConfig,
       "me1200LacpPortConfigTable": me1200LacpPortConfigTable,
       "me1200LacpPortConfigEntry": me1200LacpPortConfigEntry,
       "me1200LacpPortConfigInterfaceNo": me1200LacpPortConfigInterfaceNo,
       "me1200LacpPortConfigDot3adAggrActorAdminMode": me1200LacpPortConfigDot3adAggrActorAdminMode,
       "me1200LacpPortConfigDot3adAggrActorAdminKey": me1200LacpPortConfigDot3adAggrActorAdminKey,
       "me1200LacpPortConfigDot3adAggrRole": me1200LacpPortConfigDot3adAggrRole,
       "me1200LacpPortConfigDot3adAggrTimeout": me1200LacpPortConfigDot3adAggrTimeout,
       "me1200LacpPortConfigDot3adAggrPortPriority": me1200LacpPortConfigDot3adAggrPortPriority,
       "me1200LacpStatus": me1200LacpStatus,
       "me1200LacpSystemStatusTable": me1200LacpSystemStatusTable,
       "me1200LacpSystemStatusEntry": me1200LacpSystemStatusEntry,
       "me1200LacpSystemStatusInterfaceNo": me1200LacpSystemStatusInterfaceNo,
       "me1200LacpSystemStatusDot3adAggrID": me1200LacpSystemStatusDot3adAggrID,
       "me1200LacpSystemStatusDot3adAggrPartnerSystemID": me1200LacpSystemStatusDot3adAggrPartnerSystemID,
       "me1200LacpSystemStatusDot3adAggrPartnerOperKey": me1200LacpSystemStatusDot3adAggrPartnerOperKey,
       "me1200LacpSystemStatusDot3adAggrPartnerOperSystemPriority": me1200LacpSystemStatusDot3adAggrPartnerOperSystemPriority,
       "me1200LacpSystemStatusDot3adAggrPartnerStateLastChanged": me1200LacpSystemStatusDot3adAggrPartnerStateLastChanged,
       "me1200LacpSystemStatusDot3adAggrLocalPorts": me1200LacpSystemStatusDot3adAggrLocalPorts,
       "me1200LacpPortStatusTable": me1200LacpPortStatusTable,
       "me1200LacpPortStatusEntry": me1200LacpPortStatusEntry,
       "me1200LacpPortStatusInterfaceNo": me1200LacpPortStatusInterfaceNo,
       "me1200LacpPortStatusDot3adAggrActorAdminMode": me1200LacpPortStatusDot3adAggrActorAdminMode,
       "me1200LacpPortStatusDot3adAggrActorAdminKey": me1200LacpPortStatusDot3adAggrActorAdminKey,
       "me1200LacpPortStatusDot3adAggrPartnerOperPortIndex": me1200LacpPortStatusDot3adAggrPartnerOperPortIndex,
       "me1200LacpPortStatusDot3adAggrPartnerOperPortPriority": me1200LacpPortStatusDot3adAggrPartnerOperPortPriority,
       "me1200LacpPortStatisticsTable": me1200LacpPortStatisticsTable,
       "me1200LacpPortStatisticsEntry": me1200LacpPortStatisticsEntry,
       "me1200LacpPortStatisticsInterfaceNo": me1200LacpPortStatisticsInterfaceNo,
       "me1200LacpPortStatisticsDot3adAggrRxFrames": me1200LacpPortStatisticsDot3adAggrRxFrames,
       "me1200LacpPortStatisticsDot3adAggrTxFrames": me1200LacpPortStatisticsDot3adAggrTxFrames,
       "me1200LacpPortStatisticsDot3adAggrRxIllegalFrames": me1200LacpPortStatisticsDot3adAggrRxIllegalFrames,
       "me1200LacpPortStatisticsDot3adAggrRxUnknownFrames": me1200LacpPortStatisticsDot3adAggrRxUnknownFrames,
       "me1200LacpControl": me1200LacpControl,
       "me1200LacpPortStatsClearTable": me1200LacpPortStatsClearTable,
       "me1200LacpPortStatsClearEntry": me1200LacpPortStatsClearEntry,
       "me1200LacpPortStatsClearInterfaceNo": me1200LacpPortStatsClearInterfaceNo,
       "me1200LacpPortStatsClearPortStatisticsClear": me1200LacpPortStatsClearPortStatisticsClear,
       "me1200LacpMibConformance": me1200LacpMibConformance,
       "me1200LacpMibCompliances": me1200LacpMibCompliances,
       "me1200LacpMibCompliance": me1200LacpMibCompliance,
       "me1200LacpMibGroups": me1200LacpMibGroups,
       "me1200LacpPortConfigTableInfoGroup": me1200LacpPortConfigTableInfoGroup,
       "me1200LacpSystemStatusTableInfoGroup": me1200LacpSystemStatusTableInfoGroup,
       "me1200LacpPortStatusTableInfoGroup": me1200LacpPortStatusTableInfoGroup,
       "me1200LacpPortStatisticsTableInfoGroup": me1200LacpPortStatisticsTableInfoGroup,
       "me1200LacpPortStatsClearTableInfoGroup": me1200LacpPortStatsClearTableInfoGroup}
)
