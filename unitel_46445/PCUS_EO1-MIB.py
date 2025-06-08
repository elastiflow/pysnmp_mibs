# SNMP MIB module (PCUS_EO1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/unitel_46445/PCUS_EO1-MIB.mib
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
_Pcus_eo1_ObjectIdentity = ObjectIdentity
pcus_eo1 = _Pcus_eo1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46445, 4)
)
_SystemBlockTable_Object = MibTable
systemBlockTable = _SystemBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 46445, 4, 1)
)
if mibBuilder.loadTexts:
    systemBlockTable.setStatus("current")
_SystemBlockEntry_Object = MibTableRow
systemBlockEntry = _SystemBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 46445, 4, 1, 1)
)
systemBlockEntry.setIndexNames(
    (0, "PCUS_EO1-MIB", "power"),
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
    (1, 3, 6, 1, 4, 1, 46445, 4, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 46445, 4, 1, 1, 2),
    _PowerRecovery_Type()
)
powerRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerRecovery.setStatus("current")


class _HwAlarm_Type(Integer32):
    """Custom type hwAlarm based on Integer32"""
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


_HwAlarm_Type.__name__ = "Integer32"
_HwAlarm_Object = MibTableColumn
hwAlarm = _HwAlarm_Object(
    (1, 3, 6, 1, 4, 1, 46445, 4, 1, 1, 3),
    _HwAlarm_Type()
)
hwAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAlarm.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 46445, 4, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 46445, 4, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 46445, 4, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 46445, 4, 1, 1, 7),
    _SetNewAddress_Type()
)
setNewAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setNewAddress.setStatus("current")


class _SignalizationOutput1_Type(Integer32):
    """Custom type signalizationOutput1 based on Integer32"""
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


_SignalizationOutput1_Type.__name__ = "Integer32"
_SignalizationOutput1_Object = MibTableColumn
signalizationOutput1 = _SignalizationOutput1_Object(
    (1, 3, 6, 1, 4, 1, 46445, 4, 1, 1, 8),
    _SignalizationOutput1_Type()
)
signalizationOutput1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalizationOutput1.setStatus("current")


class _SignalizationOutput2_Type(Integer32):
    """Custom type signalizationOutput2 based on Integer32"""
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


_SignalizationOutput2_Type.__name__ = "Integer32"
_SignalizationOutput2_Object = MibTableColumn
signalizationOutput2 = _SignalizationOutput2_Object(
    (1, 3, 6, 1, 4, 1, 46445, 4, 1, 1, 9),
    _SignalizationOutput2_Type()
)
signalizationOutput2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalizationOutput2.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 46445, 4, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 46445, 4, 1, 1, 11),
    _ErrorIrigB_Type()
)
errorIrigB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorIrigB.setStatus("current")


class _SetNewPassword1_Type(Integer32):
    """Custom type setNewPassword1 based on Integer32"""
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


_SetNewPassword1_Type.__name__ = "Integer32"
_SetNewPassword1_Object = MibTableColumn
setNewPassword1 = _SetNewPassword1_Object(
    (1, 3, 6, 1, 4, 1, 46445, 4, 1, 1, 12),
    _SetNewPassword1_Type()
)
setNewPassword1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setNewPassword1.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 46445, 4, 1, 1, 13),
    _ProgramReset_Type()
)
programReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programReset.setStatus("current")


class _SetNewPassword2_Type(Integer32):
    """Custom type setNewPassword2 based on Integer32"""
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


_SetNewPassword2_Type.__name__ = "Integer32"
_SetNewPassword2_Object = MibTableColumn
setNewPassword2 = _SetNewPassword2_Object(
    (1, 3, 6, 1, 4, 1, 46445, 4, 1, 1, 14),
    _SetNewPassword2_Type()
)
setNewPassword2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setNewPassword2.setStatus("current")


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
        *(("Activated", 0),
          ("Deactivated", 1))
    )


_ActivateDevice_Type.__name__ = "Integer32"
_ActivateDevice_Object = MibTableColumn
activateDevice = _ActivateDevice_Object(
    (1, 3, 6, 1, 4, 1, 46445, 4, 1, 1, 15),
    _ActivateDevice_Type()
)
activateDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activateDevice.setStatus("current")


class _SfpSetError_Type(Integer32):
    """Custom type sfpSetError based on Integer32"""
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


_SfpSetError_Type.__name__ = "Integer32"
_SfpSetError_Object = MibTableColumn
sfpSetError = _SfpSetError_Object(
    (1, 3, 6, 1, 4, 1, 46445, 4, 1, 1, 16),
    _SfpSetError_Type()
)
sfpSetError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpSetError.setStatus("current")
_CommunicationBlock_ObjectIdentity = ObjectIdentity
communicationBlock = _CommunicationBlock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46445, 4, 2)
)


class _LosOptChn_Type(Integer32):
    """Custom type losOptChn based on Integer32"""
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


_LosOptChn_Type.__name__ = "Integer32"
_LosOptChn_Object = MibScalar
losOptChn = _LosOptChn_Object(
    (1, 3, 6, 1, 4, 1, 46445, 4, 2, 1),
    _LosOptChn_Type()
)
losOptChn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    losOptChn.setStatus("current")


class _LosElChn_Type(Integer32):
    """Custom type losElChn based on Integer32"""
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


_LosElChn_Type.__name__ = "Integer32"
_LosElChn_Object = MibScalar
losElChn = _LosElChn_Object(
    (1, 3, 6, 1, 4, 1, 46445, 4, 2, 2),
    _LosElChn_Type()
)
losElChn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    losElChn.setStatus("current")


class _YellowAlarmOptChn_Type(Integer32):
    """Custom type yellowAlarmOptChn based on Integer32"""
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


_YellowAlarmOptChn_Type.__name__ = "Integer32"
_YellowAlarmOptChn_Object = MibScalar
yellowAlarmOptChn = _YellowAlarmOptChn_Object(
    (1, 3, 6, 1, 4, 1, 46445, 4, 2, 3),
    _YellowAlarmOptChn_Type()
)
yellowAlarmOptChn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yellowAlarmOptChn.setStatus("current")


class _YellowAlarmElChn_Type(Integer32):
    """Custom type yellowAlarmElChn based on Integer32"""
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


_YellowAlarmElChn_Type.__name__ = "Integer32"
_YellowAlarmElChn_Object = MibScalar
yellowAlarmElChn = _YellowAlarmElChn_Object(
    (1, 3, 6, 1, 4, 1, 46445, 4, 2, 4),
    _YellowAlarmElChn_Type()
)
yellowAlarmElChn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yellowAlarmElChn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PCUS_EO1-MIB",
    **{"system": system,
       "sysDescr": sysDescr,
       "sysObjectID": sysObjectID,
       "sysContact": sysContact,
       "sysName": sysName,
       "sysLocation": sysLocation,
       "uni-eng": uni_eng,
       "pcus_eo1": pcus_eo1,
       "systemBlockTable": systemBlockTable,
       "systemBlockEntry": systemBlockEntry,
       "power": power,
       "powerRecovery": powerRecovery,
       "hwAlarm": hwAlarm,
       "setTimeAlarm": setTimeAlarm,
       "errorReadConfig": errorReadConfig,
       "save_configFlash": save_configFlash,
       "setNewAddress": setNewAddress,
       "signalizationOutput1": signalizationOutput1,
       "signalizationOutput2": signalizationOutput2,
       "signalizationAlarmOutput": signalizationAlarmOutput,
       "errorIrigB": errorIrigB,
       "setNewPassword1": setNewPassword1,
       "programReset": programReset,
       "setNewPassword2": setNewPassword2,
       "activateDevice": activateDevice,
       "sfpSetError": sfpSetError,
       "communicationBlock": communicationBlock,
       "losOptChn": losOptChn,
       "losElChn": losElChn,
       "yellowAlarmOptChn": yellowAlarmOptChn,
       "yellowAlarmElChn": yellowAlarmElChn}
)
