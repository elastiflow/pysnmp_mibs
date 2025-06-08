# SNMP MIB module (TROPIC-POWERMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-POWERMGMT-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:04:12 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(tnPowerMgmtMIB,
 tnSystemModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnPowerMgmtMIB",
    "tnSystemModules")

(tnShelfIndex,) = mibBuilder.importSymbols(
    "TROPIC-SHELF-MIB",
    "tnShelfIndex")

(tnSlotIndex,) = mibBuilder.importSymbols(
    "TROPIC-SLOT-MIB",
    "tnSlotIndex")

(AluWdmOtuBitRate,
 AluWdmOtuEncoding,
 TnCommand) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "AluWdmOtuBitRate",
    "AluWdmOtuEncoding",
    "TnCommand")

(tnChannel,
 tnDirection) = mibBuilder.importSymbols(
    "TROPIC-WAVEKEY-MIB",
    "tnChannel",
    "tnDirection")


# MODULE-IDENTITY

tnPowerMgmtMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    tnPowerMgmtMibModule.setRevisions(
        ("2008-02-16 12:00",
         "2008-10-16 12:00",
         "2010-05-10 12:00",
         "2010-06-16 12:00",
         "2010-06-23 12:00",
         "2010-11-10 12:00",
         "2011-04-03 12:00",
         "2011-05-23 12:00",
         "2011-07-22 12:00",
         "2011-07-29 12:00",
         "2011-08-03 12:00",
         "2011-08-12 12:00",
         "2011-11-05 12:00",
         "2011-11-21 12:00",
         "2011-11-26 12:00",
         "2011-12-14 12:00",
         "2012-01-04 12:00",
         "2012-05-18 12:00",
         "2012-06-13 12:00",
         "2012-09-01 12:00",
         "2012-11-05 12:00",
         "2013-01-10 12:00",
         "2013-05-20 12:00",
         "2013-11-25 12:00",
         "2013-12-06 12:00",
         "2014-09-10 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TropicPowerMgmtStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("completed", 1),
          ("inProgress", 2))
    )



class TropicPowerMgmtResult(SnmpAdminString):
    status = "current"
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class TropicPowerMgmtPercentCompleted(TextualConvention, Unsigned32):
    status = "current"


class TropicPowerMgmtType(TextualConvention, Integer32):
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
          ("manual", 2))
    )



class AluWdmWTDecoderUsageType(TextualConvention, Integer32):
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
        *(("wtdPpcOnAlmOn", 1),
          ("wtdPpcOffAlmOff", 2),
          ("wtdPpcOnAlmOff", 3),
          ("wtocm", 4),
          ("wtdInferred", 5),
          ("wtocmAd", 6))
    )



class AluWdmPowerMgmtSRSTiltAdjStatus(TextualConvention, Integer32):
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
        *(("completed", 1),
          ("inProgress", 2),
          ("notInProgress", 3))
    )



# MIB Managed Objects in the order of their OIDs

_TnPowerMgmtConf_ObjectIdentity = ObjectIdentity
tnPowerMgmtConf = _TnPowerMgmtConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1)
)
_TnPowerMgmtGroups_ObjectIdentity = ObjectIdentity
tnPowerMgmtGroups = _TnPowerMgmtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1)
)
_TnPowerMgmtCompliances_ObjectIdentity = ObjectIdentity
tnPowerMgmtCompliances = _TnPowerMgmtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 2)
)
_TnPowerMgmtObjs_ObjectIdentity = ObjectIdentity
tnPowerMgmtObjs = _TnPowerMgmtObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2)
)
_TnPowerMgmtBasics_ObjectIdentity = ObjectIdentity
tnPowerMgmtBasics = _TnPowerMgmtBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1)
)
_TnPowerMgmtGlobal_ObjectIdentity = ObjectIdentity
tnPowerMgmtGlobal = _TnPowerMgmtGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 1)
)
_TnPowerMgmtGlobalMinStepSize_Type = Unsigned32
_TnPowerMgmtGlobalMinStepSize_Object = MibScalar
tnPowerMgmtGlobalMinStepSize = _TnPowerMgmtGlobalMinStepSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 1, 2),
    _TnPowerMgmtGlobalMinStepSize_Type()
)
tnPowerMgmtGlobalMinStepSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPowerMgmtGlobalMinStepSize.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtGlobalMinStepSize.setUnits("mB")
_TnPowerMgmtGlobalMaxStepSize_Type = Unsigned32
_TnPowerMgmtGlobalMaxStepSize_Object = MibScalar
tnPowerMgmtGlobalMaxStepSize = _TnPowerMgmtGlobalMaxStepSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 1, 3),
    _TnPowerMgmtGlobalMaxStepSize_Type()
)
tnPowerMgmtGlobalMaxStepSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPowerMgmtGlobalMaxStepSize.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtGlobalMaxStepSize.setUnits("mB")
_TnPowerMgmtGlobalResetToDefaults_Type = TnCommand
_TnPowerMgmtGlobalResetToDefaults_Object = MibScalar
tnPowerMgmtGlobalResetToDefaults = _TnPowerMgmtGlobalResetToDefaults_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 1, 4),
    _TnPowerMgmtGlobalResetToDefaults_Type()
)
tnPowerMgmtGlobalResetToDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPowerMgmtGlobalResetToDefaults.setStatus("current")
_TnPowerMgmtGlobalAutoEnabled_Type = TruthValue
_TnPowerMgmtGlobalAutoEnabled_Object = MibScalar
tnPowerMgmtGlobalAutoEnabled = _TnPowerMgmtGlobalAutoEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 1, 5),
    _TnPowerMgmtGlobalAutoEnabled_Type()
)
tnPowerMgmtGlobalAutoEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPowerMgmtGlobalAutoEnabled.setStatus("current")
_TnPowerMgmtGlobalNumberOfAutoPowerAdjPoints_Type = Unsigned32
_TnPowerMgmtGlobalNumberOfAutoPowerAdjPoints_Object = MibScalar
tnPowerMgmtGlobalNumberOfAutoPowerAdjPoints = _TnPowerMgmtGlobalNumberOfAutoPowerAdjPoints_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 1, 6),
    _TnPowerMgmtGlobalNumberOfAutoPowerAdjPoints_Type()
)
tnPowerMgmtGlobalNumberOfAutoPowerAdjPoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtGlobalNumberOfAutoPowerAdjPoints.setStatus("current")
_TnPowerMgmtGlobalAlarmWhenDisabled_Type = TruthValue
_TnPowerMgmtGlobalAlarmWhenDisabled_Object = MibScalar
tnPowerMgmtGlobalAlarmWhenDisabled = _TnPowerMgmtGlobalAlarmWhenDisabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 1, 7),
    _TnPowerMgmtGlobalAlarmWhenDisabled_Type()
)
tnPowerMgmtGlobalAlarmWhenDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPowerMgmtGlobalAlarmWhenDisabled.setStatus("current")
_TnPowerMgmtControlTable_Object = MibTable
tnPowerMgmtControlTable = _TnPowerMgmtControlTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tnPowerMgmtControlTable.setStatus("current")
_TnPowerMgmtControlEntry_Object = MibTableRow
tnPowerMgmtControlEntry = _TnPowerMgmtControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 2, 1)
)
tnPowerMgmtControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-POWERMGMT-MIB", "tnPowerMgmtDirection"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtControlEntry.setStatus("current")


class _TnPowerMgmtDirection_Type(Integer32):
    """Custom type tnPowerMgmtDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tx", 1),
          ("rx", 2))
    )


_TnPowerMgmtDirection_Type.__name__ = "Integer32"
_TnPowerMgmtDirection_Object = MibTableColumn
tnPowerMgmtDirection = _TnPowerMgmtDirection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 2, 1, 1),
    _TnPowerMgmtDirection_Type()
)
tnPowerMgmtDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPowerMgmtDirection.setStatus("current")
_TnPowerMgmtControlPercentCompleted_Type = TropicPowerMgmtPercentCompleted
_TnPowerMgmtControlPercentCompleted_Object = MibTableColumn
tnPowerMgmtControlPercentCompleted = _TnPowerMgmtControlPercentCompleted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 2, 1, 3),
    _TnPowerMgmtControlPercentCompleted_Type()
)
tnPowerMgmtControlPercentCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtControlPercentCompleted.setStatus("current")
_TnPowerMgmtControlRowStatus_Type = RowStatus
_TnPowerMgmtControlRowStatus_Object = MibTableColumn
tnPowerMgmtControlRowStatus = _TnPowerMgmtControlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 2, 1, 5),
    _TnPowerMgmtControlRowStatus_Type()
)
tnPowerMgmtControlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtControlRowStatus.setStatus("current")
_TnPowerMgmtIngressTable_Object = MibTable
tnPowerMgmtIngressTable = _TnPowerMgmtIngressTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tnPowerMgmtIngressTable.setStatus("current")
_TnPowerMgmtIngressEntry_Object = MibTableRow
tnPowerMgmtIngressEntry = _TnPowerMgmtIngressEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1)
)
tnPowerMgmtIngressEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtIngressEntry.setStatus("current")


class _TnPowerMgmtIngressAdjustPowerGain_Type(Integer32):
    """Custom type tnPowerMgmtIngressAdjustPowerGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("execute", 2),
          ("executeWithForce", 3))
    )


_TnPowerMgmtIngressAdjustPowerGain_Type.__name__ = "Integer32"
_TnPowerMgmtIngressAdjustPowerGain_Object = MibTableColumn
tnPowerMgmtIngressAdjustPowerGain = _TnPowerMgmtIngressAdjustPowerGain_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 1),
    _TnPowerMgmtIngressAdjustPowerGain_Type()
)
tnPowerMgmtIngressAdjustPowerGain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressAdjustPowerGain.setStatus("current")
_TnPowerMgmtIngressAdjustPowerGainLastResult_Type = TropicPowerMgmtResult
_TnPowerMgmtIngressAdjustPowerGainLastResult_Object = MibTableColumn
tnPowerMgmtIngressAdjustPowerGainLastResult = _TnPowerMgmtIngressAdjustPowerGainLastResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 2),
    _TnPowerMgmtIngressAdjustPowerGainLastResult_Type()
)
tnPowerMgmtIngressAdjustPowerGainLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressAdjustPowerGainLastResult.setStatus("current")


class _TnPowerMgmtIngressAcceptPowers_Type(Integer32):
    """Custom type tnPowerMgmtIngressAcceptPowers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("execute", 2),
          ("executeWithClear", 3))
    )


_TnPowerMgmtIngressAcceptPowers_Type.__name__ = "Integer32"
_TnPowerMgmtIngressAcceptPowers_Object = MibTableColumn
tnPowerMgmtIngressAcceptPowers = _TnPowerMgmtIngressAcceptPowers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 3),
    _TnPowerMgmtIngressAcceptPowers_Type()
)
tnPowerMgmtIngressAcceptPowers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressAcceptPowers.setStatus("current")
_TnPowerMgmtIngressAcceptPowersLastResult_Type = TropicPowerMgmtResult
_TnPowerMgmtIngressAcceptPowersLastResult_Object = MibTableColumn
tnPowerMgmtIngressAcceptPowersLastResult = _TnPowerMgmtIngressAcceptPowersLastResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 4),
    _TnPowerMgmtIngressAcceptPowersLastResult_Type()
)
tnPowerMgmtIngressAcceptPowersLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressAcceptPowersLastResult.setStatus("current")
_TnPowerMgmtIngressRippleAllowance_Type = Integer32
_TnPowerMgmtIngressRippleAllowance_Object = MibTableColumn
tnPowerMgmtIngressRippleAllowance = _TnPowerMgmtIngressRippleAllowance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 5),
    _TnPowerMgmtIngressRippleAllowance_Type()
)
tnPowerMgmtIngressRippleAllowance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressRippleAllowance.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressRippleAllowance.setUnits("mB")
_TnPowerMgmtIngressAdjustPowerGainTargetGain_Type = Unsigned32
_TnPowerMgmtIngressAdjustPowerGainTargetGain_Object = MibTableColumn
tnPowerMgmtIngressAdjustPowerGainTargetGain = _TnPowerMgmtIngressAdjustPowerGainTargetGain_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 6),
    _TnPowerMgmtIngressAdjustPowerGainTargetGain_Type()
)
tnPowerMgmtIngressAdjustPowerGainTargetGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressAdjustPowerGainTargetGain.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressAdjustPowerGainTargetGain.setUnits("mB")
_TnPowerMgmtIngressAdjustPowerGainStatus_Type = TropicPowerMgmtStatus
_TnPowerMgmtIngressAdjustPowerGainStatus_Object = MibTableColumn
tnPowerMgmtIngressAdjustPowerGainStatus = _TnPowerMgmtIngressAdjustPowerGainStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 7),
    _TnPowerMgmtIngressAdjustPowerGainStatus_Type()
)
tnPowerMgmtIngressAdjustPowerGainStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressAdjustPowerGainStatus.setStatus("current")
_TnPowerMgmtIngressStartAseAdjust_Type = TnCommand
_TnPowerMgmtIngressStartAseAdjust_Object = MibTableColumn
tnPowerMgmtIngressStartAseAdjust = _TnPowerMgmtIngressStartAseAdjust_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 8),
    _TnPowerMgmtIngressStartAseAdjust_Type()
)
tnPowerMgmtIngressStartAseAdjust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressStartAseAdjust.setStatus("current")
_TnPowerMgmtIngressAseAdjustLastResult_Type = TropicPowerMgmtResult
_TnPowerMgmtIngressAseAdjustLastResult_Object = MibTableColumn
tnPowerMgmtIngressAseAdjustLastResult = _TnPowerMgmtIngressAseAdjustLastResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 9),
    _TnPowerMgmtIngressAseAdjustLastResult_Type()
)
tnPowerMgmtIngressAseAdjustLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressAseAdjustLastResult.setStatus("current")
_TnPowerMgmtIngressAseAdjustStatus_Type = TropicPowerMgmtStatus
_TnPowerMgmtIngressAseAdjustStatus_Object = MibTableColumn
tnPowerMgmtIngressAseAdjustStatus = _TnPowerMgmtIngressAseAdjustStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 10),
    _TnPowerMgmtIngressAseAdjustStatus_Type()
)
tnPowerMgmtIngressAseAdjustStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressAseAdjustStatus.setStatus("current")


class _TnPowerMgmtIngressCommissioned_Type(TruthValue):
    """Custom type tnPowerMgmtIngressCommissioned based on TruthValue"""
    defaultValue = 2


_TnPowerMgmtIngressCommissioned_Type.__name__ = "TruthValue"
_TnPowerMgmtIngressCommissioned_Object = MibTableColumn
tnPowerMgmtIngressCommissioned = _TnPowerMgmtIngressCommissioned_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 11),
    _TnPowerMgmtIngressCommissioned_Type()
)
tnPowerMgmtIngressCommissioned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressCommissioned.setStatus("current")


class _TnPowerMgmtIngressGainSetOffset_Type(Integer32):
    """Custom type tnPowerMgmtIngressGainSetOffset based on Integer32"""
    defaultValue = 0


_TnPowerMgmtIngressGainSetOffset_Type.__name__ = "Integer32"
_TnPowerMgmtIngressGainSetOffset_Object = MibTableColumn
tnPowerMgmtIngressGainSetOffset = _TnPowerMgmtIngressGainSetOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 12),
    _TnPowerMgmtIngressGainSetOffset_Type()
)
tnPowerMgmtIngressGainSetOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressGainSetOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressGainSetOffset.setUnits("mB")


class _TnPowerMgmtIngressCommissionedGain_Type(Integer32):
    """Custom type tnPowerMgmtIngressCommissionedGain based on Integer32"""
    defaultValue = 0


_TnPowerMgmtIngressCommissionedGain_Type.__name__ = "Integer32"
_TnPowerMgmtIngressCommissionedGain_Object = MibTableColumn
tnPowerMgmtIngressCommissionedGain = _TnPowerMgmtIngressCommissionedGain_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 13),
    _TnPowerMgmtIngressCommissionedGain_Type()
)
tnPowerMgmtIngressCommissionedGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressCommissionedGain.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressCommissionedGain.setUnits("mB")


class _TnPowerMgmtIngressSRSTiltPostFraction_Type(Integer32):
    """Custom type tnPowerMgmtIngressSRSTiltPostFraction based on Integer32"""
    defaultValue = 0


_TnPowerMgmtIngressSRSTiltPostFraction_Type.__name__ = "Integer32"
_TnPowerMgmtIngressSRSTiltPostFraction_Object = MibTableColumn
tnPowerMgmtIngressSRSTiltPostFraction = _TnPowerMgmtIngressSRSTiltPostFraction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 14),
    _TnPowerMgmtIngressSRSTiltPostFraction_Type()
)
tnPowerMgmtIngressSRSTiltPostFraction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressSRSTiltPostFraction.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressSRSTiltPostFraction.setUnits("100ths")


class _TnPowerMgmtIngressSRSTiltAdjResult_Type(TropicPowerMgmtResult):
    """Custom type tnPowerMgmtIngressSRSTiltAdjResult based on TropicPowerMgmtResult"""
    defaultValue = OctetString("Not applicable")


_TnPowerMgmtIngressSRSTiltAdjResult_Type.__name__ = "TropicPowerMgmtResult"
_TnPowerMgmtIngressSRSTiltAdjResult_Object = MibTableColumn
tnPowerMgmtIngressSRSTiltAdjResult = _TnPowerMgmtIngressSRSTiltAdjResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 15),
    _TnPowerMgmtIngressSRSTiltAdjResult_Type()
)
tnPowerMgmtIngressSRSTiltAdjResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressSRSTiltAdjResult.setStatus("current")


class _TnPowerMgmtIngressSRSTiltAdjStatus_Type(AluWdmPowerMgmtSRSTiltAdjStatus):
    """Custom type tnPowerMgmtIngressSRSTiltAdjStatus based on AluWdmPowerMgmtSRSTiltAdjStatus"""
    defaultValue = 3


_TnPowerMgmtIngressSRSTiltAdjStatus_Type.__name__ = "AluWdmPowerMgmtSRSTiltAdjStatus"
_TnPowerMgmtIngressSRSTiltAdjStatus_Object = MibTableColumn
tnPowerMgmtIngressSRSTiltAdjStatus = _TnPowerMgmtIngressSRSTiltAdjStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 16),
    _TnPowerMgmtIngressSRSTiltAdjStatus_Type()
)
tnPowerMgmtIngressSRSTiltAdjStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressSRSTiltAdjStatus.setStatus("current")


class _TnPowerMgmtIngressPassed_Type(TruthValue):
    """Custom type tnPowerMgmtIngressPassed based on TruthValue"""
    defaultValue = 1


_TnPowerMgmtIngressPassed_Type.__name__ = "TruthValue"
_TnPowerMgmtIngressPassed_Object = MibTableColumn
tnPowerMgmtIngressPassed = _TnPowerMgmtIngressPassed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 17),
    _TnPowerMgmtIngressPassed_Type()
)
tnPowerMgmtIngressPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPassed.setStatus("current")


class _TnPowerMgmtIngressSRSTiltCalcOffset_Type(Integer32):
    """Custom type tnPowerMgmtIngressSRSTiltCalcOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_TnPowerMgmtIngressSRSTiltCalcOffset_Type.__name__ = "Integer32"
_TnPowerMgmtIngressSRSTiltCalcOffset_Object = MibTableColumn
tnPowerMgmtIngressSRSTiltCalcOffset = _TnPowerMgmtIngressSRSTiltCalcOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 18),
    _TnPowerMgmtIngressSRSTiltCalcOffset_Type()
)
tnPowerMgmtIngressSRSTiltCalcOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressSRSTiltCalcOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressSRSTiltCalcOffset.setUnits("mB")
_TnPowerMgmtEgressTable_Object = MibTable
tnPowerMgmtEgressTable = _TnPowerMgmtEgressTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tnPowerMgmtEgressTable.setStatus("current")
_TnPowerMgmtEgressEntry_Object = MibTableRow
tnPowerMgmtEgressEntry = _TnPowerMgmtEgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1)
)
tnPowerMgmtEgressEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtEgressEntry.setStatus("current")
_TnPowerMgmtEgressAdjustPowerWithOptimization_Type = TnCommand
_TnPowerMgmtEgressAdjustPowerWithOptimization_Object = MibTableColumn
tnPowerMgmtEgressAdjustPowerWithOptimization = _TnPowerMgmtEgressAdjustPowerWithOptimization_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 1),
    _TnPowerMgmtEgressAdjustPowerWithOptimization_Type()
)
tnPowerMgmtEgressAdjustPowerWithOptimization.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressAdjustPowerWithOptimization.setStatus("current")
_TnPowerMgmtEgressAdjustPowerWithOptimizationStatus_Type = TropicPowerMgmtStatus
_TnPowerMgmtEgressAdjustPowerWithOptimizationStatus_Object = MibTableColumn
tnPowerMgmtEgressAdjustPowerWithOptimizationStatus = _TnPowerMgmtEgressAdjustPowerWithOptimizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 2),
    _TnPowerMgmtEgressAdjustPowerWithOptimizationStatus_Type()
)
tnPowerMgmtEgressAdjustPowerWithOptimizationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressAdjustPowerWithOptimizationStatus.setStatus("current")
_TnPowerMgmtEgressAdjustPowerWithOptimizationAbort_Type = TnCommand
_TnPowerMgmtEgressAdjustPowerWithOptimizationAbort_Object = MibTableColumn
tnPowerMgmtEgressAdjustPowerWithOptimizationAbort = _TnPowerMgmtEgressAdjustPowerWithOptimizationAbort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 3),
    _TnPowerMgmtEgressAdjustPowerWithOptimizationAbort_Type()
)
tnPowerMgmtEgressAdjustPowerWithOptimizationAbort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressAdjustPowerWithOptimizationAbort.setStatus("current")
_TnPowerMgmtEgressAcceptPowers_Type = TnCommand
_TnPowerMgmtEgressAcceptPowers_Object = MibTableColumn
tnPowerMgmtEgressAcceptPowers = _TnPowerMgmtEgressAcceptPowers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 4),
    _TnPowerMgmtEgressAcceptPowers_Type()
)
tnPowerMgmtEgressAcceptPowers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressAcceptPowers.setStatus("current")
_TnPowerMgmtEgressAdjustPowerWithOptimizationLastResult_Type = TropicPowerMgmtResult
_TnPowerMgmtEgressAdjustPowerWithOptimizationLastResult_Object = MibTableColumn
tnPowerMgmtEgressAdjustPowerWithOptimizationLastResult = _TnPowerMgmtEgressAdjustPowerWithOptimizationLastResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 6),
    _TnPowerMgmtEgressAdjustPowerWithOptimizationLastResult_Type()
)
tnPowerMgmtEgressAdjustPowerWithOptimizationLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressAdjustPowerWithOptimizationLastResult.setStatus("current")
_TnPowerMgmtEgressAcceptPowersLastResult_Type = TropicPowerMgmtResult
_TnPowerMgmtEgressAcceptPowersLastResult_Object = MibTableColumn
tnPowerMgmtEgressAcceptPowersLastResult = _TnPowerMgmtEgressAcceptPowersLastResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 7),
    _TnPowerMgmtEgressAcceptPowersLastResult_Type()
)
tnPowerMgmtEgressAcceptPowersLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressAcceptPowersLastResult.setStatus("current")
_TnPowerMgmtEgressAdjustPowerWithOptimizationTargetGain_Type = Unsigned32
_TnPowerMgmtEgressAdjustPowerWithOptimizationTargetGain_Object = MibTableColumn
tnPowerMgmtEgressAdjustPowerWithOptimizationTargetGain = _TnPowerMgmtEgressAdjustPowerWithOptimizationTargetGain_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 9),
    _TnPowerMgmtEgressAdjustPowerWithOptimizationTargetGain_Type()
)
tnPowerMgmtEgressAdjustPowerWithOptimizationTargetGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressAdjustPowerWithOptimizationTargetGain.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressAdjustPowerWithOptimizationTargetGain.setUnits("mB")
_TnPowerMgmtEgressStartAseAdjust_Type = TnCommand
_TnPowerMgmtEgressStartAseAdjust_Object = MibTableColumn
tnPowerMgmtEgressStartAseAdjust = _TnPowerMgmtEgressStartAseAdjust_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 10),
    _TnPowerMgmtEgressStartAseAdjust_Type()
)
tnPowerMgmtEgressStartAseAdjust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressStartAseAdjust.setStatus("current")
_TnPowerMgmtEgressStopAseAdjust_Type = TnCommand
_TnPowerMgmtEgressStopAseAdjust_Object = MibTableColumn
tnPowerMgmtEgressStopAseAdjust = _TnPowerMgmtEgressStopAseAdjust_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 11),
    _TnPowerMgmtEgressStopAseAdjust_Type()
)
tnPowerMgmtEgressStopAseAdjust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressStopAseAdjust.setStatus("current")
_TnPowerMgmtEgressAseAdjustLastResult_Type = TropicPowerMgmtResult
_TnPowerMgmtEgressAseAdjustLastResult_Object = MibTableColumn
tnPowerMgmtEgressAseAdjustLastResult = _TnPowerMgmtEgressAseAdjustLastResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 12),
    _TnPowerMgmtEgressAseAdjustLastResult_Type()
)
tnPowerMgmtEgressAseAdjustLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressAseAdjustLastResult.setStatus("current")
_TnPowerMgmtEgressAseAdjustStatus_Type = TropicPowerMgmtStatus
_TnPowerMgmtEgressAseAdjustStatus_Object = MibTableColumn
tnPowerMgmtEgressAseAdjustStatus = _TnPowerMgmtEgressAseAdjustStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 13),
    _TnPowerMgmtEgressAseAdjustStatus_Type()
)
tnPowerMgmtEgressAseAdjustStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressAseAdjustStatus.setStatus("current")


class _TnPowerMgmtEgressCommissioned_Type(TruthValue):
    """Custom type tnPowerMgmtEgressCommissioned based on TruthValue"""
    defaultValue = 2


_TnPowerMgmtEgressCommissioned_Type.__name__ = "TruthValue"
_TnPowerMgmtEgressCommissioned_Object = MibTableColumn
tnPowerMgmtEgressCommissioned = _TnPowerMgmtEgressCommissioned_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 14),
    _TnPowerMgmtEgressCommissioned_Type()
)
tnPowerMgmtEgressCommissioned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressCommissioned.setStatus("current")
_TnPowerMgmtEgressAmpIfIndex_Type = InterfaceIndex
_TnPowerMgmtEgressAmpIfIndex_Object = MibTableColumn
tnPowerMgmtEgressAmpIfIndex = _TnPowerMgmtEgressAmpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 15),
    _TnPowerMgmtEgressAmpIfIndex_Type()
)
tnPowerMgmtEgressAmpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressAmpIfIndex.setStatus("current")
_TnPowerMgmtEgressWssIfIndex_Type = InterfaceIndex
_TnPowerMgmtEgressWssIfIndex_Object = MibTableColumn
tnPowerMgmtEgressWssIfIndex = _TnPowerMgmtEgressWssIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 16),
    _TnPowerMgmtEgressWssIfIndex_Type()
)
tnPowerMgmtEgressWssIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressWssIfIndex.setStatus("current")


class _TnPowerMgmtEgressSRSTiltCalcMultiplier_Type(Integer32):
    """Custom type tnPowerMgmtEgressSRSTiltCalcMultiplier based on Integer32"""
    defaultValue = 100


_TnPowerMgmtEgressSRSTiltCalcMultiplier_Type.__name__ = "Integer32"
_TnPowerMgmtEgressSRSTiltCalcMultiplier_Object = MibTableColumn
tnPowerMgmtEgressSRSTiltCalcMultiplier = _TnPowerMgmtEgressSRSTiltCalcMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 17),
    _TnPowerMgmtEgressSRSTiltCalcMultiplier_Type()
)
tnPowerMgmtEgressSRSTiltCalcMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressSRSTiltCalcMultiplier.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressSRSTiltCalcMultiplier.setUnits("100ths")


class _TnPowerMgmtEgressSRSTiltPreFraction_Type(Integer32):
    """Custom type tnPowerMgmtEgressSRSTiltPreFraction based on Integer32"""
    defaultValue = 0


_TnPowerMgmtEgressSRSTiltPreFraction_Type.__name__ = "Integer32"
_TnPowerMgmtEgressSRSTiltPreFraction_Object = MibTableColumn
tnPowerMgmtEgressSRSTiltPreFraction = _TnPowerMgmtEgressSRSTiltPreFraction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 18),
    _TnPowerMgmtEgressSRSTiltPreFraction_Type()
)
tnPowerMgmtEgressSRSTiltPreFraction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressSRSTiltPreFraction.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressSRSTiltPreFraction.setUnits("100ths")


class _TnPowerMgmtEgressSRSTiltCalcACoeff_Type(Integer32):
    """Custom type tnPowerMgmtEgressSRSTiltCalcACoeff based on Integer32"""
    defaultValue = 0


_TnPowerMgmtEgressSRSTiltCalcACoeff_Type.__name__ = "Integer32"
_TnPowerMgmtEgressSRSTiltCalcACoeff_Object = MibTableColumn
tnPowerMgmtEgressSRSTiltCalcACoeff = _TnPowerMgmtEgressSRSTiltCalcACoeff_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 19),
    _TnPowerMgmtEgressSRSTiltCalcACoeff_Type()
)
tnPowerMgmtEgressSRSTiltCalcACoeff.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressSRSTiltCalcACoeff.setStatus("current")


class _TnPowerMgmtEgressSRSTiltCalcOutputLoss_Type(Integer32):
    """Custom type tnPowerMgmtEgressSRSTiltCalcOutputLoss based on Integer32"""
    defaultValue = 0


_TnPowerMgmtEgressSRSTiltCalcOutputLoss_Type.__name__ = "Integer32"
_TnPowerMgmtEgressSRSTiltCalcOutputLoss_Object = MibTableColumn
tnPowerMgmtEgressSRSTiltCalcOutputLoss = _TnPowerMgmtEgressSRSTiltCalcOutputLoss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 20),
    _TnPowerMgmtEgressSRSTiltCalcOutputLoss_Type()
)
tnPowerMgmtEgressSRSTiltCalcOutputLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressSRSTiltCalcOutputLoss.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressSRSTiltCalcOutputLoss.setUnits("mB")


class _TnPowerMgmtEgressSRSTiltAdjResult_Type(TropicPowerMgmtResult):
    """Custom type tnPowerMgmtEgressSRSTiltAdjResult based on TropicPowerMgmtResult"""
    defaultValue = OctetString("Not applicable")


_TnPowerMgmtEgressSRSTiltAdjResult_Type.__name__ = "TropicPowerMgmtResult"
_TnPowerMgmtEgressSRSTiltAdjResult_Object = MibTableColumn
tnPowerMgmtEgressSRSTiltAdjResult = _TnPowerMgmtEgressSRSTiltAdjResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 22),
    _TnPowerMgmtEgressSRSTiltAdjResult_Type()
)
tnPowerMgmtEgressSRSTiltAdjResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressSRSTiltAdjResult.setStatus("current")


class _TnPowerMgmtEgressSRSTiltAdjStatus_Type(AluWdmPowerMgmtSRSTiltAdjStatus):
    """Custom type tnPowerMgmtEgressSRSTiltAdjStatus based on AluWdmPowerMgmtSRSTiltAdjStatus"""
    defaultValue = 3


_TnPowerMgmtEgressSRSTiltAdjStatus_Type.__name__ = "AluWdmPowerMgmtSRSTiltAdjStatus"
_TnPowerMgmtEgressSRSTiltAdjStatus_Object = MibTableColumn
tnPowerMgmtEgressSRSTiltAdjStatus = _TnPowerMgmtEgressSRSTiltAdjStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 23),
    _TnPowerMgmtEgressSRSTiltAdjStatus_Type()
)
tnPowerMgmtEgressSRSTiltAdjStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressSRSTiltAdjStatus.setStatus("current")


class _TnPowerMgmtEgressPassed_Type(TruthValue):
    """Custom type tnPowerMgmtEgressPassed based on TruthValue"""
    defaultValue = 1


_TnPowerMgmtEgressPassed_Type.__name__ = "TruthValue"
_TnPowerMgmtEgressPassed_Object = MibTableColumn
tnPowerMgmtEgressPassed = _TnPowerMgmtEgressPassed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 24),
    _TnPowerMgmtEgressPassed_Type()
)
tnPowerMgmtEgressPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPassed.setStatus("current")


class _TnPowerMgmtEgressLHLaunchAtten_Type(Integer32):
    """Custom type tnPowerMgmtEgressLHLaunchAtten based on Integer32"""
    defaultValue = 0


_TnPowerMgmtEgressLHLaunchAtten_Type.__name__ = "Integer32"
_TnPowerMgmtEgressLHLaunchAtten_Object = MibTableColumn
tnPowerMgmtEgressLHLaunchAtten = _TnPowerMgmtEgressLHLaunchAtten_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 25),
    _TnPowerMgmtEgressLHLaunchAtten_Type()
)
tnPowerMgmtEgressLHLaunchAtten.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressLHLaunchAtten.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressLHLaunchAtten.setUnits("mB")


class _TnPowerMgmtFiberSpanTiltPreComp_Type(Unsigned32):
    """Custom type tnPowerMgmtFiberSpanTiltPreComp based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_TnPowerMgmtFiberSpanTiltPreComp_Type.__name__ = "Unsigned32"
_TnPowerMgmtFiberSpanTiltPreComp_Object = MibTableColumn
tnPowerMgmtFiberSpanTiltPreComp = _TnPowerMgmtFiberSpanTiltPreComp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 27),
    _TnPowerMgmtFiberSpanTiltPreComp_Type()
)
tnPowerMgmtFiberSpanTiltPreComp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtFiberSpanTiltPreComp.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtFiberSpanTiltPreComp.setUnits("mB")
_TnPowerMgmtPortTable_Object = MibTable
tnPowerMgmtPortTable = _TnPowerMgmtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7)
)
if mibBuilder.loadTexts:
    tnPowerMgmtPortTable.setStatus("current")
_TnPowerMgmtPortEntry_Object = MibTableRow
tnPowerMgmtPortEntry = _TnPowerMgmtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1)
)
tnPowerMgmtPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtPortEntry.setStatus("current")


class _TnPowerMgmtPortIsCommissioned_Type(TruthValue):
    """Custom type tnPowerMgmtPortIsCommissioned based on TruthValue"""
    defaultValue = 2


_TnPowerMgmtPortIsCommissioned_Type.__name__ = "TruthValue"
_TnPowerMgmtPortIsCommissioned_Object = MibTableColumn
tnPowerMgmtPortIsCommissioned = _TnPowerMgmtPortIsCommissioned_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 1),
    _TnPowerMgmtPortIsCommissioned_Type()
)
tnPowerMgmtPortIsCommissioned.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortIsCommissioned.setStatus("current")
_TnPowerMgmtPortTypeIn_Type = TropicPowerMgmtType
_TnPowerMgmtPortTypeIn_Object = MibTableColumn
tnPowerMgmtPortTypeIn = _TnPowerMgmtPortTypeIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 2),
    _TnPowerMgmtPortTypeIn_Type()
)
tnPowerMgmtPortTypeIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortTypeIn.setStatus("current")
_TnPowerMgmtPortTypeOut_Type = TropicPowerMgmtType
_TnPowerMgmtPortTypeOut_Object = MibTableColumn
tnPowerMgmtPortTypeOut = _TnPowerMgmtPortTypeOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 3),
    _TnPowerMgmtPortTypeOut_Type()
)
tnPowerMgmtPortTypeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortTypeOut.setStatus("current")


class _TnPowerMgmtPortWTDecoderUsageTypeIn_Type(AluWdmWTDecoderUsageType):
    """Custom type tnPowerMgmtPortWTDecoderUsageTypeIn based on AluWdmWTDecoderUsageType"""
    defaultValue = 2


_TnPowerMgmtPortWTDecoderUsageTypeIn_Type.__name__ = "AluWdmWTDecoderUsageType"
_TnPowerMgmtPortWTDecoderUsageTypeIn_Object = MibTableColumn
tnPowerMgmtPortWTDecoderUsageTypeIn = _TnPowerMgmtPortWTDecoderUsageTypeIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 6),
    _TnPowerMgmtPortWTDecoderUsageTypeIn_Type()
)
tnPowerMgmtPortWTDecoderUsageTypeIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortWTDecoderUsageTypeIn.setStatus("current")


class _TnPowerMgmtPortWTDecoderUsageTypeOut_Type(AluWdmWTDecoderUsageType):
    """Custom type tnPowerMgmtPortWTDecoderUsageTypeOut based on AluWdmWTDecoderUsageType"""
    defaultValue = 2


_TnPowerMgmtPortWTDecoderUsageTypeOut_Type.__name__ = "AluWdmWTDecoderUsageType"
_TnPowerMgmtPortWTDecoderUsageTypeOut_Object = MibTableColumn
tnPowerMgmtPortWTDecoderUsageTypeOut = _TnPowerMgmtPortWTDecoderUsageTypeOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 7),
    _TnPowerMgmtPortWTDecoderUsageTypeOut_Type()
)
tnPowerMgmtPortWTDecoderUsageTypeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortWTDecoderUsageTypeOut.setStatus("current")


class _TnPowerMgmtPortGainAdjSchedBase_Type(Integer32):
    """Custom type tnPowerMgmtPortGainAdjSchedBase based on Integer32"""
    defaultValue = -1


_TnPowerMgmtPortGainAdjSchedBase_Type.__name__ = "Integer32"
_TnPowerMgmtPortGainAdjSchedBase_Object = MibTableColumn
tnPowerMgmtPortGainAdjSchedBase = _TnPowerMgmtPortGainAdjSchedBase_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 8),
    _TnPowerMgmtPortGainAdjSchedBase_Type()
)
tnPowerMgmtPortGainAdjSchedBase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortGainAdjSchedBase.setStatus("current")


class _TnPowerMgmtPortGainAdjTimerPeriod_Type(Integer32):
    """Custom type tnPowerMgmtPortGainAdjTimerPeriod based on Integer32"""
    defaultValue = -1


_TnPowerMgmtPortGainAdjTimerPeriod_Type.__name__ = "Integer32"
_TnPowerMgmtPortGainAdjTimerPeriod_Object = MibTableColumn
tnPowerMgmtPortGainAdjTimerPeriod = _TnPowerMgmtPortGainAdjTimerPeriod_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 9),
    _TnPowerMgmtPortGainAdjTimerPeriod_Type()
)
tnPowerMgmtPortGainAdjTimerPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortGainAdjTimerPeriod.setStatus("current")


class _TnPowerMgmtPortGainAdjTimerLength_Type(Integer32):
    """Custom type tnPowerMgmtPortGainAdjTimerLength based on Integer32"""
    defaultValue = -1


_TnPowerMgmtPortGainAdjTimerLength_Type.__name__ = "Integer32"
_TnPowerMgmtPortGainAdjTimerLength_Object = MibTableColumn
tnPowerMgmtPortGainAdjTimerLength = _TnPowerMgmtPortGainAdjTimerLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 10),
    _TnPowerMgmtPortGainAdjTimerLength_Type()
)
tnPowerMgmtPortGainAdjTimerLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortGainAdjTimerLength.setStatus("current")


class _TnPowerMgmtPortInGainAdjAutoEnabled_Type(TruthValue):
    """Custom type tnPowerMgmtPortInGainAdjAutoEnabled based on TruthValue"""
    defaultValue = 2


_TnPowerMgmtPortInGainAdjAutoEnabled_Type.__name__ = "TruthValue"
_TnPowerMgmtPortInGainAdjAutoEnabled_Object = MibTableColumn
tnPowerMgmtPortInGainAdjAutoEnabled = _TnPowerMgmtPortInGainAdjAutoEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 11),
    _TnPowerMgmtPortInGainAdjAutoEnabled_Type()
)
tnPowerMgmtPortInGainAdjAutoEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortInGainAdjAutoEnabled.setStatus("current")


class _TnPowerMgmtPortSRSTiltAdjAutoEnabled_Type(TruthValue):
    """Custom type tnPowerMgmtPortSRSTiltAdjAutoEnabled based on TruthValue"""
    defaultValue = 2


_TnPowerMgmtPortSRSTiltAdjAutoEnabled_Type.__name__ = "TruthValue"
_TnPowerMgmtPortSRSTiltAdjAutoEnabled_Object = MibTableColumn
tnPowerMgmtPortSRSTiltAdjAutoEnabled = _TnPowerMgmtPortSRSTiltAdjAutoEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 12),
    _TnPowerMgmtPortSRSTiltAdjAutoEnabled_Type()
)
tnPowerMgmtPortSRSTiltAdjAutoEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortSRSTiltAdjAutoEnabled.setStatus("current")


class _TnPowerMgmtPortFiberSpanTilt_Type(Unsigned32):
    """Custom type tnPowerMgmtPortFiberSpanTilt based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_TnPowerMgmtPortFiberSpanTilt_Type.__name__ = "Unsigned32"
_TnPowerMgmtPortFiberSpanTilt_Object = MibTableColumn
tnPowerMgmtPortFiberSpanTilt = _TnPowerMgmtPortFiberSpanTilt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 13),
    _TnPowerMgmtPortFiberSpanTilt_Type()
)
tnPowerMgmtPortFiberSpanTilt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortFiberSpanTilt.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtPortFiberSpanTilt.setUnits("mB")


class _TnPowerMgmtPortSRSTiltMaintenanceMode_Type(TruthValue):
    """Custom type tnPowerMgmtPortSRSTiltMaintenanceMode based on TruthValue"""
    defaultValue = 2


_TnPowerMgmtPortSRSTiltMaintenanceMode_Type.__name__ = "TruthValue"
_TnPowerMgmtPortSRSTiltMaintenanceMode_Object = MibTableColumn
tnPowerMgmtPortSRSTiltMaintenanceMode = _TnPowerMgmtPortSRSTiltMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 14),
    _TnPowerMgmtPortSRSTiltMaintenanceMode_Type()
)
tnPowerMgmtPortSRSTiltMaintenanceMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortSRSTiltMaintenanceMode.setStatus("current")


class _TnPowerMgmtPortDegreeFunction_Type(Integer32):
    """Custom type tnPowerMgmtPortDegreeFunction based on Integer32"""
    defaultValue = 1

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
        *(("notDefined", 1),
          ("ila", 2),
          ("dge", 3),
          ("oadm", 4))
    )


_TnPowerMgmtPortDegreeFunction_Type.__name__ = "Integer32"
_TnPowerMgmtPortDegreeFunction_Object = MibTableColumn
tnPowerMgmtPortDegreeFunction = _TnPowerMgmtPortDegreeFunction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 15),
    _TnPowerMgmtPortDegreeFunction_Type()
)
tnPowerMgmtPortDegreeFunction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortDegreeFunction.setStatus("current")
_TnPowerMgmtPerChannelStatusTable_Object = MibTable
tnPowerMgmtPerChannelStatusTable = _TnPowerMgmtPerChannelStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 8)
)
if mibBuilder.loadTexts:
    tnPowerMgmtPerChannelStatusTable.setStatus("current")
_TnPowerMgmtPerChannelStatusEntry_Object = MibTableRow
tnPowerMgmtPerChannelStatusEntry = _TnPowerMgmtPerChannelStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 8, 1)
)
tnPowerMgmtPerChannelStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-WAVEKEY-MIB", "tnDirection"),
    (0, "TROPIC-WAVEKEY-MIB", "tnChannel"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtPerChannelStatusEntry.setStatus("current")
_TnPowerMgmtPerChannelStatusResult_Type = TropicPowerMgmtResult
_TnPowerMgmtPerChannelStatusResult_Object = MibTableColumn
tnPowerMgmtPerChannelStatusResult = _TnPowerMgmtPerChannelStatusResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 8, 1, 1),
    _TnPowerMgmtPerChannelStatusResult_Type()
)
tnPowerMgmtPerChannelStatusResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtPerChannelStatusResult.setStatus("current")
_TnPowerMgmtPerChannelStatusIntegerResult_Type = Integer32
_TnPowerMgmtPerChannelStatusIntegerResult_Object = MibTableColumn
tnPowerMgmtPerChannelStatusIntegerResult = _TnPowerMgmtPerChannelStatusIntegerResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 8, 1, 2),
    _TnPowerMgmtPerChannelStatusIntegerResult_Type()
)
tnPowerMgmtPerChannelStatusIntegerResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtPerChannelStatusIntegerResult.setStatus("current")
_TnPowerMgmtPerChannelStatusControlPointIfIndex_Type = InterfaceIndex
_TnPowerMgmtPerChannelStatusControlPointIfIndex_Object = MibTableColumn
tnPowerMgmtPerChannelStatusControlPointIfIndex = _TnPowerMgmtPerChannelStatusControlPointIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 8, 1, 3),
    _TnPowerMgmtPerChannelStatusControlPointIfIndex_Type()
)
tnPowerMgmtPerChannelStatusControlPointIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtPerChannelStatusControlPointIfIndex.setStatus("current")
_TnPowerMgmtPerChannelStatusControlPointPower_Type = Integer32
_TnPowerMgmtPerChannelStatusControlPointPower_Object = MibTableColumn
tnPowerMgmtPerChannelStatusControlPointPower = _TnPowerMgmtPerChannelStatusControlPointPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 8, 1, 4),
    _TnPowerMgmtPerChannelStatusControlPointPower_Type()
)
tnPowerMgmtPerChannelStatusControlPointPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtPerChannelStatusControlPointPower.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtPerChannelStatusControlPointPower.setUnits("mBm")
_TnPowerMgmtPowerOffsetInTable_Object = MibTable
tnPowerMgmtPowerOffsetInTable = _TnPowerMgmtPowerOffsetInTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 9)
)
if mibBuilder.loadTexts:
    tnPowerMgmtPowerOffsetInTable.setStatus("current")
_TnPowerMgmtPowerOffsetInEntry_Object = MibTableRow
tnPowerMgmtPowerOffsetInEntry = _TnPowerMgmtPowerOffsetInEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 9, 1)
)
tnPowerMgmtPowerOffsetInEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-POWERMGMT-MIB", "tnPowerMgmtBitRate"),
    (0, "TROPIC-POWERMGMT-MIB", "tnPowerMgmtEncoding"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtPowerOffsetInEntry.setStatus("current")
_TnPowerMgmtBitRate_Type = AluWdmOtuBitRate
_TnPowerMgmtBitRate_Object = MibTableColumn
tnPowerMgmtBitRate = _TnPowerMgmtBitRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 9, 1, 1),
    _TnPowerMgmtBitRate_Type()
)
tnPowerMgmtBitRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPowerMgmtBitRate.setStatus("current")
_TnPowerMgmtEncoding_Type = AluWdmOtuEncoding
_TnPowerMgmtEncoding_Object = MibTableColumn
tnPowerMgmtEncoding = _TnPowerMgmtEncoding_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 9, 1, 2),
    _TnPowerMgmtEncoding_Type()
)
tnPowerMgmtEncoding.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPowerMgmtEncoding.setStatus("current")


class _TnPowerMgmtOffsetInPowerOffset_Type(Integer32):
    """Custom type tnPowerMgmtOffsetInPowerOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 300),
    )


_TnPowerMgmtOffsetInPowerOffset_Type.__name__ = "Integer32"
_TnPowerMgmtOffsetInPowerOffset_Object = MibTableColumn
tnPowerMgmtOffsetInPowerOffset = _TnPowerMgmtOffsetInPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 9, 1, 3),
    _TnPowerMgmtOffsetInPowerOffset_Type()
)
tnPowerMgmtOffsetInPowerOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtOffsetInPowerOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtOffsetInPowerOffset.setUnits("mB")
_TnPowerMgmtPowerOffsetOutTable_Object = MibTable
tnPowerMgmtPowerOffsetOutTable = _TnPowerMgmtPowerOffsetOutTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 10)
)
if mibBuilder.loadTexts:
    tnPowerMgmtPowerOffsetOutTable.setStatus("current")
_TnPowerMgmtPowerOffsetOutEntry_Object = MibTableRow
tnPowerMgmtPowerOffsetOutEntry = _TnPowerMgmtPowerOffsetOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 10, 1)
)
tnPowerMgmtPowerOffsetOutEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-POWERMGMT-MIB", "tnPowerMgmtBitRate"),
    (0, "TROPIC-POWERMGMT-MIB", "tnPowerMgmtEncoding"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtPowerOffsetOutEntry.setStatus("current")


class _TnPowerMgmtOffsetOutPowerOffset_Type(Integer32):
    """Custom type tnPowerMgmtOffsetOutPowerOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 300),
    )


_TnPowerMgmtOffsetOutPowerOffset_Type.__name__ = "Integer32"
_TnPowerMgmtOffsetOutPowerOffset_Object = MibTableColumn
tnPowerMgmtOffsetOutPowerOffset = _TnPowerMgmtOffsetOutPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 10, 1, 1),
    _TnPowerMgmtOffsetOutPowerOffset_Type()
)
tnPowerMgmtOffsetOutPowerOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtOffsetOutPowerOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtOffsetOutPowerOffset.setUnits("mB")
_TnPowerMgmtIngressPerChannelTable_Object = MibTable
tnPowerMgmtIngressPerChannelTable = _TnPowerMgmtIngressPerChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 11)
)
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPerChannelTable.setStatus("current")
_TnPowerMgmtIngressPerChannelEntry_Object = MibTableRow
tnPowerMgmtIngressPerChannelEntry = _TnPowerMgmtIngressPerChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 11, 1)
)
tnPowerMgmtIngressPerChannelEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
    (0, "TROPIC-WAVEKEY-MIB", "tnChannel"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPerChannelEntry.setStatus("current")


class _TnPowerMgmtIngressPerChannelSystemTargetOffset_Type(Integer32):
    """Custom type tnPowerMgmtIngressPerChannelSystemTargetOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 300),
    )


_TnPowerMgmtIngressPerChannelSystemTargetOffset_Type.__name__ = "Integer32"
_TnPowerMgmtIngressPerChannelSystemTargetOffset_Object = MibTableColumn
tnPowerMgmtIngressPerChannelSystemTargetOffset = _TnPowerMgmtIngressPerChannelSystemTargetOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 11, 1, 1),
    _TnPowerMgmtIngressPerChannelSystemTargetOffset_Type()
)
tnPowerMgmtIngressPerChannelSystemTargetOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPerChannelSystemTargetOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPerChannelSystemTargetOffset.setUnits("mB")


class _TnPowerMgmtIngressPerChannelUserTargetOffset_Type(Integer32):
    """Custom type tnPowerMgmtIngressPerChannelUserTargetOffset based on Integer32"""
    defaultValue = -9900


_TnPowerMgmtIngressPerChannelUserTargetOffset_Type.__name__ = "Integer32"
_TnPowerMgmtIngressPerChannelUserTargetOffset_Object = MibTableColumn
tnPowerMgmtIngressPerChannelUserTargetOffset = _TnPowerMgmtIngressPerChannelUserTargetOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 11, 1, 2),
    _TnPowerMgmtIngressPerChannelUserTargetOffset_Type()
)
tnPowerMgmtIngressPerChannelUserTargetOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPerChannelUserTargetOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPerChannelUserTargetOffset.setUnits("mB")


class _TnPowerMgmtIngressPerChannelInUseTargetOffset_Type(Integer32):
    """Custom type tnPowerMgmtIngressPerChannelInUseTargetOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 300),
    )


_TnPowerMgmtIngressPerChannelInUseTargetOffset_Type.__name__ = "Integer32"
_TnPowerMgmtIngressPerChannelInUseTargetOffset_Object = MibTableColumn
tnPowerMgmtIngressPerChannelInUseTargetOffset = _TnPowerMgmtIngressPerChannelInUseTargetOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 11, 1, 3),
    _TnPowerMgmtIngressPerChannelInUseTargetOffset_Type()
)
tnPowerMgmtIngressPerChannelInUseTargetOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPerChannelInUseTargetOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPerChannelInUseTargetOffset.setUnits("mB")


class _TnPowerMgmtIngressPerChannelTargetAbsolute_Type(Integer32):
    """Custom type tnPowerMgmtIngressPerChannelTargetAbsolute based on Integer32"""
    defaultValue = -9900


_TnPowerMgmtIngressPerChannelTargetAbsolute_Type.__name__ = "Integer32"
_TnPowerMgmtIngressPerChannelTargetAbsolute_Object = MibTableColumn
tnPowerMgmtIngressPerChannelTargetAbsolute = _TnPowerMgmtIngressPerChannelTargetAbsolute_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 11, 1, 4),
    _TnPowerMgmtIngressPerChannelTargetAbsolute_Type()
)
tnPowerMgmtIngressPerChannelTargetAbsolute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPerChannelTargetAbsolute.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPerChannelTargetAbsolute.setUnits("mBm")


class _TnPowerMgmtIngressPerChannelApplicability_Type(Integer32):
    """Custom type tnPowerMgmtIngressPerChannelApplicability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("applicable", 2))
    )


_TnPowerMgmtIngressPerChannelApplicability_Type.__name__ = "Integer32"
_TnPowerMgmtIngressPerChannelApplicability_Object = MibTableColumn
tnPowerMgmtIngressPerChannelApplicability = _TnPowerMgmtIngressPerChannelApplicability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 11, 1, 5),
    _TnPowerMgmtIngressPerChannelApplicability_Type()
)
tnPowerMgmtIngressPerChannelApplicability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPerChannelApplicability.setStatus("current")
_TnPowerMgmtEgressPerChannelTable_Object = MibTable
tnPowerMgmtEgressPerChannelTable = _TnPowerMgmtEgressPerChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 12)
)
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPerChannelTable.setStatus("current")
_TnPowerMgmtEgressPerChannelEntry_Object = MibTableRow
tnPowerMgmtEgressPerChannelEntry = _TnPowerMgmtEgressPerChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 12, 1)
)
tnPowerMgmtEgressPerChannelEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
    (0, "TROPIC-WAVEKEY-MIB", "tnChannel"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPerChannelEntry.setStatus("current")


class _TnPowerMgmtEgressPerChannelSystemTargetOffset_Type(Integer32):
    """Custom type tnPowerMgmtEgressPerChannelSystemTargetOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 300),
    )


_TnPowerMgmtEgressPerChannelSystemTargetOffset_Type.__name__ = "Integer32"
_TnPowerMgmtEgressPerChannelSystemTargetOffset_Object = MibTableColumn
tnPowerMgmtEgressPerChannelSystemTargetOffset = _TnPowerMgmtEgressPerChannelSystemTargetOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 12, 1, 1),
    _TnPowerMgmtEgressPerChannelSystemTargetOffset_Type()
)
tnPowerMgmtEgressPerChannelSystemTargetOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPerChannelSystemTargetOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPerChannelSystemTargetOffset.setUnits("mB")


class _TnPowerMgmtEgressPerChannelUserTargetOffset_Type(Integer32):
    """Custom type tnPowerMgmtEgressPerChannelUserTargetOffset based on Integer32"""
    defaultValue = -9900


_TnPowerMgmtEgressPerChannelUserTargetOffset_Type.__name__ = "Integer32"
_TnPowerMgmtEgressPerChannelUserTargetOffset_Object = MibTableColumn
tnPowerMgmtEgressPerChannelUserTargetOffset = _TnPowerMgmtEgressPerChannelUserTargetOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 12, 1, 2),
    _TnPowerMgmtEgressPerChannelUserTargetOffset_Type()
)
tnPowerMgmtEgressPerChannelUserTargetOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPerChannelUserTargetOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPerChannelUserTargetOffset.setUnits("mB")


class _TnPowerMgmtEgressPerChannelInUseTargetOffset_Type(Integer32):
    """Custom type tnPowerMgmtEgressPerChannelInUseTargetOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 300),
    )


_TnPowerMgmtEgressPerChannelInUseTargetOffset_Type.__name__ = "Integer32"
_TnPowerMgmtEgressPerChannelInUseTargetOffset_Object = MibTableColumn
tnPowerMgmtEgressPerChannelInUseTargetOffset = _TnPowerMgmtEgressPerChannelInUseTargetOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 12, 1, 3),
    _TnPowerMgmtEgressPerChannelInUseTargetOffset_Type()
)
tnPowerMgmtEgressPerChannelInUseTargetOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPerChannelInUseTargetOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPerChannelInUseTargetOffset.setUnits("mB")


class _TnPowerMgmtEgressPerChannelTargetAbsolute_Type(Integer32):
    """Custom type tnPowerMgmtEgressPerChannelTargetAbsolute based on Integer32"""
    defaultValue = -9900


_TnPowerMgmtEgressPerChannelTargetAbsolute_Type.__name__ = "Integer32"
_TnPowerMgmtEgressPerChannelTargetAbsolute_Object = MibTableColumn
tnPowerMgmtEgressPerChannelTargetAbsolute = _TnPowerMgmtEgressPerChannelTargetAbsolute_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 12, 1, 4),
    _TnPowerMgmtEgressPerChannelTargetAbsolute_Type()
)
tnPowerMgmtEgressPerChannelTargetAbsolute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPerChannelTargetAbsolute.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPerChannelTargetAbsolute.setUnits("mBm")


class _TnPowerMgmtEgressPerChannelApplicability_Type(Integer32):
    """Custom type tnPowerMgmtEgressPerChannelApplicability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("applicable", 2))
    )


_TnPowerMgmtEgressPerChannelApplicability_Type.__name__ = "Integer32"
_TnPowerMgmtEgressPerChannelApplicability_Object = MibTableColumn
tnPowerMgmtEgressPerChannelApplicability = _TnPowerMgmtEgressPerChannelApplicability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 12, 1, 5),
    _TnPowerMgmtEgressPerChannelApplicability_Type()
)
tnPowerMgmtEgressPerChannelApplicability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPerChannelApplicability.setStatus("current")
_TnPowerMgmtTechnologyTypesTable_Object = MibTable
tnPowerMgmtTechnologyTypesTable = _TnPowerMgmtTechnologyTypesTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 13)
)
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesTable.setStatus("current")
_TnPowerMgmtTechnologyTypesEntry_Object = MibTableRow
tnPowerMgmtTechnologyTypesEntry = _TnPowerMgmtTechnologyTypesEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 13, 1)
)
tnPowerMgmtTechnologyTypesEntry.setIndexNames(
    (0, "TROPIC-POWERMGMT-MIB", "tnPowerMgmtBitRate"),
    (0, "TROPIC-POWERMGMT-MIB", "tnPowerMgmtEncoding"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesEntry.setStatus("current")


class _TnPowerMgmtTechnologyTypesBitRateText_Type(SnmpAdminString):
    """Custom type tnPowerMgmtTechnologyTypesBitRateText based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TnPowerMgmtTechnologyTypesBitRateText_Type.__name__ = "SnmpAdminString"
_TnPowerMgmtTechnologyTypesBitRateText_Object = MibTableColumn
tnPowerMgmtTechnologyTypesBitRateText = _TnPowerMgmtTechnologyTypesBitRateText_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 13, 1, 1),
    _TnPowerMgmtTechnologyTypesBitRateText_Type()
)
tnPowerMgmtTechnologyTypesBitRateText.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesBitRateText.setStatus("current")


class _TnPowerMgmtTechnologyTypesEncodingText_Type(SnmpAdminString):
    """Custom type tnPowerMgmtTechnologyTypesEncodingText based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TnPowerMgmtTechnologyTypesEncodingText_Type.__name__ = "SnmpAdminString"
_TnPowerMgmtTechnologyTypesEncodingText_Object = MibTableColumn
tnPowerMgmtTechnologyTypesEncodingText = _TnPowerMgmtTechnologyTypesEncodingText_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 13, 1, 2),
    _TnPowerMgmtTechnologyTypesEncodingText_Type()
)
tnPowerMgmtTechnologyTypesEncodingText.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesEncodingText.setStatus("current")


class _TnPowerMgmtTechnologyTypesWtocmCalib_Type(Integer32):
    """Custom type tnPowerMgmtTechnologyTypesWtocmCalib based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_TnPowerMgmtTechnologyTypesWtocmCalib_Type.__name__ = "Integer32"
_TnPowerMgmtTechnologyTypesWtocmCalib_Object = MibTableColumn
tnPowerMgmtTechnologyTypesWtocmCalib = _TnPowerMgmtTechnologyTypesWtocmCalib_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 13, 1, 3),
    _TnPowerMgmtTechnologyTypesWtocmCalib_Type()
)
tnPowerMgmtTechnologyTypesWtocmCalib.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesWtocmCalib.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesWtocmCalib.setUnits("mB")
_TnPowerMgmtTechnologyTypesRowStatus_Type = RowStatus
_TnPowerMgmtTechnologyTypesRowStatus_Object = MibTableColumn
tnPowerMgmtTechnologyTypesRowStatus = _TnPowerMgmtTechnologyTypesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 13, 1, 4),
    _TnPowerMgmtTechnologyTypesRowStatus_Type()
)
tnPowerMgmtTechnologyTypesRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesRowStatus.setStatus("current")


class _TnPowerMgmtTechnologyTypesOsnrCalib_Type(Integer32):
    """Custom type tnPowerMgmtTechnologyTypesOsnrCalib based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_TnPowerMgmtTechnologyTypesOsnrCalib_Type.__name__ = "Integer32"
_TnPowerMgmtTechnologyTypesOsnrCalib_Object = MibTableColumn
tnPowerMgmtTechnologyTypesOsnrCalib = _TnPowerMgmtTechnologyTypesOsnrCalib_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 13, 1, 5),
    _TnPowerMgmtTechnologyTypesOsnrCalib_Type()
)
tnPowerMgmtTechnologyTypesOsnrCalib.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesOsnrCalib.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesOsnrCalib.setUnits("mB")


class _TnPowerMgmtTechnologyTypesWtocmaCalib_Type(Integer32):
    """Custom type tnPowerMgmtTechnologyTypesWtocmaCalib based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_TnPowerMgmtTechnologyTypesWtocmaCalib_Type.__name__ = "Integer32"
_TnPowerMgmtTechnologyTypesWtocmaCalib_Object = MibTableColumn
tnPowerMgmtTechnologyTypesWtocmaCalib = _TnPowerMgmtTechnologyTypesWtocmaCalib_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 13, 1, 6),
    _TnPowerMgmtTechnologyTypesWtocmaCalib_Type()
)
tnPowerMgmtTechnologyTypesWtocmaCalib.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesWtocmaCalib.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesWtocmaCalib.setUnits("mB")


class _TnPowerMgmtTechnologyTypesWtocmfCalib_Type(Integer32):
    """Custom type tnPowerMgmtTechnologyTypesWtocmfCalib based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_TnPowerMgmtTechnologyTypesWtocmfCalib_Type.__name__ = "Integer32"
_TnPowerMgmtTechnologyTypesWtocmfCalib_Object = MibTableColumn
tnPowerMgmtTechnologyTypesWtocmfCalib = _TnPowerMgmtTechnologyTypesWtocmfCalib_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 13, 1, 7),
    _TnPowerMgmtTechnologyTypesWtocmfCalib_Type()
)
tnPowerMgmtTechnologyTypesWtocmfCalib.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesWtocmfCalib.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesWtocmfCalib.setUnits("mB")
_TnPowerMgmtAnyAddTable_Object = MibTable
tnPowerMgmtAnyAddTable = _TnPowerMgmtAnyAddTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 14)
)
if mibBuilder.loadTexts:
    tnPowerMgmtAnyAddTable.setStatus("current")
_TnPowerMgmtAnyAddEntry_Object = MibTableRow
tnPowerMgmtAnyAddEntry = _TnPowerMgmtAnyAddEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 14, 1)
)
tnPowerMgmtAnyAddEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtAnyAddEntry.setStatus("current")
_TnPowerMgmtAnyAddAdjustPowerGain_Type = TnCommand
_TnPowerMgmtAnyAddAdjustPowerGain_Object = MibTableColumn
tnPowerMgmtAnyAddAdjustPowerGain = _TnPowerMgmtAnyAddAdjustPowerGain_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 14, 1, 1),
    _TnPowerMgmtAnyAddAdjustPowerGain_Type()
)
tnPowerMgmtAnyAddAdjustPowerGain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtAnyAddAdjustPowerGain.setStatus("current")


class _TnPowerMgmtAnyAddAdjustPowerGainLastResult_Type(TropicPowerMgmtResult):
    """Custom type tnPowerMgmtAnyAddAdjustPowerGainLastResult based on TropicPowerMgmtResult"""
    defaultValue = OctetString("Not applicable")


_TnPowerMgmtAnyAddAdjustPowerGainLastResult_Type.__name__ = "TropicPowerMgmtResult"
_TnPowerMgmtAnyAddAdjustPowerGainLastResult_Object = MibTableColumn
tnPowerMgmtAnyAddAdjustPowerGainLastResult = _TnPowerMgmtAnyAddAdjustPowerGainLastResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 14, 1, 2),
    _TnPowerMgmtAnyAddAdjustPowerGainLastResult_Type()
)
tnPowerMgmtAnyAddAdjustPowerGainLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtAnyAddAdjustPowerGainLastResult.setStatus("current")


class _TnPowerMgmtAnyAddAdjustPowerGainStatus_Type(TropicPowerMgmtStatus):
    """Custom type tnPowerMgmtAnyAddAdjustPowerGainStatus based on TropicPowerMgmtStatus"""
    defaultValue = 1


_TnPowerMgmtAnyAddAdjustPowerGainStatus_Type.__name__ = "TropicPowerMgmtStatus"
_TnPowerMgmtAnyAddAdjustPowerGainStatus_Object = MibTableColumn
tnPowerMgmtAnyAddAdjustPowerGainStatus = _TnPowerMgmtAnyAddAdjustPowerGainStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 14, 1, 3),
    _TnPowerMgmtAnyAddAdjustPowerGainStatus_Type()
)
tnPowerMgmtAnyAddAdjustPowerGainStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtAnyAddAdjustPowerGainStatus.setStatus("current")


class _TnPowerMgmtAnyAddCommissioned_Type(TruthValue):
    """Custom type tnPowerMgmtAnyAddCommissioned based on TruthValue"""
    defaultValue = 2


_TnPowerMgmtAnyAddCommissioned_Type.__name__ = "TruthValue"
_TnPowerMgmtAnyAddCommissioned_Object = MibTableColumn
tnPowerMgmtAnyAddCommissioned = _TnPowerMgmtAnyAddCommissioned_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 14, 1, 4),
    _TnPowerMgmtAnyAddCommissioned_Type()
)
tnPowerMgmtAnyAddCommissioned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtAnyAddCommissioned.setStatus("current")


class _TnPowerMgmtAnyAddPassed_Type(TruthValue):
    """Custom type tnPowerMgmtAnyAddPassed based on TruthValue"""
    defaultValue = 1


_TnPowerMgmtAnyAddPassed_Type.__name__ = "TruthValue"
_TnPowerMgmtAnyAddPassed_Object = MibTableColumn
tnPowerMgmtAnyAddPassed = _TnPowerMgmtAnyAddPassed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 14, 1, 5),
    _TnPowerMgmtAnyAddPassed_Type()
)
tnPowerMgmtAnyAddPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtAnyAddPassed.setStatus("current")
_TnPowerMgmtAnyAddAmpIfIndex_Type = InterfaceIndex
_TnPowerMgmtAnyAddAmpIfIndex_Object = MibTableColumn
tnPowerMgmtAnyAddAmpIfIndex = _TnPowerMgmtAnyAddAmpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 14, 1, 6),
    _TnPowerMgmtAnyAddAmpIfIndex_Type()
)
tnPowerMgmtAnyAddAmpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtAnyAddAmpIfIndex.setStatus("current")
_TnPowerMgmtAnyAddAdjustPowerGainAbort_Type = TnCommand
_TnPowerMgmtAnyAddAdjustPowerGainAbort_Object = MibTableColumn
tnPowerMgmtAnyAddAdjustPowerGainAbort = _TnPowerMgmtAnyAddAdjustPowerGainAbort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 14, 1, 7),
    _TnPowerMgmtAnyAddAdjustPowerGainAbort_Type()
)
tnPowerMgmtAnyAddAdjustPowerGainAbort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtAnyAddAdjustPowerGainAbort.setStatus("current")
_TnPowerMgmtAnyDropTable_Object = MibTable
tnPowerMgmtAnyDropTable = _TnPowerMgmtAnyDropTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 15)
)
if mibBuilder.loadTexts:
    tnPowerMgmtAnyDropTable.setStatus("current")
_TnPowerMgmtAnyDropEntry_Object = MibTableRow
tnPowerMgmtAnyDropEntry = _TnPowerMgmtAnyDropEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 15, 1)
)
tnPowerMgmtAnyDropEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtAnyDropEntry.setStatus("current")
_TnPowerMgmtAnyDropAdjustPowerGain_Type = TnCommand
_TnPowerMgmtAnyDropAdjustPowerGain_Object = MibTableColumn
tnPowerMgmtAnyDropAdjustPowerGain = _TnPowerMgmtAnyDropAdjustPowerGain_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 15, 1, 1),
    _TnPowerMgmtAnyDropAdjustPowerGain_Type()
)
tnPowerMgmtAnyDropAdjustPowerGain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtAnyDropAdjustPowerGain.setStatus("current")


class _TnPowerMgmtAnyDropAdjustPowerGainLastResult_Type(TropicPowerMgmtResult):
    """Custom type tnPowerMgmtAnyDropAdjustPowerGainLastResult based on TropicPowerMgmtResult"""
    defaultValue = OctetString("Not applicable")


_TnPowerMgmtAnyDropAdjustPowerGainLastResult_Type.__name__ = "TropicPowerMgmtResult"
_TnPowerMgmtAnyDropAdjustPowerGainLastResult_Object = MibTableColumn
tnPowerMgmtAnyDropAdjustPowerGainLastResult = _TnPowerMgmtAnyDropAdjustPowerGainLastResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 15, 1, 2),
    _TnPowerMgmtAnyDropAdjustPowerGainLastResult_Type()
)
tnPowerMgmtAnyDropAdjustPowerGainLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtAnyDropAdjustPowerGainLastResult.setStatus("current")


class _TnPowerMgmtAnyDropAdjustPowerGainStatus_Type(TropicPowerMgmtStatus):
    """Custom type tnPowerMgmtAnyDropAdjustPowerGainStatus based on TropicPowerMgmtStatus"""
    defaultValue = 1


_TnPowerMgmtAnyDropAdjustPowerGainStatus_Type.__name__ = "TropicPowerMgmtStatus"
_TnPowerMgmtAnyDropAdjustPowerGainStatus_Object = MibTableColumn
tnPowerMgmtAnyDropAdjustPowerGainStatus = _TnPowerMgmtAnyDropAdjustPowerGainStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 15, 1, 3),
    _TnPowerMgmtAnyDropAdjustPowerGainStatus_Type()
)
tnPowerMgmtAnyDropAdjustPowerGainStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtAnyDropAdjustPowerGainStatus.setStatus("current")


class _TnPowerMgmtAnyDropCommissioned_Type(TruthValue):
    """Custom type tnPowerMgmtAnyDropCommissioned based on TruthValue"""
    defaultValue = 2


_TnPowerMgmtAnyDropCommissioned_Type.__name__ = "TruthValue"
_TnPowerMgmtAnyDropCommissioned_Object = MibTableColumn
tnPowerMgmtAnyDropCommissioned = _TnPowerMgmtAnyDropCommissioned_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 15, 1, 4),
    _TnPowerMgmtAnyDropCommissioned_Type()
)
tnPowerMgmtAnyDropCommissioned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtAnyDropCommissioned.setStatus("current")


class _TnPowerMgmtAnyDropPassed_Type(TruthValue):
    """Custom type tnPowerMgmtAnyDropPassed based on TruthValue"""
    defaultValue = 1


_TnPowerMgmtAnyDropPassed_Type.__name__ = "TruthValue"
_TnPowerMgmtAnyDropPassed_Object = MibTableColumn
tnPowerMgmtAnyDropPassed = _TnPowerMgmtAnyDropPassed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 15, 1, 5),
    _TnPowerMgmtAnyDropPassed_Type()
)
tnPowerMgmtAnyDropPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtAnyDropPassed.setStatus("current")
_TnPowerMgmtAnyDropAmpIfIndex_Type = InterfaceIndex
_TnPowerMgmtAnyDropAmpIfIndex_Object = MibTableColumn
tnPowerMgmtAnyDropAmpIfIndex = _TnPowerMgmtAnyDropAmpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 15, 1, 6),
    _TnPowerMgmtAnyDropAmpIfIndex_Type()
)
tnPowerMgmtAnyDropAmpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtAnyDropAmpIfIndex.setStatus("current")

# Managed Objects groups

tnPowerMgmtGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 1)
)
tnPowerMgmtGlobalGroup.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtGlobalMinStepSize"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtGlobalMaxStepSize"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtGlobalResetToDefaults"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtGlobalAutoEnabled"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtGlobalNumberOfAutoPowerAdjPoints"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtGlobalAlarmWhenDisabled"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtGlobalGroup.setStatus("current")

tnPowerMgmtControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 2)
)
tnPowerMgmtControlGroup.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtControlPercentCompleted"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtControlRowStatus"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtControlGroup.setStatus("current")

tnPowerMgmtIngressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 4)
)
tnPowerMgmtIngressGroup.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressAdjustPowerGain"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressAdjustPowerGainLastResult"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressAcceptPowers"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressAcceptPowersLastResult"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressRippleAllowance"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressAdjustPowerGainTargetGain"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressAdjustPowerGainStatus"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressStartAseAdjust"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressAseAdjustLastResult"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressAseAdjustStatus"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressCommissioned"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressGainSetOffset"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressCommissionedGain"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressSRSTiltPostFraction"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressSRSTiltAdjResult"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressSRSTiltAdjStatus"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPassed"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressSRSTiltCalcOffset"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtIngressGroup.setStatus("current")

tnPowerMgmtEgressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 5)
)
tnPowerMgmtEgressGroup.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressAdjustPowerWithOptimization"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressAdjustPowerWithOptimizationStatus"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressAdjustPowerWithOptimizationAbort"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressAcceptPowers"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressAdjustPowerWithOptimizationLastResult"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressAcceptPowersLastResult"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressAdjustPowerWithOptimizationTargetGain"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressStartAseAdjust"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressStopAseAdjust"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressAseAdjustLastResult"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressAseAdjustStatus"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressCommissioned"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressAmpIfIndex"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressWssIfIndex"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressSRSTiltCalcMultiplier"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressSRSTiltPreFraction"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressSRSTiltCalcACoeff"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressSRSTiltCalcOutputLoss"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressSRSTiltAdjResult"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressSRSTiltAdjStatus"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPassed"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressLHLaunchAtten"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtFiberSpanTiltPreComp"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtEgressGroup.setStatus("current")

tnPowerMgmtPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 7)
)
tnPowerMgmtPortGroup.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortIsCommissioned"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortTypeIn"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortTypeOut"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortWTDecoderUsageTypeIn"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortWTDecoderUsageTypeOut"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortGainAdjSchedBase"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortGainAdjTimerPeriod"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortGainAdjTimerLength"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortInGainAdjAutoEnabled"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortSRSTiltAdjAutoEnabled"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortFiberSpanTilt"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortSRSTiltMaintenanceMode"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortDegreeFunction"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtPortGroup.setStatus("current")

tnPowerMgmtPerChannelStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 8)
)
tnPowerMgmtPerChannelStatusGroup.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPerChannelStatusResult"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPerChannelStatusIntegerResult"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPerChannelStatusControlPointIfIndex"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPerChannelStatusControlPointPower"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtPerChannelStatusGroup.setStatus("current")

tnPowerMgmtPowerOffsetInGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 9)
)
tnPowerMgmtPowerOffsetInGroup.setObjects(
    ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtOffsetInPowerOffset")
)
if mibBuilder.loadTexts:
    tnPowerMgmtPowerOffsetInGroup.setStatus("current")

tnPowerMgmtPowerOffsetOutGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 10)
)
tnPowerMgmtPowerOffsetOutGroup.setObjects(
    ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtOffsetOutPowerOffset")
)
if mibBuilder.loadTexts:
    tnPowerMgmtPowerOffsetOutGroup.setStatus("current")

tnPowerMgmtIngressPerChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 11)
)
tnPowerMgmtIngressPerChannelGroup.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPerChannelSystemTargetOffset"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPerChannelUserTargetOffset"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPerChannelInUseTargetOffset"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPerChannelTargetAbsolute"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPerChannelApplicability"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPerChannelGroup.setStatus("current")

tnPowerMgmtEgressPerChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 12)
)
tnPowerMgmtEgressPerChannelGroup.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPerChannelSystemTargetOffset"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPerChannelUserTargetOffset"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPerChannelInUseTargetOffset"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPerChannelTargetAbsolute"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPerChannelApplicability"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPerChannelGroup.setStatus("current")

tnPowerMgmtTechnologyTypesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 13)
)
tnPowerMgmtTechnologyTypesGroup.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtTechnologyTypesBitRateText"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtTechnologyTypesEncodingText"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtTechnologyTypesWtocmCalib"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtTechnologyTypesRowStatus"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtTechnologyTypesOsnrCalib"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtTechnologyTypesWtocmaCalib"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtTechnologyTypesWtocmfCalib"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesGroup.setStatus("current")

tnPowerMgmtAnyAddGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 14)
)
tnPowerMgmtAnyAddGroup.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyAddAdjustPowerGain"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyAddAdjustPowerGainLastResult"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyAddAdjustPowerGainStatus"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyAddCommissioned"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyAddPassed"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyAddAmpIfIndex"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyAddAdjustPowerGainAbort"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtAnyAddGroup.setStatus("current")

tnPowerMgmtAnyDropGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 15)
)
tnPowerMgmtAnyDropGroup.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyDropAdjustPowerGain"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyDropAdjustPowerGainLastResult"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyDropAdjustPowerGainStatus"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyDropCommissioned"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyDropPassed"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyDropAmpIfIndex"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtAnyDropGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnPowerMgmtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 2, 1)
)
tnPowerMgmtCompliance.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtGlobalGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtControlGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPerChannelStatusGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPowerOffsetInGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPowerOffsetOutGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPerChannelGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPerChannelGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtTechnologyTypesGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyAddGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyDropGroup"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-POWERMGMT-MIB",
    **{"TropicPowerMgmtStatus": TropicPowerMgmtStatus,
       "TropicPowerMgmtResult": TropicPowerMgmtResult,
       "TropicPowerMgmtPercentCompleted": TropicPowerMgmtPercentCompleted,
       "TropicPowerMgmtType": TropicPowerMgmtType,
       "AluWdmWTDecoderUsageType": AluWdmWTDecoderUsageType,
       "AluWdmPowerMgmtSRSTiltAdjStatus": AluWdmPowerMgmtSRSTiltAdjStatus,
       "tnPowerMgmtMibModule": tnPowerMgmtMibModule,
       "tnPowerMgmtConf": tnPowerMgmtConf,
       "tnPowerMgmtGroups": tnPowerMgmtGroups,
       "tnPowerMgmtGlobalGroup": tnPowerMgmtGlobalGroup,
       "tnPowerMgmtControlGroup": tnPowerMgmtControlGroup,
       "tnPowerMgmtIngressGroup": tnPowerMgmtIngressGroup,
       "tnPowerMgmtEgressGroup": tnPowerMgmtEgressGroup,
       "tnPowerMgmtPortGroup": tnPowerMgmtPortGroup,
       "tnPowerMgmtPerChannelStatusGroup": tnPowerMgmtPerChannelStatusGroup,
       "tnPowerMgmtPowerOffsetInGroup": tnPowerMgmtPowerOffsetInGroup,
       "tnPowerMgmtPowerOffsetOutGroup": tnPowerMgmtPowerOffsetOutGroup,
       "tnPowerMgmtIngressPerChannelGroup": tnPowerMgmtIngressPerChannelGroup,
       "tnPowerMgmtEgressPerChannelGroup": tnPowerMgmtEgressPerChannelGroup,
       "tnPowerMgmtTechnologyTypesGroup": tnPowerMgmtTechnologyTypesGroup,
       "tnPowerMgmtAnyAddGroup": tnPowerMgmtAnyAddGroup,
       "tnPowerMgmtAnyDropGroup": tnPowerMgmtAnyDropGroup,
       "tnPowerMgmtCompliances": tnPowerMgmtCompliances,
       "tnPowerMgmtCompliance": tnPowerMgmtCompliance,
       "tnPowerMgmtObjs": tnPowerMgmtObjs,
       "tnPowerMgmtBasics": tnPowerMgmtBasics,
       "tnPowerMgmtGlobal": tnPowerMgmtGlobal,
       "tnPowerMgmtGlobalMinStepSize": tnPowerMgmtGlobalMinStepSize,
       "tnPowerMgmtGlobalMaxStepSize": tnPowerMgmtGlobalMaxStepSize,
       "tnPowerMgmtGlobalResetToDefaults": tnPowerMgmtGlobalResetToDefaults,
       "tnPowerMgmtGlobalAutoEnabled": tnPowerMgmtGlobalAutoEnabled,
       "tnPowerMgmtGlobalNumberOfAutoPowerAdjPoints": tnPowerMgmtGlobalNumberOfAutoPowerAdjPoints,
       "tnPowerMgmtGlobalAlarmWhenDisabled": tnPowerMgmtGlobalAlarmWhenDisabled,
       "tnPowerMgmtControlTable": tnPowerMgmtControlTable,
       "tnPowerMgmtControlEntry": tnPowerMgmtControlEntry,
       "tnPowerMgmtDirection": tnPowerMgmtDirection,
       "tnPowerMgmtControlPercentCompleted": tnPowerMgmtControlPercentCompleted,
       "tnPowerMgmtControlRowStatus": tnPowerMgmtControlRowStatus,
       "tnPowerMgmtIngressTable": tnPowerMgmtIngressTable,
       "tnPowerMgmtIngressEntry": tnPowerMgmtIngressEntry,
       "tnPowerMgmtIngressAdjustPowerGain": tnPowerMgmtIngressAdjustPowerGain,
       "tnPowerMgmtIngressAdjustPowerGainLastResult": tnPowerMgmtIngressAdjustPowerGainLastResult,
       "tnPowerMgmtIngressAcceptPowers": tnPowerMgmtIngressAcceptPowers,
       "tnPowerMgmtIngressAcceptPowersLastResult": tnPowerMgmtIngressAcceptPowersLastResult,
       "tnPowerMgmtIngressRippleAllowance": tnPowerMgmtIngressRippleAllowance,
       "tnPowerMgmtIngressAdjustPowerGainTargetGain": tnPowerMgmtIngressAdjustPowerGainTargetGain,
       "tnPowerMgmtIngressAdjustPowerGainStatus": tnPowerMgmtIngressAdjustPowerGainStatus,
       "tnPowerMgmtIngressStartAseAdjust": tnPowerMgmtIngressStartAseAdjust,
       "tnPowerMgmtIngressAseAdjustLastResult": tnPowerMgmtIngressAseAdjustLastResult,
       "tnPowerMgmtIngressAseAdjustStatus": tnPowerMgmtIngressAseAdjustStatus,
       "tnPowerMgmtIngressCommissioned": tnPowerMgmtIngressCommissioned,
       "tnPowerMgmtIngressGainSetOffset": tnPowerMgmtIngressGainSetOffset,
       "tnPowerMgmtIngressCommissionedGain": tnPowerMgmtIngressCommissionedGain,
       "tnPowerMgmtIngressSRSTiltPostFraction": tnPowerMgmtIngressSRSTiltPostFraction,
       "tnPowerMgmtIngressSRSTiltAdjResult": tnPowerMgmtIngressSRSTiltAdjResult,
       "tnPowerMgmtIngressSRSTiltAdjStatus": tnPowerMgmtIngressSRSTiltAdjStatus,
       "tnPowerMgmtIngressPassed": tnPowerMgmtIngressPassed,
       "tnPowerMgmtIngressSRSTiltCalcOffset": tnPowerMgmtIngressSRSTiltCalcOffset,
       "tnPowerMgmtEgressTable": tnPowerMgmtEgressTable,
       "tnPowerMgmtEgressEntry": tnPowerMgmtEgressEntry,
       "tnPowerMgmtEgressAdjustPowerWithOptimization": tnPowerMgmtEgressAdjustPowerWithOptimization,
       "tnPowerMgmtEgressAdjustPowerWithOptimizationStatus": tnPowerMgmtEgressAdjustPowerWithOptimizationStatus,
       "tnPowerMgmtEgressAdjustPowerWithOptimizationAbort": tnPowerMgmtEgressAdjustPowerWithOptimizationAbort,
       "tnPowerMgmtEgressAcceptPowers": tnPowerMgmtEgressAcceptPowers,
       "tnPowerMgmtEgressAdjustPowerWithOptimizationLastResult": tnPowerMgmtEgressAdjustPowerWithOptimizationLastResult,
       "tnPowerMgmtEgressAcceptPowersLastResult": tnPowerMgmtEgressAcceptPowersLastResult,
       "tnPowerMgmtEgressAdjustPowerWithOptimizationTargetGain": tnPowerMgmtEgressAdjustPowerWithOptimizationTargetGain,
       "tnPowerMgmtEgressStartAseAdjust": tnPowerMgmtEgressStartAseAdjust,
       "tnPowerMgmtEgressStopAseAdjust": tnPowerMgmtEgressStopAseAdjust,
       "tnPowerMgmtEgressAseAdjustLastResult": tnPowerMgmtEgressAseAdjustLastResult,
       "tnPowerMgmtEgressAseAdjustStatus": tnPowerMgmtEgressAseAdjustStatus,
       "tnPowerMgmtEgressCommissioned": tnPowerMgmtEgressCommissioned,
       "tnPowerMgmtEgressAmpIfIndex": tnPowerMgmtEgressAmpIfIndex,
       "tnPowerMgmtEgressWssIfIndex": tnPowerMgmtEgressWssIfIndex,
       "tnPowerMgmtEgressSRSTiltCalcMultiplier": tnPowerMgmtEgressSRSTiltCalcMultiplier,
       "tnPowerMgmtEgressSRSTiltPreFraction": tnPowerMgmtEgressSRSTiltPreFraction,
       "tnPowerMgmtEgressSRSTiltCalcACoeff": tnPowerMgmtEgressSRSTiltCalcACoeff,
       "tnPowerMgmtEgressSRSTiltCalcOutputLoss": tnPowerMgmtEgressSRSTiltCalcOutputLoss,
       "tnPowerMgmtEgressSRSTiltAdjResult": tnPowerMgmtEgressSRSTiltAdjResult,
       "tnPowerMgmtEgressSRSTiltAdjStatus": tnPowerMgmtEgressSRSTiltAdjStatus,
       "tnPowerMgmtEgressPassed": tnPowerMgmtEgressPassed,
       "tnPowerMgmtEgressLHLaunchAtten": tnPowerMgmtEgressLHLaunchAtten,
       "tnPowerMgmtFiberSpanTiltPreComp": tnPowerMgmtFiberSpanTiltPreComp,
       "tnPowerMgmtPortTable": tnPowerMgmtPortTable,
       "tnPowerMgmtPortEntry": tnPowerMgmtPortEntry,
       "tnPowerMgmtPortIsCommissioned": tnPowerMgmtPortIsCommissioned,
       "tnPowerMgmtPortTypeIn": tnPowerMgmtPortTypeIn,
       "tnPowerMgmtPortTypeOut": tnPowerMgmtPortTypeOut,
       "tnPowerMgmtPortWTDecoderUsageTypeIn": tnPowerMgmtPortWTDecoderUsageTypeIn,
       "tnPowerMgmtPortWTDecoderUsageTypeOut": tnPowerMgmtPortWTDecoderUsageTypeOut,
       "tnPowerMgmtPortGainAdjSchedBase": tnPowerMgmtPortGainAdjSchedBase,
       "tnPowerMgmtPortGainAdjTimerPeriod": tnPowerMgmtPortGainAdjTimerPeriod,
       "tnPowerMgmtPortGainAdjTimerLength": tnPowerMgmtPortGainAdjTimerLength,
       "tnPowerMgmtPortInGainAdjAutoEnabled": tnPowerMgmtPortInGainAdjAutoEnabled,
       "tnPowerMgmtPortSRSTiltAdjAutoEnabled": tnPowerMgmtPortSRSTiltAdjAutoEnabled,
       "tnPowerMgmtPortFiberSpanTilt": tnPowerMgmtPortFiberSpanTilt,
       "tnPowerMgmtPortSRSTiltMaintenanceMode": tnPowerMgmtPortSRSTiltMaintenanceMode,
       "tnPowerMgmtPortDegreeFunction": tnPowerMgmtPortDegreeFunction,
       "tnPowerMgmtPerChannelStatusTable": tnPowerMgmtPerChannelStatusTable,
       "tnPowerMgmtPerChannelStatusEntry": tnPowerMgmtPerChannelStatusEntry,
       "tnPowerMgmtPerChannelStatusResult": tnPowerMgmtPerChannelStatusResult,
       "tnPowerMgmtPerChannelStatusIntegerResult": tnPowerMgmtPerChannelStatusIntegerResult,
       "tnPowerMgmtPerChannelStatusControlPointIfIndex": tnPowerMgmtPerChannelStatusControlPointIfIndex,
       "tnPowerMgmtPerChannelStatusControlPointPower": tnPowerMgmtPerChannelStatusControlPointPower,
       "tnPowerMgmtPowerOffsetInTable": tnPowerMgmtPowerOffsetInTable,
       "tnPowerMgmtPowerOffsetInEntry": tnPowerMgmtPowerOffsetInEntry,
       "tnPowerMgmtBitRate": tnPowerMgmtBitRate,
       "tnPowerMgmtEncoding": tnPowerMgmtEncoding,
       "tnPowerMgmtOffsetInPowerOffset": tnPowerMgmtOffsetInPowerOffset,
       "tnPowerMgmtPowerOffsetOutTable": tnPowerMgmtPowerOffsetOutTable,
       "tnPowerMgmtPowerOffsetOutEntry": tnPowerMgmtPowerOffsetOutEntry,
       "tnPowerMgmtOffsetOutPowerOffset": tnPowerMgmtOffsetOutPowerOffset,
       "tnPowerMgmtIngressPerChannelTable": tnPowerMgmtIngressPerChannelTable,
       "tnPowerMgmtIngressPerChannelEntry": tnPowerMgmtIngressPerChannelEntry,
       "tnPowerMgmtIngressPerChannelSystemTargetOffset": tnPowerMgmtIngressPerChannelSystemTargetOffset,
       "tnPowerMgmtIngressPerChannelUserTargetOffset": tnPowerMgmtIngressPerChannelUserTargetOffset,
       "tnPowerMgmtIngressPerChannelInUseTargetOffset": tnPowerMgmtIngressPerChannelInUseTargetOffset,
       "tnPowerMgmtIngressPerChannelTargetAbsolute": tnPowerMgmtIngressPerChannelTargetAbsolute,
       "tnPowerMgmtIngressPerChannelApplicability": tnPowerMgmtIngressPerChannelApplicability,
       "tnPowerMgmtEgressPerChannelTable": tnPowerMgmtEgressPerChannelTable,
       "tnPowerMgmtEgressPerChannelEntry": tnPowerMgmtEgressPerChannelEntry,
       "tnPowerMgmtEgressPerChannelSystemTargetOffset": tnPowerMgmtEgressPerChannelSystemTargetOffset,
       "tnPowerMgmtEgressPerChannelUserTargetOffset": tnPowerMgmtEgressPerChannelUserTargetOffset,
       "tnPowerMgmtEgressPerChannelInUseTargetOffset": tnPowerMgmtEgressPerChannelInUseTargetOffset,
       "tnPowerMgmtEgressPerChannelTargetAbsolute": tnPowerMgmtEgressPerChannelTargetAbsolute,
       "tnPowerMgmtEgressPerChannelApplicability": tnPowerMgmtEgressPerChannelApplicability,
       "tnPowerMgmtTechnologyTypesTable": tnPowerMgmtTechnologyTypesTable,
       "tnPowerMgmtTechnologyTypesEntry": tnPowerMgmtTechnologyTypesEntry,
       "tnPowerMgmtTechnologyTypesBitRateText": tnPowerMgmtTechnologyTypesBitRateText,
       "tnPowerMgmtTechnologyTypesEncodingText": tnPowerMgmtTechnologyTypesEncodingText,
       "tnPowerMgmtTechnologyTypesWtocmCalib": tnPowerMgmtTechnologyTypesWtocmCalib,
       "tnPowerMgmtTechnologyTypesRowStatus": tnPowerMgmtTechnologyTypesRowStatus,
       "tnPowerMgmtTechnologyTypesOsnrCalib": tnPowerMgmtTechnologyTypesOsnrCalib,
       "tnPowerMgmtTechnologyTypesWtocmaCalib": tnPowerMgmtTechnologyTypesWtocmaCalib,
       "tnPowerMgmtTechnologyTypesWtocmfCalib": tnPowerMgmtTechnologyTypesWtocmfCalib,
       "tnPowerMgmtAnyAddTable": tnPowerMgmtAnyAddTable,
       "tnPowerMgmtAnyAddEntry": tnPowerMgmtAnyAddEntry,
       "tnPowerMgmtAnyAddAdjustPowerGain": tnPowerMgmtAnyAddAdjustPowerGain,
       "tnPowerMgmtAnyAddAdjustPowerGainLastResult": tnPowerMgmtAnyAddAdjustPowerGainLastResult,
       "tnPowerMgmtAnyAddAdjustPowerGainStatus": tnPowerMgmtAnyAddAdjustPowerGainStatus,
       "tnPowerMgmtAnyAddCommissioned": tnPowerMgmtAnyAddCommissioned,
       "tnPowerMgmtAnyAddPassed": tnPowerMgmtAnyAddPassed,
       "tnPowerMgmtAnyAddAmpIfIndex": tnPowerMgmtAnyAddAmpIfIndex,
       "tnPowerMgmtAnyAddAdjustPowerGainAbort": tnPowerMgmtAnyAddAdjustPowerGainAbort,
       "tnPowerMgmtAnyDropTable": tnPowerMgmtAnyDropTable,
       "tnPowerMgmtAnyDropEntry": tnPowerMgmtAnyDropEntry,
       "tnPowerMgmtAnyDropAdjustPowerGain": tnPowerMgmtAnyDropAdjustPowerGain,
       "tnPowerMgmtAnyDropAdjustPowerGainLastResult": tnPowerMgmtAnyDropAdjustPowerGainLastResult,
       "tnPowerMgmtAnyDropAdjustPowerGainStatus": tnPowerMgmtAnyDropAdjustPowerGainStatus,
       "tnPowerMgmtAnyDropCommissioned": tnPowerMgmtAnyDropCommissioned,
       "tnPowerMgmtAnyDropPassed": tnPowerMgmtAnyDropPassed,
       "tnPowerMgmtAnyDropAmpIfIndex": tnPowerMgmtAnyDropAmpIfIndex}
)
