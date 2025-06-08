# SNMP MIB module (CONTELEC-VLFDUMMYLOAD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/continental_48307/CONTELEC-VLFDUMMYLOAD-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:57:19 2025
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

(cecVLF,) = mibBuilder.importSymbols(
    "CONTELEC-COMMON-MIB",
    "cecVLF")

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

contelecVLFDummyLoad = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1)
)
if mibBuilder.loadTexts:
    contelecVLFDummyLoad.setRevisions(
        ("2016-08-02 16:10",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ContelecVLFDLConformance_ObjectIdentity = ObjectIdentity
contelecVLFDLConformance = _ContelecVLFDLConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1, 2)
)
_ContelecVLFDLCompliances_ObjectIdentity = ObjectIdentity
contelecVLFDLCompliances = _ContelecVLFDLCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1, 2, 1)
)
_ContelecVLFDLGroups_ObjectIdentity = ObjectIdentity
contelecVLFDLGroups = _ContelecVLFDLGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1, 2, 2)
)
_ContelecVLFDLobject_ObjectIdentity = ObjectIdentity
contelecVLFDLobject = _ContelecVLFDLobject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1, 3)
)
_ContelecVLFDLTraps_ObjectIdentity = ObjectIdentity
contelecVLFDLTraps = _ContelecVLFDLTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1, 3, 0)
)
_ContelecVLFDLSpecs_ObjectIdentity = ObjectIdentity
contelecVLFDLSpecs = _ContelecVLFDLSpecs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1, 3, 1)
)


class _ContelecVLFDLInletTemperature_Type(Integer32):
    """Custom type contelecVLFDLInletTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 10000),
    )


_ContelecVLFDLInletTemperature_Type.__name__ = "Integer32"
_ContelecVLFDLInletTemperature_Object = MibScalar
contelecVLFDLInletTemperature = _ContelecVLFDLInletTemperature_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1, 3, 1, 1),
    _ContelecVLFDLInletTemperature_Type()
)
contelecVLFDLInletTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFDLInletTemperature.setStatus("current")


class _ContelecVLFDLOutletTemperature_Type(Integer32):
    """Custom type contelecVLFDLOutletTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 10000),
    )


_ContelecVLFDLOutletTemperature_Type.__name__ = "Integer32"
_ContelecVLFDLOutletTemperature_Object = MibScalar
contelecVLFDLOutletTemperature = _ContelecVLFDLOutletTemperature_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1, 3, 1, 2),
    _ContelecVLFDLOutletTemperature_Type()
)
contelecVLFDLOutletTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFDLOutletTemperature.setStatus("current")


class _ContelecVLFDLWaterFlowRate_Type(Integer32):
    """Custom type contelecVLFDLWaterFlowRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ContelecVLFDLWaterFlowRate_Type.__name__ = "Integer32"
_ContelecVLFDLWaterFlowRate_Object = MibScalar
contelecVLFDLWaterFlowRate = _ContelecVLFDLWaterFlowRate_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1, 3, 1, 3),
    _ContelecVLFDLWaterFlowRate_Type()
)
contelecVLFDLWaterFlowRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFDLWaterFlowRate.setStatus("current")


class _ContelecVLFDLPowerKilowatts_Type(Integer32):
    """Custom type contelecVLFDLPowerKilowatts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_ContelecVLFDLPowerKilowatts_Type.__name__ = "Integer32"
_ContelecVLFDLPowerKilowatts_Object = MibScalar
contelecVLFDLPowerKilowatts = _ContelecVLFDLPowerKilowatts_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1, 3, 1, 4),
    _ContelecVLFDLPowerKilowatts_Type()
)
contelecVLFDLPowerKilowatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFDLPowerKilowatts.setStatus("current")
_ContelecVLFDLWaterFlowLowWarn_Type = TruthValue
_ContelecVLFDLWaterFlowLowWarn_Object = MibScalar
contelecVLFDLWaterFlowLowWarn = _ContelecVLFDLWaterFlowLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1, 3, 1, 5),
    _ContelecVLFDLWaterFlowLowWarn_Type()
)
contelecVLFDLWaterFlowLowWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFDLWaterFlowLowWarn.setStatus("current")
_ContelecVLFDLWaterFlowLowFault_Type = TruthValue
_ContelecVLFDLWaterFlowLowFault_Object = MibScalar
contelecVLFDLWaterFlowLowFault = _ContelecVLFDLWaterFlowLowFault_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1, 3, 1, 6),
    _ContelecVLFDLWaterFlowLowFault_Type()
)
contelecVLFDLWaterFlowLowFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFDLWaterFlowLowFault.setStatus("current")
_ContelecVLFDLWaterFlowHighWarn_Type = TruthValue
_ContelecVLFDLWaterFlowHighWarn_Object = MibScalar
contelecVLFDLWaterFlowHighWarn = _ContelecVLFDLWaterFlowHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1, 3, 1, 7),
    _ContelecVLFDLWaterFlowHighWarn_Type()
)
contelecVLFDLWaterFlowHighWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFDLWaterFlowHighWarn.setStatus("current")
_ContelecVLFDLWaterOutletTempHighFault_Type = TruthValue
_ContelecVLFDLWaterOutletTempHighFault_Object = MibScalar
contelecVLFDLWaterOutletTempHighFault = _ContelecVLFDLWaterOutletTempHighFault_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1, 3, 1, 8),
    _ContelecVLFDLWaterOutletTempHighFault_Type()
)
contelecVLFDLWaterOutletTempHighFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFDLWaterOutletTempHighFault.setStatus("current")
_ContelecVLFDLWaterOutletTempHighWarn_Type = TruthValue
_ContelecVLFDLWaterOutletTempHighWarn_Object = MibScalar
contelecVLFDLWaterOutletTempHighWarn = _ContelecVLFDLWaterOutletTempHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1, 3, 1, 9),
    _ContelecVLFDLWaterOutletTempHighWarn_Type()
)
contelecVLFDLWaterOutletTempHighWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contelecVLFDLWaterOutletTempHighWarn.setStatus("current")
_ContelecVLFDLPumpOnCmd_Type = TruthValue
_ContelecVLFDLPumpOnCmd_Object = MibScalar
contelecVLFDLPumpOnCmd = _ContelecVLFDLPumpOnCmd_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1, 3, 1, 10),
    _ContelecVLFDLPumpOnCmd_Type()
)
contelecVLFDLPumpOnCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contelecVLFDLPumpOnCmd.setStatus("current")

# Managed Objects groups

contelecVLFDLGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1, 2, 2, 1)
)
contelecVLFDLGroup.setObjects(
      *(("CONTELEC-VLFDUMMYLOAD-MIB", "contelecVLFDLInletTemperature"),
        ("CONTELEC-VLFDUMMYLOAD-MIB", "contelecVLFDLOutletTemperature"),
        ("CONTELEC-VLFDUMMYLOAD-MIB", "contelecVLFDLWaterFlowRate"),
        ("CONTELEC-VLFDUMMYLOAD-MIB", "contelecVLFDLPowerKilowatts"),
        ("CONTELEC-VLFDUMMYLOAD-MIB", "contelecVLFDLWaterFlowLowWarn"),
        ("CONTELEC-VLFDUMMYLOAD-MIB", "contelecVLFDLWaterFlowLowFault"),
        ("CONTELEC-VLFDUMMYLOAD-MIB", "contelecVLFDLWaterFlowHighWarn"),
        ("CONTELEC-VLFDUMMYLOAD-MIB", "contelecVLFDLWaterOutletTempHighFault"),
        ("CONTELEC-VLFDUMMYLOAD-MIB", "contelecVLFDLWaterOutletTempHighWarn"),
        ("CONTELEC-VLFDUMMYLOAD-MIB", "contelecVLFDLPumpOnCmd"))
)
if mibBuilder.loadTexts:
    contelecVLFDLGroup.setStatus("current")


# Notification objects

coldStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1, 3, 0, 1)
)
if mibBuilder.loadTexts:
    coldStart.setStatus(
        "current"
    )

warmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1, 3, 0, 2)
)
if mibBuilder.loadTexts:
    warmStart.setStatus(
        "current"
    )

linkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1, 3, 0, 3)
)
if mibBuilder.loadTexts:
    linkDown.setStatus(
        "current"
    )

linkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1, 3, 0, 4)
)
if mibBuilder.loadTexts:
    linkUp.setStatus(
        "current"
    )

contelecVLFDLWarnWaterFlowLowAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1, 3, 0, 5)
)
if mibBuilder.loadTexts:
    contelecVLFDLWarnWaterFlowLowAlarm.setStatus(
        "current"
    )

contelecVLFDLFaultWaterFlowLowAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1, 3, 0, 6)
)
if mibBuilder.loadTexts:
    contelecVLFDLFaultWaterFlowLowAlarm.setStatus(
        "current"
    )

contelecVLFDLWarnWaterFlowHighAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1, 3, 0, 7)
)
if mibBuilder.loadTexts:
    contelecVLFDLWarnWaterFlowHighAlarm.setStatus(
        "current"
    )

contelecVLFDLFaultWaterOutletTempHighAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1, 3, 0, 8)
)
if mibBuilder.loadTexts:
    contelecVLFDLFaultWaterOutletTempHighAlarm.setStatus(
        "current"
    )

contelecVLFDLWarnWaterOutletTempHighAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1, 3, 0, 9)
)
if mibBuilder.loadTexts:
    contelecVLFDLWarnWaterOutletTempHighAlarm.setStatus(
        "current"
    )


# Notifications groups

contelecVLFDLNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1, 2, 2, 2)
)
contelecVLFDLNotificationGroup.setObjects(
      *(("CONTELEC-VLFDUMMYLOAD-MIB", "coldStart"),
        ("CONTELEC-VLFDUMMYLOAD-MIB", "warmStart"),
        ("CONTELEC-VLFDUMMYLOAD-MIB", "linkDown"),
        ("CONTELEC-VLFDUMMYLOAD-MIB", "linkUp"),
        ("CONTELEC-VLFDUMMYLOAD-MIB", "contelecVLFDLWarnWaterFlowLowAlarm"),
        ("CONTELEC-VLFDUMMYLOAD-MIB", "contelecVLFDLFaultWaterFlowLowAlarm"),
        ("CONTELEC-VLFDUMMYLOAD-MIB", "contelecVLFDLWarnWaterFlowHighAlarm"),
        ("CONTELEC-VLFDUMMYLOAD-MIB", "contelecVLFDLFaultWaterOutletTempHighAlarm"),
        ("CONTELEC-VLFDUMMYLOAD-MIB", "contelecVLFDLWarnWaterOutletTempHighAlarm"))
)
if mibBuilder.loadTexts:
    contelecVLFDLNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

contelecVLFDLCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 48307, 1, 1, 2, 1, 1)
)
contelecVLFDLCompliance.setObjects(
      *(("CONTELEC-VLFDUMMYLOAD-MIB", "contelecVLFDLGroup"),
        ("CONTELEC-VLFDUMMYLOAD-MIB", "contelecVLFDLNotificationGroup"))
)
if mibBuilder.loadTexts:
    contelecVLFDLCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CONTELEC-VLFDUMMYLOAD-MIB",
    **{"contelecVLFDummyLoad": contelecVLFDummyLoad,
       "contelecVLFDLConformance": contelecVLFDLConformance,
       "contelecVLFDLCompliances": contelecVLFDLCompliances,
       "contelecVLFDLCompliance": contelecVLFDLCompliance,
       "contelecVLFDLGroups": contelecVLFDLGroups,
       "contelecVLFDLGroup": contelecVLFDLGroup,
       "contelecVLFDLNotificationGroup": contelecVLFDLNotificationGroup,
       "contelecVLFDLobject": contelecVLFDLobject,
       "contelecVLFDLTraps": contelecVLFDLTraps,
       "coldStart": coldStart,
       "warmStart": warmStart,
       "linkDown": linkDown,
       "linkUp": linkUp,
       "contelecVLFDLWarnWaterFlowLowAlarm": contelecVLFDLWarnWaterFlowLowAlarm,
       "contelecVLFDLFaultWaterFlowLowAlarm": contelecVLFDLFaultWaterFlowLowAlarm,
       "contelecVLFDLWarnWaterFlowHighAlarm": contelecVLFDLWarnWaterFlowHighAlarm,
       "contelecVLFDLFaultWaterOutletTempHighAlarm": contelecVLFDLFaultWaterOutletTempHighAlarm,
       "contelecVLFDLWarnWaterOutletTempHighAlarm": contelecVLFDLWarnWaterOutletTempHighAlarm,
       "contelecVLFDLSpecs": contelecVLFDLSpecs,
       "contelecVLFDLInletTemperature": contelecVLFDLInletTemperature,
       "contelecVLFDLOutletTemperature": contelecVLFDLOutletTemperature,
       "contelecVLFDLWaterFlowRate": contelecVLFDLWaterFlowRate,
       "contelecVLFDLPowerKilowatts": contelecVLFDLPowerKilowatts,
       "contelecVLFDLWaterFlowLowWarn": contelecVLFDLWaterFlowLowWarn,
       "contelecVLFDLWaterFlowLowFault": contelecVLFDLWaterFlowLowFault,
       "contelecVLFDLWaterFlowHighWarn": contelecVLFDLWaterFlowHighWarn,
       "contelecVLFDLWaterOutletTempHighFault": contelecVLFDLWaterOutletTempHighFault,
       "contelecVLFDLWaterOutletTempHighWarn": contelecVLFDLWaterOutletTempHighWarn,
       "contelecVLFDLPumpOnCmd": contelecVLFDLPumpOnCmd}
)
