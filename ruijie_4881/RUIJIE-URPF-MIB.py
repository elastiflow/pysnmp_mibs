# SNMP MIB module (RUIJIE-URPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-URPF-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:06 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

ruijieUrpfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46)
)
if mibBuilder.loadTexts:
    ruijieUrpfMIB.setRevisions(
        ("2009-04-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieUrpfMIBObjects_ObjectIdentity = ObjectIdentity
ruijieUrpfMIBObjects = _RuijieUrpfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 0)
)
_RuijieUrpfScalar_ObjectIdentity = ObjectIdentity
ruijieUrpfScalar = _RuijieUrpfScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 0, 1)
)


class _RuijieUrpfComputeInterval_Type(Integer32):
    """Custom type ruijieUrpfComputeInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_RuijieUrpfComputeInterval_Type.__name__ = "Integer32"
_RuijieUrpfComputeInterval_Object = MibScalar
ruijieUrpfComputeInterval = _RuijieUrpfComputeInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 0, 1, 1),
    _RuijieUrpfComputeInterval_Type()
)
ruijieUrpfComputeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieUrpfComputeInterval.setStatus("current")
if mibBuilder.loadTexts:
    ruijieUrpfComputeInterval.setUnits("seconds")


class _RuijieUrpfDropRateWindow_Type(Integer32):
    """Custom type ruijieUrpfDropRateWindow based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 1500),
    )


_RuijieUrpfDropRateWindow_Type.__name__ = "Integer32"
_RuijieUrpfDropRateWindow_Object = MibScalar
ruijieUrpfDropRateWindow = _RuijieUrpfDropRateWindow_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 0, 1, 2),
    _RuijieUrpfDropRateWindow_Type()
)
ruijieUrpfDropRateWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieUrpfDropRateWindow.setStatus("current")
if mibBuilder.loadTexts:
    ruijieUrpfDropRateWindow.setUnits("seconds")


class _RuijieUrpfDropNotifyHoldDownTime_Type(Integer32):
    """Custom type ruijieUrpfDropNotifyHoldDownTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_RuijieUrpfDropNotifyHoldDownTime_Type.__name__ = "Integer32"
_RuijieUrpfDropNotifyHoldDownTime_Object = MibScalar
ruijieUrpfDropNotifyHoldDownTime = _RuijieUrpfDropNotifyHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 0, 1, 3),
    _RuijieUrpfDropNotifyHoldDownTime_Type()
)
ruijieUrpfDropNotifyHoldDownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieUrpfDropNotifyHoldDownTime.setStatus("current")
if mibBuilder.loadTexts:
    ruijieUrpfDropNotifyHoldDownTime.setUnits("seconds")
_RuijieUrpfStatistics_ObjectIdentity = ObjectIdentity
ruijieUrpfStatistics = _RuijieUrpfStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 0, 2)
)
_RuijieUrpfTable_Object = MibTable
ruijieUrpfTable = _RuijieUrpfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 0, 2, 1)
)
if mibBuilder.loadTexts:
    ruijieUrpfTable.setStatus("current")
_RuijieUrpfEntry_Object = MibTableRow
ruijieUrpfEntry = _RuijieUrpfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 0, 2, 1, 1)
)
ruijieUrpfEntry.setIndexNames(
    (0, "RUIJIE-URPF-MIB", "ruijieUrpfIpVersion"),
)
if mibBuilder.loadTexts:
    ruijieUrpfEntry.setStatus("current")


class _RuijieUrpfIpVersion_Type(Integer32):
    """Custom type ruijieUrpfIpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_RuijieUrpfIpVersion_Type.__name__ = "Integer32"
_RuijieUrpfIpVersion_Object = MibTableColumn
ruijieUrpfIpVersion = _RuijieUrpfIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 0, 2, 1, 1, 1),
    _RuijieUrpfIpVersion_Type()
)
ruijieUrpfIpVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieUrpfIpVersion.setStatus("current")
_RuijieUrpfDrops_Type = Counter32
_RuijieUrpfDrops_Object = MibTableColumn
ruijieUrpfDrops = _RuijieUrpfDrops_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 0, 2, 1, 1, 2),
    _RuijieUrpfDrops_Type()
)
ruijieUrpfDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieUrpfDrops.setStatus("current")
if mibBuilder.loadTexts:
    ruijieUrpfDrops.setUnits("packets")
_RuijieUrpfDropRate_Type = Gauge32
_RuijieUrpfDropRate_Object = MibTableColumn
ruijieUrpfDropRate = _RuijieUrpfDropRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 0, 2, 1, 1, 3),
    _RuijieUrpfDropRate_Type()
)
ruijieUrpfDropRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieUrpfDropRate.setStatus("current")
if mibBuilder.loadTexts:
    ruijieUrpfDropRate.setUnits("packets per second")
_RuijieUrpfIfMonTable_Object = MibTable
ruijieUrpfIfMonTable = _RuijieUrpfIfMonTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 0, 2, 2)
)
if mibBuilder.loadTexts:
    ruijieUrpfIfMonTable.setStatus("current")
_RuijieUrpfIfMonEntry_Object = MibTableRow
ruijieUrpfIfMonEntry = _RuijieUrpfIfMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 0, 2, 2, 1)
)
ruijieUrpfIfMonEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RUIJIE-URPF-MIB", "ruijieUrpfIfIpVersion"),
)
if mibBuilder.loadTexts:
    ruijieUrpfIfMonEntry.setStatus("current")


class _RuijieUrpfIfIpVersion_Type(Integer32):
    """Custom type ruijieUrpfIfIpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_RuijieUrpfIfIpVersion_Type.__name__ = "Integer32"
_RuijieUrpfIfIpVersion_Object = MibTableColumn
ruijieUrpfIfIpVersion = _RuijieUrpfIfIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 0, 2, 2, 1, 1),
    _RuijieUrpfIfIpVersion_Type()
)
ruijieUrpfIfIpVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieUrpfIfIpVersion.setStatus("current")
_RuijieUrpfIfDrops_Type = Counter32
_RuijieUrpfIfDrops_Object = MibTableColumn
ruijieUrpfIfDrops = _RuijieUrpfIfDrops_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 0, 2, 2, 1, 2),
    _RuijieUrpfIfDrops_Type()
)
ruijieUrpfIfDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieUrpfIfDrops.setStatus("current")
if mibBuilder.loadTexts:
    ruijieUrpfIfDrops.setUnits("packets")
_RuijieUrpfIfDropRate_Type = Gauge32
_RuijieUrpfIfDropRate_Object = MibTableColumn
ruijieUrpfIfDropRate = _RuijieUrpfIfDropRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 0, 2, 2, 1, 3),
    _RuijieUrpfIfDropRate_Type()
)
ruijieUrpfIfDropRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieUrpfIfDropRate.setStatus("current")
if mibBuilder.loadTexts:
    ruijieUrpfIfDropRate.setUnits("packets/second")
_RuijieUrpfInterfaceConfig_ObjectIdentity = ObjectIdentity
ruijieUrpfInterfaceConfig = _RuijieUrpfInterfaceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 0, 3)
)
_RuijieUrpfIfConfTable_Object = MibTable
ruijieUrpfIfConfTable = _RuijieUrpfIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 0, 3, 1)
)
if mibBuilder.loadTexts:
    ruijieUrpfIfConfTable.setStatus("current")
_RuijieUrpfIfConfEntry_Object = MibTableRow
ruijieUrpfIfConfEntry = _RuijieUrpfIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 0, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieUrpfIfConfEntry.setStatus("current")


class _RuijieUrpfIfCheckStrict_Type(Integer32):
    """Custom type ruijieUrpfIfCheckStrict based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("strict", 1),
          ("loose", 2))
    )


_RuijieUrpfIfCheckStrict_Type.__name__ = "Integer32"
_RuijieUrpfIfCheckStrict_Object = MibTableColumn
ruijieUrpfIfCheckStrict = _RuijieUrpfIfCheckStrict_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 0, 3, 1, 1, 1),
    _RuijieUrpfIfCheckStrict_Type()
)
ruijieUrpfIfCheckStrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieUrpfIfCheckStrict.setStatus("current")


class _RuijieUrpfIfDropRateNotifyEnable_Type(TruthValue):
    """Custom type ruijieUrpfIfDropRateNotifyEnable based on TruthValue"""
    defaultValue = 2


_RuijieUrpfIfDropRateNotifyEnable_Type.__name__ = "TruthValue"
_RuijieUrpfIfDropRateNotifyEnable_Object = MibTableColumn
ruijieUrpfIfDropRateNotifyEnable = _RuijieUrpfIfDropRateNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 0, 3, 1, 1, 2),
    _RuijieUrpfIfDropRateNotifyEnable_Type()
)
ruijieUrpfIfDropRateNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieUrpfIfDropRateNotifyEnable.setStatus("current")


class _RuijieUrpfIfNotifyDropRateThreshold_Type(Unsigned32):
    """Custom type ruijieUrpfIfNotifyDropRateThreshold based on Unsigned32"""
    defaultValue = 1000


_RuijieUrpfIfNotifyDropRateThreshold_Type.__name__ = "Unsigned32"
_RuijieUrpfIfNotifyDropRateThreshold_Object = MibTableColumn
ruijieUrpfIfNotifyDropRateThreshold = _RuijieUrpfIfNotifyDropRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 0, 3, 1, 1, 3),
    _RuijieUrpfIfNotifyDropRateThreshold_Type()
)
ruijieUrpfIfNotifyDropRateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieUrpfIfNotifyDropRateThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ruijieUrpfIfNotifyDropRateThreshold.setUnits("packets/second")


class _RuijieUrpfIfNotifyDrHoldDownReset_Type(TruthValue):
    """Custom type ruijieUrpfIfNotifyDrHoldDownReset based on TruthValue"""
    defaultValue = 2


_RuijieUrpfIfNotifyDrHoldDownReset_Type.__name__ = "TruthValue"
_RuijieUrpfIfNotifyDrHoldDownReset_Object = MibTableColumn
ruijieUrpfIfNotifyDrHoldDownReset = _RuijieUrpfIfNotifyDrHoldDownReset_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 0, 3, 1, 1, 4),
    _RuijieUrpfIfNotifyDrHoldDownReset_Type()
)
ruijieUrpfIfNotifyDrHoldDownReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieUrpfIfNotifyDrHoldDownReset.setStatus("current")


class _RuijieUrpfIfWhichRouteTableID_Type(Integer32):
    """Custom type ruijieUrpfIfWhichRouteTableID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("vrf", 2))
    )


_RuijieUrpfIfWhichRouteTableID_Type.__name__ = "Integer32"
_RuijieUrpfIfWhichRouteTableID_Object = MibTableColumn
ruijieUrpfIfWhichRouteTableID = _RuijieUrpfIfWhichRouteTableID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 0, 3, 1, 1, 5),
    _RuijieUrpfIfWhichRouteTableID_Type()
)
ruijieUrpfIfWhichRouteTableID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieUrpfIfWhichRouteTableID.setStatus("current")


class _RuijieUrpfIfVrfName_Type(SnmpAdminString):
    """Custom type ruijieUrpfIfVrfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieUrpfIfVrfName_Type.__name__ = "SnmpAdminString"
_RuijieUrpfIfVrfName_Object = MibTableColumn
ruijieUrpfIfVrfName = _RuijieUrpfIfVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 0, 3, 1, 1, 6),
    _RuijieUrpfIfVrfName_Type()
)
ruijieUrpfIfVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieUrpfIfVrfName.setStatus("current")
_RuijieUrpfMIBNotifs_ObjectIdentity = ObjectIdentity
ruijieUrpfMIBNotifs = _RuijieUrpfMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 1)
)
_RuijieUrpfMIBConformance_ObjectIdentity = ObjectIdentity
ruijieUrpfMIBConformance = _RuijieUrpfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 2)
)
_RuijieUrpfMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieUrpfMIBCompliances = _RuijieUrpfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 2, 1)
)
_RuijieUrpfMIBGroups_ObjectIdentity = ObjectIdentity
ruijieUrpfMIBGroups = _RuijieUrpfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 2, 2)
)
ruijieUrpfIfMonEntry.registerAugmentions(
    ("RUIJIE-URPF-MIB",
     "ruijieUrpfIfConfEntry")
)
ruijieUrpfIfConfEntry.setIndexNames(*ruijieUrpfIfMonEntry.getIndexNames())

# Managed Objects groups

ruijieUrpfMIBMainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 2, 2, 1)
)
ruijieUrpfMIBMainObjectGroup.setObjects(
      *(("RUIJIE-URPF-MIB", "ruijieUrpfComputeInterval"),
        ("RUIJIE-URPF-MIB", "ruijieUrpfDropRateWindow"),
        ("RUIJIE-URPF-MIB", "ruijieUrpfDropNotifyHoldDownTime"),
        ("RUIJIE-URPF-MIB", "ruijieUrpfDrops"),
        ("RUIJIE-URPF-MIB", "ruijieUrpfDropRate"),
        ("RUIJIE-URPF-MIB", "ruijieUrpfIfDrops"),
        ("RUIJIE-URPF-MIB", "ruijieUrpfIfDropRate"),
        ("RUIJIE-URPF-MIB", "ruijieUrpfIfCheckStrict"),
        ("RUIJIE-URPF-MIB", "ruijieUrpfIfDropRateNotifyEnable"),
        ("RUIJIE-URPF-MIB", "ruijieUrpfIfNotifyDropRateThreshold"),
        ("RUIJIE-URPF-MIB", "ruijieUrpfIfNotifyDrHoldDownReset"))
)
if mibBuilder.loadTexts:
    ruijieUrpfMIBMainObjectGroup.setStatus("current")

ruijieUrpfMIBVrfObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 2, 2, 2)
)
ruijieUrpfMIBVrfObjectGroup.setObjects(
      *(("RUIJIE-URPF-MIB", "ruijieUrpfIfWhichRouteTableID"),
        ("RUIJIE-URPF-MIB", "ruijieUrpfIfVrfName"))
)
if mibBuilder.loadTexts:
    ruijieUrpfMIBVrfObjectGroup.setStatus("current")


# Notification objects

ruijieUrpfIfDropRateNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 1, 1)
)
ruijieUrpfIfDropRateNotify.setObjects(
    ("RUIJIE-URPF-MIB", "ruijieUrpfIfDropRate")
)
if mibBuilder.loadTexts:
    ruijieUrpfIfDropRateNotify.setStatus(
        "current"
    )


# Notifications groups

ruijieUrpfMIBNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 2, 2, 3)
)
ruijieUrpfMIBNotifyGroup.setObjects(
    ("RUIJIE-URPF-MIB", "ruijieUrpfIfDropRateNotify")
)
if mibBuilder.loadTexts:
    ruijieUrpfMIBNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ruijieUrpfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 46, 2, 1, 1)
)
ruijieUrpfMIBCompliance.setObjects(
      *(("RUIJIE-URPF-MIB", "ruijieUrpfMIBMainObjectGroup"),
        ("RUIJIE-URPF-MIB", "ruijieUrpfMIBNotifyGroup"),
        ("RUIJIE-URPF-MIB", "ruijieUrpfMIBVrfObjectGroup"))
)
if mibBuilder.loadTexts:
    ruijieUrpfMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-URPF-MIB",
    **{"ruijieUrpfMIB": ruijieUrpfMIB,
       "ruijieUrpfMIBObjects": ruijieUrpfMIBObjects,
       "ruijieUrpfScalar": ruijieUrpfScalar,
       "ruijieUrpfComputeInterval": ruijieUrpfComputeInterval,
       "ruijieUrpfDropRateWindow": ruijieUrpfDropRateWindow,
       "ruijieUrpfDropNotifyHoldDownTime": ruijieUrpfDropNotifyHoldDownTime,
       "ruijieUrpfStatistics": ruijieUrpfStatistics,
       "ruijieUrpfTable": ruijieUrpfTable,
       "ruijieUrpfEntry": ruijieUrpfEntry,
       "ruijieUrpfIpVersion": ruijieUrpfIpVersion,
       "ruijieUrpfDrops": ruijieUrpfDrops,
       "ruijieUrpfDropRate": ruijieUrpfDropRate,
       "ruijieUrpfIfMonTable": ruijieUrpfIfMonTable,
       "ruijieUrpfIfMonEntry": ruijieUrpfIfMonEntry,
       "ruijieUrpfIfIpVersion": ruijieUrpfIfIpVersion,
       "ruijieUrpfIfDrops": ruijieUrpfIfDrops,
       "ruijieUrpfIfDropRate": ruijieUrpfIfDropRate,
       "ruijieUrpfInterfaceConfig": ruijieUrpfInterfaceConfig,
       "ruijieUrpfIfConfTable": ruijieUrpfIfConfTable,
       "ruijieUrpfIfConfEntry": ruijieUrpfIfConfEntry,
       "ruijieUrpfIfCheckStrict": ruijieUrpfIfCheckStrict,
       "ruijieUrpfIfDropRateNotifyEnable": ruijieUrpfIfDropRateNotifyEnable,
       "ruijieUrpfIfNotifyDropRateThreshold": ruijieUrpfIfNotifyDropRateThreshold,
       "ruijieUrpfIfNotifyDrHoldDownReset": ruijieUrpfIfNotifyDrHoldDownReset,
       "ruijieUrpfIfWhichRouteTableID": ruijieUrpfIfWhichRouteTableID,
       "ruijieUrpfIfVrfName": ruijieUrpfIfVrfName,
       "ruijieUrpfMIBNotifs": ruijieUrpfMIBNotifs,
       "ruijieUrpfIfDropRateNotify": ruijieUrpfIfDropRateNotify,
       "ruijieUrpfMIBConformance": ruijieUrpfMIBConformance,
       "ruijieUrpfMIBCompliances": ruijieUrpfMIBCompliances,
       "ruijieUrpfMIBCompliance": ruijieUrpfMIBCompliance,
       "ruijieUrpfMIBGroups": ruijieUrpfMIBGroups,
       "ruijieUrpfMIBMainObjectGroup": ruijieUrpfMIBMainObjectGroup,
       "ruijieUrpfMIBVrfObjectGroup": ruijieUrpfMIBVrfObjectGroup,
       "ruijieUrpfMIBNotifyGroup": ruijieUrpfMIBNotifyGroup}
)
