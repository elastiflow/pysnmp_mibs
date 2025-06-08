# SNMP MIB module (ME1200-UDLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-UDLD-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:31 2025
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

(ME1200DisplayString,
 ME1200InterfaceIndex) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200DisplayString",
    "ME1200InterfaceIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

me1200UdldMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123)
)
if mibBuilder.loadTexts:
    me1200UdldMib.setRevisions(
        ("2014-03-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200UdldDetectionState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("inDeterminant", 0),
          ("uniDirectional", 1),
          ("biDirectional", 2),
          ("neighborMismatch", 3),
          ("loopback", 4),
          ("multipleNeighbor", 5))
    )



class ME1200UdldMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("normal", 1),
          ("aggressive", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200UdldMibObjects_ObjectIdentity = ObjectIdentity
me1200UdldMibObjects = _Me1200UdldMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1)
)
_Me1200UdldConfig_ObjectIdentity = ObjectIdentity
me1200UdldConfig = _Me1200UdldConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 2)
)
_Me1200UdldConfigInterface_ObjectIdentity = ObjectIdentity
me1200UdldConfigInterface = _Me1200UdldConfigInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 2, 1)
)
_Me1200UdldConfigInterfaceParamTable_Object = MibTable
me1200UdldConfigInterfaceParamTable = _Me1200UdldConfigInterfaceParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    me1200UdldConfigInterfaceParamTable.setStatus("current")
_Me1200UdldConfigInterfaceParamEntry_Object = MibTableRow
me1200UdldConfigInterfaceParamEntry = _Me1200UdldConfigInterfaceParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 2, 1, 1, 1)
)
me1200UdldConfigInterfaceParamEntry.setIndexNames(
    (0, "ME1200-UDLD-MIB", "me1200UdldConfigInterfaceParamIfIndex"),
)
if mibBuilder.loadTexts:
    me1200UdldConfigInterfaceParamEntry.setStatus("current")
_Me1200UdldConfigInterfaceParamIfIndex_Type = ME1200InterfaceIndex
_Me1200UdldConfigInterfaceParamIfIndex_Object = MibTableColumn
me1200UdldConfigInterfaceParamIfIndex = _Me1200UdldConfigInterfaceParamIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 2, 1, 1, 1, 1),
    _Me1200UdldConfigInterfaceParamIfIndex_Type()
)
me1200UdldConfigInterfaceParamIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200UdldConfigInterfaceParamIfIndex.setStatus("current")
_Me1200UdldConfigInterfaceParamUdldMode_Type = ME1200UdldMode
_Me1200UdldConfigInterfaceParamUdldMode_Object = MibTableColumn
me1200UdldConfigInterfaceParamUdldMode = _Me1200UdldConfigInterfaceParamUdldMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 2, 1, 1, 1, 2),
    _Me1200UdldConfigInterfaceParamUdldMode_Type()
)
me1200UdldConfigInterfaceParamUdldMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200UdldConfigInterfaceParamUdldMode.setStatus("current")


class _Me1200UdldConfigInterfaceParamProbeMsgInterval_Type(Unsigned32):
    """Custom type me1200UdldConfigInterfaceParamProbeMsgInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 90),
    )


_Me1200UdldConfigInterfaceParamProbeMsgInterval_Type.__name__ = "Unsigned32"
_Me1200UdldConfigInterfaceParamProbeMsgInterval_Object = MibTableColumn
me1200UdldConfigInterfaceParamProbeMsgInterval = _Me1200UdldConfigInterfaceParamProbeMsgInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 2, 1, 1, 1, 3),
    _Me1200UdldConfigInterfaceParamProbeMsgInterval_Type()
)
me1200UdldConfigInterfaceParamProbeMsgInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200UdldConfigInterfaceParamProbeMsgInterval.setStatus("current")
_Me1200UdldStatus_ObjectIdentity = ObjectIdentity
me1200UdldStatus = _Me1200UdldStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3)
)
_Me1200UdldStatusInterface_ObjectIdentity = ObjectIdentity
me1200UdldStatusInterface = _Me1200UdldStatusInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3, 1)
)
_Me1200UdldStatusInterfaceTable_Object = MibTable
me1200UdldStatusInterfaceTable = _Me1200UdldStatusInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    me1200UdldStatusInterfaceTable.setStatus("current")
_Me1200UdldStatusInterfaceEntry_Object = MibTableRow
me1200UdldStatusInterfaceEntry = _Me1200UdldStatusInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3, 1, 1, 1)
)
me1200UdldStatusInterfaceEntry.setIndexNames(
    (0, "ME1200-UDLD-MIB", "me1200UdldStatusInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    me1200UdldStatusInterfaceEntry.setStatus("current")
_Me1200UdldStatusInterfaceIfIndex_Type = ME1200InterfaceIndex
_Me1200UdldStatusInterfaceIfIndex_Object = MibTableColumn
me1200UdldStatusInterfaceIfIndex = _Me1200UdldStatusInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3, 1, 1, 1, 1),
    _Me1200UdldStatusInterfaceIfIndex_Type()
)
me1200UdldStatusInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200UdldStatusInterfaceIfIndex.setStatus("current")


class _Me1200UdldStatusInterfaceDeviceID_Type(ME1200DisplayString):
    """Custom type me1200UdldStatusInterfaceDeviceID based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_Me1200UdldStatusInterfaceDeviceID_Type.__name__ = "ME1200DisplayString"
_Me1200UdldStatusInterfaceDeviceID_Object = MibTableColumn
me1200UdldStatusInterfaceDeviceID = _Me1200UdldStatusInterfaceDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3, 1, 1, 1, 2),
    _Me1200UdldStatusInterfaceDeviceID_Type()
)
me1200UdldStatusInterfaceDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200UdldStatusInterfaceDeviceID.setStatus("current")


class _Me1200UdldStatusInterfaceDeviceName_Type(ME1200DisplayString):
    """Custom type me1200UdldStatusInterfaceDeviceName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_Me1200UdldStatusInterfaceDeviceName_Type.__name__ = "ME1200DisplayString"
_Me1200UdldStatusInterfaceDeviceName_Object = MibTableColumn
me1200UdldStatusInterfaceDeviceName = _Me1200UdldStatusInterfaceDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3, 1, 1, 1, 3),
    _Me1200UdldStatusInterfaceDeviceName_Type()
)
me1200UdldStatusInterfaceDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200UdldStatusInterfaceDeviceName.setStatus("current")
_Me1200UdldStatusInterfaceLinkState_Type = ME1200UdldDetectionState
_Me1200UdldStatusInterfaceLinkState_Object = MibTableColumn
me1200UdldStatusInterfaceLinkState = _Me1200UdldStatusInterfaceLinkState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3, 1, 1, 1, 4),
    _Me1200UdldStatusInterfaceLinkState_Type()
)
me1200UdldStatusInterfaceLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200UdldStatusInterfaceLinkState.setStatus("current")
_Me1200UdldStatusInterfaceNeighborTable_Object = MibTable
me1200UdldStatusInterfaceNeighborTable = _Me1200UdldStatusInterfaceNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    me1200UdldStatusInterfaceNeighborTable.setStatus("current")
_Me1200UdldStatusInterfaceNeighborEntry_Object = MibTableRow
me1200UdldStatusInterfaceNeighborEntry = _Me1200UdldStatusInterfaceNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3, 1, 2, 1)
)
me1200UdldStatusInterfaceNeighborEntry.setIndexNames(
    (0, "ME1200-UDLD-MIB", "me1200UdldStatusInterfaceNeighborIfIndex"),
)
if mibBuilder.loadTexts:
    me1200UdldStatusInterfaceNeighborEntry.setStatus("current")
_Me1200UdldStatusInterfaceNeighborIfIndex_Type = ME1200InterfaceIndex
_Me1200UdldStatusInterfaceNeighborIfIndex_Object = MibTableColumn
me1200UdldStatusInterfaceNeighborIfIndex = _Me1200UdldStatusInterfaceNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3, 1, 2, 1, 1),
    _Me1200UdldStatusInterfaceNeighborIfIndex_Type()
)
me1200UdldStatusInterfaceNeighborIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200UdldStatusInterfaceNeighborIfIndex.setStatus("current")


class _Me1200UdldStatusInterfaceNeighborNeighborDeviceID_Type(ME1200DisplayString):
    """Custom type me1200UdldStatusInterfaceNeighborNeighborDeviceID based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_Me1200UdldStatusInterfaceNeighborNeighborDeviceID_Type.__name__ = "ME1200DisplayString"
_Me1200UdldStatusInterfaceNeighborNeighborDeviceID_Object = MibTableColumn
me1200UdldStatusInterfaceNeighborNeighborDeviceID = _Me1200UdldStatusInterfaceNeighborNeighborDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3, 1, 2, 1, 2),
    _Me1200UdldStatusInterfaceNeighborNeighborDeviceID_Type()
)
me1200UdldStatusInterfaceNeighborNeighborDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200UdldStatusInterfaceNeighborNeighborDeviceID.setStatus("current")


class _Me1200UdldStatusInterfaceNeighborNeighborPortID_Type(ME1200DisplayString):
    """Custom type me1200UdldStatusInterfaceNeighborNeighborPortID based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_Me1200UdldStatusInterfaceNeighborNeighborPortID_Type.__name__ = "ME1200DisplayString"
_Me1200UdldStatusInterfaceNeighborNeighborPortID_Object = MibTableColumn
me1200UdldStatusInterfaceNeighborNeighborPortID = _Me1200UdldStatusInterfaceNeighborNeighborPortID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3, 1, 2, 1, 3),
    _Me1200UdldStatusInterfaceNeighborNeighborPortID_Type()
)
me1200UdldStatusInterfaceNeighborNeighborPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200UdldStatusInterfaceNeighborNeighborPortID.setStatus("current")


class _Me1200UdldStatusInterfaceNeighborNeighborDeviceName_Type(ME1200DisplayString):
    """Custom type me1200UdldStatusInterfaceNeighborNeighborDeviceName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_Me1200UdldStatusInterfaceNeighborNeighborDeviceName_Type.__name__ = "ME1200DisplayString"
_Me1200UdldStatusInterfaceNeighborNeighborDeviceName_Object = MibTableColumn
me1200UdldStatusInterfaceNeighborNeighborDeviceName = _Me1200UdldStatusInterfaceNeighborNeighborDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3, 1, 2, 1, 4),
    _Me1200UdldStatusInterfaceNeighborNeighborDeviceName_Type()
)
me1200UdldStatusInterfaceNeighborNeighborDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200UdldStatusInterfaceNeighborNeighborDeviceName.setStatus("current")
_Me1200UdldStatusInterfaceNeighborLinkDetectionState_Type = ME1200UdldDetectionState
_Me1200UdldStatusInterfaceNeighborLinkDetectionState_Object = MibTableColumn
me1200UdldStatusInterfaceNeighborLinkDetectionState = _Me1200UdldStatusInterfaceNeighborLinkDetectionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3, 1, 2, 1, 5),
    _Me1200UdldStatusInterfaceNeighborLinkDetectionState_Type()
)
me1200UdldStatusInterfaceNeighborLinkDetectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200UdldStatusInterfaceNeighborLinkDetectionState.setStatus("current")
_Me1200UdldMibConformance_ObjectIdentity = ObjectIdentity
me1200UdldMibConformance = _Me1200UdldMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 2)
)
_Me1200UdldMibCompliances_ObjectIdentity = ObjectIdentity
me1200UdldMibCompliances = _Me1200UdldMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 2, 1)
)
_Me1200UdldMibGroups_ObjectIdentity = ObjectIdentity
me1200UdldMibGroups = _Me1200UdldMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 2, 2)
)

# Managed Objects groups

me1200UdldConfigInterfaceParamTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 2, 2, 1)
)
me1200UdldConfigInterfaceParamTableInfoGroup.setObjects(
      *(("ME1200-UDLD-MIB", "me1200UdldConfigInterfaceParamUdldMode"),
        ("ME1200-UDLD-MIB", "me1200UdldConfigInterfaceParamProbeMsgInterval"))
)
if mibBuilder.loadTexts:
    me1200UdldConfigInterfaceParamTableInfoGroup.setStatus("current")

me1200UdldStatusInterfaceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 2, 2, 2)
)
me1200UdldStatusInterfaceTableInfoGroup.setObjects(
      *(("ME1200-UDLD-MIB", "me1200UdldStatusInterfaceDeviceID"),
        ("ME1200-UDLD-MIB", "me1200UdldStatusInterfaceDeviceName"),
        ("ME1200-UDLD-MIB", "me1200UdldStatusInterfaceLinkState"))
)
if mibBuilder.loadTexts:
    me1200UdldStatusInterfaceTableInfoGroup.setStatus("current")

me1200UdldStatusInterfaceNeighborTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 2, 2, 3)
)
me1200UdldStatusInterfaceNeighborTableInfoGroup.setObjects(
      *(("ME1200-UDLD-MIB", "me1200UdldStatusInterfaceNeighborNeighborDeviceID"),
        ("ME1200-UDLD-MIB", "me1200UdldStatusInterfaceNeighborNeighborPortID"),
        ("ME1200-UDLD-MIB", "me1200UdldStatusInterfaceNeighborNeighborDeviceName"),
        ("ME1200-UDLD-MIB", "me1200UdldStatusInterfaceNeighborLinkDetectionState"))
)
if mibBuilder.loadTexts:
    me1200UdldStatusInterfaceNeighborTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200UdldMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 2, 1, 1)
)
me1200UdldMibCompliance.setObjects(
      *(("ME1200-UDLD-MIB", "me1200UdldConfigInterfaceParamTableInfoGroup"),
        ("ME1200-UDLD-MIB", "me1200UdldStatusInterfaceTableInfoGroup"),
        ("ME1200-UDLD-MIB", "me1200UdldStatusInterfaceNeighborTableInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200UdldMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-UDLD-MIB",
    **{"ME1200UdldDetectionState": ME1200UdldDetectionState,
       "ME1200UdldMode": ME1200UdldMode,
       "me1200UdldMib": me1200UdldMib,
       "me1200UdldMibObjects": me1200UdldMibObjects,
       "me1200UdldConfig": me1200UdldConfig,
       "me1200UdldConfigInterface": me1200UdldConfigInterface,
       "me1200UdldConfigInterfaceParamTable": me1200UdldConfigInterfaceParamTable,
       "me1200UdldConfigInterfaceParamEntry": me1200UdldConfigInterfaceParamEntry,
       "me1200UdldConfigInterfaceParamIfIndex": me1200UdldConfigInterfaceParamIfIndex,
       "me1200UdldConfigInterfaceParamUdldMode": me1200UdldConfigInterfaceParamUdldMode,
       "me1200UdldConfigInterfaceParamProbeMsgInterval": me1200UdldConfigInterfaceParamProbeMsgInterval,
       "me1200UdldStatus": me1200UdldStatus,
       "me1200UdldStatusInterface": me1200UdldStatusInterface,
       "me1200UdldStatusInterfaceTable": me1200UdldStatusInterfaceTable,
       "me1200UdldStatusInterfaceEntry": me1200UdldStatusInterfaceEntry,
       "me1200UdldStatusInterfaceIfIndex": me1200UdldStatusInterfaceIfIndex,
       "me1200UdldStatusInterfaceDeviceID": me1200UdldStatusInterfaceDeviceID,
       "me1200UdldStatusInterfaceDeviceName": me1200UdldStatusInterfaceDeviceName,
       "me1200UdldStatusInterfaceLinkState": me1200UdldStatusInterfaceLinkState,
       "me1200UdldStatusInterfaceNeighborTable": me1200UdldStatusInterfaceNeighborTable,
       "me1200UdldStatusInterfaceNeighborEntry": me1200UdldStatusInterfaceNeighborEntry,
       "me1200UdldStatusInterfaceNeighborIfIndex": me1200UdldStatusInterfaceNeighborIfIndex,
       "me1200UdldStatusInterfaceNeighborNeighborDeviceID": me1200UdldStatusInterfaceNeighborNeighborDeviceID,
       "me1200UdldStatusInterfaceNeighborNeighborPortID": me1200UdldStatusInterfaceNeighborNeighborPortID,
       "me1200UdldStatusInterfaceNeighborNeighborDeviceName": me1200UdldStatusInterfaceNeighborNeighborDeviceName,
       "me1200UdldStatusInterfaceNeighborLinkDetectionState": me1200UdldStatusInterfaceNeighborLinkDetectionState,
       "me1200UdldMibConformance": me1200UdldMibConformance,
       "me1200UdldMibCompliances": me1200UdldMibCompliances,
       "me1200UdldMibCompliance": me1200UdldMibCompliance,
       "me1200UdldMibGroups": me1200UdldMibGroups,
       "me1200UdldConfigInterfaceParamTableInfoGroup": me1200UdldConfigInterfaceParamTableInfoGroup,
       "me1200UdldStatusInterfaceTableInfoGroup": me1200UdldStatusInterfaceTableInfoGroup,
       "me1200UdldStatusInterfaceNeighborTableInfoGroup": me1200UdldStatusInterfaceNeighborTableInfoGroup}
)
