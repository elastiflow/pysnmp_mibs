# SNMP MIB module (PKUS_EO2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/unitel_46445/PKUS_EO2-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 19:48:19 2025
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
 enterprises,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "enterprises",
    "iso",
    "mib-2")

(AutonomousType,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TimeStamp")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 1)
)


class _SysDescr_Type(DisplayString):
    """Custom type sysDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysDescr_Type.__name__ = "DisplayString"
_SysDescr_Object = MibScalar
sysDescr = _SysDescr_Object(
    (1, 3, 6, 1, 2, 1, 1, 1),
    _SysDescr_Type()
)
sysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDescr.setStatus("current")
_SysObjectID_Type = ObjectIdentifier
_SysObjectID_Object = MibScalar
sysObjectID = _SysObjectID_Object(
    (1, 3, 6, 1, 2, 1, 1, 2),
    _SysObjectID_Type()
)
sysObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysObjectID.setStatus("mandatory")


class _SysContact_Type(DisplayString):
    """Custom type sysContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysContact_Type.__name__ = "DisplayString"
_SysContact_Object = MibScalar
sysContact = _SysContact_Object(
    (1, 3, 6, 1, 2, 1, 1, 4),
    _SysContact_Type()
)
sysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysContact.setStatus("current")


class _SysName_Type(DisplayString):
    """Custom type sysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysName_Type.__name__ = "DisplayString"
_SysName_Object = MibScalar
sysName = _SysName_Object(
    (1, 3, 6, 1, 2, 1, 1, 5),
    _SysName_Type()
)
sysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysName.setStatus("current")


class _SysLocation_Type(DisplayString):
    """Custom type sysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysLocation_Type.__name__ = "DisplayString"
_SysLocation_Object = MibScalar
sysLocation = _SysLocation_Object(
    (1, 3, 6, 1, 2, 1, 1, 6),
    _SysLocation_Type()
)
sysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocation.setStatus("current")
_Uni_eng_ObjectIdentity = ObjectIdentity
uni_eng = _Uni_eng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46445)
)
_Pcus_eo2_ObjectIdentity = ObjectIdentity
pcus_eo2 = _Pcus_eo2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46445, 5)
)
_SystemBlockTable_Object = MibTable
systemBlockTable = _SystemBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 46445, 5, 1)
)
if mibBuilder.loadTexts:
    systemBlockTable.setStatus("current")
_SystemBlockEntry_Object = MibTableRow
systemBlockEntry = _SystemBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 46445, 5, 1, 1)
)
systemBlockEntry.setIndexNames(
    (0, "PKUS_EO2-MIB", "power"),
)
if mibBuilder.loadTexts:
    systemBlockEntry.setStatus("mandatory")


class _Power_Type(Integer32):
    """Custom type power based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Off", 0),
          ("On", 1))
    )


_Power_Type.__name__ = "Integer32"
_Power_Object = MibTableColumn
power = _Power_Object(
    (1, 3, 6, 1, 4, 1, 46445, 5, 1, 1, 1),
    _Power_Type()
)
power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    power.setStatus("current")


class _PowerRecovery_Type(Integer32):
    """Custom type powerRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("None", 0),
          ("Recovered", 1))
    )


_PowerRecovery_Type.__name__ = "Integer32"
_PowerRecovery_Object = MibTableColumn
powerRecovery = _PowerRecovery_Object(
    (1, 3, 6, 1, 4, 1, 46445, 5, 1, 1, 2),
    _PowerRecovery_Type()
)
powerRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerRecovery.setStatus("current")


class _SetTimeAlarm_Type(Integer32):
    """Custom type setTimeAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("None", 0),
          ("Alarm", 1))
    )


_SetTimeAlarm_Type.__name__ = "Integer32"
_SetTimeAlarm_Object = MibTableColumn
setTimeAlarm = _SetTimeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 46445, 5, 1, 1, 3),
    _SetTimeAlarm_Type()
)
setTimeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setTimeAlarm.setStatus("current")


class _ErrorReadConfig_Type(Integer32):
    """Custom type errorReadConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Off", 0),
          ("On", 1))
    )


_ErrorReadConfig_Type.__name__ = "Integer32"
_ErrorReadConfig_Object = MibTableColumn
errorReadConfig = _ErrorReadConfig_Object(
    (1, 3, 6, 1, 4, 1, 46445, 5, 1, 1, 4),
    _ErrorReadConfig_Type()
)
errorReadConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorReadConfig.setStatus("current")


class _Save_configFlash_Type(Integer32):
    """Custom type save_configFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("None", 0),
          ("Saved", 1))
    )


_Save_configFlash_Type.__name__ = "Integer32"
_Save_configFlash_Object = MibTableColumn
save_configFlash = _Save_configFlash_Object(
    (1, 3, 6, 1, 4, 1, 46445, 5, 1, 1, 5),
    _Save_configFlash_Type()
)
save_configFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    save_configFlash.setStatus("current")


class _SetNewAddress_Type(Integer32):
    """Custom type setNewAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("None", 0),
          ("Setted", 1))
    )


_SetNewAddress_Type.__name__ = "Integer32"
_SetNewAddress_Object = MibTableColumn
setNewAddress = _SetNewAddress_Object(
    (1, 3, 6, 1, 4, 1, 46445, 5, 1, 1, 6),
    _SetNewAddress_Type()
)
setNewAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setNewAddress.setStatus("current")


class _SignalizationOutputElChn1Los_Type(Integer32):
    """Custom type signalizationOutputElChn1Los based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Off", 0),
          ("On", 1))
    )


_SignalizationOutputElChn1Los_Type.__name__ = "Integer32"
_SignalizationOutputElChn1Los_Object = MibTableColumn
signalizationOutputElChn1Los = _SignalizationOutputElChn1Los_Object(
    (1, 3, 6, 1, 4, 1, 46445, 5, 1, 1, 7),
    _SignalizationOutputElChn1Los_Type()
)
signalizationOutputElChn1Los.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalizationOutputElChn1Los.setStatus("current")


class _SignalizationOutputElChn2Los_Type(Integer32):
    """Custom type signalizationOutputElChn2Los based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Off", 0),
          ("On", 1))
    )


_SignalizationOutputElChn2Los_Type.__name__ = "Integer32"
_SignalizationOutputElChn2Los_Object = MibTableColumn
signalizationOutputElChn2Los = _SignalizationOutputElChn2Los_Object(
    (1, 3, 6, 1, 4, 1, 46445, 5, 1, 1, 8),
    _SignalizationOutputElChn2Los_Type()
)
signalizationOutputElChn2Los.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalizationOutputElChn2Los.setStatus("current")


class _SignalizationOutputOptChn1Los_Type(Integer32):
    """Custom type signalizationOutputOptChn1Los based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Off", 0),
          ("On", 1))
    )


_SignalizationOutputOptChn1Los_Type.__name__ = "Integer32"
_SignalizationOutputOptChn1Los_Object = MibTableColumn
signalizationOutputOptChn1Los = _SignalizationOutputOptChn1Los_Object(
    (1, 3, 6, 1, 4, 1, 46445, 5, 1, 1, 9),
    _SignalizationOutputOptChn1Los_Type()
)
signalizationOutputOptChn1Los.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalizationOutputOptChn1Los.setStatus("current")


class _SignalizationOutputOptChn2Los_Type(Integer32):
    """Custom type signalizationOutputOptChn2Los based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Off", 0),
          ("On", 1))
    )


_SignalizationOutputOptChn2Los_Type.__name__ = "Integer32"
_SignalizationOutputOptChn2Los_Object = MibTableColumn
signalizationOutputOptChn2Los = _SignalizationOutputOptChn2Los_Object(
    (1, 3, 6, 1, 4, 1, 46445, 5, 1, 1, 10),
    _SignalizationOutputOptChn2Los_Type()
)
signalizationOutputOptChn2Los.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalizationOutputOptChn2Los.setStatus("current")


class _SignalizationOutputElChn1Ay_Type(Integer32):
    """Custom type signalizationOutputElChn1Ay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Off", 0),
          ("On", 1))
    )


_SignalizationOutputElChn1Ay_Type.__name__ = "Integer32"
_SignalizationOutputElChn1Ay_Object = MibTableColumn
signalizationOutputElChn1Ay = _SignalizationOutputElChn1Ay_Object(
    (1, 3, 6, 1, 4, 1, 46445, 5, 1, 1, 11),
    _SignalizationOutputElChn1Ay_Type()
)
signalizationOutputElChn1Ay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalizationOutputElChn1Ay.setStatus("current")


class _SignalizationOutputElChn2Ay_Type(Integer32):
    """Custom type signalizationOutputElChn2Ay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Off", 0),
          ("On", 1))
    )


_SignalizationOutputElChn2Ay_Type.__name__ = "Integer32"
_SignalizationOutputElChn2Ay_Object = MibTableColumn
signalizationOutputElChn2Ay = _SignalizationOutputElChn2Ay_Object(
    (1, 3, 6, 1, 4, 1, 46445, 5, 1, 1, 12),
    _SignalizationOutputElChn2Ay_Type()
)
signalizationOutputElChn2Ay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalizationOutputElChn2Ay.setStatus("current")


class _SignalizationOutputOptChn1Ay_Type(Integer32):
    """Custom type signalizationOutputOptChn1Ay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Off", 0),
          ("On", 1))
    )


_SignalizationOutputOptChn1Ay_Type.__name__ = "Integer32"
_SignalizationOutputOptChn1Ay_Object = MibTableColumn
signalizationOutputOptChn1Ay = _SignalizationOutputOptChn1Ay_Object(
    (1, 3, 6, 1, 4, 1, 46445, 5, 1, 1, 13),
    _SignalizationOutputOptChn1Ay_Type()
)
signalizationOutputOptChn1Ay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalizationOutputOptChn1Ay.setStatus("current")


class _SignalizationOutputOptChn2Ay_Type(Integer32):
    """Custom type signalizationOutputOptChn2Ay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Off", 0),
          ("On", 1))
    )


_SignalizationOutputOptChn2Ay_Type.__name__ = "Integer32"
_SignalizationOutputOptChn2Ay_Object = MibTableColumn
signalizationOutputOptChn2Ay = _SignalizationOutputOptChn2Ay_Object(
    (1, 3, 6, 1, 4, 1, 46445, 5, 1, 1, 14),
    _SignalizationOutputOptChn2Ay_Type()
)
signalizationOutputOptChn2Ay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalizationOutputOptChn2Ay.setStatus("current")


class _SignalizationAlarmOutput_Type(Integer32):
    """Custom type signalizationAlarmOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Off", 0),
          ("On", 1))
    )


_SignalizationAlarmOutput_Type.__name__ = "Integer32"
_SignalizationAlarmOutput_Object = MibTableColumn
signalizationAlarmOutput = _SignalizationAlarmOutput_Object(
    (1, 3, 6, 1, 4, 1, 46445, 5, 1, 1, 15),
    _SignalizationAlarmOutput_Type()
)
signalizationAlarmOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalizationAlarmOutput.setStatus("current")


class _ErrorIrigB_Type(Integer32):
    """Custom type errorIrigB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Off", 0),
          ("On", 1))
    )


_ErrorIrigB_Type.__name__ = "Integer32"
_ErrorIrigB_Object = MibTableColumn
errorIrigB = _ErrorIrigB_Object(
    (1, 3, 6, 1, 4, 1, 46445, 5, 1, 1, 16),
    _ErrorIrigB_Type()
)
errorIrigB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorIrigB.setStatus("current")


class _SetNewPassword_Type(Integer32):
    """Custom type setNewPassword based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("None", 0),
          ("Setted", 1))
    )


_SetNewPassword_Type.__name__ = "Integer32"
_SetNewPassword_Object = MibTableColumn
setNewPassword = _SetNewPassword_Object(
    (1, 3, 6, 1, 4, 1, 46445, 5, 1, 1, 17),
    _SetNewPassword_Type()
)
setNewPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setNewPassword.setStatus("current")


class _ProgramReset_Type(Integer32):
    """Custom type programReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("None", 0),
          ("Reseted", 1))
    )


_ProgramReset_Type.__name__ = "Integer32"
_ProgramReset_Object = MibTableColumn
programReset = _ProgramReset_Object(
    (1, 3, 6, 1, 4, 1, 46445, 5, 1, 1, 18),
    _ProgramReset_Type()
)
programReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programReset.setStatus("current")


class _ActivateDevice_Type(Integer32):
    """Custom type activateDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("None", 0),
          ("Activated", 1))
    )


_ActivateDevice_Type.__name__ = "Integer32"
_ActivateDevice_Object = MibTableColumn
activateDevice = _ActivateDevice_Object(
    (1, 3, 6, 1, 4, 1, 46445, 5, 1, 1, 19),
    _ActivateDevice_Type()
)
activateDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activateDevice.setStatus("current")
_CommunicationBlockTable_Object = MibTable
communicationBlockTable = _CommunicationBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 46445, 5, 2)
)
if mibBuilder.loadTexts:
    communicationBlockTable.setStatus("current")
_CommunicationBlockEntry_Object = MibTableRow
communicationBlockEntry = _CommunicationBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 46445, 5, 2, 1)
)
communicationBlockEntry.setIndexNames(
    (0, "PKUS_EO2-MIB", "communicationBlockLineIndex"),
)
if mibBuilder.loadTexts:
    communicationBlockEntry.setStatus("mandatory")


class _CommunicationBlockLineIndex_Type(Integer32):
    """Custom type communicationBlockLineIndex based on Integer32"""
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
        *(("ElChn_1", 1),
          ("Elchn_2", 2),
          ("OptChn_1", 3),
          ("OptChn_2", 4))
    )


_CommunicationBlockLineIndex_Type.__name__ = "Integer32"
_CommunicationBlockLineIndex_Object = MibTableColumn
communicationBlockLineIndex = _CommunicationBlockLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 46445, 5, 2, 1, 1),
    _CommunicationBlockLineIndex_Type()
)
communicationBlockLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    communicationBlockLineIndex.setStatus("current")


class _Los_Type(Integer32):
    """Custom type los based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("None", 0),
          ("Los", 1))
    )


_Los_Type.__name__ = "Integer32"
_Los_Object = MibTableColumn
los = _Los_Object(
    (1, 3, 6, 1, 4, 1, 46445, 5, 2, 1, 2),
    _Los_Type()
)
los.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    los.setStatus("current")


class _Yellow_Type(Integer32):
    """Custom type yellow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("None", 0),
          ("Yellow", 1))
    )


_Yellow_Type.__name__ = "Integer32"
_Yellow_Object = MibTableColumn
yellow = _Yellow_Object(
    (1, 3, 6, 1, 4, 1, 46445, 5, 2, 1, 3),
    _Yellow_Type()
)
yellow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yellow.setStatus("current")


class _Transmitter_Type(Integer32):
    """Custom type transmitter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Off", 0),
          ("On", 1))
    )


_Transmitter_Type.__name__ = "Integer32"
_Transmitter_Object = MibTableColumn
transmitter = _Transmitter_Object(
    (1, 3, 6, 1, 4, 1, 46445, 5, 2, 1, 4),
    _Transmitter_Type()
)
transmitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitter.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PKUS_EO2-MIB",
    **{"system": system,
       "sysDescr": sysDescr,
       "sysObjectID": sysObjectID,
       "sysContact": sysContact,
       "sysName": sysName,
       "sysLocation": sysLocation,
       "uni-eng": uni_eng,
       "pcus_eo2": pcus_eo2,
       "systemBlockTable": systemBlockTable,
       "systemBlockEntry": systemBlockEntry,
       "power": power,
       "powerRecovery": powerRecovery,
       "setTimeAlarm": setTimeAlarm,
       "errorReadConfig": errorReadConfig,
       "save_configFlash": save_configFlash,
       "setNewAddress": setNewAddress,
       "signalizationOutputElChn1Los": signalizationOutputElChn1Los,
       "signalizationOutputElChn2Los": signalizationOutputElChn2Los,
       "signalizationOutputOptChn1Los": signalizationOutputOptChn1Los,
       "signalizationOutputOptChn2Los": signalizationOutputOptChn2Los,
       "signalizationOutputElChn1Ay": signalizationOutputElChn1Ay,
       "signalizationOutputElChn2Ay": signalizationOutputElChn2Ay,
       "signalizationOutputOptChn1Ay": signalizationOutputOptChn1Ay,
       "signalizationOutputOptChn2Ay": signalizationOutputOptChn2Ay,
       "signalizationAlarmOutput": signalizationAlarmOutput,
       "errorIrigB": errorIrigB,
       "setNewPassword": setNewPassword,
       "programReset": programReset,
       "activateDevice": activateDevice,
       "communicationBlockTable": communicationBlockTable,
       "communicationBlockEntry": communicationBlockEntry,
       "communicationBlockLineIndex": communicationBlockLineIndex,
       "los": los,
       "yellow": yellow,
       "transmitter": transmitter}
)
