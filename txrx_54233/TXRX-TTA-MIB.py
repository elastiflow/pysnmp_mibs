# SNMP MIB module (TXRX-TTA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/txrx_54233/TXRX-TTA-44x-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:05:26 2025
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

(products,
 sysContact,
 sysDescr,
 sysLocation,
 sysName,
 sysObjectID,
 sysUpTime) = mibBuilder.importSymbols(
    "TXRX-MIB",
    "products",
    "sysContact",
    "sysDescr",
    "sysLocation",
    "sysName",
    "sysObjectID",
    "sysUpTime")


# MODULE-IDENTITY

nptta = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 54233, 1, 4)
)
if mibBuilder.loadTexts:
    nptta.setRevisions(
        ("2021-07-01 00:00",
         "2020-11-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 54233, 1, 4, 1)
)
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 54233, 1, 4, 2)
)


class _TestPartition_Type(Integer32):
    """Custom type testPartition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("alarm", 1))
    )


_TestPartition_Type.__name__ = "Integer32"
_TestPartition_Object = MibScalar
testPartition = _TestPartition_Object(
    (1, 3, 6, 1, 4, 1, 54233, 1, 4, 2, 0),
    _TestPartition_Type()
)
testPartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testPartition.setStatus("current")


class _TowerTopAmplifier_Type(Integer32):
    """Custom type towerTopAmplifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("alarm", 1))
    )


_TowerTopAmplifier_Type.__name__ = "Integer32"
_TowerTopAmplifier_Object = MibScalar
towerTopAmplifier = _TowerTopAmplifier_Object(
    (1, 3, 6, 1, 4, 1, 54233, 1, 4, 2, 1),
    _TowerTopAmplifier_Type()
)
towerTopAmplifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    towerTopAmplifier.setStatus("current")


class _DistributionAmp_Type(Integer32):
    """Custom type distributionAmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("alarm", 1))
    )


_DistributionAmp_Type.__name__ = "Integer32"
_DistributionAmp_Object = MibScalar
distributionAmp = _DistributionAmp_Object(
    (1, 3, 6, 1, 4, 1, 54233, 1, 4, 2, 2),
    _DistributionAmp_Type()
)
distributionAmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    distributionAmp.setStatus("current")


class _ControlUnit_Type(Integer32):
    """Custom type controlUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("alarm", 1))
    )


_ControlUnit_Type.__name__ = "Integer32"
_ControlUnit_Object = MibScalar
controlUnit = _ControlUnit_Object(
    (1, 3, 6, 1, 4, 1, 54233, 1, 4, 2, 3),
    _ControlUnit_Type()
)
controlUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlUnit.setStatus("current")


class _HighLevelCarrier_Type(Integer32):
    """Custom type highLevelCarrier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("alarm", 1))
    )


_HighLevelCarrier_Type.__name__ = "Integer32"
_HighLevelCarrier_Object = MibScalar
highLevelCarrier = _HighLevelCarrier_Object(
    (1, 3, 6, 1, 4, 1, 54233, 1, 4, 2, 4),
    _HighLevelCarrier_Type()
)
highLevelCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highLevelCarrier.setStatus("current")


class _AuxillarySystems_Type(Integer32):
    """Custom type auxillarySystems based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("alarm", 1))
    )


_AuxillarySystems_Type.__name__ = "Integer32"
_AuxillarySystems_Object = MibScalar
auxillarySystems = _AuxillarySystems_Object(
    (1, 3, 6, 1, 4, 1, 54233, 1, 4, 2, 5),
    _AuxillarySystems_Type()
)
auxillarySystems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxillarySystems.setStatus("current")


class _AlarmStatus_Type(DisplayString):
    """Custom type alarmStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlarmStatus_Type.__name__ = "DisplayString"
_AlarmStatus_Object = MibScalar
alarmStatus = _AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 54233, 1, 4, 2, 20),
    _AlarmStatus_Type()
)
alarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStatus.setStatus("current")


class _AlarmCount_Type(Integer32):
    """Custom type alarmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlarmCount_Type.__name__ = "Integer32"
_AlarmCount_Object = MibScalar
alarmCount = _AlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 54233, 1, 4, 2, 21),
    _AlarmCount_Type()
)
alarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCount.setStatus("current")


class _Condition_Type(Integer32):
    """Custom type condition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("alarm", 1))
    )


_Condition_Type.__name__ = "Integer32"
_Condition_Object = MibScalar
condition = _Condition_Object(
    (1, 3, 6, 1, 4, 1, 54233, 1, 4, 2, 22),
    _Condition_Type()
)
condition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    condition.setStatus("current")
_ModelInfo_ObjectIdentity = ObjectIdentity
modelInfo = _ModelInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 54233, 1, 4, 3)
)


class _Serialnumber_Type(DisplayString):
    """Custom type serialnumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Serialnumber_Type.__name__ = "DisplayString"
_Serialnumber_Object = MibScalar
serialnumber = _Serialnumber_Object(
    (1, 3, 6, 1, 4, 1, 54233, 1, 4, 3, 1),
    _Serialnumber_Type()
)
serialnumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialnumber.setStatus("current")


class _ModelString_Type(DisplayString):
    """Custom type modelString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModelString_Type.__name__ = "DisplayString"
_ModelString_Object = MibScalar
modelString = _ModelString_Object(
    (1, 3, 6, 1, 4, 1, 54233, 1, 4, 3, 2),
    _ModelString_Type()
)
modelString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modelString.setStatus("current")

# Managed Objects groups


# Notification objects

testPartitionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 54233, 1, 4, 1, 0)
)
testPartitionTrap.setObjects(
      *(("TXRX-MIB", "sysLocation"),
        ("TXRX-TTA-MIB", "condition"),
        ("TXRX-TTA-MIB", "alarmCount"),
        ("TXRX-TTA-MIB", "alarmStatus"),
        ("TXRX-TTA-MIB", "testPartition"))
)
if mibBuilder.loadTexts:
    testPartitionTrap.setStatus(
        "current"
    )

towerTopAmplifierTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 54233, 1, 4, 1, 1)
)
towerTopAmplifierTrap.setObjects(
      *(("TXRX-MIB", "sysLocation"),
        ("TXRX-TTA-MIB", "condition"),
        ("TXRX-TTA-MIB", "alarmCount"),
        ("TXRX-TTA-MIB", "alarmStatus"),
        ("TXRX-TTA-MIB", "towerTopAmplifier"))
)
if mibBuilder.loadTexts:
    towerTopAmplifierTrap.setStatus(
        "current"
    )

distributionAmpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 54233, 1, 4, 1, 2)
)
distributionAmpTrap.setObjects(
      *(("TXRX-MIB", "sysLocation"),
        ("TXRX-TTA-MIB", "condition"),
        ("TXRX-TTA-MIB", "alarmCount"),
        ("TXRX-TTA-MIB", "alarmStatus"),
        ("TXRX-TTA-MIB", "distributionAmp"))
)
if mibBuilder.loadTexts:
    distributionAmpTrap.setStatus(
        "current"
    )

controlUnitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 54233, 1, 4, 1, 3)
)
controlUnitTrap.setObjects(
      *(("TXRX-MIB", "sysLocation"),
        ("TXRX-TTA-MIB", "condition"),
        ("TXRX-TTA-MIB", "alarmCount"),
        ("TXRX-TTA-MIB", "alarmStatus"),
        ("TXRX-TTA-MIB", "controlUnit"))
)
if mibBuilder.loadTexts:
    controlUnitTrap.setStatus(
        "current"
    )

highLevelCarrierTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 54233, 1, 4, 1, 4)
)
highLevelCarrierTrap.setObjects(
      *(("TXRX-MIB", "sysLocation"),
        ("TXRX-TTA-MIB", "condition"),
        ("TXRX-TTA-MIB", "alarmCount"),
        ("TXRX-TTA-MIB", "alarmStatus"),
        ("TXRX-TTA-MIB", "highLevelCarrier"))
)
if mibBuilder.loadTexts:
    highLevelCarrierTrap.setStatus(
        "current"
    )

auxillarySystemsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 54233, 1, 4, 1, 5)
)
auxillarySystemsTrap.setObjects(
      *(("TXRX-MIB", "sysLocation"),
        ("TXRX-TTA-MIB", "condition"),
        ("TXRX-TTA-MIB", "alarmCount"),
        ("TXRX-TTA-MIB", "alarmStatus"),
        ("TXRX-TTA-MIB", "auxillarySystems"))
)
if mibBuilder.loadTexts:
    auxillarySystemsTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TXRX-TTA-MIB",
    **{"nptta": nptta,
       "traps": traps,
       "testPartitionTrap": testPartitionTrap,
       "towerTopAmplifierTrap": towerTopAmplifierTrap,
       "distributionAmpTrap": distributionAmpTrap,
       "controlUnitTrap": controlUnitTrap,
       "highLevelCarrierTrap": highLevelCarrierTrap,
       "auxillarySystemsTrap": auxillarySystemsTrap,
       "status": status,
       "testPartition": testPartition,
       "towerTopAmplifier": towerTopAmplifier,
       "distributionAmp": distributionAmp,
       "controlUnit": controlUnit,
       "highLevelCarrier": highLevelCarrier,
       "auxillarySystems": auxillarySystems,
       "alarmStatus": alarmStatus,
       "alarmCount": alarmCount,
       "condition": condition,
       "modelInfo": modelInfo,
       "serialnumber": serialnumber,
       "modelString": modelString}
)
