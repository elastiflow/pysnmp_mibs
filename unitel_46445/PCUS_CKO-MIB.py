# SNMP MIB module (PCUS_CKO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/unitel_46445/PCUS_CKO-MIB.mib
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
_Pcus_cko_ObjectIdentity = ObjectIdentity
pcus_cko = _Pcus_cko_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46445, 3)
)
_SystemBlockTable_Object = MibTable
systemBlockTable = _SystemBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 1)
)
if mibBuilder.loadTexts:
    systemBlockTable.setStatus("current")
_SystemBlockEntry_Object = MibTableRow
systemBlockEntry = _SystemBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 1, 1)
)
systemBlockEntry.setIndexNames(
    (0, "PCUS_CKO-MIB", "power"),
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
    (1, 3, 6, 1, 4, 1, 46445, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 46445, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 46445, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 46445, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 46445, 3, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 46445, 3, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 46445, 3, 1, 1, 7),
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
_SignalizationOutput1_Object = MibScalar
signalizationOutput1 = _SignalizationOutput1_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 1, 1, 8),
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
_SignalizationOutput2_Object = MibScalar
signalizationOutput2 = _SignalizationOutput2_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 1, 1, 9),
    _SignalizationOutput2_Type()
)
signalizationOutput2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalizationOutput2.setStatus("current")


class _SignalizationOutput3_Type(Integer32):
    """Custom type signalizationOutput3 based on Integer32"""
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


_SignalizationOutput3_Type.__name__ = "Integer32"
_SignalizationOutput3_Object = MibScalar
signalizationOutput3 = _SignalizationOutput3_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 1, 1, 10),
    _SignalizationOutput3_Type()
)
signalizationOutput3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalizationOutput3.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 46445, 3, 1, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 46445, 3, 1, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 46445, 3, 1, 1, 13),
    _ProgramReset_Type()
)
programReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programReset.setStatus("current")


class _SignalizationOutput4_Type(Integer32):
    """Custom type signalizationOutput4 based on Integer32"""
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


_SignalizationOutput4_Type.__name__ = "Integer32"
_SignalizationOutput4_Object = MibScalar
signalizationOutput4 = _SignalizationOutput4_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 1, 1, 14),
    _SignalizationOutput4_Type()
)
signalizationOutput4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalizationOutput4.setStatus("current")


class _SignalizationOutput5_Type(Integer32):
    """Custom type signalizationOutput5 based on Integer32"""
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


_SignalizationOutput5_Type.__name__ = "Integer32"
_SignalizationOutput5_Object = MibScalar
signalizationOutput5 = _SignalizationOutput5_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 1, 1, 15),
    _SignalizationOutput5_Type()
)
signalizationOutput5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalizationOutput5.setStatus("current")


class _SignalizationOutput6_Type(Integer32):
    """Custom type signalizationOutput6 based on Integer32"""
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


_SignalizationOutput6_Type.__name__ = "Integer32"
_SignalizationOutput6_Object = MibScalar
signalizationOutput6 = _SignalizationOutput6_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 1, 1, 16),
    _SignalizationOutput6_Type()
)
signalizationOutput6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalizationOutput6.setStatus("current")


class _RemoteReset_Type(Integer32):
    """Custom type remoteReset based on Integer32"""
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


_RemoteReset_Type.__name__ = "Integer32"
_RemoteReset_Object = MibTableColumn
remoteReset = _RemoteReset_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 1, 1, 17),
    _RemoteReset_Type()
)
remoteReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteReset.setStatus("current")


class _LocalReset_Type(Integer32):
    """Custom type localReset based on Integer32"""
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


_LocalReset_Type.__name__ = "Integer32"
_LocalReset_Object = MibTableColumn
localReset = _LocalReset_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 1, 1, 18),
    _LocalReset_Type()
)
localReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localReset.setStatus("current")


class _ResetCounterFlash_Type(Integer32):
    """Custom type resetCounterFlash based on Integer32"""
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


_ResetCounterFlash_Type.__name__ = "Integer32"
_ResetCounterFlash_Object = MibTableColumn
resetCounterFlash = _ResetCounterFlash_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 1, 1, 19),
    _ResetCounterFlash_Type()
)
resetCounterFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resetCounterFlash.setStatus("current")


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
          ("None", 1))
    )


_ActivateDevice_Type.__name__ = "Integer32"
_ActivateDevice_Object = MibTableColumn
activateDevice = _ActivateDevice_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 1, 1, 20),
    _ActivateDevice_Type()
)
activateDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activateDevice.setStatus("current")


class _LineTerminatError_Type(Integer32):
    """Custom type lineTerminatError based on Integer32"""
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


_LineTerminatError_Type.__name__ = "Integer32"
_LineTerminatError_Object = MibTableColumn
lineTerminatError = _LineTerminatError_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 1, 1, 21),
    _LineTerminatError_Type()
)
lineTerminatError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineTerminatError.setStatus("current")


class _Sfp1SetError_Type(Integer32):
    """Custom type sfp1SetError based on Integer32"""
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


_Sfp1SetError_Type.__name__ = "Integer32"
_Sfp1SetError_Object = MibTableColumn
sfp1SetError = _Sfp1SetError_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 1, 1, 22),
    _Sfp1SetError_Type()
)
sfp1SetError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfp1SetError.setStatus("current")


class _Sfp2SetError_Type(Integer32):
    """Custom type sfp2SetError based on Integer32"""
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


_Sfp2SetError_Type.__name__ = "Integer32"
_Sfp2SetError_Object = MibTableColumn
sfp2SetError = _Sfp2SetError_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 1, 1, 23),
    _Sfp2SetError_Type()
)
sfp2SetError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfp2SetError.setStatus("current")
_CommunicationBlock_ObjectIdentity = ObjectIdentity
communicationBlock = _CommunicationBlock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46445, 3, 2)
)


class _Los1Tpe1_Type(Integer32):
    """Custom type los1Tpe1 based on Integer32"""
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


_Los1Tpe1_Type.__name__ = "Integer32"
_Los1Tpe1_Object = MibScalar
los1Tpe1 = _Los1Tpe1_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 2, 1),
    _Los1Tpe1_Type()
)
los1Tpe1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    los1Tpe1.setStatus("current")


class _Los2Tpe1_Type(Integer32):
    """Custom type los2Tpe1 based on Integer32"""
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


_Los2Tpe1_Type.__name__ = "Integer32"
_Los2Tpe1_Object = MibScalar
los2Tpe1 = _Los2Tpe1_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 2, 2),
    _Los2Tpe1_Type()
)
los2Tpe1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    los2Tpe1.setStatus("current")


class _YellowAlarmTpe1_Type(Integer32):
    """Custom type yellowAlarmTpe1 based on Integer32"""
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


_YellowAlarmTpe1_Type.__name__ = "Integer32"
_YellowAlarmTpe1_Object = MibScalar
yellowAlarmTpe1 = _YellowAlarmTpe1_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 2, 3),
    _YellowAlarmTpe1_Type()
)
yellowAlarmTpe1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yellowAlarmTpe1.setStatus("current")


class _YellowAlarmTpe2_Type(Integer32):
    """Custom type yellowAlarmTpe2 based on Integer32"""
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


_YellowAlarmTpe2_Type.__name__ = "Integer32"
_YellowAlarmTpe2_Object = MibScalar
yellowAlarmTpe2 = _YellowAlarmTpe2_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 2, 4),
    _YellowAlarmTpe2_Type()
)
yellowAlarmTpe2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yellowAlarmTpe2.setStatus("current")
_CommunicationBlockTable_Object = MibTable
communicationBlockTable = _CommunicationBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 2, 5)
)
if mibBuilder.loadTexts:
    communicationBlockTable.setStatus("current")
_CommunicationBlockEntry_Object = MibTableRow
communicationBlockEntry = _CommunicationBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 2, 5, 1)
)
communicationBlockEntry.setIndexNames(
    (0, "PCUS_CKO-MIB", "communicationBlockLineIndex"),
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
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("Tpe1_command1_8", 1),
          ("Tpe1_command9_16", 2),
          ("Tpe1_command17_24", 3),
          ("Tpe2_command1_8", 4),
          ("Tpe2_command9_16", 5),
          ("Tpe2_command17_24", 6),
          ("Tpe1p1_command1_8", 7),
          ("Tpe1p1_command9_16", 8),
          ("Tpe1p1_command17_24", 9),
          ("Tpe2p1_command1_8", 10),
          ("Tpe2p1_command9_16", 11),
          ("Tpe2p1_command17_24", 12))
    )


_CommunicationBlockLineIndex_Type.__name__ = "Integer32"
_CommunicationBlockLineIndex_Object = MibTableColumn
communicationBlockLineIndex = _CommunicationBlockLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 2, 5, 1, 1),
    _CommunicationBlockLineIndex_Type()
)
communicationBlockLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    communicationBlockLineIndex.setStatus("current")


class _Warning_Type(Integer32):
    """Custom type warning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("None", 0),
          ("Warning", 1))
    )


_Warning_Type.__name__ = "Integer32"
_Warning_Object = MibTableColumn
warning = _Warning_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 2, 5, 1, 2),
    _Warning_Type()
)
warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning.setStatus("current")


class _Alarm_Type(Integer32):
    """Custom type alarm based on Integer32"""
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


_Alarm_Type.__name__ = "Integer32"
_Alarm_Object = MibTableColumn
alarm = _Alarm_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 2, 5, 1, 3),
    _Alarm_Type()
)
alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarm.setStatus("current")


class _StartLooptest_Type(Integer32):
    """Custom type startLooptest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Finished", 0),
          ("Starting", 1))
    )


_StartLooptest_Type.__name__ = "Integer32"
_StartLooptest_Object = MibTableColumn
startLooptest = _StartLooptest_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 2, 5, 1, 4),
    _StartLooptest_Type()
)
startLooptest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    startLooptest.setStatus("current")


class _PassingLooptest_Type(Integer32):
    """Custom type passingLooptest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Passed", 0),
          ("Error", 1))
    )


_PassingLooptest_Type.__name__ = "Integer32"
_PassingLooptest_Object = MibTableColumn
passingLooptest = _PassingLooptest_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 2, 5, 1, 5),
    _PassingLooptest_Type()
)
passingLooptest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passingLooptest.setStatus("current")
_DiscreteIOTable_Object = MibTable
discreteIOTable = _DiscreteIOTable_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 3)
)
if mibBuilder.loadTexts:
    discreteIOTable.setStatus("current")
_DiscreteIOEntry_Object = MibTableRow
discreteIOEntry = _DiscreteIOEntry_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 3, 1)
)
discreteIOEntry.setIndexNames(
    (0, "PCUS_CKO-MIB", "discreteIOLineIndex"),
)
if mibBuilder.loadTexts:
    discreteIOEntry.setStatus("mandatory")


class _DiscreteIOLineIndex_Type(Integer32):
    """Custom type discreteIOLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("discreteIO1", 1),
          ("discreteIO2", 2),
          ("discreteIO3", 3),
          ("discreteIO4", 4),
          ("discreteIO5", 5),
          ("discreteIO6", 6),
          ("discreteIO7", 7),
          ("discreteIO8", 8),
          ("discreteIO9", 9),
          ("discreteIO10", 10),
          ("discreteIO11", 11),
          ("discreteIO12", 12),
          ("discreteIO13", 13),
          ("discreteIO14", 14),
          ("discreteIO15", 15),
          ("discreteIO16", 16))
    )


_DiscreteIOLineIndex_Type.__name__ = "Integer32"
_DiscreteIOLineIndex_Object = MibTableColumn
discreteIOLineIndex = _DiscreteIOLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 3, 1, 1),
    _DiscreteIOLineIndex_Type()
)
discreteIOLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discreteIOLineIndex.setStatus("current")


class _Discrete_Inputs_Type(Integer32):
    """Custom type discrete_Inputs based on Integer32"""
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


_Discrete_Inputs_Type.__name__ = "Integer32"
_Discrete_Inputs_Object = MibTableColumn
discrete_Inputs = _Discrete_Inputs_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 3, 1, 2),
    _Discrete_Inputs_Type()
)
discrete_Inputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discrete_Inputs.setStatus("current")


class _Discrete_Outputs_Type(Integer32):
    """Custom type discrete_Outputs based on Integer32"""
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


_Discrete_Outputs_Type.__name__ = "Integer32"
_Discrete_Outputs_Object = MibTableColumn
discrete_Outputs = _Discrete_Outputs_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 3, 1, 3),
    _Discrete_Outputs_Type()
)
discrete_Outputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discrete_Outputs.setStatus("current")


class _Discrete_InputsControl_Type(Integer32):
    """Custom type discrete_InputsControl based on Integer32"""
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


_Discrete_InputsControl_Type.__name__ = "Integer32"
_Discrete_InputsControl_Object = MibTableColumn
discrete_InputsControl = _Discrete_InputsControl_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 3, 1, 4),
    _Discrete_InputsControl_Type()
)
discrete_InputsControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discrete_InputsControl.setStatus("current")
_CommandsTable_Object = MibTable
commandsTable = _CommandsTable_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 4)
)
if mibBuilder.loadTexts:
    commandsTable.setStatus("current")
_CommandsEntry_Object = MibTableRow
commandsEntry = _CommandsEntry_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 4, 1)
)
commandsEntry.setIndexNames(
    (0, "PCUS_CKO-MIB", "commandsLineIndex"),
)
if mibBuilder.loadTexts:
    commandsEntry.setStatus("mandatory")


class _CommandsLineIndex_Type(Integer32):
    """Custom type commandsLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("command1", 1),
          ("command2", 2),
          ("command3", 3),
          ("command4", 4),
          ("command5", 5),
          ("command6", 6),
          ("command7", 7),
          ("command8", 8),
          ("command9", 9),
          ("command10", 10),
          ("command11", 11),
          ("command12", 12),
          ("command13", 13),
          ("command14", 14),
          ("command15", 15),
          ("command16", 16),
          ("command17", 17),
          ("command18", 18),
          ("command19", 19),
          ("command20", 20),
          ("command21", 21),
          ("command22", 22),
          ("command23", 23),
          ("command24", 24))
    )


_CommandsLineIndex_Type.__name__ = "Integer32"
_CommandsLineIndex_Object = MibTableColumn
commandsLineIndex = _CommandsLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 4, 1, 1),
    _CommandsLineIndex_Type()
)
commandsLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commandsLineIndex.setStatus("current")


class _CommandsTX_Type(Integer32):
    """Custom type commandsTX based on Integer32"""
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


_CommandsTX_Type.__name__ = "Integer32"
_CommandsTX_Object = MibTableColumn
commandsTX = _CommandsTX_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 4, 1, 2),
    _CommandsTX_Type()
)
commandsTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commandsTX.setStatus("current")


class _CommandsRX_Type(Integer32):
    """Custom type commandsRX based on Integer32"""
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


_CommandsRX_Type.__name__ = "Integer32"
_CommandsRX_Object = MibTableColumn
commandsRX = _CommandsRX_Object(
    (1, 3, 6, 1, 4, 1, 46445, 3, 4, 1, 3),
    _CommandsRX_Type()
)
commandsRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commandsRX.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PCUS_CKO-MIB",
    **{"system": system,
       "sysDescr": sysDescr,
       "sysObjectID": sysObjectID,
       "sysContact": sysContact,
       "sysName": sysName,
       "sysLocation": sysLocation,
       "uni-eng": uni_eng,
       "pcus_cko": pcus_cko,
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
       "signalizationOutput3": signalizationOutput3,
       "errorIrigB": errorIrigB,
       "setNewPassword": setNewPassword,
       "programReset": programReset,
       "signalizationOutput4": signalizationOutput4,
       "signalizationOutput5": signalizationOutput5,
       "signalizationOutput6": signalizationOutput6,
       "remoteReset": remoteReset,
       "localReset": localReset,
       "resetCounterFlash": resetCounterFlash,
       "activateDevice": activateDevice,
       "lineTerminatError": lineTerminatError,
       "sfp1SetError": sfp1SetError,
       "sfp2SetError": sfp2SetError,
       "communicationBlock": communicationBlock,
       "los1Tpe1": los1Tpe1,
       "los2Tpe1": los2Tpe1,
       "yellowAlarmTpe1": yellowAlarmTpe1,
       "yellowAlarmTpe2": yellowAlarmTpe2,
       "communicationBlockTable": communicationBlockTable,
       "communicationBlockEntry": communicationBlockEntry,
       "communicationBlockLineIndex": communicationBlockLineIndex,
       "warning": warning,
       "alarm": alarm,
       "startLooptest": startLooptest,
       "passingLooptest": passingLooptest,
       "discreteIOTable": discreteIOTable,
       "discreteIOEntry": discreteIOEntry,
       "discreteIOLineIndex": discreteIOLineIndex,
       "discrete_Inputs": discrete_Inputs,
       "discrete_Outputs": discrete_Outputs,
       "discrete_InputsControl": discrete_InputsControl,
       "commandsTable": commandsTable,
       "commandsEntry": commandsEntry,
       "commandsLineIndex": commandsLineIndex,
       "commandsTX": commandsTX,
       "commandsRX": commandsRX}
)
