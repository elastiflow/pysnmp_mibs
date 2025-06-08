# SNMP MIB module (ME1200-SYSUTIL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-SYSUTIL-MIB.mib
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

(ME1200DisplayString,) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200DisplayString")

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

me1200SysutilMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24)
)
if mibBuilder.loadTexts:
    me1200SysutilMib.setRevisions(
        ("2014-04-28 00:00",
         "2014-01-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200SysutilPowerSupplyStateType(TextualConvention, Integer32):
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
        *(("active", 0),
          ("standby", 1),
          ("notPresent", 2))
    )



class ME1200SysutilRebootType(TextualConvention, Integer32):
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
        *(("noReboot", 0),
          ("coldReboot", 1),
          ("warmReboot", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200SysutilMibObjects_ObjectIdentity = ObjectIdentity
me1200SysutilMibObjects = _Me1200SysutilMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1)
)
_Me1200SysutilCapabilities_ObjectIdentity = ObjectIdentity
me1200SysutilCapabilities = _Me1200SysutilCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 1)
)
_Me1200SysutilCapabilitiesWarmRebootSupported_Type = TruthValue
_Me1200SysutilCapabilitiesWarmRebootSupported_Object = MibScalar
me1200SysutilCapabilitiesWarmRebootSupported = _Me1200SysutilCapabilitiesWarmRebootSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 1, 1),
    _Me1200SysutilCapabilitiesWarmRebootSupported_Type()
)
me1200SysutilCapabilitiesWarmRebootSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SysutilCapabilitiesWarmRebootSupported.setStatus("current")
_Me1200SysutilStatus_ObjectIdentity = ObjectIdentity
me1200SysutilStatus = _Me1200SysutilStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3)
)
_Me1200SysutilStatusCpuLoad_ObjectIdentity = ObjectIdentity
me1200SysutilStatusCpuLoad = _Me1200SysutilStatusCpuLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 1)
)
_Me1200SysutilStatusCpuLoadAverage100msec_Type = Unsigned32
_Me1200SysutilStatusCpuLoadAverage100msec_Object = MibScalar
me1200SysutilStatusCpuLoadAverage100msec = _Me1200SysutilStatusCpuLoadAverage100msec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 1, 1),
    _Me1200SysutilStatusCpuLoadAverage100msec_Type()
)
me1200SysutilStatusCpuLoadAverage100msec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SysutilStatusCpuLoadAverage100msec.setStatus("current")
_Me1200SysutilStatusCpuLoadAverage1sec_Type = Unsigned32
_Me1200SysutilStatusCpuLoadAverage1sec_Object = MibScalar
me1200SysutilStatusCpuLoadAverage1sec = _Me1200SysutilStatusCpuLoadAverage1sec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 1, 2),
    _Me1200SysutilStatusCpuLoadAverage1sec_Type()
)
me1200SysutilStatusCpuLoadAverage1sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SysutilStatusCpuLoadAverage1sec.setStatus("current")
_Me1200SysutilStatusCpuLoadAverage10sec_Type = Unsigned32
_Me1200SysutilStatusCpuLoadAverage10sec_Object = MibScalar
me1200SysutilStatusCpuLoadAverage10sec = _Me1200SysutilStatusCpuLoadAverage10sec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 1, 3),
    _Me1200SysutilStatusCpuLoadAverage10sec_Type()
)
me1200SysutilStatusCpuLoadAverage10sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SysutilStatusCpuLoadAverage10sec.setStatus("current")
_Me1200SysutilStatusPowerSupplyTable_Object = MibTable
me1200SysutilStatusPowerSupplyTable = _Me1200SysutilStatusPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 2)
)
if mibBuilder.loadTexts:
    me1200SysutilStatusPowerSupplyTable.setStatus("current")
_Me1200SysutilStatusPowerSupplyEntry_Object = MibTableRow
me1200SysutilStatusPowerSupplyEntry = _Me1200SysutilStatusPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 2, 1)
)
me1200SysutilStatusPowerSupplyEntry.setIndexNames(
    (0, "ME1200-SYSUTIL-MIB", "me1200SysutilStatusPowerSupplySwitchId"),
    (0, "ME1200-SYSUTIL-MIB", "me1200SysutilStatusPowerSupplyPsuId"),
)
if mibBuilder.loadTexts:
    me1200SysutilStatusPowerSupplyEntry.setStatus("current")


class _Me1200SysutilStatusPowerSupplySwitchId_Type(Integer32):
    """Custom type me1200SysutilStatusPowerSupplySwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Me1200SysutilStatusPowerSupplySwitchId_Type.__name__ = "Integer32"
_Me1200SysutilStatusPowerSupplySwitchId_Object = MibTableColumn
me1200SysutilStatusPowerSupplySwitchId = _Me1200SysutilStatusPowerSupplySwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 2, 1, 1),
    _Me1200SysutilStatusPowerSupplySwitchId_Type()
)
me1200SysutilStatusPowerSupplySwitchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200SysutilStatusPowerSupplySwitchId.setStatus("current")


class _Me1200SysutilStatusPowerSupplyPsuId_Type(Integer32):
    """Custom type me1200SysutilStatusPowerSupplyPsuId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Me1200SysutilStatusPowerSupplyPsuId_Type.__name__ = "Integer32"
_Me1200SysutilStatusPowerSupplyPsuId_Object = MibTableColumn
me1200SysutilStatusPowerSupplyPsuId = _Me1200SysutilStatusPowerSupplyPsuId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 2, 1, 2),
    _Me1200SysutilStatusPowerSupplyPsuId_Type()
)
me1200SysutilStatusPowerSupplyPsuId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200SysutilStatusPowerSupplyPsuId.setStatus("current")
_Me1200SysutilStatusPowerSupplyState_Type = ME1200SysutilPowerSupplyStateType
_Me1200SysutilStatusPowerSupplyState_Object = MibTableColumn
me1200SysutilStatusPowerSupplyState = _Me1200SysutilStatusPowerSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 2, 1, 3),
    _Me1200SysutilStatusPowerSupplyState_Type()
)
me1200SysutilStatusPowerSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SysutilStatusPowerSupplyState.setStatus("current")


class _Me1200SysutilStatusPowerSupplyDescription_Type(ME1200DisplayString):
    """Custom type me1200SysutilStatusPowerSupplyDescription based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Me1200SysutilStatusPowerSupplyDescription_Type.__name__ = "ME1200DisplayString"
_Me1200SysutilStatusPowerSupplyDescription_Object = MibTableColumn
me1200SysutilStatusPowerSupplyDescription = _Me1200SysutilStatusPowerSupplyDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 2, 1, 4),
    _Me1200SysutilStatusPowerSupplyDescription_Type()
)
me1200SysutilStatusPowerSupplyDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SysutilStatusPowerSupplyDescription.setStatus("current")
_Me1200SysutilControl_ObjectIdentity = ObjectIdentity
me1200SysutilControl = _Me1200SysutilControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 4)
)
_Me1200SysutilControlRebootTable_Object = MibTable
me1200SysutilControlRebootTable = _Me1200SysutilControlRebootTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 4, 1)
)
if mibBuilder.loadTexts:
    me1200SysutilControlRebootTable.setStatus("current")
_Me1200SysutilControlRebootEntry_Object = MibTableRow
me1200SysutilControlRebootEntry = _Me1200SysutilControlRebootEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 4, 1, 1)
)
me1200SysutilControlRebootEntry.setIndexNames(
    (0, "ME1200-SYSUTIL-MIB", "me1200SysutilControlRebootSwitchId"),
)
if mibBuilder.loadTexts:
    me1200SysutilControlRebootEntry.setStatus("current")


class _Me1200SysutilControlRebootSwitchId_Type(Integer32):
    """Custom type me1200SysutilControlRebootSwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Me1200SysutilControlRebootSwitchId_Type.__name__ = "Integer32"
_Me1200SysutilControlRebootSwitchId_Object = MibTableColumn
me1200SysutilControlRebootSwitchId = _Me1200SysutilControlRebootSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 4, 1, 1, 1),
    _Me1200SysutilControlRebootSwitchId_Type()
)
me1200SysutilControlRebootSwitchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200SysutilControlRebootSwitchId.setStatus("current")
_Me1200SysutilControlRebootType_Type = ME1200SysutilRebootType
_Me1200SysutilControlRebootType_Object = MibTableColumn
me1200SysutilControlRebootType = _Me1200SysutilControlRebootType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 4, 1, 1, 2),
    _Me1200SysutilControlRebootType_Type()
)
me1200SysutilControlRebootType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200SysutilControlRebootType.setStatus("current")
_Me1200SysutilMibConformance_ObjectIdentity = ObjectIdentity
me1200SysutilMibConformance = _Me1200SysutilMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 2)
)
_Me1200SysutilMibCompliances_ObjectIdentity = ObjectIdentity
me1200SysutilMibCompliances = _Me1200SysutilMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 2, 1)
)
_Me1200SysutilMibGroups_ObjectIdentity = ObjectIdentity
me1200SysutilMibGroups = _Me1200SysutilMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 2, 2)
)

# Managed Objects groups

me1200SysutilCapabilitiesInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 2, 2, 1)
)
me1200SysutilCapabilitiesInfoGroup.setObjects(
    ("ME1200-SYSUTIL-MIB", "me1200SysutilCapabilitiesWarmRebootSupported")
)
if mibBuilder.loadTexts:
    me1200SysutilCapabilitiesInfoGroup.setStatus("current")

me1200SysutilStatusCpuLoadInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 2, 2, 2)
)
me1200SysutilStatusCpuLoadInfoGroup.setObjects(
      *(("ME1200-SYSUTIL-MIB", "me1200SysutilStatusCpuLoadAverage100msec"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilStatusCpuLoadAverage1sec"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilStatusCpuLoadAverage10sec"))
)
if mibBuilder.loadTexts:
    me1200SysutilStatusCpuLoadInfoGroup.setStatus("current")

me1200SysutilStatusPowerSupplyInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 2, 2, 3)
)
me1200SysutilStatusPowerSupplyInfoGroup.setObjects(
      *(("ME1200-SYSUTIL-MIB", "me1200SysutilStatusPowerSupplyState"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilStatusPowerSupplyDescription"))
)
if mibBuilder.loadTexts:
    me1200SysutilStatusPowerSupplyInfoGroup.setStatus("current")

me1200SysutilControlRebootInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 2, 2, 4)
)
me1200SysutilControlRebootInfoGroup.setObjects(
    ("ME1200-SYSUTIL-MIB", "me1200SysutilControlRebootType")
)
if mibBuilder.loadTexts:
    me1200SysutilControlRebootInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200SysutilMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 2, 1, 1)
)
me1200SysutilMibCompliance.setObjects(
      *(("ME1200-SYSUTIL-MIB", "me1200SysutilCapabilitiesInfoGroup"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilStatusCpuLoadInfoGroup"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilStatusPowerSupplyInfoGroup"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilControlRebootInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200SysutilMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-SYSUTIL-MIB",
    **{"ME1200SysutilPowerSupplyStateType": ME1200SysutilPowerSupplyStateType,
       "ME1200SysutilRebootType": ME1200SysutilRebootType,
       "me1200SysutilMib": me1200SysutilMib,
       "me1200SysutilMibObjects": me1200SysutilMibObjects,
       "me1200SysutilCapabilities": me1200SysutilCapabilities,
       "me1200SysutilCapabilitiesWarmRebootSupported": me1200SysutilCapabilitiesWarmRebootSupported,
       "me1200SysutilStatus": me1200SysutilStatus,
       "me1200SysutilStatusCpuLoad": me1200SysutilStatusCpuLoad,
       "me1200SysutilStatusCpuLoadAverage100msec": me1200SysutilStatusCpuLoadAverage100msec,
       "me1200SysutilStatusCpuLoadAverage1sec": me1200SysutilStatusCpuLoadAverage1sec,
       "me1200SysutilStatusCpuLoadAverage10sec": me1200SysutilStatusCpuLoadAverage10sec,
       "me1200SysutilStatusPowerSupplyTable": me1200SysutilStatusPowerSupplyTable,
       "me1200SysutilStatusPowerSupplyEntry": me1200SysutilStatusPowerSupplyEntry,
       "me1200SysutilStatusPowerSupplySwitchId": me1200SysutilStatusPowerSupplySwitchId,
       "me1200SysutilStatusPowerSupplyPsuId": me1200SysutilStatusPowerSupplyPsuId,
       "me1200SysutilStatusPowerSupplyState": me1200SysutilStatusPowerSupplyState,
       "me1200SysutilStatusPowerSupplyDescription": me1200SysutilStatusPowerSupplyDescription,
       "me1200SysutilControl": me1200SysutilControl,
       "me1200SysutilControlRebootTable": me1200SysutilControlRebootTable,
       "me1200SysutilControlRebootEntry": me1200SysutilControlRebootEntry,
       "me1200SysutilControlRebootSwitchId": me1200SysutilControlRebootSwitchId,
       "me1200SysutilControlRebootType": me1200SysutilControlRebootType,
       "me1200SysutilMibConformance": me1200SysutilMibConformance,
       "me1200SysutilMibCompliances": me1200SysutilMibCompliances,
       "me1200SysutilMibCompliance": me1200SysutilMibCompliance,
       "me1200SysutilMibGroups": me1200SysutilMibGroups,
       "me1200SysutilCapabilitiesInfoGroup": me1200SysutilCapabilitiesInfoGroup,
       "me1200SysutilStatusCpuLoadInfoGroup": me1200SysutilStatusCpuLoadInfoGroup,
       "me1200SysutilStatusPowerSupplyInfoGroup": me1200SysutilStatusPowerSupplyInfoGroup,
       "me1200SysutilControlRebootInfoGroup": me1200SysutilControlRebootInfoGroup}
)
