# SNMP MIB module (CISCO-OPTICAL-OTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-OPTICAL-OTS-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:13:24 2025
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

(CoiIntervalType,
 CoiOptAlarmServiceAffecting,
 CoiOptAlarmSeverity,
 CoiOptAlarmStatus,
 CoiOptAlarmType,
 CoiOpticalPower,
 CoiOpticalWavelength) = mibBuilder.importSymbols(
    "CISCO-OPTICAL-MIB",
    "CoiIntervalType",
    "CoiOptAlarmServiceAffecting",
    "CoiOptAlarmSeverity",
    "CoiOptAlarmStatus",
    "CoiOptAlarmType",
    "CoiOpticalPower",
    "CoiOpticalWavelength")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifName")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoOpticalOtsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 834)
)
if mibBuilder.loadTexts:
    ciscoOpticalOtsMIB.setRevisions(
        ("2020-04-08 00:00",
         "2018-06-06 00:00",
         "2016-12-16 00:00",
         "2016-12-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoOpticalOtsPortType(TextualConvention, Integer32):
    status = "current"
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
        *(("line", 1),
          ("com", 2),
          ("osc", 3),
          ("comCheck", 4),
          ("working", 5),
          ("protected", 6))
    )



class CiscoOpticalOtsGainInDb(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 4000),
    )



class CiscoOpticalOtsTiltInDb(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )



class CiscoOpticalOtsVoaAttenInDb(TextualConvention, Unsigned32):
    status = "current"


class CiscoOpticalOtsLaserStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("on", 2),
          ("off", 3),
          ("apr", 4))
    )



class CiscoOpticalOtsAmpliControlMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("auto", 2))
    )



class CiscoOpticalOtsAmpliGainRange(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("extended", 2))
    )



class CiscoOpticalOtsAmpliSafetyCtrlMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("disabled", 2))
    )



class CiscoOpticalOtsOsri(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )



class CiscoOpticalOtsProtectionPortRole(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )



class CiscoOpticalOtsState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("adminDown", 3))
    )



class CiscoOpticalOtsTranspAdminState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfService", 2),
          ("maintenance", 3),
          ("ains", 4))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoOpticalOtsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoOpticalOtsMIBNotifs = _CiscoOpticalOtsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 0)
)
_CiscoOpticalOtsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoOpticalOtsMIBObjects = _CiscoOpticalOtsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1)
)
_CooOtsController_ObjectIdentity = ObjectIdentity
cooOtsController = _CooOtsController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1)
)


class _CooOtsNotifEnabled_Type(TruthValue):
    """Custom type cooOtsNotifEnabled based on TruthValue"""
    defaultValue = 2


_CooOtsNotifEnabled_Type.__name__ = "TruthValue"
_CooOtsNotifEnabled_Object = MibScalar
cooOtsNotifEnabled = _CooOtsNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 1),
    _CooOtsNotifEnabled_Type()
)
cooOtsNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOtsNotifEnabled.setStatus("current")
_CooOtsControllerTable_Object = MibTable
cooOtsControllerTable = _CooOtsControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cooOtsControllerTable.setStatus("current")
_CooOtsControllerEntry_Object = MibTableRow
cooOtsControllerEntry = _CooOtsControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 2, 1)
)
cooOtsControllerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cooOtsControllerEntry.setStatus("current")
_CooOtsControllerPortType_Type = CiscoOpticalOtsPortType
_CooOtsControllerPortType_Object = MibTableColumn
cooOtsControllerPortType = _CooOtsControllerPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 2, 1, 1),
    _CooOtsControllerPortType_Type()
)
cooOtsControllerPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOtsControllerPortType.setStatus("current")
_CooOtsControllerLaserStatus_Type = CiscoOpticalOtsLaserStatus
_CooOtsControllerLaserStatus_Object = MibTableColumn
cooOtsControllerLaserStatus = _CooOtsControllerLaserStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 2, 1, 2),
    _CooOtsControllerLaserStatus_Type()
)
cooOtsControllerLaserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOtsControllerLaserStatus.setStatus("current")
_CooOtsControllerRXPower_Type = CoiOpticalPower
_CooOtsControllerRXPower_Object = MibTableColumn
cooOtsControllerRXPower = _CooOtsControllerRXPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 2, 1, 3),
    _CooOtsControllerRXPower_Type()
)
cooOtsControllerRXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOtsControllerRXPower.setStatus("current")
if mibBuilder.loadTexts:
    cooOtsControllerRXPower.setUnits("1/100 dBm")
_CooOtsControllerTXPower_Type = CoiOpticalPower
_CooOtsControllerTXPower_Object = MibTableColumn
cooOtsControllerTXPower = _CooOtsControllerTXPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 2, 1, 4),
    _CooOtsControllerTXPower_Type()
)
cooOtsControllerTXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOtsControllerTXPower.setStatus("current")
if mibBuilder.loadTexts:
    cooOtsControllerTXPower.setUnits("1/100 dBm")
_CooOtsControllerAmpliGain_Type = CiscoOpticalOtsGainInDb
_CooOtsControllerAmpliGain_Object = MibTableColumn
cooOtsControllerAmpliGain = _CooOtsControllerAmpliGain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 2, 1, 5),
    _CooOtsControllerAmpliGain_Type()
)
cooOtsControllerAmpliGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOtsControllerAmpliGain.setStatus("current")
if mibBuilder.loadTexts:
    cooOtsControllerAmpliGain.setUnits("1/100 dB")
_CooOtsControllerAmpliTilt_Type = CiscoOpticalOtsTiltInDb
_CooOtsControllerAmpliTilt_Object = MibTableColumn
cooOtsControllerAmpliTilt = _CooOtsControllerAmpliTilt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 2, 1, 6),
    _CooOtsControllerAmpliTilt_Type()
)
cooOtsControllerAmpliTilt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOtsControllerAmpliTilt.setStatus("current")
if mibBuilder.loadTexts:
    cooOtsControllerAmpliTilt.setUnits("1/100 dB")
_CooOtsControllerTotalRXPower_Type = CoiOpticalPower
_CooOtsControllerTotalRXPower_Object = MibTableColumn
cooOtsControllerTotalRXPower = _CooOtsControllerTotalRXPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 2, 1, 7),
    _CooOtsControllerTotalRXPower_Type()
)
cooOtsControllerTotalRXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOtsControllerTotalRXPower.setStatus("current")
if mibBuilder.loadTexts:
    cooOtsControllerTotalRXPower.setUnits("1/100 dBm")
_CooOtsControllerTotalTXPower_Type = CoiOpticalPower
_CooOtsControllerTotalTXPower_Object = MibTableColumn
cooOtsControllerTotalTXPower = _CooOtsControllerTotalTXPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 2, 1, 8),
    _CooOtsControllerTotalTXPower_Type()
)
cooOtsControllerTotalTXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOtsControllerTotalTXPower.setStatus("current")
if mibBuilder.loadTexts:
    cooOtsControllerTotalTXPower.setUnits("1/100 dBm")
_CooOtsControllerRXVoaAttenuation_Type = CiscoOpticalOtsVoaAttenInDb
_CooOtsControllerRXVoaAttenuation_Object = MibTableColumn
cooOtsControllerRXVoaAttenuation = _CooOtsControllerRXVoaAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 2, 1, 9),
    _CooOtsControllerRXVoaAttenuation_Type()
)
cooOtsControllerRXVoaAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOtsControllerRXVoaAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    cooOtsControllerRXVoaAttenuation.setUnits("1/100 dB")
_CooOtsControllerTXVoaAttenuation_Type = CiscoOpticalOtsVoaAttenInDb
_CooOtsControllerTXVoaAttenuation_Object = MibTableColumn
cooOtsControllerTXVoaAttenuation = _CooOtsControllerTXVoaAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 2, 1, 10),
    _CooOtsControllerTXVoaAttenuation_Type()
)
cooOtsControllerTXVoaAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOtsControllerTXVoaAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    cooOtsControllerTXVoaAttenuation.setUnits("1/100 dB")
_CooOtsControllerRXLowThreshold_Type = CoiOpticalPower
_CooOtsControllerRXLowThreshold_Object = MibTableColumn
cooOtsControllerRXLowThreshold = _CooOtsControllerRXLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 2, 1, 11),
    _CooOtsControllerRXLowThreshold_Type()
)
cooOtsControllerRXLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOtsControllerRXLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cooOtsControllerRXLowThreshold.setUnits("1/100 dBm")
_CooOtsControllerTXLowThreshold_Type = CoiOpticalPower
_CooOtsControllerTXLowThreshold_Object = MibTableColumn
cooOtsControllerTXLowThreshold = _CooOtsControllerTXLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 2, 1, 12),
    _CooOtsControllerTXLowThreshold_Type()
)
cooOtsControllerTXLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOtsControllerTXLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cooOtsControllerTXLowThreshold.setUnits("1/100 dBm")
_CooOtsControllerAmpliChannelPwr_Type = CoiOpticalPower
_CooOtsControllerAmpliChannelPwr_Object = MibTableColumn
cooOtsControllerAmpliChannelPwr = _CooOtsControllerAmpliChannelPwr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 2, 1, 13),
    _CooOtsControllerAmpliChannelPwr_Type()
)
cooOtsControllerAmpliChannelPwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOtsControllerAmpliChannelPwr.setStatus("current")
if mibBuilder.loadTexts:
    cooOtsControllerAmpliChannelPwr.setUnits("1/100 dBm")
_CooOtsControllerChannelPwrMaxDelta_Type = CoiOpticalPower
_CooOtsControllerChannelPwrMaxDelta_Object = MibTableColumn
cooOtsControllerChannelPwrMaxDelta = _CooOtsControllerChannelPwrMaxDelta_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 2, 1, 14),
    _CooOtsControllerChannelPwrMaxDelta_Type()
)
cooOtsControllerChannelPwrMaxDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOtsControllerChannelPwrMaxDelta.setStatus("current")
if mibBuilder.loadTexts:
    cooOtsControllerChannelPwrMaxDelta.setUnits("1/100 dBm")
_CooOtsControllerAmpliControlMode_Type = CiscoOpticalOtsAmpliControlMode
_CooOtsControllerAmpliControlMode_Object = MibTableColumn
cooOtsControllerAmpliControlMode = _CooOtsControllerAmpliControlMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 2, 1, 15),
    _CooOtsControllerAmpliControlMode_Type()
)
cooOtsControllerAmpliControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOtsControllerAmpliControlMode.setStatus("current")
_CooOtsControllerAmpliGainRange_Type = CiscoOpticalOtsAmpliGainRange
_CooOtsControllerAmpliGainRange_Object = MibTableColumn
cooOtsControllerAmpliGainRange = _CooOtsControllerAmpliGainRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 2, 1, 16),
    _CooOtsControllerAmpliGainRange_Type()
)
cooOtsControllerAmpliGainRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOtsControllerAmpliGainRange.setStatus("current")
_CooOtsControllerAmpliSafetyCtrlMode_Type = CiscoOpticalOtsAmpliSafetyCtrlMode
_CooOtsControllerAmpliSafetyCtrlMode_Object = MibTableColumn
cooOtsControllerAmpliSafetyCtrlMode = _CooOtsControllerAmpliSafetyCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 2, 1, 17),
    _CooOtsControllerAmpliSafetyCtrlMode_Type()
)
cooOtsControllerAmpliSafetyCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOtsControllerAmpliSafetyCtrlMode.setStatus("current")
_CooOtsControllerOsri_Type = CiscoOpticalOtsOsri
_CooOtsControllerOsri_Object = MibTableColumn
cooOtsControllerOsri = _CooOtsControllerOsri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 2, 1, 18),
    _CooOtsControllerOsri_Type()
)
cooOtsControllerOsri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOtsControllerOsri.setStatus("current")
_CooOtsControllerProtectionPortRole_Type = CiscoOpticalOtsProtectionPortRole
_CooOtsControllerProtectionPortRole_Object = MibTableColumn
cooOtsControllerProtectionPortRole = _CooOtsControllerProtectionPortRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 2, 1, 19),
    _CooOtsControllerProtectionPortRole_Type()
)
cooOtsControllerProtectionPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOtsControllerProtectionPortRole.setStatus("current")
_CooOtsControllerState_Type = CiscoOpticalOtsState
_CooOtsControllerState_Object = MibTableColumn
cooOtsControllerState = _CooOtsControllerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 2, 1, 20),
    _CooOtsControllerState_Type()
)
cooOtsControllerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOtsControllerState.setStatus("current")
_CooOtsControllerTranspAdminState_Type = CiscoOpticalOtsTranspAdminState
_CooOtsControllerTranspAdminState_Object = MibTableColumn
cooOtsControllerTranspAdminState = _CooOtsControllerTranspAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 2, 1, 21),
    _CooOtsControllerTranspAdminState_Type()
)
cooOtsControllerTranspAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOtsControllerTranspAdminState.setStatus("current")


class _CooOtsControllerAlarmState_Type(Bits):
    """Custom type cooOtsControllerAlarmState based on Bits"""
    namedValues = NamedValues(
        *(("noDefect", 0),
          ("highRXPwr", 1),
          ("highTXPwr", 2),
          ("lowRXPwr", 3),
          ("lowTXPwr", 4),
          ("lospRXPwr", 5),
          ("locRXPwr", 6),
          ("degLowGain", 7),
          ("degHighGain", 8),
          ("alsAmp", 9),
          ("aprAmp", 10),
          ("noEqAutoAmp", 11),
          ("misAutoAmp", 12),
          ("switchToProtect", 13),
          ("autoAmpliCtrlRunning", 14))
    )

_CooOtsControllerAlarmState_Type.__name__ = "Bits"
_CooOtsControllerAlarmState_Object = MibTableColumn
cooOtsControllerAlarmState = _CooOtsControllerAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 2, 1, 22),
    _CooOtsControllerAlarmState_Type()
)
cooOtsControllerAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOtsControllerAlarmState.setStatus("current")


class _CooOtsControllerRXSpanLoss_Type(CoiOpticalPower):
    """Custom type cooOtsControllerRXSpanLoss based on CoiOpticalPower"""
    subtypeSpec = CoiOpticalPower.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4000, 3000),
    )


_CooOtsControllerRXSpanLoss_Type.__name__ = "CoiOpticalPower"
_CooOtsControllerRXSpanLoss_Object = MibTableColumn
cooOtsControllerRXSpanLoss = _CooOtsControllerRXSpanLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 2, 1, 23),
    _CooOtsControllerRXSpanLoss_Type()
)
cooOtsControllerRXSpanLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOtsControllerRXSpanLoss.setStatus("current")
if mibBuilder.loadTexts:
    cooOtsControllerRXSpanLoss.setUnits("1/100 dBm")


class _CooOtsControllerTXSpanLoss_Type(CoiOpticalPower):
    """Custom type cooOtsControllerTXSpanLoss based on CoiOpticalPower"""
    subtypeSpec = CoiOpticalPower.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4000, 3000),
    )


_CooOtsControllerTXSpanLoss_Type.__name__ = "CoiOpticalPower"
_CooOtsControllerTXSpanLoss_Object = MibTableColumn
cooOtsControllerTXSpanLoss = _CooOtsControllerTXSpanLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 2, 1, 24),
    _CooOtsControllerTXSpanLoss_Type()
)
cooOtsControllerTXSpanLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOtsControllerTXSpanLoss.setStatus("current")
if mibBuilder.loadTexts:
    cooOtsControllerTXSpanLoss.setUnits("1/100 dBm")
_CooOtsControllerRXEnabled_Type = TruthValue
_CooOtsControllerRXEnabled_Object = MibTableColumn
cooOtsControllerRXEnabled = _CooOtsControllerRXEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 2, 1, 25),
    _CooOtsControllerRXEnabled_Type()
)
cooOtsControllerRXEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOtsControllerRXEnabled.setStatus("current")
_CooOtsControllerTXEnabled_Type = TruthValue
_CooOtsControllerTXEnabled_Object = MibTableColumn
cooOtsControllerTXEnabled = _CooOtsControllerTXEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 2, 1, 26),
    _CooOtsControllerTXEnabled_Type()
)
cooOtsControllerTXEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOtsControllerTXEnabled.setStatus("current")
_CooOtsOchControllerTable_Object = MibTable
cooOtsOchControllerTable = _CooOtsOchControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cooOtsOchControllerTable.setStatus("current")
_CooOtsOchControllerEntry_Object = MibTableRow
cooOtsOchControllerEntry = _CooOtsOchControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 3, 1)
)
cooOtsOchControllerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cooOtsOchControllerEntry.setStatus("current")
_CooOtsOchControllerPortType_Type = CiscoOpticalOtsPortType
_CooOtsOchControllerPortType_Object = MibTableColumn
cooOtsOchControllerPortType = _CooOtsOchControllerPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 3, 1, 1),
    _CooOtsOchControllerPortType_Type()
)
cooOtsOchControllerPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOtsOchControllerPortType.setStatus("current")
_CooOtsOchControllerLaserStatus_Type = CiscoOpticalOtsLaserStatus
_CooOtsOchControllerLaserStatus_Object = MibTableColumn
cooOtsOchControllerLaserStatus = _CooOtsOchControllerLaserStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 3, 1, 2),
    _CooOtsOchControllerLaserStatus_Type()
)
cooOtsOchControllerLaserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOtsOchControllerLaserStatus.setStatus("current")
_CooOtsOchControllerRXPower_Type = CoiOpticalPower
_CooOtsOchControllerRXPower_Object = MibTableColumn
cooOtsOchControllerRXPower = _CooOtsOchControllerRXPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 3, 1, 3),
    _CooOtsOchControllerRXPower_Type()
)
cooOtsOchControllerRXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOtsOchControllerRXPower.setStatus("current")
if mibBuilder.loadTexts:
    cooOtsOchControllerRXPower.setUnits("1/100 dBm")
_CooOtsOchControllerTXPower_Type = CoiOpticalPower
_CooOtsOchControllerTXPower_Object = MibTableColumn
cooOtsOchControllerTXPower = _CooOtsOchControllerTXPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 3, 1, 4),
    _CooOtsOchControllerTXPower_Type()
)
cooOtsOchControllerTXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOtsOchControllerTXPower.setStatus("current")
if mibBuilder.loadTexts:
    cooOtsOchControllerTXPower.setUnits("1/100 dBm")
_CooOtsOchControllerRXLowThreshold_Type = CoiOpticalPower
_CooOtsOchControllerRXLowThreshold_Object = MibTableColumn
cooOtsOchControllerRXLowThreshold = _CooOtsOchControllerRXLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 3, 1, 5),
    _CooOtsOchControllerRXLowThreshold_Type()
)
cooOtsOchControllerRXLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOtsOchControllerRXLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cooOtsOchControllerRXLowThreshold.setUnits("1/100 dBm")
_CooOtsOchControllerTXLowThreshold_Type = CoiOpticalPower
_CooOtsOchControllerTXLowThreshold_Object = MibTableColumn
cooOtsOchControllerTXLowThreshold = _CooOtsOchControllerTXLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 3, 1, 6),
    _CooOtsOchControllerTXLowThreshold_Type()
)
cooOtsOchControllerTXLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOtsOchControllerTXLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cooOtsOchControllerTXLowThreshold.setUnits("1/100 dBm")


class _CooOtsOchControllerWavelength_Type(CoiOpticalWavelength):
    """Custom type cooOtsOchControllerWavelength based on CoiOpticalWavelength"""
    defaultValue = 0


_CooOtsOchControllerWavelength_Type.__name__ = "CoiOpticalWavelength"
_CooOtsOchControllerWavelength_Object = MibTableColumn
cooOtsOchControllerWavelength = _CooOtsOchControllerWavelength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 3, 1, 7),
    _CooOtsOchControllerWavelength_Type()
)
cooOtsOchControllerWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOtsOchControllerWavelength.setStatus("current")
if mibBuilder.loadTexts:
    cooOtsOchControllerWavelength.setUnits("1/100 nm")


class _CooOtsOchControllerFrequency_Type(Unsigned32):
    """Custom type cooOtsOchControllerFrequency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1913500, 1961000),
    )


_CooOtsOchControllerFrequency_Type.__name__ = "Unsigned32"
_CooOtsOchControllerFrequency_Object = MibTableColumn
cooOtsOchControllerFrequency = _CooOtsOchControllerFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 3, 1, 8),
    _CooOtsOchControllerFrequency_Type()
)
cooOtsOchControllerFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOtsOchControllerFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cooOtsOchControllerFrequency.setUnits("100 MHz")


class _CooOtsOchControllerChannelNumber_Type(Unsigned32):
    """Custom type cooOtsOchControllerChannelNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 384),
    )


_CooOtsOchControllerChannelNumber_Type.__name__ = "Unsigned32"
_CooOtsOchControllerChannelNumber_Object = MibTableColumn
cooOtsOchControllerChannelNumber = _CooOtsOchControllerChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 3, 1, 9),
    _CooOtsOchControllerChannelNumber_Type()
)
cooOtsOchControllerChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOtsOchControllerChannelNumber.setStatus("current")
_CooOtsOchControllerState_Type = CiscoOpticalOtsState
_CooOtsOchControllerState_Object = MibTableColumn
cooOtsOchControllerState = _CooOtsOchControllerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 3, 1, 10),
    _CooOtsOchControllerState_Type()
)
cooOtsOchControllerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOtsOchControllerState.setStatus("current")
_CooOtsOchControllerTranspAdminState_Type = CiscoOpticalOtsTranspAdminState
_CooOtsOchControllerTranspAdminState_Object = MibTableColumn
cooOtsOchControllerTranspAdminState = _CooOtsOchControllerTranspAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 3, 1, 11),
    _CooOtsOchControllerTranspAdminState_Type()
)
cooOtsOchControllerTranspAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOtsOchControllerTranspAdminState.setStatus("current")


class _CooOtsOchControllerAlarmState_Type(Bits):
    """Custom type cooOtsOchControllerAlarmState based on Bits"""
    namedValues = NamedValues(
        *(("noDefect", 0),
          ("highRXPwr", 1),
          ("highTXPwr", 2),
          ("lowRXPwr", 3),
          ("lowTXPwr", 4),
          ("lospRXPwr", 5),
          ("locRXPwr", 6),
          ("degLowGain", 7),
          ("degHighGain", 8),
          ("alsAmp", 9),
          ("aprAmp", 10),
          ("noEqAutoAmp", 11),
          ("misAutoAmp", 12),
          ("switchToProtect", 13))
    )

_CooOtsOchControllerAlarmState_Type.__name__ = "Bits"
_CooOtsOchControllerAlarmState_Object = MibTableColumn
cooOtsOchControllerAlarmState = _CooOtsOchControllerAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 3, 1, 12),
    _CooOtsOchControllerAlarmState_Type()
)
cooOtsOchControllerAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOtsOchControllerAlarmState.setStatus("current")


class _CooOtsOchControllerWidth_Type(Unsigned32):
    """Custom type cooOtsOchControllerWidth based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 8000),
    )


_CooOtsOchControllerWidth_Type.__name__ = "Unsigned32"
_CooOtsOchControllerWidth_Object = MibTableColumn
cooOtsOchControllerWidth = _CooOtsOchControllerWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 3, 1, 13),
    _CooOtsOchControllerWidth_Type()
)
cooOtsOchControllerWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooOtsOchControllerWidth.setStatus("current")
if mibBuilder.loadTexts:
    cooOtsOchControllerWidth.setUnits("1/10 GHz")


class _CooOtsOchNotifEnabled_Type(TruthValue):
    """Custom type cooOtsOchNotifEnabled based on TruthValue"""
    defaultValue = 2


_CooOtsOchNotifEnabled_Type.__name__ = "TruthValue"
_CooOtsOchNotifEnabled_Object = MibScalar
cooOtsOchNotifEnabled = _CooOtsOchNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 1, 4),
    _CooOtsOchNotifEnabled_Type()
)
cooOtsOchNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooOtsOchNotifEnabled.setStatus("current")
_CooOtsPerformanceMonitoring_ObjectIdentity = ObjectIdentity
cooOtsPerformanceMonitoring = _CooOtsPerformanceMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2)
)
_CooOtsThresholdTable_Object = MibTable
cooOtsThresholdTable = _CooOtsThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cooOtsThresholdTable.setStatus("current")
_CooOtsThresholdEntry_Object = MibTableRow
cooOtsThresholdEntry = _CooOtsThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 1, 1)
)
cooOtsThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-OPTICAL-OTS-MIB", "cooThreshIntervalType"),
)
if mibBuilder.loadTexts:
    cooOtsThresholdEntry.setStatus("current")
_CooThreshIntervalType_Type = CoiIntervalType
_CooThreshIntervalType_Object = MibTableColumn
cooThreshIntervalType = _CooThreshIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 1, 1, 1),
    _CooThreshIntervalType_Type()
)
cooThreshIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cooThreshIntervalType.setStatus("current")
_CooThreshTXPowerMin_Type = CoiOpticalPower
_CooThreshTXPowerMin_Object = MibTableColumn
cooThreshTXPowerMin = _CooThreshTXPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 1, 1, 2),
    _CooThreshTXPowerMin_Type()
)
cooThreshTXPowerMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooThreshTXPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    cooThreshTXPowerMin.setUnits("1/100 dBm")
_CooThreshRXPowerMin_Type = CoiOpticalPower
_CooThreshRXPowerMin_Object = MibTableColumn
cooThreshRXPowerMin = _CooThreshRXPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 1, 1, 3),
    _CooThreshRXPowerMin_Type()
)
cooThreshRXPowerMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooThreshRXPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    cooThreshRXPowerMin.setUnits("1/100 dBm")


class _CooThreshLBCMin_Type(Unsigned32):
    """Custom type cooThreshLBCMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CooThreshLBCMin_Type.__name__ = "Unsigned32"
_CooThreshLBCMin_Object = MibTableColumn
cooThreshLBCMin = _CooThreshLBCMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 1, 1, 4),
    _CooThreshLBCMin_Type()
)
cooThreshLBCMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooThreshLBCMin.setStatus("current")
if mibBuilder.loadTexts:
    cooThreshLBCMin.setUnits("1/10 percent")
_CooThreshTXPowerMax_Type = CoiOpticalPower
_CooThreshTXPowerMax_Object = MibTableColumn
cooThreshTXPowerMax = _CooThreshTXPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 1, 1, 5),
    _CooThreshTXPowerMax_Type()
)
cooThreshTXPowerMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooThreshTXPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    cooThreshTXPowerMax.setUnits("1/100 dBm")
_CooThreshRXPowerMax_Type = CoiOpticalPower
_CooThreshRXPowerMax_Object = MibTableColumn
cooThreshRXPowerMax = _CooThreshRXPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 1, 1, 6),
    _CooThreshRXPowerMax_Type()
)
cooThreshRXPowerMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooThreshRXPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    cooThreshRXPowerMax.setUnits("1/100 dBm")


class _CooThreshLBCMax_Type(Unsigned32):
    """Custom type cooThreshLBCMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CooThreshLBCMax_Type.__name__ = "Unsigned32"
_CooThreshLBCMax_Object = MibTableColumn
cooThreshLBCMax = _CooThreshLBCMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 1, 1, 7),
    _CooThreshLBCMax_Type()
)
cooThreshLBCMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooThreshLBCMax.setStatus("current")
if mibBuilder.loadTexts:
    cooThreshLBCMax.setUnits("1/10 percent")


class _CooThreshTXPowerEnableMin_Type(TruthValue):
    """Custom type cooThreshTXPowerEnableMin based on TruthValue"""
    defaultValue = 2


_CooThreshTXPowerEnableMin_Type.__name__ = "TruthValue"
_CooThreshTXPowerEnableMin_Object = MibTableColumn
cooThreshTXPowerEnableMin = _CooThreshTXPowerEnableMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 1, 1, 8),
    _CooThreshTXPowerEnableMin_Type()
)
cooThreshTXPowerEnableMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooThreshTXPowerEnableMin.setStatus("current")


class _CooThreshRXPowerEnableMin_Type(TruthValue):
    """Custom type cooThreshRXPowerEnableMin based on TruthValue"""
    defaultValue = 2


_CooThreshRXPowerEnableMin_Type.__name__ = "TruthValue"
_CooThreshRXPowerEnableMin_Object = MibTableColumn
cooThreshRXPowerEnableMin = _CooThreshRXPowerEnableMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 1, 1, 9),
    _CooThreshRXPowerEnableMin_Type()
)
cooThreshRXPowerEnableMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooThreshRXPowerEnableMin.setStatus("current")


class _CooThreshLBCEnableMin_Type(TruthValue):
    """Custom type cooThreshLBCEnableMin based on TruthValue"""
    defaultValue = 2


_CooThreshLBCEnableMin_Type.__name__ = "TruthValue"
_CooThreshLBCEnableMin_Object = MibTableColumn
cooThreshLBCEnableMin = _CooThreshLBCEnableMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 1, 1, 10),
    _CooThreshLBCEnableMin_Type()
)
cooThreshLBCEnableMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooThreshLBCEnableMin.setStatus("current")


class _CooThreshTXPowerEnableMax_Type(TruthValue):
    """Custom type cooThreshTXPowerEnableMax based on TruthValue"""
    defaultValue = 2


_CooThreshTXPowerEnableMax_Type.__name__ = "TruthValue"
_CooThreshTXPowerEnableMax_Object = MibTableColumn
cooThreshTXPowerEnableMax = _CooThreshTXPowerEnableMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 1, 1, 11),
    _CooThreshTXPowerEnableMax_Type()
)
cooThreshTXPowerEnableMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooThreshTXPowerEnableMax.setStatus("current")


class _CooThreshRXPowerEnableMax_Type(TruthValue):
    """Custom type cooThreshRXPowerEnableMax based on TruthValue"""
    defaultValue = 2


_CooThreshRXPowerEnableMax_Type.__name__ = "TruthValue"
_CooThreshRXPowerEnableMax_Object = MibTableColumn
cooThreshRXPowerEnableMax = _CooThreshRXPowerEnableMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 1, 1, 12),
    _CooThreshRXPowerEnableMax_Type()
)
cooThreshRXPowerEnableMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooThreshRXPowerEnableMax.setStatus("current")


class _CooThreshLBCEnableMax_Type(TruthValue):
    """Custom type cooThreshLBCEnableMax based on TruthValue"""
    defaultValue = 2


_CooThreshLBCEnableMax_Type.__name__ = "TruthValue"
_CooThreshLBCEnableMax_Object = MibTableColumn
cooThreshLBCEnableMax = _CooThreshLBCEnableMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 1, 1, 13),
    _CooThreshLBCEnableMax_Type()
)
cooThreshLBCEnableMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooThreshLBCEnableMax.setStatus("current")


class _CooThreshAmpliGainMin_Type(Integer32):
    """Custom type cooThreshAmpliGainMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_CooThreshAmpliGainMin_Type.__name__ = "Integer32"
_CooThreshAmpliGainMin_Object = MibTableColumn
cooThreshAmpliGainMin = _CooThreshAmpliGainMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 1, 1, 14),
    _CooThreshAmpliGainMin_Type()
)
cooThreshAmpliGainMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooThreshAmpliGainMin.setStatus("current")
if mibBuilder.loadTexts:
    cooThreshAmpliGainMin.setUnits("1/100 dB")


class _CooThreshAmpliGainMax_Type(Integer32):
    """Custom type cooThreshAmpliGainMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_CooThreshAmpliGainMax_Type.__name__ = "Integer32"
_CooThreshAmpliGainMax_Object = MibTableColumn
cooThreshAmpliGainMax = _CooThreshAmpliGainMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 1, 1, 15),
    _CooThreshAmpliGainMax_Type()
)
cooThreshAmpliGainMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooThreshAmpliGainMax.setStatus("current")
if mibBuilder.loadTexts:
    cooThreshAmpliGainMax.setUnits("1/100 dB")


class _CooThreshAmpliGainEnableMax_Type(TruthValue):
    """Custom type cooThreshAmpliGainEnableMax based on TruthValue"""
    defaultValue = 2


_CooThreshAmpliGainEnableMax_Type.__name__ = "TruthValue"
_CooThreshAmpliGainEnableMax_Object = MibTableColumn
cooThreshAmpliGainEnableMax = _CooThreshAmpliGainEnableMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 1, 1, 16),
    _CooThreshAmpliGainEnableMax_Type()
)
cooThreshAmpliGainEnableMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooThreshAmpliGainEnableMax.setStatus("current")


class _CooThreshAmpliGainEnableMin_Type(TruthValue):
    """Custom type cooThreshAmpliGainEnableMin based on TruthValue"""
    defaultValue = 2


_CooThreshAmpliGainEnableMin_Type.__name__ = "TruthValue"
_CooThreshAmpliGainEnableMin_Object = MibTableColumn
cooThreshAmpliGainEnableMin = _CooThreshAmpliGainEnableMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 1, 1, 17),
    _CooThreshAmpliGainEnableMin_Type()
)
cooThreshAmpliGainEnableMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooThreshAmpliGainEnableMin.setStatus("current")


class _CooThreshAmpliGainTiltMin_Type(Integer32):
    """Custom type cooThreshAmpliGainTiltMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 50),
    )


_CooThreshAmpliGainTiltMin_Type.__name__ = "Integer32"
_CooThreshAmpliGainTiltMin_Object = MibTableColumn
cooThreshAmpliGainTiltMin = _CooThreshAmpliGainTiltMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 1, 1, 18),
    _CooThreshAmpliGainTiltMin_Type()
)
cooThreshAmpliGainTiltMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooThreshAmpliGainTiltMin.setStatus("current")
if mibBuilder.loadTexts:
    cooThreshAmpliGainTiltMin.setUnits("1/100 dB")


class _CooThreshAmpliGainTiltMax_Type(Integer32):
    """Custom type cooThreshAmpliGainTiltMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 50),
    )


_CooThreshAmpliGainTiltMax_Type.__name__ = "Integer32"
_CooThreshAmpliGainTiltMax_Object = MibTableColumn
cooThreshAmpliGainTiltMax = _CooThreshAmpliGainTiltMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 1, 1, 19),
    _CooThreshAmpliGainTiltMax_Type()
)
cooThreshAmpliGainTiltMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooThreshAmpliGainTiltMax.setStatus("current")
if mibBuilder.loadTexts:
    cooThreshAmpliGainTiltMax.setUnits("1/100 db")


class _CooThreshAmpliGainTiltEnableMax_Type(TruthValue):
    """Custom type cooThreshAmpliGainTiltEnableMax based on TruthValue"""
    defaultValue = 2


_CooThreshAmpliGainTiltEnableMax_Type.__name__ = "TruthValue"
_CooThreshAmpliGainTiltEnableMax_Object = MibTableColumn
cooThreshAmpliGainTiltEnableMax = _CooThreshAmpliGainTiltEnableMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 1, 1, 20),
    _CooThreshAmpliGainTiltEnableMax_Type()
)
cooThreshAmpliGainTiltEnableMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooThreshAmpliGainTiltEnableMax.setStatus("current")


class _CooThreshAmpliGainTiltEnableMin_Type(TruthValue):
    """Custom type cooThreshAmpliGainTiltEnableMin based on TruthValue"""
    defaultValue = 2


_CooThreshAmpliGainTiltEnableMin_Type.__name__ = "TruthValue"
_CooThreshAmpliGainTiltEnableMin_Object = MibTableColumn
cooThreshAmpliGainTiltEnableMin = _CooThreshAmpliGainTiltEnableMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 1, 1, 21),
    _CooThreshAmpliGainTiltEnableMin_Type()
)
cooThreshAmpliGainTiltEnableMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cooThreshAmpliGainTiltEnableMin.setStatus("current")
_CooOtsCurrentTable_Object = MibTable
cooOtsCurrentTable = _CooOtsCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cooOtsCurrentTable.setStatus("current")
_CooOtsCurrentEntry_Object = MibTableRow
cooOtsCurrentEntry = _CooOtsCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 2, 1)
)
cooOtsCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-OPTICAL-OTS-MIB", "cooCurrentIntervalType"),
)
if mibBuilder.loadTexts:
    cooOtsCurrentEntry.setStatus("current")
_CooCurrentIntervalType_Type = CoiIntervalType
_CooCurrentIntervalType_Object = MibTableColumn
cooCurrentIntervalType = _CooCurrentIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 2, 1, 1),
    _CooCurrentIntervalType_Type()
)
cooCurrentIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cooCurrentIntervalType.setStatus("current")
_CooCurrentTXPowerMax_Type = CoiOpticalPower
_CooCurrentTXPowerMax_Object = MibTableColumn
cooCurrentTXPowerMax = _CooCurrentTXPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 2, 1, 2),
    _CooCurrentTXPowerMax_Type()
)
cooCurrentTXPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooCurrentTXPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    cooCurrentTXPowerMax.setUnits("1/100 dBm")
_CooCurrentRXPowerMax_Type = CoiOpticalPower
_CooCurrentRXPowerMax_Object = MibTableColumn
cooCurrentRXPowerMax = _CooCurrentRXPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 2, 1, 3),
    _CooCurrentRXPowerMax_Type()
)
cooCurrentRXPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooCurrentRXPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    cooCurrentRXPowerMax.setUnits("1/100 dBm")


class _CooCurrentLBCMax_Type(Unsigned32):
    """Custom type cooCurrentLBCMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CooCurrentLBCMax_Type.__name__ = "Unsigned32"
_CooCurrentLBCMax_Object = MibTableColumn
cooCurrentLBCMax = _CooCurrentLBCMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 2, 1, 4),
    _CooCurrentLBCMax_Type()
)
cooCurrentLBCMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooCurrentLBCMax.setStatus("current")
if mibBuilder.loadTexts:
    cooCurrentLBCMax.setUnits("1/10 percent")
_CooCurrentTXPowerMin_Type = CoiOpticalPower
_CooCurrentTXPowerMin_Object = MibTableColumn
cooCurrentTXPowerMin = _CooCurrentTXPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 2, 1, 5),
    _CooCurrentTXPowerMin_Type()
)
cooCurrentTXPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooCurrentTXPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    cooCurrentTXPowerMin.setUnits("1/100 dBm")
_CooCurrentRXPowerMin_Type = CoiOpticalPower
_CooCurrentRXPowerMin_Object = MibTableColumn
cooCurrentRXPowerMin = _CooCurrentRXPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 2, 1, 6),
    _CooCurrentRXPowerMin_Type()
)
cooCurrentRXPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooCurrentRXPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    cooCurrentRXPowerMin.setUnits("1/100 dBm")


class _CooCurrentLBCMin_Type(Unsigned32):
    """Custom type cooCurrentLBCMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CooCurrentLBCMin_Type.__name__ = "Unsigned32"
_CooCurrentLBCMin_Object = MibTableColumn
cooCurrentLBCMin = _CooCurrentLBCMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 2, 1, 7),
    _CooCurrentLBCMin_Type()
)
cooCurrentLBCMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooCurrentLBCMin.setStatus("current")
if mibBuilder.loadTexts:
    cooCurrentLBCMin.setUnits("1/10 percent")
_CooCurrentTXPowerAvg_Type = CoiOpticalPower
_CooCurrentTXPowerAvg_Object = MibTableColumn
cooCurrentTXPowerAvg = _CooCurrentTXPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 2, 1, 8),
    _CooCurrentTXPowerAvg_Type()
)
cooCurrentTXPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooCurrentTXPowerAvg.setStatus("current")
if mibBuilder.loadTexts:
    cooCurrentTXPowerAvg.setUnits("1/100 dBm")
_CooCurrentRXPowerAvg_Type = CoiOpticalPower
_CooCurrentRXPowerAvg_Object = MibTableColumn
cooCurrentRXPowerAvg = _CooCurrentRXPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 2, 1, 9),
    _CooCurrentRXPowerAvg_Type()
)
cooCurrentRXPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooCurrentRXPowerAvg.setStatus("current")
if mibBuilder.loadTexts:
    cooCurrentRXPowerAvg.setUnits("1/100 dBm")


class _CooCurrentLBCAvg_Type(Unsigned32):
    """Custom type cooCurrentLBCAvg based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CooCurrentLBCAvg_Type.__name__ = "Unsigned32"
_CooCurrentLBCAvg_Object = MibTableColumn
cooCurrentLBCAvg = _CooCurrentLBCAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 2, 1, 10),
    _CooCurrentLBCAvg_Type()
)
cooCurrentLBCAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooCurrentLBCAvg.setStatus("current")
if mibBuilder.loadTexts:
    cooCurrentLBCAvg.setUnits("1/10 percent")
_CooCurrentTimestamp_Type = OctetString
_CooCurrentTimestamp_Object = MibTableColumn
cooCurrentTimestamp = _CooCurrentTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 2, 1, 11),
    _CooCurrentTimestamp_Type()
)
cooCurrentTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooCurrentTimestamp.setStatus("current")
_CooCurrentAmpliGainMin_Type = Integer32
_CooCurrentAmpliGainMin_Object = MibTableColumn
cooCurrentAmpliGainMin = _CooCurrentAmpliGainMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 2, 1, 12),
    _CooCurrentAmpliGainMin_Type()
)
cooCurrentAmpliGainMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooCurrentAmpliGainMin.setStatus("current")
if mibBuilder.loadTexts:
    cooCurrentAmpliGainMin.setUnits("1/100 dB")
_CooCurrentAmpliGainMax_Type = Integer32
_CooCurrentAmpliGainMax_Object = MibTableColumn
cooCurrentAmpliGainMax = _CooCurrentAmpliGainMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 2, 1, 13),
    _CooCurrentAmpliGainMax_Type()
)
cooCurrentAmpliGainMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooCurrentAmpliGainMax.setStatus("current")
if mibBuilder.loadTexts:
    cooCurrentAmpliGainMax.setUnits("1/100 dB")
_CooCurrentAmpliGainAvg_Type = Integer32
_CooCurrentAmpliGainAvg_Object = MibTableColumn
cooCurrentAmpliGainAvg = _CooCurrentAmpliGainAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 2, 1, 14),
    _CooCurrentAmpliGainAvg_Type()
)
cooCurrentAmpliGainAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooCurrentAmpliGainAvg.setStatus("current")
if mibBuilder.loadTexts:
    cooCurrentAmpliGainAvg.setUnits("1/100 dB")
_CooCurrentAmpliGainTiltMin_Type = Integer32
_CooCurrentAmpliGainTiltMin_Object = MibTableColumn
cooCurrentAmpliGainTiltMin = _CooCurrentAmpliGainTiltMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 2, 1, 15),
    _CooCurrentAmpliGainTiltMin_Type()
)
cooCurrentAmpliGainTiltMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooCurrentAmpliGainTiltMin.setStatus("current")
if mibBuilder.loadTexts:
    cooCurrentAmpliGainTiltMin.setUnits("1/100 dB")
_CooCurrentAmpliGainTiltMax_Type = Integer32
_CooCurrentAmpliGainTiltMax_Object = MibTableColumn
cooCurrentAmpliGainTiltMax = _CooCurrentAmpliGainTiltMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 2, 1, 16),
    _CooCurrentAmpliGainTiltMax_Type()
)
cooCurrentAmpliGainTiltMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooCurrentAmpliGainTiltMax.setStatus("current")
if mibBuilder.loadTexts:
    cooCurrentAmpliGainTiltMax.setUnits("1/100 dB")
_CooCurrentAmpliGainTiltAvg_Type = Integer32
_CooCurrentAmpliGainTiltAvg_Object = MibTableColumn
cooCurrentAmpliGainTiltAvg = _CooCurrentAmpliGainTiltAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 2, 1, 17),
    _CooCurrentAmpliGainTiltAvg_Type()
)
cooCurrentAmpliGainTiltAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooCurrentAmpliGainTiltAvg.setStatus("current")
if mibBuilder.loadTexts:
    cooCurrentAmpliGainTiltAvg.setUnits("1/100 dB")
_CooOtsIntervalTable_Object = MibTable
cooOtsIntervalTable = _CooOtsIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cooOtsIntervalTable.setStatus("current")
_CooOtsIntervalEntry_Object = MibTableRow
cooOtsIntervalEntry = _CooOtsIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 3, 1)
)
cooOtsIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-OPTICAL-OTS-MIB", "cooIntervalType"),
    (0, "CISCO-OPTICAL-OTS-MIB", "cooIntervalNum"),
)
if mibBuilder.loadTexts:
    cooOtsIntervalEntry.setStatus("current")
_CooIntervalType_Type = CoiIntervalType
_CooIntervalType_Object = MibTableColumn
cooIntervalType = _CooIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 3, 1, 1),
    _CooIntervalType_Type()
)
cooIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cooIntervalType.setStatus("current")


class _CooIntervalNum_Type(Unsigned32):
    """Custom type cooIntervalNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_CooIntervalNum_Type.__name__ = "Unsigned32"
_CooIntervalNum_Object = MibTableColumn
cooIntervalNum = _CooIntervalNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 3, 1, 2),
    _CooIntervalNum_Type()
)
cooIntervalNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cooIntervalNum.setStatus("current")
_CooIntervalTXPowerMax_Type = CoiOpticalPower
_CooIntervalTXPowerMax_Object = MibTableColumn
cooIntervalTXPowerMax = _CooIntervalTXPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 3, 1, 3),
    _CooIntervalTXPowerMax_Type()
)
cooIntervalTXPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooIntervalTXPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    cooIntervalTXPowerMax.setUnits("1/100 dBm")
_CooIntervalRXPowerMax_Type = CoiOpticalPower
_CooIntervalRXPowerMax_Object = MibTableColumn
cooIntervalRXPowerMax = _CooIntervalRXPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 3, 1, 4),
    _CooIntervalRXPowerMax_Type()
)
cooIntervalRXPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooIntervalRXPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    cooIntervalRXPowerMax.setUnits("1/100 dBm")


class _CooIntervalLBCMax_Type(Unsigned32):
    """Custom type cooIntervalLBCMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CooIntervalLBCMax_Type.__name__ = "Unsigned32"
_CooIntervalLBCMax_Object = MibTableColumn
cooIntervalLBCMax = _CooIntervalLBCMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 3, 1, 5),
    _CooIntervalLBCMax_Type()
)
cooIntervalLBCMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooIntervalLBCMax.setStatus("current")
if mibBuilder.loadTexts:
    cooIntervalLBCMax.setUnits("1/10 percent")
_CooIntervalTXPowerMin_Type = CoiOpticalPower
_CooIntervalTXPowerMin_Object = MibTableColumn
cooIntervalTXPowerMin = _CooIntervalTXPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 3, 1, 6),
    _CooIntervalTXPowerMin_Type()
)
cooIntervalTXPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooIntervalTXPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    cooIntervalTXPowerMin.setUnits("1/100 dBm")
_CooIntervalRXPowerMin_Type = CoiOpticalPower
_CooIntervalRXPowerMin_Object = MibTableColumn
cooIntervalRXPowerMin = _CooIntervalRXPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 3, 1, 7),
    _CooIntervalRXPowerMin_Type()
)
cooIntervalRXPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooIntervalRXPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    cooIntervalRXPowerMin.setUnits("1/100 dBm")


class _CooIntervalLBCMin_Type(Unsigned32):
    """Custom type cooIntervalLBCMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CooIntervalLBCMin_Type.__name__ = "Unsigned32"
_CooIntervalLBCMin_Object = MibTableColumn
cooIntervalLBCMin = _CooIntervalLBCMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 3, 1, 8),
    _CooIntervalLBCMin_Type()
)
cooIntervalLBCMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooIntervalLBCMin.setStatus("current")
if mibBuilder.loadTexts:
    cooIntervalLBCMin.setUnits("1/10 percent")
_CooIntervalTXPowerAvg_Type = CoiOpticalPower
_CooIntervalTXPowerAvg_Object = MibTableColumn
cooIntervalTXPowerAvg = _CooIntervalTXPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 3, 1, 9),
    _CooIntervalTXPowerAvg_Type()
)
cooIntervalTXPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooIntervalTXPowerAvg.setStatus("current")
if mibBuilder.loadTexts:
    cooIntervalTXPowerAvg.setUnits("1/100 dBm")
_CooIntervalRXPowerAvg_Type = CoiOpticalPower
_CooIntervalRXPowerAvg_Object = MibTableColumn
cooIntervalRXPowerAvg = _CooIntervalRXPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 3, 1, 10),
    _CooIntervalRXPowerAvg_Type()
)
cooIntervalRXPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooIntervalRXPowerAvg.setStatus("current")
if mibBuilder.loadTexts:
    cooIntervalRXPowerAvg.setUnits("1/100 dBm")


class _CooIntervalLBCAvg_Type(Unsigned32):
    """Custom type cooIntervalLBCAvg based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CooIntervalLBCAvg_Type.__name__ = "Unsigned32"
_CooIntervalLBCAvg_Object = MibTableColumn
cooIntervalLBCAvg = _CooIntervalLBCAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 3, 1, 11),
    _CooIntervalLBCAvg_Type()
)
cooIntervalLBCAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooIntervalLBCAvg.setStatus("current")
if mibBuilder.loadTexts:
    cooIntervalLBCAvg.setUnits("1/10 percent")
_CooIntervalTimestamp_Type = OctetString
_CooIntervalTimestamp_Object = MibTableColumn
cooIntervalTimestamp = _CooIntervalTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 3, 1, 12),
    _CooIntervalTimestamp_Type()
)
cooIntervalTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooIntervalTimestamp.setStatus("current")
_CooIntervalAmpliGainMin_Type = Integer32
_CooIntervalAmpliGainMin_Object = MibTableColumn
cooIntervalAmpliGainMin = _CooIntervalAmpliGainMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 3, 1, 13),
    _CooIntervalAmpliGainMin_Type()
)
cooIntervalAmpliGainMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooIntervalAmpliGainMin.setStatus("current")
if mibBuilder.loadTexts:
    cooIntervalAmpliGainMin.setUnits("1/100 dB")
_CooIntervalAmpliGainMax_Type = Integer32
_CooIntervalAmpliGainMax_Object = MibTableColumn
cooIntervalAmpliGainMax = _CooIntervalAmpliGainMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 3, 1, 14),
    _CooIntervalAmpliGainMax_Type()
)
cooIntervalAmpliGainMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooIntervalAmpliGainMax.setStatus("current")
if mibBuilder.loadTexts:
    cooIntervalAmpliGainMax.setUnits("1/100 dB")
_CooIntervalAmpliGainAvg_Type = Integer32
_CooIntervalAmpliGainAvg_Object = MibTableColumn
cooIntervalAmpliGainAvg = _CooIntervalAmpliGainAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 3, 1, 15),
    _CooIntervalAmpliGainAvg_Type()
)
cooIntervalAmpliGainAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooIntervalAmpliGainAvg.setStatus("current")
_CooIntervalAmpliGainTiltMin_Type = Integer32
_CooIntervalAmpliGainTiltMin_Object = MibTableColumn
cooIntervalAmpliGainTiltMin = _CooIntervalAmpliGainTiltMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 3, 1, 16),
    _CooIntervalAmpliGainTiltMin_Type()
)
cooIntervalAmpliGainTiltMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooIntervalAmpliGainTiltMin.setStatus("current")
if mibBuilder.loadTexts:
    cooIntervalAmpliGainTiltMin.setUnits("1/100 dB")
_CooIntervalAmpliGainTiltMax_Type = Integer32
_CooIntervalAmpliGainTiltMax_Object = MibTableColumn
cooIntervalAmpliGainTiltMax = _CooIntervalAmpliGainTiltMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 3, 1, 17),
    _CooIntervalAmpliGainTiltMax_Type()
)
cooIntervalAmpliGainTiltMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooIntervalAmpliGainTiltMax.setStatus("current")
if mibBuilder.loadTexts:
    cooIntervalAmpliGainTiltMax.setUnits("1/100 dB")
_CooIntervalAmpliGainTiltAvg_Type = Integer32
_CooIntervalAmpliGainTiltAvg_Object = MibTableColumn
cooIntervalAmpliGainTiltAvg = _CooIntervalAmpliGainTiltAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 2, 3, 1, 18),
    _CooIntervalAmpliGainTiltAvg_Type()
)
cooIntervalAmpliGainTiltAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cooIntervalAmpliGainTiltAvg.setStatus("current")
if mibBuilder.loadTexts:
    cooIntervalAmpliGainTiltAvg.setUnits("1/100 dB")
_CooOtsEquipmentAlarmGroup_ObjectIdentity = ObjectIdentity
cooOtsEquipmentAlarmGroup = _CooOtsEquipmentAlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 5)
)
_CooOtsAlarmLocation_Type = SnmpAdminString
_CooOtsAlarmLocation_Object = MibScalar
cooOtsAlarmLocation = _CooOtsAlarmLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 5, 1),
    _CooOtsAlarmLocation_Type()
)
cooOtsAlarmLocation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cooOtsAlarmLocation.setStatus("current")
_CooOtsAlarmType_Type = CoiOptAlarmType
_CooOtsAlarmType_Object = MibScalar
cooOtsAlarmType = _CooOtsAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 5, 2),
    _CooOtsAlarmType_Type()
)
cooOtsAlarmType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cooOtsAlarmType.setStatus("current")
_CooOtsAlarmTimeStamp_Type = TimeStamp
_CooOtsAlarmTimeStamp_Object = MibScalar
cooOtsAlarmTimeStamp = _CooOtsAlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 5, 3),
    _CooOtsAlarmTimeStamp_Type()
)
cooOtsAlarmTimeStamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cooOtsAlarmTimeStamp.setStatus("current")
_CooOtsAlarmName_Type = SnmpAdminString
_CooOtsAlarmName_Object = MibScalar
cooOtsAlarmName = _CooOtsAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 5, 4),
    _CooOtsAlarmName_Type()
)
cooOtsAlarmName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cooOtsAlarmName.setStatus("current")
_CooOtsAlarmAdditionalInfo_Type = SnmpAdminString
_CooOtsAlarmAdditionalInfo_Object = MibScalar
cooOtsAlarmAdditionalInfo = _CooOtsAlarmAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 5, 5),
    _CooOtsAlarmAdditionalInfo_Type()
)
cooOtsAlarmAdditionalInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cooOtsAlarmAdditionalInfo.setStatus("current")
_CooOtsAlarmSeverity_Type = CoiOptAlarmSeverity
_CooOtsAlarmSeverity_Object = MibScalar
cooOtsAlarmSeverity = _CooOtsAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 5, 6),
    _CooOtsAlarmSeverity_Type()
)
cooOtsAlarmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cooOtsAlarmSeverity.setStatus("current")
_CooOtsAlarmStatus_Type = CoiOptAlarmStatus
_CooOtsAlarmStatus_Object = MibScalar
cooOtsAlarmStatus = _CooOtsAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 5, 7),
    _CooOtsAlarmStatus_Type()
)
cooOtsAlarmStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cooOtsAlarmStatus.setStatus("current")
_CooOtsAlarmServiceAffecting_Type = CoiOptAlarmServiceAffecting
_CooOtsAlarmServiceAffecting_Object = MibScalar
cooOtsAlarmServiceAffecting = _CooOtsAlarmServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 1, 5, 8),
    _CooOtsAlarmServiceAffecting_Type()
)
cooOtsAlarmServiceAffecting.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cooOtsAlarmServiceAffecting.setStatus("current")
_CiscoOpticalOtsMIBConformance_ObjectIdentity = ObjectIdentity
ciscoOpticalOtsMIBConformance = _CiscoOpticalOtsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 2)
)
_CiscoOpticalOtsMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoOpticalOtsMIBCompliances = _CiscoOpticalOtsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 2, 1)
)
_CiscoOpticalOtsMIBGroups_ObjectIdentity = ObjectIdentity
ciscoOpticalOtsMIBGroups = _CiscoOpticalOtsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 2, 2)
)

# Managed Objects groups

cooOtsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 2, 2, 1)
)
cooOtsGroup.setObjects(
      *(("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerPortType"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerLaserStatus"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerRXPower"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerTXPower"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerAmpliGain"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerAmpliTilt"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerTotalRXPower"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerTotalTXPower"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerRXVoaAttenuation"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerTXVoaAttenuation"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerRXLowThreshold"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerTXLowThreshold"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerAmpliChannelPwr"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerChannelPwrMaxDelta"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerAmpliControlMode"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerAmpliGainRange"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerAmpliSafetyCtrlMode"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerOsri"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerProtectionPortRole"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerState"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerTranspAdminState"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerAlarmState"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshTXPowerMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshRXPowerMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshLBCMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshTXPowerMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshRXPowerMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshLBCMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentTXPowerMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentRXPowerMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentLBCMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentTXPowerMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentRXPowerMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentLBCMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentTXPowerAvg"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentRXPowerAvg"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentLBCAvg"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalTXPowerMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalRXPowerMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalLBCMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalTXPowerMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalRXPowerMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalLBCMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalTXPowerAvg"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalRXPowerAvg"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalLBCAvg"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerRXSpanLoss"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerTXSpanLoss"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerRXEnabled"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerTXEnabled"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshAmpliGainMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshAmpliGainMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshAmpliGainEnableMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshAmpliGainEnableMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshAmpliGainTiltMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshAmpliGainTiltMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshAmpliGainTiltEnableMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshAmpliGainTiltEnableMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentAmpliGainMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentAmpliGainMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentAmpliGainAvg"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentAmpliGainTiltMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentAmpliGainTiltMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentAmpliGainTiltAvg"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalAmpliGainMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalAmpliGainMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalAmpliGainAvg"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalAmpliGainTiltMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalAmpliGainTiltMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalAmpliGainTiltAvg"))
)
if mibBuilder.loadTexts:
    cooOtsGroup.setStatus("current")

cooOtsOchGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 2, 2, 2)
)
cooOtsOchGroup.setObjects(
      *(("CISCO-OPTICAL-OTS-MIB", "cooOtsOchControllerPortType"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsOchControllerLaserStatus"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsOchControllerRXPower"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsOchControllerTXPower"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsOchControllerRXLowThreshold"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsOchControllerTXLowThreshold"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsOchControllerWavelength"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsOchControllerFrequency"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsOchControllerChannelNumber"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsOchControllerState"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsOchControllerTranspAdminState"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsOchControllerAlarmState"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshTXPowerMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshRXPowerMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshLBCMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshTXPowerMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshRXPowerMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshLBCMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentTXPowerMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentRXPowerMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentLBCMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentTXPowerMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentRXPowerMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentLBCMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentTXPowerAvg"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentRXPowerAvg"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentLBCAvg"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalTXPowerMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalRXPowerMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalLBCMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalTXPowerMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalRXPowerMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalLBCMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalTXPowerAvg"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalRXPowerAvg"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalLBCAvg"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsOchControllerWidth"))
)
if mibBuilder.loadTexts:
    cooOtsOchGroup.setStatus("current")

cooOtsControllerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 2, 2, 3)
)
cooOtsControllerGroup.setObjects(
      *(("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerAmpliGain"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerAmpliTilt"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerRXVoaAttenuation"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerTXVoaAttenuation"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerRXLowThreshold"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerTXLowThreshold"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerAmpliChannelPwr"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerChannelPwrMaxDelta"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerAmpliControlMode"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerAmpliGainRange"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerAmpliSafetyCtrlMode"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerOsri"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerRXEnabled"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerTXEnabled"))
)
if mibBuilder.loadTexts:
    cooOtsControllerGroup.setStatus("current")

cooOtsOchControllerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 2, 2, 4)
)
cooOtsOchControllerGroup.setObjects(
      *(("CISCO-OPTICAL-OTS-MIB", "cooOtsOchControllerRXLowThreshold"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsOchControllerTXLowThreshold"))
)
if mibBuilder.loadTexts:
    cooOtsOchControllerGroup.setStatus("current")

cooOtsThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 2, 2, 5)
)
cooOtsThresholdGroup.setObjects(
      *(("CISCO-OPTICAL-OTS-MIB", "cooThreshTXPowerMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshRXPowerMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshLBCMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshTXPowerMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshRXPowerMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshLBCMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshTXPowerEnableMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshRXPowerEnableMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshLBCEnableMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshTXPowerEnableMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshRXPowerEnableMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshLBCEnableMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshAmpliGainMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshAmpliGainMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshAmpliGainEnableMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshAmpliGainEnableMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshAmpliGainTiltMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshAmpliGainTiltMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshAmpliGainTiltEnableMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooThreshAmpliGainTiltEnableMin"))
)
if mibBuilder.loadTexts:
    cooOtsThresholdGroup.setStatus("current")

cooOtsCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 2, 2, 6)
)
cooOtsCurrentGroup.setObjects(
      *(("CISCO-OPTICAL-OTS-MIB", "cooCurrentTXPowerMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentRXPowerMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentLBCMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentTXPowerMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentRXPowerMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentLBCMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentTXPowerAvg"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentRXPowerAvg"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentLBCAvg"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentTimestamp"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentAmpliGainMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentAmpliGainMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentAmpliGainAvg"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentAmpliGainTiltMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentAmpliGainTiltMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooCurrentAmpliGainTiltAvg"))
)
if mibBuilder.loadTexts:
    cooOtsCurrentGroup.setStatus("current")

cooOtsIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 2, 2, 7)
)
cooOtsIntervalGroup.setObjects(
      *(("CISCO-OPTICAL-OTS-MIB", "cooIntervalTXPowerMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalRXPowerMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalLBCMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalTXPowerMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalRXPowerMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalLBCMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalTXPowerAvg"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalRXPowerAvg"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalLBCAvg"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalTimestamp"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalAmpliGainMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalAmpliGainMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalAmpliGainAvg"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalAmpliGainTiltMin"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalAmpliGainTiltMax"),
        ("CISCO-OPTICAL-OTS-MIB", "cooIntervalAmpliGainTiltAvg"))
)
if mibBuilder.loadTexts:
    cooOtsIntervalGroup.setStatus("current")

cooOtsNotifEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 2, 2, 8)
)
cooOtsNotifEnableGroup.setObjects(
    ("CISCO-OPTICAL-OTS-MIB", "cooOtsNotifEnabled")
)
if mibBuilder.loadTexts:
    cooOtsNotifEnableGroup.setStatus("current")

cooOtsEquipmentAlarmInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 2, 2, 11)
)
cooOtsEquipmentAlarmInfoGroup.setObjects(
      *(("CISCO-OPTICAL-OTS-MIB", "cooOtsAlarmLocation"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsAlarmType"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsAlarmTimeStamp"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsAlarmName"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsAlarmAdditionalInfo"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsAlarmSeverity"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsAlarmStatus"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsAlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    cooOtsEquipmentAlarmInfoGroup.setStatus("current")

cooOtsPowerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 2, 2, 12)
)
cooOtsPowerGroup.setObjects(
      *(("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerTotalRXPower"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerTotalTXPower"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerRXPower"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerTXPower"))
)
if mibBuilder.loadTexts:
    cooOtsPowerGroup.setStatus("current")

cooOtsOchNotifEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 2, 2, 13)
)
cooOtsOchNotifEnableGroup.setObjects(
    ("CISCO-OPTICAL-OTS-MIB", "cooOtsOchNotifEnabled")
)
if mibBuilder.loadTexts:
    cooOtsOchNotifEnableGroup.setStatus("current")


# Notification objects

cooOtsStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 0, 1)
)
cooOtsStatusChange.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerPortType"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerAlarmState"))
)
if mibBuilder.loadTexts:
    cooOtsStatusChange.setStatus(
        "current"
    )

cooOtsOchStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 0, 2)
)
cooOtsOchStatusChange.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsOchControllerPortType"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsOchControllerAlarmState"))
)
if mibBuilder.loadTexts:
    cooOtsOchStatusChange.setStatus(
        "current"
    )

cooOtsEquipmentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 0, 3)
)
cooOtsEquipmentAlarm.setObjects(
      *(("CISCO-OPTICAL-OTS-MIB", "cooOtsAlarmLocation"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsAlarmType"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsAlarmTimeStamp"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsAlarmName"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsAlarmAdditionalInfo"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsAlarmSeverity"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsAlarmStatus"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsAlarmServiceAffecting"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    cooOtsEquipmentAlarm.setStatus(
        "current"
    )


# Notifications groups

cooOtsNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 2, 2, 9)
)
cooOtsNotifGroup.setObjects(
      *(("CISCO-OPTICAL-OTS-MIB", "cooOtsStatusChange"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsEquipmentAlarm"))
)
if mibBuilder.loadTexts:
    cooOtsNotifGroup.setStatus(
        "current"
    )

cooOtsOchNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 2, 2, 10)
)
cooOtsOchNotifGroup.setObjects(
      *(("CISCO-OPTICAL-OTS-MIB", "cooOtsOchStatusChange"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsEquipmentAlarm"))
)
if mibBuilder.loadTexts:
    cooOtsOchNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoOpticalOtsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 834, 2, 1, 1)
)
ciscoOpticalOtsMIBCompliance.setObjects(
      *(("CISCO-OPTICAL-OTS-MIB", "cooOtsGroup"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsOchGroup"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsControllerGroup"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsOchControllerGroup"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsThresholdGroup"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsCurrentGroup"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsIntervalGroup"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsNotifEnableGroup"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsNotifGroup"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsOchNotifGroup"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsEquipmentAlarmInfoGroup"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsPowerGroup"),
        ("CISCO-OPTICAL-OTS-MIB", "cooOtsOchNotifEnableGroup"))
)
if mibBuilder.loadTexts:
    ciscoOpticalOtsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-OPTICAL-OTS-MIB",
    **{"CiscoOpticalOtsPortType": CiscoOpticalOtsPortType,
       "CiscoOpticalOtsGainInDb": CiscoOpticalOtsGainInDb,
       "CiscoOpticalOtsTiltInDb": CiscoOpticalOtsTiltInDb,
       "CiscoOpticalOtsVoaAttenInDb": CiscoOpticalOtsVoaAttenInDb,
       "CiscoOpticalOtsLaserStatus": CiscoOpticalOtsLaserStatus,
       "CiscoOpticalOtsAmpliControlMode": CiscoOpticalOtsAmpliControlMode,
       "CiscoOpticalOtsAmpliGainRange": CiscoOpticalOtsAmpliGainRange,
       "CiscoOpticalOtsAmpliSafetyCtrlMode": CiscoOpticalOtsAmpliSafetyCtrlMode,
       "CiscoOpticalOtsOsri": CiscoOpticalOtsOsri,
       "CiscoOpticalOtsProtectionPortRole": CiscoOpticalOtsProtectionPortRole,
       "CiscoOpticalOtsState": CiscoOpticalOtsState,
       "CiscoOpticalOtsTranspAdminState": CiscoOpticalOtsTranspAdminState,
       "ciscoOpticalOtsMIB": ciscoOpticalOtsMIB,
       "ciscoOpticalOtsMIBNotifs": ciscoOpticalOtsMIBNotifs,
       "cooOtsStatusChange": cooOtsStatusChange,
       "cooOtsOchStatusChange": cooOtsOchStatusChange,
       "cooOtsEquipmentAlarm": cooOtsEquipmentAlarm,
       "ciscoOpticalOtsMIBObjects": ciscoOpticalOtsMIBObjects,
       "cooOtsController": cooOtsController,
       "cooOtsNotifEnabled": cooOtsNotifEnabled,
       "cooOtsControllerTable": cooOtsControllerTable,
       "cooOtsControllerEntry": cooOtsControllerEntry,
       "cooOtsControllerPortType": cooOtsControllerPortType,
       "cooOtsControllerLaserStatus": cooOtsControllerLaserStatus,
       "cooOtsControllerRXPower": cooOtsControllerRXPower,
       "cooOtsControllerTXPower": cooOtsControllerTXPower,
       "cooOtsControllerAmpliGain": cooOtsControllerAmpliGain,
       "cooOtsControllerAmpliTilt": cooOtsControllerAmpliTilt,
       "cooOtsControllerTotalRXPower": cooOtsControllerTotalRXPower,
       "cooOtsControllerTotalTXPower": cooOtsControllerTotalTXPower,
       "cooOtsControllerRXVoaAttenuation": cooOtsControllerRXVoaAttenuation,
       "cooOtsControllerTXVoaAttenuation": cooOtsControllerTXVoaAttenuation,
       "cooOtsControllerRXLowThreshold": cooOtsControllerRXLowThreshold,
       "cooOtsControllerTXLowThreshold": cooOtsControllerTXLowThreshold,
       "cooOtsControllerAmpliChannelPwr": cooOtsControllerAmpliChannelPwr,
       "cooOtsControllerChannelPwrMaxDelta": cooOtsControllerChannelPwrMaxDelta,
       "cooOtsControllerAmpliControlMode": cooOtsControllerAmpliControlMode,
       "cooOtsControllerAmpliGainRange": cooOtsControllerAmpliGainRange,
       "cooOtsControllerAmpliSafetyCtrlMode": cooOtsControllerAmpliSafetyCtrlMode,
       "cooOtsControllerOsri": cooOtsControllerOsri,
       "cooOtsControllerProtectionPortRole": cooOtsControllerProtectionPortRole,
       "cooOtsControllerState": cooOtsControllerState,
       "cooOtsControllerTranspAdminState": cooOtsControllerTranspAdminState,
       "cooOtsControllerAlarmState": cooOtsControllerAlarmState,
       "cooOtsControllerRXSpanLoss": cooOtsControllerRXSpanLoss,
       "cooOtsControllerTXSpanLoss": cooOtsControllerTXSpanLoss,
       "cooOtsControllerRXEnabled": cooOtsControllerRXEnabled,
       "cooOtsControllerTXEnabled": cooOtsControllerTXEnabled,
       "cooOtsOchControllerTable": cooOtsOchControllerTable,
       "cooOtsOchControllerEntry": cooOtsOchControllerEntry,
       "cooOtsOchControllerPortType": cooOtsOchControllerPortType,
       "cooOtsOchControllerLaserStatus": cooOtsOchControllerLaserStatus,
       "cooOtsOchControllerRXPower": cooOtsOchControllerRXPower,
       "cooOtsOchControllerTXPower": cooOtsOchControllerTXPower,
       "cooOtsOchControllerRXLowThreshold": cooOtsOchControllerRXLowThreshold,
       "cooOtsOchControllerTXLowThreshold": cooOtsOchControllerTXLowThreshold,
       "cooOtsOchControllerWavelength": cooOtsOchControllerWavelength,
       "cooOtsOchControllerFrequency": cooOtsOchControllerFrequency,
       "cooOtsOchControllerChannelNumber": cooOtsOchControllerChannelNumber,
       "cooOtsOchControllerState": cooOtsOchControllerState,
       "cooOtsOchControllerTranspAdminState": cooOtsOchControllerTranspAdminState,
       "cooOtsOchControllerAlarmState": cooOtsOchControllerAlarmState,
       "cooOtsOchControllerWidth": cooOtsOchControllerWidth,
       "cooOtsOchNotifEnabled": cooOtsOchNotifEnabled,
       "cooOtsPerformanceMonitoring": cooOtsPerformanceMonitoring,
       "cooOtsThresholdTable": cooOtsThresholdTable,
       "cooOtsThresholdEntry": cooOtsThresholdEntry,
       "cooThreshIntervalType": cooThreshIntervalType,
       "cooThreshTXPowerMin": cooThreshTXPowerMin,
       "cooThreshRXPowerMin": cooThreshRXPowerMin,
       "cooThreshLBCMin": cooThreshLBCMin,
       "cooThreshTXPowerMax": cooThreshTXPowerMax,
       "cooThreshRXPowerMax": cooThreshRXPowerMax,
       "cooThreshLBCMax": cooThreshLBCMax,
       "cooThreshTXPowerEnableMin": cooThreshTXPowerEnableMin,
       "cooThreshRXPowerEnableMin": cooThreshRXPowerEnableMin,
       "cooThreshLBCEnableMin": cooThreshLBCEnableMin,
       "cooThreshTXPowerEnableMax": cooThreshTXPowerEnableMax,
       "cooThreshRXPowerEnableMax": cooThreshRXPowerEnableMax,
       "cooThreshLBCEnableMax": cooThreshLBCEnableMax,
       "cooThreshAmpliGainMin": cooThreshAmpliGainMin,
       "cooThreshAmpliGainMax": cooThreshAmpliGainMax,
       "cooThreshAmpliGainEnableMax": cooThreshAmpliGainEnableMax,
       "cooThreshAmpliGainEnableMin": cooThreshAmpliGainEnableMin,
       "cooThreshAmpliGainTiltMin": cooThreshAmpliGainTiltMin,
       "cooThreshAmpliGainTiltMax": cooThreshAmpliGainTiltMax,
       "cooThreshAmpliGainTiltEnableMax": cooThreshAmpliGainTiltEnableMax,
       "cooThreshAmpliGainTiltEnableMin": cooThreshAmpliGainTiltEnableMin,
       "cooOtsCurrentTable": cooOtsCurrentTable,
       "cooOtsCurrentEntry": cooOtsCurrentEntry,
       "cooCurrentIntervalType": cooCurrentIntervalType,
       "cooCurrentTXPowerMax": cooCurrentTXPowerMax,
       "cooCurrentRXPowerMax": cooCurrentRXPowerMax,
       "cooCurrentLBCMax": cooCurrentLBCMax,
       "cooCurrentTXPowerMin": cooCurrentTXPowerMin,
       "cooCurrentRXPowerMin": cooCurrentRXPowerMin,
       "cooCurrentLBCMin": cooCurrentLBCMin,
       "cooCurrentTXPowerAvg": cooCurrentTXPowerAvg,
       "cooCurrentRXPowerAvg": cooCurrentRXPowerAvg,
       "cooCurrentLBCAvg": cooCurrentLBCAvg,
       "cooCurrentTimestamp": cooCurrentTimestamp,
       "cooCurrentAmpliGainMin": cooCurrentAmpliGainMin,
       "cooCurrentAmpliGainMax": cooCurrentAmpliGainMax,
       "cooCurrentAmpliGainAvg": cooCurrentAmpliGainAvg,
       "cooCurrentAmpliGainTiltMin": cooCurrentAmpliGainTiltMin,
       "cooCurrentAmpliGainTiltMax": cooCurrentAmpliGainTiltMax,
       "cooCurrentAmpliGainTiltAvg": cooCurrentAmpliGainTiltAvg,
       "cooOtsIntervalTable": cooOtsIntervalTable,
       "cooOtsIntervalEntry": cooOtsIntervalEntry,
       "cooIntervalType": cooIntervalType,
       "cooIntervalNum": cooIntervalNum,
       "cooIntervalTXPowerMax": cooIntervalTXPowerMax,
       "cooIntervalRXPowerMax": cooIntervalRXPowerMax,
       "cooIntervalLBCMax": cooIntervalLBCMax,
       "cooIntervalTXPowerMin": cooIntervalTXPowerMin,
       "cooIntervalRXPowerMin": cooIntervalRXPowerMin,
       "cooIntervalLBCMin": cooIntervalLBCMin,
       "cooIntervalTXPowerAvg": cooIntervalTXPowerAvg,
       "cooIntervalRXPowerAvg": cooIntervalRXPowerAvg,
       "cooIntervalLBCAvg": cooIntervalLBCAvg,
       "cooIntervalTimestamp": cooIntervalTimestamp,
       "cooIntervalAmpliGainMin": cooIntervalAmpliGainMin,
       "cooIntervalAmpliGainMax": cooIntervalAmpliGainMax,
       "cooIntervalAmpliGainAvg": cooIntervalAmpliGainAvg,
       "cooIntervalAmpliGainTiltMin": cooIntervalAmpliGainTiltMin,
       "cooIntervalAmpliGainTiltMax": cooIntervalAmpliGainTiltMax,
       "cooIntervalAmpliGainTiltAvg": cooIntervalAmpliGainTiltAvg,
       "cooOtsEquipmentAlarmGroup": cooOtsEquipmentAlarmGroup,
       "cooOtsAlarmLocation": cooOtsAlarmLocation,
       "cooOtsAlarmType": cooOtsAlarmType,
       "cooOtsAlarmTimeStamp": cooOtsAlarmTimeStamp,
       "cooOtsAlarmName": cooOtsAlarmName,
       "cooOtsAlarmAdditionalInfo": cooOtsAlarmAdditionalInfo,
       "cooOtsAlarmSeverity": cooOtsAlarmSeverity,
       "cooOtsAlarmStatus": cooOtsAlarmStatus,
       "cooOtsAlarmServiceAffecting": cooOtsAlarmServiceAffecting,
       "ciscoOpticalOtsMIBConformance": ciscoOpticalOtsMIBConformance,
       "ciscoOpticalOtsMIBCompliances": ciscoOpticalOtsMIBCompliances,
       "ciscoOpticalOtsMIBCompliance": ciscoOpticalOtsMIBCompliance,
       "ciscoOpticalOtsMIBGroups": ciscoOpticalOtsMIBGroups,
       "cooOtsGroup": cooOtsGroup,
       "cooOtsOchGroup": cooOtsOchGroup,
       "cooOtsControllerGroup": cooOtsControllerGroup,
       "cooOtsOchControllerGroup": cooOtsOchControllerGroup,
       "cooOtsThresholdGroup": cooOtsThresholdGroup,
       "cooOtsCurrentGroup": cooOtsCurrentGroup,
       "cooOtsIntervalGroup": cooOtsIntervalGroup,
       "cooOtsNotifEnableGroup": cooOtsNotifEnableGroup,
       "cooOtsNotifGroup": cooOtsNotifGroup,
       "cooOtsOchNotifGroup": cooOtsOchNotifGroup,
       "cooOtsEquipmentAlarmInfoGroup": cooOtsEquipmentAlarmInfoGroup,
       "cooOtsPowerGroup": cooOtsPowerGroup,
       "cooOtsOchNotifEnableGroup": cooOtsOchNotifEnableGroup}
)
