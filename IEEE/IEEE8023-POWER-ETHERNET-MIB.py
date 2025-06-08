# SNMP MIB module (IEEE8023-POWER-ETHERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/IEEE/IEEE8023-POWER-ETHERNET-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:13:47 2025
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
 iso,
 org) = mibBuilder.importSymbols(
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
    "iso",
    "org")

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

ieee8023powerEthernetMIB = ModuleIdentity(
    (1, 3, 111, 2, 802, 3, 1, 8)
)
if mibBuilder.loadTexts:
    ieee8023powerEthernetMIB.setRevisions(
        ("2013-04-11 00:00",
         "2011-02-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PethNotifications_ObjectIdentity = ObjectIdentity
pethNotifications = _PethNotifications_ObjectIdentity(
    (1, 3, 111, 2, 802, 3, 1, 8, 0)
)
_PethObjects_ObjectIdentity = ObjectIdentity
pethObjects = _PethObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 3, 1, 8, 1)
)
_PethPsePortTable_Object = MibTable
pethPsePortTable = _PethPsePortTable_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    pethPsePortTable.setStatus("current")
_PethPsePortEntry_Object = MibTableRow
pethPsePortEntry = _PethPsePortEntry_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 1, 1)
)
pethPsePortEntry.setIndexNames(
    (0, "IEEE8023-POWER-ETHERNET-MIB", "pethPsePortGroupIndex"),
    (0, "IEEE8023-POWER-ETHERNET-MIB", "pethPsePortIndex"),
)
if mibBuilder.loadTexts:
    pethPsePortEntry.setStatus("current")


class _PethPsePortGroupIndex_Type(Integer32):
    """Custom type pethPsePortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PethPsePortGroupIndex_Type.__name__ = "Integer32"
_PethPsePortGroupIndex_Object = MibTableColumn
pethPsePortGroupIndex = _PethPsePortGroupIndex_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 1, 1, 1),
    _PethPsePortGroupIndex_Type()
)
pethPsePortGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pethPsePortGroupIndex.setStatus("current")


class _PethPsePortIndex_Type(Integer32):
    """Custom type pethPsePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PethPsePortIndex_Type.__name__ = "Integer32"
_PethPsePortIndex_Object = MibTableColumn
pethPsePortIndex = _PethPsePortIndex_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 1, 1, 2),
    _PethPsePortIndex_Type()
)
pethPsePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pethPsePortIndex.setStatus("current")
_PethPsePortAdminEnable_Type = TruthValue
_PethPsePortAdminEnable_Object = MibTableColumn
pethPsePortAdminEnable = _PethPsePortAdminEnable_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 1, 1, 3),
    _PethPsePortAdminEnable_Type()
)
pethPsePortAdminEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pethPsePortAdminEnable.setStatus("current")
_PethPsePortPowerPairsControlAbility_Type = TruthValue
_PethPsePortPowerPairsControlAbility_Object = MibTableColumn
pethPsePortPowerPairsControlAbility = _PethPsePortPowerPairsControlAbility_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 1, 1, 4),
    _PethPsePortPowerPairsControlAbility_Type()
)
pethPsePortPowerPairsControlAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethPsePortPowerPairsControlAbility.setStatus("current")


class _PethPsePortPowerPairs_Type(Integer32):
    """Custom type pethPsePortPowerPairs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("signal", 1),
          ("spare", 2))
    )


_PethPsePortPowerPairs_Type.__name__ = "Integer32"
_PethPsePortPowerPairs_Object = MibTableColumn
pethPsePortPowerPairs = _PethPsePortPowerPairs_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 1, 1, 5),
    _PethPsePortPowerPairs_Type()
)
pethPsePortPowerPairs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pethPsePortPowerPairs.setStatus("current")


class _PethPsePortDetectionStatus_Type(Integer32):
    """Custom type pethPsePortDetectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("searching", 2),
          ("deliveringPower", 3),
          ("fault", 4),
          ("test", 5),
          ("otherFault", 6))
    )


_PethPsePortDetectionStatus_Type.__name__ = "Integer32"
_PethPsePortDetectionStatus_Object = MibTableColumn
pethPsePortDetectionStatus = _PethPsePortDetectionStatus_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 1, 1, 6),
    _PethPsePortDetectionStatus_Type()
)
pethPsePortDetectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethPsePortDetectionStatus.setStatus("current")


class _PethPsePortPowerPriority_Type(Integer32):
    """Custom type pethPsePortPowerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("high", 2),
          ("low", 3))
    )


_PethPsePortPowerPriority_Type.__name__ = "Integer32"
_PethPsePortPowerPriority_Object = MibTableColumn
pethPsePortPowerPriority = _PethPsePortPowerPriority_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 1, 1, 7),
    _PethPsePortPowerPriority_Type()
)
pethPsePortPowerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pethPsePortPowerPriority.setStatus("current")
_PethPsePortMPSAbsentCounter_Type = Counter32
_PethPsePortMPSAbsentCounter_Object = MibTableColumn
pethPsePortMPSAbsentCounter = _PethPsePortMPSAbsentCounter_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 1, 1, 8),
    _PethPsePortMPSAbsentCounter_Type()
)
pethPsePortMPSAbsentCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethPsePortMPSAbsentCounter.setStatus("current")
_PethPsePortType_Type = SnmpAdminString
_PethPsePortType_Object = MibTableColumn
pethPsePortType = _PethPsePortType_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 1, 1, 9),
    _PethPsePortType_Type()
)
pethPsePortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pethPsePortType.setStatus("current")


class _PethPsePortPowerClassifications_Type(Integer32):
    """Custom type pethPsePortPowerClassifications based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5))
    )


_PethPsePortPowerClassifications_Type.__name__ = "Integer32"
_PethPsePortPowerClassifications_Object = MibTableColumn
pethPsePortPowerClassifications = _PethPsePortPowerClassifications_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 1, 1, 10),
    _PethPsePortPowerClassifications_Type()
)
pethPsePortPowerClassifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethPsePortPowerClassifications.setStatus("current")
_PethPsePortInvalidSignatureCounter_Type = Counter32
_PethPsePortInvalidSignatureCounter_Object = MibTableColumn
pethPsePortInvalidSignatureCounter = _PethPsePortInvalidSignatureCounter_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 1, 1, 11),
    _PethPsePortInvalidSignatureCounter_Type()
)
pethPsePortInvalidSignatureCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethPsePortInvalidSignatureCounter.setStatus("current")
_PethPsePortPowerDeniedCounter_Type = Counter32
_PethPsePortPowerDeniedCounter_Object = MibTableColumn
pethPsePortPowerDeniedCounter = _PethPsePortPowerDeniedCounter_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 1, 1, 12),
    _PethPsePortPowerDeniedCounter_Type()
)
pethPsePortPowerDeniedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethPsePortPowerDeniedCounter.setStatus("current")
_PethPsePortOverLoadCounter_Type = Counter32
_PethPsePortOverLoadCounter_Object = MibTableColumn
pethPsePortOverLoadCounter = _PethPsePortOverLoadCounter_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 1, 1, 13),
    _PethPsePortOverLoadCounter_Type()
)
pethPsePortOverLoadCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethPsePortOverLoadCounter.setStatus("current")
_PethPsePortShortCounter_Type = Counter32
_PethPsePortShortCounter_Object = MibTableColumn
pethPsePortShortCounter = _PethPsePortShortCounter_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 1, 1, 14),
    _PethPsePortShortCounter_Type()
)
pethPsePortShortCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethPsePortShortCounter.setStatus("current")
_PethPsePortActualPower_Type = Integer32
_PethPsePortActualPower_Object = MibTableColumn
pethPsePortActualPower = _PethPsePortActualPower_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 1, 1, 15),
    _PethPsePortActualPower_Type()
)
pethPsePortActualPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethPsePortActualPower.setStatus("current")
_PethPsePortPowerAccuracy_Type = Integer32
_PethPsePortPowerAccuracy_Object = MibTableColumn
pethPsePortPowerAccuracy = _PethPsePortPowerAccuracy_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 1, 1, 16),
    _PethPsePortPowerAccuracy_Type()
)
pethPsePortPowerAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethPsePortPowerAccuracy.setStatus("current")
_PethPsePortCumulativeEnergy_Type = Counter32
_PethPsePortCumulativeEnergy_Object = MibTableColumn
pethPsePortCumulativeEnergy = _PethPsePortCumulativeEnergy_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 1, 1, 17),
    _PethPsePortCumulativeEnergy_Type()
)
pethPsePortCumulativeEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethPsePortCumulativeEnergy.setStatus("current")
_PethMainPseObjects_ObjectIdentity = ObjectIdentity
pethMainPseObjects = _PethMainPseObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 3)
)
_PethMainPseTable_Object = MibTable
pethMainPseTable = _PethMainPseTable_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 3, 1)
)
if mibBuilder.loadTexts:
    pethMainPseTable.setStatus("current")
_PethMainPseEntry_Object = MibTableRow
pethMainPseEntry = _PethMainPseEntry_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 3, 1, 1)
)
pethMainPseEntry.setIndexNames(
    (0, "IEEE8023-POWER-ETHERNET-MIB", "pethMainPseGroupIndex"),
)
if mibBuilder.loadTexts:
    pethMainPseEntry.setStatus("current")


class _PethMainPseGroupIndex_Type(Integer32):
    """Custom type pethMainPseGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PethMainPseGroupIndex_Type.__name__ = "Integer32"
_PethMainPseGroupIndex_Object = MibTableColumn
pethMainPseGroupIndex = _PethMainPseGroupIndex_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 3, 1, 1, 1),
    _PethMainPseGroupIndex_Type()
)
pethMainPseGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pethMainPseGroupIndex.setStatus("current")


class _PethMainPsePower_Type(Gauge32):
    """Custom type pethMainPsePower based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PethMainPsePower_Type.__name__ = "Gauge32"
_PethMainPsePower_Object = MibTableColumn
pethMainPsePower = _PethMainPsePower_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 3, 1, 1, 2),
    _PethMainPsePower_Type()
)
pethMainPsePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethMainPsePower.setStatus("current")
if mibBuilder.loadTexts:
    pethMainPsePower.setUnits("Watts")


class _PethMainPseOperStatus_Type(Integer32):
    """Custom type pethMainPseOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("faulty", 3))
    )


_PethMainPseOperStatus_Type.__name__ = "Integer32"
_PethMainPseOperStatus_Object = MibTableColumn
pethMainPseOperStatus = _PethMainPseOperStatus_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 3, 1, 1, 3),
    _PethMainPseOperStatus_Type()
)
pethMainPseOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethMainPseOperStatus.setStatus("current")
_PethMainPseConsumptionPower_Type = Gauge32
_PethMainPseConsumptionPower_Object = MibTableColumn
pethMainPseConsumptionPower = _PethMainPseConsumptionPower_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 3, 1, 1, 4),
    _PethMainPseConsumptionPower_Type()
)
pethMainPseConsumptionPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethMainPseConsumptionPower.setStatus("current")
if mibBuilder.loadTexts:
    pethMainPseConsumptionPower.setUnits("Watts")


class _PethMainPseUsageThreshold_Type(Integer32):
    """Custom type pethMainPseUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_PethMainPseUsageThreshold_Type.__name__ = "Integer32"
_PethMainPseUsageThreshold_Object = MibTableColumn
pethMainPseUsageThreshold = _PethMainPseUsageThreshold_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 3, 1, 1, 5),
    _PethMainPseUsageThreshold_Type()
)
pethMainPseUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pethMainPseUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    pethMainPseUsageThreshold.setUnits("%")
_PethNotificationControl_ObjectIdentity = ObjectIdentity
pethNotificationControl = _PethNotificationControl_ObjectIdentity(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 4)
)
_PethNotificationControlTable_Object = MibTable
pethNotificationControlTable = _PethNotificationControlTable_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 4, 1)
)
if mibBuilder.loadTexts:
    pethNotificationControlTable.setStatus("current")
_PethNotificationControlEntry_Object = MibTableRow
pethNotificationControlEntry = _PethNotificationControlEntry_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 4, 1, 1)
)
pethNotificationControlEntry.setIndexNames(
    (0, "IEEE8023-POWER-ETHERNET-MIB", "pethNotificationControlGroupIndex"),
)
if mibBuilder.loadTexts:
    pethNotificationControlEntry.setStatus("current")


class _PethNotificationControlGroupIndex_Type(Integer32):
    """Custom type pethNotificationControlGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PethNotificationControlGroupIndex_Type.__name__ = "Integer32"
_PethNotificationControlGroupIndex_Object = MibTableColumn
pethNotificationControlGroupIndex = _PethNotificationControlGroupIndex_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 4, 1, 1, 1),
    _PethNotificationControlGroupIndex_Type()
)
pethNotificationControlGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pethNotificationControlGroupIndex.setStatus("current")
_PethNotificationControlEnable_Type = TruthValue
_PethNotificationControlEnable_Object = MibTableColumn
pethNotificationControlEnable = _PethNotificationControlEnable_Object(
    (1, 3, 111, 2, 802, 3, 1, 8, 1, 4, 1, 1, 2),
    _PethNotificationControlEnable_Type()
)
pethNotificationControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pethNotificationControlEnable.setStatus("current")
_PethConformance_ObjectIdentity = ObjectIdentity
pethConformance = _PethConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 3, 1, 8, 2)
)
_PethCompliances_ObjectIdentity = ObjectIdentity
pethCompliances = _PethCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 3, 1, 8, 2, 1)
)
_PethGroups_ObjectIdentity = ObjectIdentity
pethGroups = _PethGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 3, 1, 8, 2, 2)
)

# Managed Objects groups

pethPsePortGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 8, 2, 2, 1)
)
pethPsePortGroup.setObjects(
      *(("IEEE8023-POWER-ETHERNET-MIB", "pethPsePortAdminEnable"),
        ("IEEE8023-POWER-ETHERNET-MIB", "pethPsePortPowerPairsControlAbility"),
        ("IEEE8023-POWER-ETHERNET-MIB", "pethPsePortPowerPairs"),
        ("IEEE8023-POWER-ETHERNET-MIB", "pethPsePortDetectionStatus"),
        ("IEEE8023-POWER-ETHERNET-MIB", "pethPsePortPowerPriority"),
        ("IEEE8023-POWER-ETHERNET-MIB", "pethPsePortMPSAbsentCounter"),
        ("IEEE8023-POWER-ETHERNET-MIB", "pethPsePortInvalidSignatureCounter"),
        ("IEEE8023-POWER-ETHERNET-MIB", "pethPsePortPowerDeniedCounter"),
        ("IEEE8023-POWER-ETHERNET-MIB", "pethPsePortOverLoadCounter"),
        ("IEEE8023-POWER-ETHERNET-MIB", "pethPsePortShortCounter"),
        ("IEEE8023-POWER-ETHERNET-MIB", "pethPsePortType"),
        ("IEEE8023-POWER-ETHERNET-MIB", "pethPsePortPowerClassifications"),
        ("IEEE8023-POWER-ETHERNET-MIB", "pethPsePortActualPower"),
        ("IEEE8023-POWER-ETHERNET-MIB", "pethPsePortPowerAccuracy"),
        ("IEEE8023-POWER-ETHERNET-MIB", "pethPsePortCumulativeEnergy"))
)
if mibBuilder.loadTexts:
    pethPsePortGroup.setStatus("current")

pethMainPseGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 8, 2, 2, 2)
)
pethMainPseGroup.setObjects(
      *(("IEEE8023-POWER-ETHERNET-MIB", "pethMainPsePower"),
        ("IEEE8023-POWER-ETHERNET-MIB", "pethMainPseOperStatus"),
        ("IEEE8023-POWER-ETHERNET-MIB", "pethMainPseConsumptionPower"),
        ("IEEE8023-POWER-ETHERNET-MIB", "pethMainPseUsageThreshold"))
)
if mibBuilder.loadTexts:
    pethMainPseGroup.setStatus("current")

pethNotificationControlGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 3, 1, 8, 2, 2, 3)
)
pethNotificationControlGroup.setObjects(
    ("IEEE8023-POWER-ETHERNET-MIB", "pethNotificationControlEnable")
)
if mibBuilder.loadTexts:
    pethNotificationControlGroup.setStatus("current")


# Notification objects

pethPsePortOnOffNotification = NotificationType(
    (1, 3, 111, 2, 802, 3, 1, 8, 0, 1)
)
pethPsePortOnOffNotification.setObjects(
    ("IEEE8023-POWER-ETHERNET-MIB", "pethPsePortDetectionStatus")
)
if mibBuilder.loadTexts:
    pethPsePortOnOffNotification.setStatus(
        "current"
    )

pethMainPowerUsageOnNotification = NotificationType(
    (1, 3, 111, 2, 802, 3, 1, 8, 0, 2)
)
pethMainPowerUsageOnNotification.setObjects(
    ("IEEE8023-POWER-ETHERNET-MIB", "pethMainPseConsumptionPower")
)
if mibBuilder.loadTexts:
    pethMainPowerUsageOnNotification.setStatus(
        "current"
    )

pethMainPowerUsageOffNotification = NotificationType(
    (1, 3, 111, 2, 802, 3, 1, 8, 0, 3)
)
pethMainPowerUsageOffNotification.setObjects(
    ("IEEE8023-POWER-ETHERNET-MIB", "pethMainPseConsumptionPower")
)
if mibBuilder.loadTexts:
    pethMainPowerUsageOffNotification.setStatus(
        "current"
    )


# Notifications groups

pethPsePortNotificationGroup = NotificationGroup(
    (1, 3, 111, 2, 802, 3, 1, 8, 2, 2, 4)
)
pethPsePortNotificationGroup.setObjects(
    ("IEEE8023-POWER-ETHERNET-MIB", "pethPsePortOnOffNotification")
)
if mibBuilder.loadTexts:
    pethPsePortNotificationGroup.setStatus(
        "current"
    )

pethMainPowerNotificationGroup = NotificationGroup(
    (1, 3, 111, 2, 802, 3, 1, 8, 2, 2, 5)
)
pethMainPowerNotificationGroup.setObjects(
      *(("IEEE8023-POWER-ETHERNET-MIB", "pethMainPowerUsageOnNotification"),
        ("IEEE8023-POWER-ETHERNET-MIB", "pethMainPowerUsageOffNotification"))
)
if mibBuilder.loadTexts:
    pethMainPowerNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

pethCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 3, 1, 8, 2, 1, 1)
)
pethCompliance.setObjects(
      *(("IEEE8023-POWER-ETHERNET-MIB", "pethPsePortGroup"),
        ("IEEE8023-POWER-ETHERNET-MIB", "pethPsePortNotificationGroup"),
        ("IEEE8023-POWER-ETHERNET-MIB", "pethNotificationControlGroup"),
        ("IEEE8023-POWER-ETHERNET-MIB", "pethMainPseGroup"),
        ("IEEE8023-POWER-ETHERNET-MIB", "pethMainPowerNotificationGroup"))
)
if mibBuilder.loadTexts:
    pethCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8023-POWER-ETHERNET-MIB",
    **{"ieee8023powerEthernetMIB": ieee8023powerEthernetMIB,
       "pethNotifications": pethNotifications,
       "pethPsePortOnOffNotification": pethPsePortOnOffNotification,
       "pethMainPowerUsageOnNotification": pethMainPowerUsageOnNotification,
       "pethMainPowerUsageOffNotification": pethMainPowerUsageOffNotification,
       "pethObjects": pethObjects,
       "pethPsePortTable": pethPsePortTable,
       "pethPsePortEntry": pethPsePortEntry,
       "pethPsePortGroupIndex": pethPsePortGroupIndex,
       "pethPsePortIndex": pethPsePortIndex,
       "pethPsePortAdminEnable": pethPsePortAdminEnable,
       "pethPsePortPowerPairsControlAbility": pethPsePortPowerPairsControlAbility,
       "pethPsePortPowerPairs": pethPsePortPowerPairs,
       "pethPsePortDetectionStatus": pethPsePortDetectionStatus,
       "pethPsePortPowerPriority": pethPsePortPowerPriority,
       "pethPsePortMPSAbsentCounter": pethPsePortMPSAbsentCounter,
       "pethPsePortType": pethPsePortType,
       "pethPsePortPowerClassifications": pethPsePortPowerClassifications,
       "pethPsePortInvalidSignatureCounter": pethPsePortInvalidSignatureCounter,
       "pethPsePortPowerDeniedCounter": pethPsePortPowerDeniedCounter,
       "pethPsePortOverLoadCounter": pethPsePortOverLoadCounter,
       "pethPsePortShortCounter": pethPsePortShortCounter,
       "pethPsePortActualPower": pethPsePortActualPower,
       "pethPsePortPowerAccuracy": pethPsePortPowerAccuracy,
       "pethPsePortCumulativeEnergy": pethPsePortCumulativeEnergy,
       "pethMainPseObjects": pethMainPseObjects,
       "pethMainPseTable": pethMainPseTable,
       "pethMainPseEntry": pethMainPseEntry,
       "pethMainPseGroupIndex": pethMainPseGroupIndex,
       "pethMainPsePower": pethMainPsePower,
       "pethMainPseOperStatus": pethMainPseOperStatus,
       "pethMainPseConsumptionPower": pethMainPseConsumptionPower,
       "pethMainPseUsageThreshold": pethMainPseUsageThreshold,
       "pethNotificationControl": pethNotificationControl,
       "pethNotificationControlTable": pethNotificationControlTable,
       "pethNotificationControlEntry": pethNotificationControlEntry,
       "pethNotificationControlGroupIndex": pethNotificationControlGroupIndex,
       "pethNotificationControlEnable": pethNotificationControlEnable,
       "pethConformance": pethConformance,
       "pethCompliances": pethCompliances,
       "pethCompliance": pethCompliance,
       "pethGroups": pethGroups,
       "pethPsePortGroup": pethPsePortGroup,
       "pethMainPseGroup": pethMainPseGroup,
       "pethNotificationControlGroup": pethNotificationControlGroup,
       "pethPsePortNotificationGroup": pethPsePortNotificationGroup,
       "pethMainPowerNotificationGroup": pethMainPowerNotificationGroup}
)
