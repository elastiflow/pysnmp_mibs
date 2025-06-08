# SNMP MIB module (ME1200-POST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-POST-MIB.mib
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

me1200PostMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118)
)
if mibBuilder.loadTexts:
    me1200PostMib.setRevisions(
        ("2016-05-03 00:00",
         "2014-05-16 00:00",
         "2014-05-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200PostTestResult(TextualConvention, Integer32):
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
        *(("notTested", 0),
          ("pass", 1),
          ("failed", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200PostMibObjects_ObjectIdentity = ObjectIdentity
me1200PostMibObjects = _Me1200PostMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1)
)
_Me1200PostConfig_ObjectIdentity = ObjectIdentity
me1200PostConfig = _Me1200PostConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 2)
)
_Me1200PostConfigGlobals_ObjectIdentity = ObjectIdentity
me1200PostConfigGlobals = _Me1200PostConfigGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 2, 1)
)
_Me1200PostConfigGlobalsMode_Type = TruthValue
_Me1200PostConfigGlobalsMode_Object = MibScalar
me1200PostConfigGlobalsMode = _Me1200PostConfigGlobalsMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 2, 1, 1),
    _Me1200PostConfigGlobalsMode_Type()
)
me1200PostConfigGlobalsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PostConfigGlobalsMode.setStatus("current")
_Me1200PostStatus_ObjectIdentity = ObjectIdentity
me1200PostStatus = _Me1200PostStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 3)
)
_Me1200PostStatusHwComponentTable_Object = MibTable
me1200PostStatusHwComponentTable = _Me1200PostStatusHwComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 3, 1)
)
if mibBuilder.loadTexts:
    me1200PostStatusHwComponentTable.setStatus("current")
_Me1200PostStatusHwComponentEntry_Object = MibTableRow
me1200PostStatusHwComponentEntry = _Me1200PostStatusHwComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 3, 1, 1)
)
me1200PostStatusHwComponentEntry.setIndexNames(
    (0, "ME1200-POST-MIB", "me1200PostStatusHwComponentSwitchId"),
)
if mibBuilder.loadTexts:
    me1200PostStatusHwComponentEntry.setStatus("current")


class _Me1200PostStatusHwComponentSwitchId_Type(Integer32):
    """Custom type me1200PostStatusHwComponentSwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Me1200PostStatusHwComponentSwitchId_Type.__name__ = "Integer32"
_Me1200PostStatusHwComponentSwitchId_Object = MibTableColumn
me1200PostStatusHwComponentSwitchId = _Me1200PostStatusHwComponentSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 3, 1, 1, 1),
    _Me1200PostStatusHwComponentSwitchId_Type()
)
me1200PostStatusHwComponentSwitchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PostStatusHwComponentSwitchId.setStatus("current")
_Me1200PostStatusHwComponentHwBist_Type = ME1200PostTestResult
_Me1200PostStatusHwComponentHwBist_Object = MibTableColumn
me1200PostStatusHwComponentHwBist = _Me1200PostStatusHwComponentHwBist_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 3, 1, 1, 2),
    _Me1200PostStatusHwComponentHwBist_Type()
)
me1200PostStatusHwComponentHwBist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PostStatusHwComponentHwBist.setStatus("current")
_Me1200PostStatusHwComponentTcamBistIs0_Type = ME1200PostTestResult
_Me1200PostStatusHwComponentTcamBistIs0_Object = MibTableColumn
me1200PostStatusHwComponentTcamBistIs0 = _Me1200PostStatusHwComponentTcamBistIs0_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 3, 1, 1, 3),
    _Me1200PostStatusHwComponentTcamBistIs0_Type()
)
me1200PostStatusHwComponentTcamBistIs0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PostStatusHwComponentTcamBistIs0.setStatus("current")
_Me1200PostStatusHwComponentTcamBistIs1_Type = ME1200PostTestResult
_Me1200PostStatusHwComponentTcamBistIs1_Object = MibTableColumn
me1200PostStatusHwComponentTcamBistIs1 = _Me1200PostStatusHwComponentTcamBistIs1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 3, 1, 1, 4),
    _Me1200PostStatusHwComponentTcamBistIs1_Type()
)
me1200PostStatusHwComponentTcamBistIs1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PostStatusHwComponentTcamBistIs1.setStatus("current")
_Me1200PostStatusHwComponentTcamBistIs2_Type = ME1200PostTestResult
_Me1200PostStatusHwComponentTcamBistIs2_Object = MibTableColumn
me1200PostStatusHwComponentTcamBistIs2 = _Me1200PostStatusHwComponentTcamBistIs2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 3, 1, 1, 5),
    _Me1200PostStatusHwComponentTcamBistIs2_Type()
)
me1200PostStatusHwComponentTcamBistIs2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PostStatusHwComponentTcamBistIs2.setStatus("current")
_Me1200PostStatusHwComponentTcamBistEs0_Type = ME1200PostTestResult
_Me1200PostStatusHwComponentTcamBistEs0_Object = MibTableColumn
me1200PostStatusHwComponentTcamBistEs0 = _Me1200PostStatusHwComponentTcamBistEs0_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 3, 1, 1, 6),
    _Me1200PostStatusHwComponentTcamBistEs0_Type()
)
me1200PostStatusHwComponentTcamBistEs0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PostStatusHwComponentTcamBistEs0.setStatus("current")
_Me1200PostStatusHwComponentDdr_Type = ME1200PostTestResult
_Me1200PostStatusHwComponentDdr_Object = MibTableColumn
me1200PostStatusHwComponentDdr = _Me1200PostStatusHwComponentDdr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 3, 1, 1, 7),
    _Me1200PostStatusHwComponentDdr_Type()
)
me1200PostStatusHwComponentDdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PostStatusHwComponentDdr.setStatus("current")
_Me1200PostStatusHwComponentEeprom_Type = ME1200PostTestResult
_Me1200PostStatusHwComponentEeprom_Object = MibTableColumn
me1200PostStatusHwComponentEeprom = _Me1200PostStatusHwComponentEeprom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 3, 1, 1, 8),
    _Me1200PostStatusHwComponentEeprom_Type()
)
me1200PostStatusHwComponentEeprom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PostStatusHwComponentEeprom.setStatus("current")
_Me1200PostStatusInterfaceTable_Object = MibTable
me1200PostStatusInterfaceTable = _Me1200PostStatusInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 3, 2)
)
if mibBuilder.loadTexts:
    me1200PostStatusInterfaceTable.setStatus("current")
_Me1200PostStatusInterfaceEntry_Object = MibTableRow
me1200PostStatusInterfaceEntry = _Me1200PostStatusInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 3, 2, 1)
)
me1200PostStatusInterfaceEntry.setIndexNames(
    (0, "ME1200-POST-MIB", "me1200PostStatusInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    me1200PostStatusInterfaceEntry.setStatus("current")
_Me1200PostStatusInterfaceIfIndex_Type = ME1200InterfaceIndex
_Me1200PostStatusInterfaceIfIndex_Object = MibTableColumn
me1200PostStatusInterfaceIfIndex = _Me1200PostStatusInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 3, 2, 1, 1),
    _Me1200PostStatusInterfaceIfIndex_Type()
)
me1200PostStatusInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PostStatusInterfaceIfIndex.setStatus("current")
_Me1200PostStatusInterfaceLoopback_Type = ME1200PostTestResult
_Me1200PostStatusInterfaceLoopback_Object = MibTableColumn
me1200PostStatusInterfaceLoopback = _Me1200PostStatusInterfaceLoopback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 3, 2, 1, 2),
    _Me1200PostStatusInterfaceLoopback_Type()
)
me1200PostStatusInterfaceLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PostStatusInterfaceLoopback.setStatus("current")
_Me1200PostStatusInterfaceI2cBusScan_Type = ME1200PostTestResult
_Me1200PostStatusInterfaceI2cBusScan_Object = MibTableColumn
me1200PostStatusInterfaceI2cBusScan = _Me1200PostStatusInterfaceI2cBusScan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 3, 2, 1, 3),
    _Me1200PostStatusInterfaceI2cBusScan_Type()
)
me1200PostStatusInterfaceI2cBusScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PostStatusInterfaceI2cBusScan.setStatus("current")
_Me1200PostStatusMonitorIcTable_Object = MibTable
me1200PostStatusMonitorIcTable = _Me1200PostStatusMonitorIcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 3, 3)
)
if mibBuilder.loadTexts:
    me1200PostStatusMonitorIcTable.setStatus("current")
_Me1200PostStatusMonitorIcEntry_Object = MibTableRow
me1200PostStatusMonitorIcEntry = _Me1200PostStatusMonitorIcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 3, 3, 1)
)
me1200PostStatusMonitorIcEntry.setIndexNames(
    (0, "ME1200-POST-MIB", "me1200PostStatusMonitorIcSwitchId"),
    (0, "ME1200-POST-MIB", "me1200PostStatusMonitorIcIcId"),
)
if mibBuilder.loadTexts:
    me1200PostStatusMonitorIcEntry.setStatus("current")


class _Me1200PostStatusMonitorIcSwitchId_Type(Integer32):
    """Custom type me1200PostStatusMonitorIcSwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Me1200PostStatusMonitorIcSwitchId_Type.__name__ = "Integer32"
_Me1200PostStatusMonitorIcSwitchId_Object = MibTableColumn
me1200PostStatusMonitorIcSwitchId = _Me1200PostStatusMonitorIcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 3, 3, 1, 1),
    _Me1200PostStatusMonitorIcSwitchId_Type()
)
me1200PostStatusMonitorIcSwitchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PostStatusMonitorIcSwitchId.setStatus("current")


class _Me1200PostStatusMonitorIcIcId_Type(Integer32):
    """Custom type me1200PostStatusMonitorIcIcId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Me1200PostStatusMonitorIcIcId_Type.__name__ = "Integer32"
_Me1200PostStatusMonitorIcIcId_Object = MibTableColumn
me1200PostStatusMonitorIcIcId = _Me1200PostStatusMonitorIcIcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 3, 3, 1, 2),
    _Me1200PostStatusMonitorIcIcId_Type()
)
me1200PostStatusMonitorIcIcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PostStatusMonitorIcIcId.setStatus("current")
_Me1200PostStatusMonitorIcI2cBusScan_Type = ME1200PostTestResult
_Me1200PostStatusMonitorIcI2cBusScan_Object = MibTableColumn
me1200PostStatusMonitorIcI2cBusScan = _Me1200PostStatusMonitorIcI2cBusScan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 3, 3, 1, 3),
    _Me1200PostStatusMonitorIcI2cBusScan_Type()
)
me1200PostStatusMonitorIcI2cBusScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PostStatusMonitorIcI2cBusScan.setStatus("current")


class _Me1200PostStatusMonitorIcV5_Type(ME1200DisplayString):
    """Custom type me1200PostStatusMonitorIcV5 based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Me1200PostStatusMonitorIcV5_Type.__name__ = "ME1200DisplayString"
_Me1200PostStatusMonitorIcV5_Object = MibTableColumn
me1200PostStatusMonitorIcV5 = _Me1200PostStatusMonitorIcV5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 3, 3, 1, 4),
    _Me1200PostStatusMonitorIcV5_Type()
)
me1200PostStatusMonitorIcV5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PostStatusMonitorIcV5.setStatus("current")


class _Me1200PostStatusMonitorIcV12_Type(ME1200DisplayString):
    """Custom type me1200PostStatusMonitorIcV12 based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Me1200PostStatusMonitorIcV12_Type.__name__ = "ME1200DisplayString"
_Me1200PostStatusMonitorIcV12_Object = MibTableColumn
me1200PostStatusMonitorIcV12 = _Me1200PostStatusMonitorIcV12_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 3, 3, 1, 5),
    _Me1200PostStatusMonitorIcV12_Type()
)
me1200PostStatusMonitorIcV12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PostStatusMonitorIcV12.setStatus("current")


class _Me1200PostStatusMonitorIcV2dot5_Type(ME1200DisplayString):
    """Custom type me1200PostStatusMonitorIcV2dot5 based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Me1200PostStatusMonitorIcV2dot5_Type.__name__ = "ME1200DisplayString"
_Me1200PostStatusMonitorIcV2dot5_Object = MibTableColumn
me1200PostStatusMonitorIcV2dot5 = _Me1200PostStatusMonitorIcV2dot5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 3, 3, 1, 6),
    _Me1200PostStatusMonitorIcV2dot5_Type()
)
me1200PostStatusMonitorIcV2dot5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PostStatusMonitorIcV2dot5.setStatus("current")


class _Me1200PostStatusMonitorIcVccp_Type(ME1200DisplayString):
    """Custom type me1200PostStatusMonitorIcVccp based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Me1200PostStatusMonitorIcVccp_Type.__name__ = "ME1200DisplayString"
_Me1200PostStatusMonitorIcVccp_Object = MibTableColumn
me1200PostStatusMonitorIcVccp = _Me1200PostStatusMonitorIcVccp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 3, 3, 1, 7),
    _Me1200PostStatusMonitorIcVccp_Type()
)
me1200PostStatusMonitorIcVccp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PostStatusMonitorIcVccp.setStatus("current")
_Me1200PostStatusMonitorIcLocalTemperature_Type = Unsigned32
_Me1200PostStatusMonitorIcLocalTemperature_Object = MibTableColumn
me1200PostStatusMonitorIcLocalTemperature = _Me1200PostStatusMonitorIcLocalTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 3, 3, 1, 8),
    _Me1200PostStatusMonitorIcLocalTemperature_Type()
)
me1200PostStatusMonitorIcLocalTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PostStatusMonitorIcLocalTemperature.setStatus("current")
_Me1200PostStatusMonitorIcRemoteTemperature_Type = Unsigned32
_Me1200PostStatusMonitorIcRemoteTemperature_Object = MibTableColumn
me1200PostStatusMonitorIcRemoteTemperature = _Me1200PostStatusMonitorIcRemoteTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 3, 3, 1, 9),
    _Me1200PostStatusMonitorIcRemoteTemperature_Type()
)
me1200PostStatusMonitorIcRemoteTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PostStatusMonitorIcRemoteTemperature.setStatus("current")
_Me1200PostNotificationPrefix_ObjectIdentity = ObjectIdentity
me1200PostNotificationPrefix = _Me1200PostNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 4)
)
_Me1200PostNotification_ObjectIdentity = ObjectIdentity
me1200PostNotification = _Me1200PostNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 4, 0)
)
_Me1200PostMibConformance_ObjectIdentity = ObjectIdentity
me1200PostMibConformance = _Me1200PostMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 2)
)
_Me1200PostMibCompliances_ObjectIdentity = ObjectIdentity
me1200PostMibCompliances = _Me1200PostMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 2, 1)
)
_Me1200PostMibGroups_ObjectIdentity = ObjectIdentity
me1200PostMibGroups = _Me1200PostMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 2, 2)
)

# Managed Objects groups

me1200PostConfigGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 2, 2, 1)
)
me1200PostConfigGlobalsInfoGroup.setObjects(
    ("ME1200-POST-MIB", "me1200PostConfigGlobalsMode")
)
if mibBuilder.loadTexts:
    me1200PostConfigGlobalsInfoGroup.setStatus("current")

me1200PostStatusHwComponentTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 2, 2, 2)
)
me1200PostStatusHwComponentTableInfoGroup.setObjects(
      *(("ME1200-POST-MIB", "me1200PostStatusHwComponentHwBist"),
        ("ME1200-POST-MIB", "me1200PostStatusHwComponentTcamBistIs0"),
        ("ME1200-POST-MIB", "me1200PostStatusHwComponentTcamBistIs1"),
        ("ME1200-POST-MIB", "me1200PostStatusHwComponentTcamBistIs2"),
        ("ME1200-POST-MIB", "me1200PostStatusHwComponentTcamBistEs0"),
        ("ME1200-POST-MIB", "me1200PostStatusHwComponentDdr"),
        ("ME1200-POST-MIB", "me1200PostStatusHwComponentEeprom"))
)
if mibBuilder.loadTexts:
    me1200PostStatusHwComponentTableInfoGroup.setStatus("current")

me1200PostStatusInterfaceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 2, 2, 3)
)
me1200PostStatusInterfaceTableInfoGroup.setObjects(
      *(("ME1200-POST-MIB", "me1200PostStatusInterfaceLoopback"),
        ("ME1200-POST-MIB", "me1200PostStatusInterfaceI2cBusScan"))
)
if mibBuilder.loadTexts:
    me1200PostStatusInterfaceTableInfoGroup.setStatus("current")

me1200PostStatusMonitorIcTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 2, 2, 4)
)
me1200PostStatusMonitorIcTableInfoGroup.setObjects(
      *(("ME1200-POST-MIB", "me1200PostStatusMonitorIcI2cBusScan"),
        ("ME1200-POST-MIB", "me1200PostStatusMonitorIcV5"),
        ("ME1200-POST-MIB", "me1200PostStatusMonitorIcV12"),
        ("ME1200-POST-MIB", "me1200PostStatusMonitorIcV2dot5"),
        ("ME1200-POST-MIB", "me1200PostStatusMonitorIcVccp"),
        ("ME1200-POST-MIB", "me1200PostStatusMonitorIcLocalTemperature"),
        ("ME1200-POST-MIB", "me1200PostStatusMonitorIcRemoteTemperature"))
)
if mibBuilder.loadTexts:
    me1200PostStatusMonitorIcTableInfoGroup.setStatus("current")


# Notification objects

me1200PostNotificationErrorDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 1, 4, 0, 1)
)
if mibBuilder.loadTexts:
    me1200PostNotificationErrorDetected.setStatus(
        "current"
    )


# Notifications groups

me1200PostNotificationInfoGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 2, 2, 5)
)
me1200PostNotificationInfoGroup.setObjects(
    ("ME1200-POST-MIB", "me1200PostNotificationErrorDetected")
)
if mibBuilder.loadTexts:
    me1200PostNotificationInfoGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

me1200PostMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 118, 2, 1, 1)
)
me1200PostMibCompliance.setObjects(
      *(("ME1200-POST-MIB", "me1200PostConfigGlobalsInfoGroup"),
        ("ME1200-POST-MIB", "me1200PostStatusHwComponentTableInfoGroup"),
        ("ME1200-POST-MIB", "me1200PostStatusInterfaceTableInfoGroup"),
        ("ME1200-POST-MIB", "me1200PostStatusMonitorIcTableInfoGroup"),
        ("ME1200-POST-MIB", "me1200PostNotificationInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200PostMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-POST-MIB",
    **{"ME1200PostTestResult": ME1200PostTestResult,
       "me1200PostMib": me1200PostMib,
       "me1200PostMibObjects": me1200PostMibObjects,
       "me1200PostConfig": me1200PostConfig,
       "me1200PostConfigGlobals": me1200PostConfigGlobals,
       "me1200PostConfigGlobalsMode": me1200PostConfigGlobalsMode,
       "me1200PostStatus": me1200PostStatus,
       "me1200PostStatusHwComponentTable": me1200PostStatusHwComponentTable,
       "me1200PostStatusHwComponentEntry": me1200PostStatusHwComponentEntry,
       "me1200PostStatusHwComponentSwitchId": me1200PostStatusHwComponentSwitchId,
       "me1200PostStatusHwComponentHwBist": me1200PostStatusHwComponentHwBist,
       "me1200PostStatusHwComponentTcamBistIs0": me1200PostStatusHwComponentTcamBistIs0,
       "me1200PostStatusHwComponentTcamBistIs1": me1200PostStatusHwComponentTcamBistIs1,
       "me1200PostStatusHwComponentTcamBistIs2": me1200PostStatusHwComponentTcamBistIs2,
       "me1200PostStatusHwComponentTcamBistEs0": me1200PostStatusHwComponentTcamBistEs0,
       "me1200PostStatusHwComponentDdr": me1200PostStatusHwComponentDdr,
       "me1200PostStatusHwComponentEeprom": me1200PostStatusHwComponentEeprom,
       "me1200PostStatusInterfaceTable": me1200PostStatusInterfaceTable,
       "me1200PostStatusInterfaceEntry": me1200PostStatusInterfaceEntry,
       "me1200PostStatusInterfaceIfIndex": me1200PostStatusInterfaceIfIndex,
       "me1200PostStatusInterfaceLoopback": me1200PostStatusInterfaceLoopback,
       "me1200PostStatusInterfaceI2cBusScan": me1200PostStatusInterfaceI2cBusScan,
       "me1200PostStatusMonitorIcTable": me1200PostStatusMonitorIcTable,
       "me1200PostStatusMonitorIcEntry": me1200PostStatusMonitorIcEntry,
       "me1200PostStatusMonitorIcSwitchId": me1200PostStatusMonitorIcSwitchId,
       "me1200PostStatusMonitorIcIcId": me1200PostStatusMonitorIcIcId,
       "me1200PostStatusMonitorIcI2cBusScan": me1200PostStatusMonitorIcI2cBusScan,
       "me1200PostStatusMonitorIcV5": me1200PostStatusMonitorIcV5,
       "me1200PostStatusMonitorIcV12": me1200PostStatusMonitorIcV12,
       "me1200PostStatusMonitorIcV2dot5": me1200PostStatusMonitorIcV2dot5,
       "me1200PostStatusMonitorIcVccp": me1200PostStatusMonitorIcVccp,
       "me1200PostStatusMonitorIcLocalTemperature": me1200PostStatusMonitorIcLocalTemperature,
       "me1200PostStatusMonitorIcRemoteTemperature": me1200PostStatusMonitorIcRemoteTemperature,
       "me1200PostNotificationPrefix": me1200PostNotificationPrefix,
       "me1200PostNotification": me1200PostNotification,
       "me1200PostNotificationErrorDetected": me1200PostNotificationErrorDetected,
       "me1200PostMibConformance": me1200PostMibConformance,
       "me1200PostMibCompliances": me1200PostMibCompliances,
       "me1200PostMibCompliance": me1200PostMibCompliance,
       "me1200PostMibGroups": me1200PostMibGroups,
       "me1200PostConfigGlobalsInfoGroup": me1200PostConfigGlobalsInfoGroup,
       "me1200PostStatusHwComponentTableInfoGroup": me1200PostStatusHwComponentTableInfoGroup,
       "me1200PostStatusInterfaceTableInfoGroup": me1200PostStatusInterfaceTableInfoGroup,
       "me1200PostStatusMonitorIcTableInfoGroup": me1200PostStatusMonitorIcTableInfoGroup,
       "me1200PostNotificationInfoGroup": me1200PostNotificationInfoGroup}
)
