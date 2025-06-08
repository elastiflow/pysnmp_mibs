# SNMP MIB module (TIMETRA-OAM-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-OAM-PM-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:37:39 2025
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

(Dot1agCfmMepIdOrZero,) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMepIdOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(svcId,) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "svcId")

(TFCName,
 TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TProfile,
 TmnxEnabledDisabled,
 TmnxEnabledDisabledOrNA,
 TmnxOperState) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TFCName",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TProfile",
    "TmnxEnabledDisabled",
    "TmnxEnabledDisabledOrNA",
    "TmnxOperState")


# MODULE-IDENTITY

timetraOamPmMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 92)
)
if mibBuilder.loadTexts:
    timetraOamPmMIBModule.setRevisions(
        ("2013-07-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxOamPmBinGroupId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class TmnxOamPmBinType(TextualConvention, Integer32):
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
        *(("fd", 1),
          ("fdr", 2),
          ("ifdv", 3))
    )



class TmnxOamPmMeasIntervalDuration(TextualConvention, Integer32):
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
        *(("miRaw", 1),
          ("mi15Minutes", 2),
          ("mi1Hour", 3),
          ("mi1Day", 4))
    )



class TmnxOamPmCfgMeasIntervalDuration(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mi15Minutes", 2),
          ("mi1Hour", 3),
          ("mi1Day", 4))
    )



class TmnxOamPmSessionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("proactive", 1),
          ("onDemand", 2))
    )



class TmnxOamPmStsIntvlNum(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class TmnxOamPmTestFamily(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("ip", 2))
    )



class TmnxOamPmTestType(TextualConvention, Integer32):
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
        *(("dmm", 1),
          ("slm", 2),
          ("twampLight", 3),
          ("lmm", 4))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxOamPmConformance_ObjectIdentity = ObjectIdentity
tmnxOamPmConformance = _TmnxOamPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92)
)
_TmnxOamPmCompliances_ObjectIdentity = ObjectIdentity
tmnxOamPmCompliances = _TmnxOamPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 1)
)
_TmnxOamPmObjGroups_ObjectIdentity = ObjectIdentity
tmnxOamPmObjGroups = _TmnxOamPmObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 2)
)
_TmnxOamPmV12v0ObjGroups_ObjectIdentity = ObjectIdentity
tmnxOamPmV12v0ObjGroups = _TmnxOamPmV12v0ObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 2, 1)
)
_TmnxOamPmNotifGroups_ObjectIdentity = ObjectIdentity
tmnxOamPmNotifGroups = _TmnxOamPmNotifGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 3)
)
_TmnxOamPmV12v0NotifGroups_ObjectIdentity = ObjectIdentity
tmnxOamPmV12v0NotifGroups = _TmnxOamPmV12v0NotifGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 3, 1)
)
_TmnxOamPmObjs_ObjectIdentity = ObjectIdentity
tmnxOamPmObjs = _TmnxOamPmObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92)
)
_TmnxOamPmCfgObjs_ObjectIdentity = ObjectIdentity
tmnxOamPmCfgObjs = _TmnxOamPmCfgObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1)
)
_TmnxOamPmCfgScalarObjs_ObjectIdentity = ObjectIdentity
tmnxOamPmCfgScalarObjs = _TmnxOamPmCfgScalarObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 1)
)


class _TmnxOamPmCfgTwlRflInactTimer_Type(Unsigned32):
    """Custom type tmnxOamPmCfgTwlRflInactTimer based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_TmnxOamPmCfgTwlRflInactTimer_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgTwlRflInactTimer_Object = MibScalar
tmnxOamPmCfgTwlRflInactTimer = _TmnxOamPmCfgTwlRflInactTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 1, 1),
    _TmnxOamPmCfgTwlRflInactTimer_Type()
)
tmnxOamPmCfgTwlRflInactTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflInactTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflInactTimer.setUnits("seconds")
_TmnxOamPmTableLastChgObjs_ObjectIdentity = ObjectIdentity
tmnxOamPmTableLastChgObjs = _TmnxOamPmTableLastChgObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2)
)
_TmnxOamPmCfgBinGroupTableLastChg_Type = TimeStamp
_TmnxOamPmCfgBinGroupTableLastChg_Object = MibScalar
tmnxOamPmCfgBinGroupTableLastChg = _TmnxOamPmCfgBinGroupTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 1),
    _TmnxOamPmCfgBinGroupTableLastChg_Type()
)
tmnxOamPmCfgBinGroupTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinGroupTableLastChg.setStatus("current")
_TmnxOamPmCfgBinTableLastChg_Type = TimeStamp
_TmnxOamPmCfgBinTableLastChg_Object = MibScalar
tmnxOamPmCfgBinTableLastChg = _TmnxOamPmCfgBinTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 2),
    _TmnxOamPmCfgBinTableLastChg_Type()
)
tmnxOamPmCfgBinTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinTableLastChg.setStatus("current")
_TmnxOamPmCfgSessTableLastChg_Type = TimeStamp
_TmnxOamPmCfgSessTableLastChg_Object = MibScalar
tmnxOamPmCfgSessTableLastChg = _TmnxOamPmCfgSessTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 3),
    _TmnxOamPmCfgSessTableLastChg_Type()
)
tmnxOamPmCfgSessTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessTableLastChg.setStatus("current")
_TmnxOamPmCfgSessEthTableLastChg_Type = TimeStamp
_TmnxOamPmCfgSessEthTableLastChg_Object = MibScalar
tmnxOamPmCfgSessEthTableLastChg = _TmnxOamPmCfgSessEthTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 4),
    _TmnxOamPmCfgSessEthTableLastChg_Type()
)
tmnxOamPmCfgSessEthTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessEthTableLastChg.setStatus("current")
_TmnxOamPmCfgDelayDmmTableLastChg_Type = TimeStamp
_TmnxOamPmCfgDelayDmmTableLastChg_Object = MibScalar
tmnxOamPmCfgDelayDmmTableLastChg = _TmnxOamPmCfgDelayDmmTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 5),
    _TmnxOamPmCfgDelayDmmTableLastChg_Type()
)
tmnxOamPmCfgDelayDmmTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmTableLastChg.setStatus("current")
_TmnxOamPmCfgLossSlmTableLastChg_Type = TimeStamp
_TmnxOamPmCfgLossSlmTableLastChg_Object = MibScalar
tmnxOamPmCfgLossSlmTableLastChg = _TmnxOamPmCfgLossSlmTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 6),
    _TmnxOamPmCfgLossSlmTableLastChg_Type()
)
tmnxOamPmCfgLossSlmTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmTableLastChg.setStatus("current")
_TmnxOamPmCfgMeasIntvlTableLstChg_Type = TimeStamp
_TmnxOamPmCfgMeasIntvlTableLstChg_Object = MibScalar
tmnxOamPmCfgMeasIntvlTableLstChg = _TmnxOamPmCfgMeasIntvlTableLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 7),
    _TmnxOamPmCfgMeasIntvlTableLstChg_Type()
)
tmnxOamPmCfgMeasIntvlTableLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgMeasIntvlTableLstChg.setStatus("current")
_TmnxOamPmCfgSessIpTableLastChg_Type = TimeStamp
_TmnxOamPmCfgSessIpTableLastChg_Object = MibScalar
tmnxOamPmCfgSessIpTableLastChg = _TmnxOamPmCfgSessIpTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 8),
    _TmnxOamPmCfgSessIpTableLastChg_Type()
)
tmnxOamPmCfgSessIpTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpTableLastChg.setStatus("current")
_TmnxOamPmCfgTwampLtTableLastChg_Type = TimeStamp
_TmnxOamPmCfgTwampLtTableLastChg_Object = MibScalar
tmnxOamPmCfgTwampLtTableLastChg = _TmnxOamPmCfgTwampLtTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 9),
    _TmnxOamPmCfgTwampLtTableLastChg_Type()
)
tmnxOamPmCfgTwampLtTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtTableLastChg.setStatus("current")
_TmnxOamPmCfgTwlRflTableLastChg_Type = TimeStamp
_TmnxOamPmCfgTwlRflTableLastChg_Object = MibScalar
tmnxOamPmCfgTwlRflTableLastChg = _TmnxOamPmCfgTwlRflTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 10),
    _TmnxOamPmCfgTwlRflTableLastChg_Type()
)
tmnxOamPmCfgTwlRflTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflTableLastChg.setStatus("current")
_TmnxOamPmCfgTwlRflPfxTableLstChg_Type = TimeStamp
_TmnxOamPmCfgTwlRflPfxTableLstChg_Object = MibScalar
tmnxOamPmCfgTwlRflPfxTableLstChg = _TmnxOamPmCfgTwlRflPfxTableLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 11),
    _TmnxOamPmCfgTwlRflPfxTableLstChg_Type()
)
tmnxOamPmCfgTwlRflPfxTableLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflPfxTableLstChg.setStatus("current")
_TmnxOamPmCfgLossLmmTableLastChg_Type = TimeStamp
_TmnxOamPmCfgLossLmmTableLastChg_Object = MibScalar
tmnxOamPmCfgLossLmmTableLastChg = _TmnxOamPmCfgLossLmmTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 12),
    _TmnxOamPmCfgLossLmmTableLastChg_Type()
)
tmnxOamPmCfgLossLmmTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmTableLastChg.setStatus("current")
_TmnxOamPmCfgTableObjs_ObjectIdentity = ObjectIdentity
tmnxOamPmCfgTableObjs = _TmnxOamPmCfgTableObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3)
)
_TmnxOamPmCfgBinGroupTable_Object = MibTable
tmnxOamPmCfgBinGroupTable = _TmnxOamPmCfgBinGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinGroupTable.setStatus("current")
_TmnxOamPmCfgBinGroupEntry_Object = MibTableRow
tmnxOamPmCfgBinGroupEntry = _TmnxOamPmCfgBinGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 1, 1)
)
tmnxOamPmCfgBinGroupEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinGroupId"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinGroupEntry.setStatus("current")
_TmnxOamPmCfgBinGroupId_Type = TmnxOamPmBinGroupId
_TmnxOamPmCfgBinGroupId_Object = MibTableColumn
tmnxOamPmCfgBinGroupId = _TmnxOamPmCfgBinGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 1, 1, 1),
    _TmnxOamPmCfgBinGroupId_Type()
)
tmnxOamPmCfgBinGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinGroupId.setStatus("current")
_TmnxOamPmCfgBinGroupRowStatus_Type = RowStatus
_TmnxOamPmCfgBinGroupRowStatus_Object = MibTableColumn
tmnxOamPmCfgBinGroupRowStatus = _TmnxOamPmCfgBinGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 1, 1, 2),
    _TmnxOamPmCfgBinGroupRowStatus_Type()
)
tmnxOamPmCfgBinGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinGroupRowStatus.setStatus("current")


class _TmnxOamPmCfgBinGroupAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type tmnxOamPmCfgBinGroupAdminStatus based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxOamPmCfgBinGroupAdminStatus_Type.__name__ = "TmnxEnabledDisabled"
_TmnxOamPmCfgBinGroupAdminStatus_Object = MibTableColumn
tmnxOamPmCfgBinGroupAdminStatus = _TmnxOamPmCfgBinGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 1, 1, 3),
    _TmnxOamPmCfgBinGroupAdminStatus_Type()
)
tmnxOamPmCfgBinGroupAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinGroupAdminStatus.setStatus("current")


class _TmnxOamPmCfgBinGroupDescription_Type(TItemDescription):
    """Custom type tmnxOamPmCfgBinGroupDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxOamPmCfgBinGroupDescription_Type.__name__ = "TItemDescription"
_TmnxOamPmCfgBinGroupDescription_Object = MibTableColumn
tmnxOamPmCfgBinGroupDescription = _TmnxOamPmCfgBinGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 1, 1, 4),
    _TmnxOamPmCfgBinGroupDescription_Type()
)
tmnxOamPmCfgBinGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinGroupDescription.setStatus("current")


class _TmnxOamPmCfgBinGroupFdBinCount_Type(Unsigned32):
    """Custom type tmnxOamPmCfgBinGroupFdBinCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_TmnxOamPmCfgBinGroupFdBinCount_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgBinGroupFdBinCount_Object = MibTableColumn
tmnxOamPmCfgBinGroupFdBinCount = _TmnxOamPmCfgBinGroupFdBinCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 1, 1, 5),
    _TmnxOamPmCfgBinGroupFdBinCount_Type()
)
tmnxOamPmCfgBinGroupFdBinCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinGroupFdBinCount.setStatus("current")


class _TmnxOamPmCfgBinGroupFdrBinCount_Type(Unsigned32):
    """Custom type tmnxOamPmCfgBinGroupFdrBinCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_TmnxOamPmCfgBinGroupFdrBinCount_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgBinGroupFdrBinCount_Object = MibTableColumn
tmnxOamPmCfgBinGroupFdrBinCount = _TmnxOamPmCfgBinGroupFdrBinCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 1, 1, 6),
    _TmnxOamPmCfgBinGroupFdrBinCount_Type()
)
tmnxOamPmCfgBinGroupFdrBinCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinGroupFdrBinCount.setStatus("current")


class _TmnxOamPmCfgBinGroupIfdvBinCount_Type(Unsigned32):
    """Custom type tmnxOamPmCfgBinGroupIfdvBinCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_TmnxOamPmCfgBinGroupIfdvBinCount_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgBinGroupIfdvBinCount_Object = MibTableColumn
tmnxOamPmCfgBinGroupIfdvBinCount = _TmnxOamPmCfgBinGroupIfdvBinCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 1, 1, 7),
    _TmnxOamPmCfgBinGroupIfdvBinCount_Type()
)
tmnxOamPmCfgBinGroupIfdvBinCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinGroupIfdvBinCount.setStatus("current")
_TmnxOamPmCfgBinTable_Object = MibTable
tmnxOamPmCfgBinTable = _TmnxOamPmCfgBinTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinTable.setStatus("current")
_TmnxOamPmCfgBinEntry_Object = MibTableRow
tmnxOamPmCfgBinEntry = _TmnxOamPmCfgBinEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 2, 1)
)
tmnxOamPmCfgBinEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinGroupId"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinType"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinNum"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinEntry.setStatus("current")
_TmnxOamPmCfgBinType_Type = TmnxOamPmBinType
_TmnxOamPmCfgBinType_Object = MibTableColumn
tmnxOamPmCfgBinType = _TmnxOamPmCfgBinType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 2, 1, 1),
    _TmnxOamPmCfgBinType_Type()
)
tmnxOamPmCfgBinType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinType.setStatus("current")


class _TmnxOamPmCfgBinNum_Type(Unsigned32):
    """Custom type tmnxOamPmCfgBinNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_TmnxOamPmCfgBinNum_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgBinNum_Object = MibTableColumn
tmnxOamPmCfgBinNum = _TmnxOamPmCfgBinNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 2, 1, 2),
    _TmnxOamPmCfgBinNum_Type()
)
tmnxOamPmCfgBinNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinNum.setStatus("current")


class _TmnxOamPmCfgBinLowerBound_Type(Unsigned32):
    """Custom type tmnxOamPmCfgBinLowerBound based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamPmCfgBinLowerBound_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgBinLowerBound_Object = MibTableColumn
tmnxOamPmCfgBinLowerBound = _TmnxOamPmCfgBinLowerBound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 2, 1, 3),
    _TmnxOamPmCfgBinLowerBound_Type()
)
tmnxOamPmCfgBinLowerBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinLowerBound.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinLowerBound.setUnits("microseconds")
_TmnxOamPmCfgSessTable_Object = MibTable
tmnxOamPmCfgSessTable = _TmnxOamPmCfgSessTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 3)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessTable.setStatus("current")
_TmnxOamPmCfgSessEntry_Object = MibTableRow
tmnxOamPmCfgSessEntry = _TmnxOamPmCfgSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 3, 1)
)
tmnxOamPmCfgSessEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessEntry.setStatus("current")
_TmnxOamPmCfgSessName_Type = TNamedItem
_TmnxOamPmCfgSessName_Object = MibTableColumn
tmnxOamPmCfgSessName = _TmnxOamPmCfgSessName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 3, 1, 1),
    _TmnxOamPmCfgSessName_Type()
)
tmnxOamPmCfgSessName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessName.setStatus("current")
_TmnxOamPmCfgSessRowStatus_Type = RowStatus
_TmnxOamPmCfgSessRowStatus_Object = MibTableColumn
tmnxOamPmCfgSessRowStatus = _TmnxOamPmCfgSessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 3, 1, 2),
    _TmnxOamPmCfgSessRowStatus_Type()
)
tmnxOamPmCfgSessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessRowStatus.setStatus("current")
_TmnxOamPmCfgSessTestFamily_Type = TmnxOamPmTestFamily
_TmnxOamPmCfgSessTestFamily_Object = MibTableColumn
tmnxOamPmCfgSessTestFamily = _TmnxOamPmCfgSessTestFamily_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 3, 1, 3),
    _TmnxOamPmCfgSessTestFamily_Type()
)
tmnxOamPmCfgSessTestFamily.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessTestFamily.setStatus("current")


class _TmnxOamPmCfgSessType_Type(TmnxOamPmSessionType):
    """Custom type tmnxOamPmCfgSessType based on TmnxOamPmSessionType"""
    defaultValue = 1


_TmnxOamPmCfgSessType_Type.__name__ = "TmnxOamPmSessionType"
_TmnxOamPmCfgSessType_Object = MibTableColumn
tmnxOamPmCfgSessType = _TmnxOamPmCfgSessType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 3, 1, 4),
    _TmnxOamPmCfgSessType_Type()
)
tmnxOamPmCfgSessType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessType.setStatus("current")


class _TmnxOamPmCfgSessBinGroupId_Type(TmnxOamPmBinGroupId):
    """Custom type tmnxOamPmCfgSessBinGroupId based on TmnxOamPmBinGroupId"""
    defaultValue = 1


_TmnxOamPmCfgSessBinGroupId_Type.__name__ = "TmnxOamPmBinGroupId"
_TmnxOamPmCfgSessBinGroupId_Object = MibTableColumn
tmnxOamPmCfgSessBinGroupId = _TmnxOamPmCfgSessBinGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 3, 1, 5),
    _TmnxOamPmCfgSessBinGroupId_Type()
)
tmnxOamPmCfgSessBinGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessBinGroupId.setStatus("current")


class _TmnxOamPmCfgSessDescription_Type(TItemDescription):
    """Custom type tmnxOamPmCfgSessDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxOamPmCfgSessDescription_Type.__name__ = "TItemDescription"
_TmnxOamPmCfgSessDescription_Object = MibTableColumn
tmnxOamPmCfgSessDescription = _TmnxOamPmCfgSessDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 3, 1, 6),
    _TmnxOamPmCfgSessDescription_Type()
)
tmnxOamPmCfgSessDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessDescription.setStatus("current")
_TmnxOamPmCfgSessEthTable_Object = MibTable
tmnxOamPmCfgSessEthTable = _TmnxOamPmCfgSessEthTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 4)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessEthTable.setStatus("current")
_TmnxOamPmCfgSessEthEntry_Object = MibTableRow
tmnxOamPmCfgSessEthEntry = _TmnxOamPmCfgSessEthEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 4, 1)
)
tmnxOamPmCfgSessEthEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessEthEntry.setStatus("current")


class _TmnxOamPmCfgSessEthSrcMepId_Type(Dot1agCfmMepIdOrZero):
    """Custom type tmnxOamPmCfgSessEthSrcMepId based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_TmnxOamPmCfgSessEthSrcMepId_Type.__name__ = "Dot1agCfmMepIdOrZero"
_TmnxOamPmCfgSessEthSrcMepId_Object = MibTableColumn
tmnxOamPmCfgSessEthSrcMepId = _TmnxOamPmCfgSessEthSrcMepId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 4, 1, 1),
    _TmnxOamPmCfgSessEthSrcMepId_Type()
)
tmnxOamPmCfgSessEthSrcMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessEthSrcMepId.setStatus("current")


class _TmnxOamPmCfgSessEthSrcMdIndex_Type(Unsigned32):
    """Custom type tmnxOamPmCfgSessEthSrcMdIndex based on Unsigned32"""
    defaultValue = 0


_TmnxOamPmCfgSessEthSrcMdIndex_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgSessEthSrcMdIndex_Object = MibTableColumn
tmnxOamPmCfgSessEthSrcMdIndex = _TmnxOamPmCfgSessEthSrcMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 4, 1, 2),
    _TmnxOamPmCfgSessEthSrcMdIndex_Type()
)
tmnxOamPmCfgSessEthSrcMdIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessEthSrcMdIndex.setStatus("current")


class _TmnxOamPmCfgSessEthSrcMaIndex_Type(Unsigned32):
    """Custom type tmnxOamPmCfgSessEthSrcMaIndex based on Unsigned32"""
    defaultValue = 0


_TmnxOamPmCfgSessEthSrcMaIndex_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgSessEthSrcMaIndex_Object = MibTableColumn
tmnxOamPmCfgSessEthSrcMaIndex = _TmnxOamPmCfgSessEthSrcMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 4, 1, 3),
    _TmnxOamPmCfgSessEthSrcMaIndex_Type()
)
tmnxOamPmCfgSessEthSrcMaIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessEthSrcMaIndex.setStatus("current")


class _TmnxOamPmCfgSessEthPriority_Type(Unsigned32):
    """Custom type tmnxOamPmCfgSessEthPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TmnxOamPmCfgSessEthPriority_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgSessEthPriority_Object = MibTableColumn
tmnxOamPmCfgSessEthPriority = _TmnxOamPmCfgSessEthPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 4, 1, 4),
    _TmnxOamPmCfgSessEthPriority_Type()
)
tmnxOamPmCfgSessEthPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessEthPriority.setStatus("current")


class _TmnxOamPmCfgSessEthDestMacAddr_Type(MacAddress):
    """Custom type tmnxOamPmCfgSessEthDestMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxOamPmCfgSessEthDestMacAddr_Type.__name__ = "MacAddress"
_TmnxOamPmCfgSessEthDestMacAddr_Object = MibTableColumn
tmnxOamPmCfgSessEthDestMacAddr = _TmnxOamPmCfgSessEthDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 4, 1, 5),
    _TmnxOamPmCfgSessEthDestMacAddr_Type()
)
tmnxOamPmCfgSessEthDestMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessEthDestMacAddr.setStatus("current")
_TmnxOamPmCfgDelayDmmTable_Object = MibTable
tmnxOamPmCfgDelayDmmTable = _TmnxOamPmCfgDelayDmmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 5)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmTable.setStatus("current")
_TmnxOamPmCfgDelayDmmEntry_Object = MibTableRow
tmnxOamPmCfgDelayDmmEntry = _TmnxOamPmCfgDelayDmmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 5, 1)
)
tmnxOamPmCfgDelayDmmEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmEntry.setStatus("current")
_TmnxOamPmCfgDelayDmmRowStatus_Type = RowStatus
_TmnxOamPmCfgDelayDmmRowStatus_Object = MibTableColumn
tmnxOamPmCfgDelayDmmRowStatus = _TmnxOamPmCfgDelayDmmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 5, 1, 1),
    _TmnxOamPmCfgDelayDmmRowStatus_Type()
)
tmnxOamPmCfgDelayDmmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmRowStatus.setStatus("current")


class _TmnxOamPmCfgDelayDmmAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type tmnxOamPmCfgDelayDmmAdminStatus based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxOamPmCfgDelayDmmAdminStatus_Type.__name__ = "TmnxEnabledDisabled"
_TmnxOamPmCfgDelayDmmAdminStatus_Object = MibTableColumn
tmnxOamPmCfgDelayDmmAdminStatus = _TmnxOamPmCfgDelayDmmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 5, 1, 2),
    _TmnxOamPmCfgDelayDmmAdminStatus_Type()
)
tmnxOamPmCfgDelayDmmAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmAdminStatus.setStatus("current")
_TmnxOamPmCfgDelayDmmOnDmndStatus_Type = TmnxEnabledDisabledOrNA
_TmnxOamPmCfgDelayDmmOnDmndStatus_Object = MibTableColumn
tmnxOamPmCfgDelayDmmOnDmndStatus = _TmnxOamPmCfgDelayDmmOnDmndStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 5, 1, 3),
    _TmnxOamPmCfgDelayDmmOnDmndStatus_Type()
)
tmnxOamPmCfgDelayDmmOnDmndStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmOnDmndStatus.setStatus("current")


class _TmnxOamPmCfgDelayDmmTestId_Type(Unsigned32):
    """Custom type tmnxOamPmCfgDelayDmmTestId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxOamPmCfgDelayDmmTestId_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgDelayDmmTestId_Object = MibTableColumn
tmnxOamPmCfgDelayDmmTestId = _TmnxOamPmCfgDelayDmmTestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 5, 1, 4),
    _TmnxOamPmCfgDelayDmmTestId_Type()
)
tmnxOamPmCfgDelayDmmTestId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmTestId.setStatus("current")


class _TmnxOamPmCfgDelayDmmInterval_Type(Unsigned32):
    """Custom type tmnxOamPmCfgDelayDmmInterval based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(1000, 1000),
    )


_TmnxOamPmCfgDelayDmmInterval_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgDelayDmmInterval_Object = MibTableColumn
tmnxOamPmCfgDelayDmmInterval = _TmnxOamPmCfgDelayDmmInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 5, 1, 5),
    _TmnxOamPmCfgDelayDmmInterval_Type()
)
tmnxOamPmCfgDelayDmmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmInterval.setUnits("milliseconds")


class _TmnxOamPmCfgDelayDmmDataTlvSize_Type(Unsigned32):
    """Custom type tmnxOamPmCfgDelayDmmDataTlvSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 2000),
    )


_TmnxOamPmCfgDelayDmmDataTlvSize_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgDelayDmmDataTlvSize_Object = MibTableColumn
tmnxOamPmCfgDelayDmmDataTlvSize = _TmnxOamPmCfgDelayDmmDataTlvSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 5, 1, 6),
    _TmnxOamPmCfgDelayDmmDataTlvSize_Type()
)
tmnxOamPmCfgDelayDmmDataTlvSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmDataTlvSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmDataTlvSize.setUnits("octets")


class _TmnxOamPmCfgDelayDmmTestDuration_Type(Unsigned32):
    """Custom type tmnxOamPmCfgDelayDmmTestDuration based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TmnxOamPmCfgDelayDmmTestDuration_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgDelayDmmTestDuration_Object = MibTableColumn
tmnxOamPmCfgDelayDmmTestDuration = _TmnxOamPmCfgDelayDmmTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 5, 1, 7),
    _TmnxOamPmCfgDelayDmmTestDuration_Type()
)
tmnxOamPmCfgDelayDmmTestDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmTestDuration.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmTestDuration.setUnits("seconds")


class _TmnxOamPmCfgDelayDmmRunTimeLeft_Type(Unsigned32):
    """Custom type tmnxOamPmCfgDelayDmmRunTimeLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TmnxOamPmCfgDelayDmmRunTimeLeft_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgDelayDmmRunTimeLeft_Object = MibTableColumn
tmnxOamPmCfgDelayDmmRunTimeLeft = _TmnxOamPmCfgDelayDmmRunTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 5, 1, 8),
    _TmnxOamPmCfgDelayDmmRunTimeLeft_Type()
)
tmnxOamPmCfgDelayDmmRunTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmRunTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmRunTimeLeft.setUnits("seconds")
_TmnxOamPmCfgLossSlmTable_Object = MibTable
tmnxOamPmCfgLossSlmTable = _TmnxOamPmCfgLossSlmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmTable.setStatus("current")
_TmnxOamPmCfgLossSlmEntry_Object = MibTableRow
tmnxOamPmCfgLossSlmEntry = _TmnxOamPmCfgLossSlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6, 1)
)
tmnxOamPmCfgLossSlmEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmEntry.setStatus("current")
_TmnxOamPmCfgLossSlmRowStatus_Type = RowStatus
_TmnxOamPmCfgLossSlmRowStatus_Object = MibTableColumn
tmnxOamPmCfgLossSlmRowStatus = _TmnxOamPmCfgLossSlmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6, 1, 1),
    _TmnxOamPmCfgLossSlmRowStatus_Type()
)
tmnxOamPmCfgLossSlmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmRowStatus.setStatus("current")


class _TmnxOamPmCfgLossSlmAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type tmnxOamPmCfgLossSlmAdminStatus based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxOamPmCfgLossSlmAdminStatus_Type.__name__ = "TmnxEnabledDisabled"
_TmnxOamPmCfgLossSlmAdminStatus_Object = MibTableColumn
tmnxOamPmCfgLossSlmAdminStatus = _TmnxOamPmCfgLossSlmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6, 1, 2),
    _TmnxOamPmCfgLossSlmAdminStatus_Type()
)
tmnxOamPmCfgLossSlmAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmAdminStatus.setStatus("current")
_TmnxOamPmCfgLossSlmOnDmndStatus_Type = TmnxEnabledDisabledOrNA
_TmnxOamPmCfgLossSlmOnDmndStatus_Object = MibTableColumn
tmnxOamPmCfgLossSlmOnDmndStatus = _TmnxOamPmCfgLossSlmOnDmndStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6, 1, 3),
    _TmnxOamPmCfgLossSlmOnDmndStatus_Type()
)
tmnxOamPmCfgLossSlmOnDmndStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmOnDmndStatus.setStatus("current")


class _TmnxOamPmCfgLossSlmTestId_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossSlmTestId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxOamPmCfgLossSlmTestId_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossSlmTestId_Object = MibTableColumn
tmnxOamPmCfgLossSlmTestId = _TmnxOamPmCfgLossSlmTestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6, 1, 4),
    _TmnxOamPmCfgLossSlmTestId_Type()
)
tmnxOamPmCfgLossSlmTestId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmTestId.setStatus("current")


class _TmnxOamPmCfgLossSlmInterval_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossSlmInterval based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(1000, 1000),
    )


_TmnxOamPmCfgLossSlmInterval_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossSlmInterval_Object = MibTableColumn
tmnxOamPmCfgLossSlmInterval = _TmnxOamPmCfgLossSlmInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6, 1, 5),
    _TmnxOamPmCfgLossSlmInterval_Type()
)
tmnxOamPmCfgLossSlmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmInterval.setUnits("milliseconds")


class _TmnxOamPmCfgLossSlmDataTlvSize_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossSlmDataTlvSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 2000),
    )


_TmnxOamPmCfgLossSlmDataTlvSize_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossSlmDataTlvSize_Object = MibTableColumn
tmnxOamPmCfgLossSlmDataTlvSize = _TmnxOamPmCfgLossSlmDataTlvSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6, 1, 6),
    _TmnxOamPmCfgLossSlmDataTlvSize_Type()
)
tmnxOamPmCfgLossSlmDataTlvSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmDataTlvSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmDataTlvSize.setUnits("octets")


class _TmnxOamPmCfgLossSlmTxFrmsPerDelT_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossSlmTxFrmsPerDelT based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_TmnxOamPmCfgLossSlmTxFrmsPerDelT_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossSlmTxFrmsPerDelT_Object = MibTableColumn
tmnxOamPmCfgLossSlmTxFrmsPerDelT = _TmnxOamPmCfgLossSlmTxFrmsPerDelT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6, 1, 7),
    _TmnxOamPmCfgLossSlmTxFrmsPerDelT_Type()
)
tmnxOamPmCfgLossSlmTxFrmsPerDelT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmTxFrmsPerDelT.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmTxFrmsPerDelT.setUnits("frames")


class _TmnxOamPmCfgLossSlmConsecDeltaTs_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossSlmConsecDeltaTs based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_TmnxOamPmCfgLossSlmConsecDeltaTs_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossSlmConsecDeltaTs_Object = MibTableColumn
tmnxOamPmCfgLossSlmConsecDeltaTs = _TmnxOamPmCfgLossSlmConsecDeltaTs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6, 1, 8),
    _TmnxOamPmCfgLossSlmConsecDeltaTs_Type()
)
tmnxOamPmCfgLossSlmConsecDeltaTs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmConsecDeltaTs.setStatus("current")


class _TmnxOamPmCfgLossSlmChliThreshold_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossSlmChliThreshold based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_TmnxOamPmCfgLossSlmChliThreshold_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossSlmChliThreshold_Object = MibTableColumn
tmnxOamPmCfgLossSlmChliThreshold = _TmnxOamPmCfgLossSlmChliThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6, 1, 9),
    _TmnxOamPmCfgLossSlmChliThreshold_Type()
)
tmnxOamPmCfgLossSlmChliThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmChliThreshold.setStatus("current")


class _TmnxOamPmCfgLossSlmFlrThreshold_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossSlmFlrThreshold based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxOamPmCfgLossSlmFlrThreshold_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossSlmFlrThreshold_Object = MibTableColumn
tmnxOamPmCfgLossSlmFlrThreshold = _TmnxOamPmCfgLossSlmFlrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6, 1, 10),
    _TmnxOamPmCfgLossSlmFlrThreshold_Type()
)
tmnxOamPmCfgLossSlmFlrThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmFlrThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmFlrThreshold.setUnits("percent")


class _TmnxOamPmCfgLossSlmTestDuration_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossSlmTestDuration based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TmnxOamPmCfgLossSlmTestDuration_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossSlmTestDuration_Object = MibTableColumn
tmnxOamPmCfgLossSlmTestDuration = _TmnxOamPmCfgLossSlmTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6, 1, 11),
    _TmnxOamPmCfgLossSlmTestDuration_Type()
)
tmnxOamPmCfgLossSlmTestDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmTestDuration.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmTestDuration.setUnits("seconds")


class _TmnxOamPmCfgLossSlmRunTimeLeft_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossSlmRunTimeLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TmnxOamPmCfgLossSlmRunTimeLeft_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossSlmRunTimeLeft_Object = MibTableColumn
tmnxOamPmCfgLossSlmRunTimeLeft = _TmnxOamPmCfgLossSlmRunTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6, 1, 12),
    _TmnxOamPmCfgLossSlmRunTimeLeft_Type()
)
tmnxOamPmCfgLossSlmRunTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmRunTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmRunTimeLeft.setUnits("seconds")
_TmnxOamPmCfgMeasIntvlTable_Object = MibTable
tmnxOamPmCfgMeasIntvlTable = _TmnxOamPmCfgMeasIntvlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 7)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgMeasIntvlTable.setStatus("current")
_TmnxOamPmCfgMeasIntvlEntry_Object = MibTableRow
tmnxOamPmCfgMeasIntvlEntry = _TmnxOamPmCfgMeasIntvlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 7, 1)
)
tmnxOamPmCfgMeasIntvlEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgMeasIntvlDuration"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgMeasIntvlEntry.setStatus("current")
_TmnxOamPmCfgMeasIntvlDuration_Type = TmnxOamPmCfgMeasIntervalDuration
_TmnxOamPmCfgMeasIntvlDuration_Object = MibTableColumn
tmnxOamPmCfgMeasIntvlDuration = _TmnxOamPmCfgMeasIntvlDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 7, 1, 1),
    _TmnxOamPmCfgMeasIntvlDuration_Type()
)
tmnxOamPmCfgMeasIntvlDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmCfgMeasIntvlDuration.setStatus("current")
_TmnxOamPmCfgMeasIntvlRowStatus_Type = RowStatus
_TmnxOamPmCfgMeasIntvlRowStatus_Object = MibTableColumn
tmnxOamPmCfgMeasIntvlRowStatus = _TmnxOamPmCfgMeasIntvlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 7, 1, 2),
    _TmnxOamPmCfgMeasIntvlRowStatus_Type()
)
tmnxOamPmCfgMeasIntvlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgMeasIntvlRowStatus.setStatus("current")


class _TmnxOamPmCfgMeasIntvlAccntPolicy_Type(Unsigned32):
    """Custom type tmnxOamPmCfgMeasIntvlAccntPolicy based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 99),
    )


_TmnxOamPmCfgMeasIntvlAccntPolicy_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgMeasIntvlAccntPolicy_Object = MibTableColumn
tmnxOamPmCfgMeasIntvlAccntPolicy = _TmnxOamPmCfgMeasIntvlAccntPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 7, 1, 3),
    _TmnxOamPmCfgMeasIntvlAccntPolicy_Type()
)
tmnxOamPmCfgMeasIntvlAccntPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgMeasIntvlAccntPolicy.setStatus("current")


class _TmnxOamPmCfgMeasIntvlsStored_Type(Unsigned32):
    """Custom type tmnxOamPmCfgMeasIntvlsStored based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_TmnxOamPmCfgMeasIntvlsStored_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgMeasIntvlsStored_Object = MibTableColumn
tmnxOamPmCfgMeasIntvlsStored = _TmnxOamPmCfgMeasIntvlsStored_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 7, 1, 4),
    _TmnxOamPmCfgMeasIntvlsStored_Type()
)
tmnxOamPmCfgMeasIntvlsStored.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgMeasIntvlsStored.setStatus("current")


class _TmnxOamPmCfgMeasIntvlBoundaryTyp_Type(Integer32):
    """Custom type tmnxOamPmCfgMeasIntvlBoundaryTyp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clockAligned", 1),
          ("testRelative", 2))
    )


_TmnxOamPmCfgMeasIntvlBoundaryTyp_Type.__name__ = "Integer32"
_TmnxOamPmCfgMeasIntvlBoundaryTyp_Object = MibTableColumn
tmnxOamPmCfgMeasIntvlBoundaryTyp = _TmnxOamPmCfgMeasIntvlBoundaryTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 7, 1, 5),
    _TmnxOamPmCfgMeasIntvlBoundaryTyp_Type()
)
tmnxOamPmCfgMeasIntvlBoundaryTyp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgMeasIntvlBoundaryTyp.setStatus("current")


class _TmnxOamPmCfgMeasIntvlClockOffset_Type(Unsigned32):
    """Custom type tmnxOamPmCfgMeasIntvlClockOffset based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_TmnxOamPmCfgMeasIntvlClockOffset_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgMeasIntvlClockOffset_Object = MibTableColumn
tmnxOamPmCfgMeasIntvlClockOffset = _TmnxOamPmCfgMeasIntvlClockOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 7, 1, 6),
    _TmnxOamPmCfgMeasIntvlClockOffset_Type()
)
tmnxOamPmCfgMeasIntvlClockOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgMeasIntvlClockOffset.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgMeasIntvlClockOffset.setUnits("seconds")
_TmnxOamPmCfgSessIpTable_Object = MibTable
tmnxOamPmCfgSessIpTable = _TmnxOamPmCfgSessIpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpTable.setStatus("current")
_TmnxOamPmCfgSessIpEntry_Object = MibTableRow
tmnxOamPmCfgSessIpEntry = _TmnxOamPmCfgSessIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1)
)
tmnxOamPmCfgSessIpEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpEntry.setStatus("current")


class _TmnxOamPmCfgSessIpServiceId_Type(Unsigned32):
    """Custom type tmnxOamPmCfgSessIpServiceId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxOamPmCfgSessIpServiceId_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgSessIpServiceId_Object = MibTableColumn
tmnxOamPmCfgSessIpServiceId = _TmnxOamPmCfgSessIpServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 1),
    _TmnxOamPmCfgSessIpServiceId_Type()
)
tmnxOamPmCfgSessIpServiceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpServiceId.setStatus("current")


class _TmnxOamPmCfgSessIpSrcAddressType_Type(InetAddressType):
    """Custom type tmnxOamPmCfgSessIpSrcAddressType based on InetAddressType"""
    defaultValue = 0


_TmnxOamPmCfgSessIpSrcAddressType_Type.__name__ = "InetAddressType"
_TmnxOamPmCfgSessIpSrcAddressType_Object = MibTableColumn
tmnxOamPmCfgSessIpSrcAddressType = _TmnxOamPmCfgSessIpSrcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 2),
    _TmnxOamPmCfgSessIpSrcAddressType_Type()
)
tmnxOamPmCfgSessIpSrcAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpSrcAddressType.setStatus("current")


class _TmnxOamPmCfgSessIpSrcAddress_Type(InetAddress):
    """Custom type tmnxOamPmCfgSessIpSrcAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamPmCfgSessIpSrcAddress_Type.__name__ = "InetAddress"
_TmnxOamPmCfgSessIpSrcAddress_Object = MibTableColumn
tmnxOamPmCfgSessIpSrcAddress = _TmnxOamPmCfgSessIpSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 3),
    _TmnxOamPmCfgSessIpSrcAddress_Type()
)
tmnxOamPmCfgSessIpSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpSrcAddress.setStatus("current")


class _TmnxOamPmCfgSessIpDstAddressType_Type(InetAddressType):
    """Custom type tmnxOamPmCfgSessIpDstAddressType based on InetAddressType"""
    defaultValue = 0


_TmnxOamPmCfgSessIpDstAddressType_Type.__name__ = "InetAddressType"
_TmnxOamPmCfgSessIpDstAddressType_Object = MibTableColumn
tmnxOamPmCfgSessIpDstAddressType = _TmnxOamPmCfgSessIpDstAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 4),
    _TmnxOamPmCfgSessIpDstAddressType_Type()
)
tmnxOamPmCfgSessIpDstAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpDstAddressType.setStatus("current")


class _TmnxOamPmCfgSessIpDstAddress_Type(InetAddress):
    """Custom type tmnxOamPmCfgSessIpDstAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamPmCfgSessIpDstAddress_Type.__name__ = "InetAddress"
_TmnxOamPmCfgSessIpDstAddress_Object = MibTableColumn
tmnxOamPmCfgSessIpDstAddress = _TmnxOamPmCfgSessIpDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 5),
    _TmnxOamPmCfgSessIpDstAddress_Type()
)
tmnxOamPmCfgSessIpDstAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpDstAddress.setStatus("current")


class _TmnxOamPmCfgSessIpDstUdpPort_Type(InetPortNumber):
    """Custom type tmnxOamPmCfgSessIpDstUdpPort based on InetPortNumber"""
    defaultValue = 0

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1024, 65535),
    )


_TmnxOamPmCfgSessIpDstUdpPort_Type.__name__ = "InetPortNumber"
_TmnxOamPmCfgSessIpDstUdpPort_Object = MibTableColumn
tmnxOamPmCfgSessIpDstUdpPort = _TmnxOamPmCfgSessIpDstUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 6),
    _TmnxOamPmCfgSessIpDstUdpPort_Type()
)
tmnxOamPmCfgSessIpDstUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpDstUdpPort.setStatus("current")


class _TmnxOamPmCfgSessIpBypassRouting_Type(TruthValue):
    """Custom type tmnxOamPmCfgSessIpBypassRouting based on TruthValue"""
    defaultValue = 2


_TmnxOamPmCfgSessIpBypassRouting_Type.__name__ = "TruthValue"
_TmnxOamPmCfgSessIpBypassRouting_Object = MibTableColumn
tmnxOamPmCfgSessIpBypassRouting = _TmnxOamPmCfgSessIpBypassRouting_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 7),
    _TmnxOamPmCfgSessIpBypassRouting_Type()
)
tmnxOamPmCfgSessIpBypassRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpBypassRouting.setStatus("current")


class _TmnxOamPmCfgSessIpEgressIfName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOamPmCfgSessIpEgressIfName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOamPmCfgSessIpEgressIfName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOamPmCfgSessIpEgressIfName_Object = MibTableColumn
tmnxOamPmCfgSessIpEgressIfName = _TmnxOamPmCfgSessIpEgressIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 8),
    _TmnxOamPmCfgSessIpEgressIfName_Type()
)
tmnxOamPmCfgSessIpEgressIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpEgressIfName.setStatus("current")


class _TmnxOamPmCfgSessIpNhAddressType_Type(InetAddressType):
    """Custom type tmnxOamPmCfgSessIpNhAddressType based on InetAddressType"""
    defaultValue = 0


_TmnxOamPmCfgSessIpNhAddressType_Type.__name__ = "InetAddressType"
_TmnxOamPmCfgSessIpNhAddressType_Object = MibTableColumn
tmnxOamPmCfgSessIpNhAddressType = _TmnxOamPmCfgSessIpNhAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 9),
    _TmnxOamPmCfgSessIpNhAddressType_Type()
)
tmnxOamPmCfgSessIpNhAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpNhAddressType.setStatus("current")


class _TmnxOamPmCfgSessIpNhAddress_Type(InetAddress):
    """Custom type tmnxOamPmCfgSessIpNhAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamPmCfgSessIpNhAddress_Type.__name__ = "InetAddress"
_TmnxOamPmCfgSessIpNhAddress_Object = MibTableColumn
tmnxOamPmCfgSessIpNhAddress = _TmnxOamPmCfgSessIpNhAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 10),
    _TmnxOamPmCfgSessIpNhAddress_Type()
)
tmnxOamPmCfgSessIpNhAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpNhAddress.setStatus("current")


class _TmnxOamPmCfgSessIpForwardClass_Type(TFCName):
    """Custom type tmnxOamPmCfgSessIpForwardClass based on TFCName"""
    defaultValue = OctetString("be")


_TmnxOamPmCfgSessIpForwardClass_Type.__name__ = "TFCName"
_TmnxOamPmCfgSessIpForwardClass_Object = MibTableColumn
tmnxOamPmCfgSessIpForwardClass = _TmnxOamPmCfgSessIpForwardClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 11),
    _TmnxOamPmCfgSessIpForwardClass_Type()
)
tmnxOamPmCfgSessIpForwardClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpForwardClass.setStatus("current")


class _TmnxOamPmCfgSessIpProfile_Type(TProfile):
    """Custom type tmnxOamPmCfgSessIpProfile based on TProfile"""
    defaultValue = 2


_TmnxOamPmCfgSessIpProfile_Type.__name__ = "TProfile"
_TmnxOamPmCfgSessIpProfile_Object = MibTableColumn
tmnxOamPmCfgSessIpProfile = _TmnxOamPmCfgSessIpProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 12),
    _TmnxOamPmCfgSessIpProfile_Type()
)
tmnxOamPmCfgSessIpProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpProfile.setStatus("current")


class _TmnxOamPmCfgSessIpTtl_Type(Unsigned32):
    """Custom type tmnxOamPmCfgSessIpTtl based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamPmCfgSessIpTtl_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgSessIpTtl_Object = MibTableColumn
tmnxOamPmCfgSessIpTtl = _TmnxOamPmCfgSessIpTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 13),
    _TmnxOamPmCfgSessIpTtl_Type()
)
tmnxOamPmCfgSessIpTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpTtl.setStatus("current")
_TmnxOamPmCfgTwampLtTable_Object = MibTable
tmnxOamPmCfgTwampLtTable = _TmnxOamPmCfgTwampLtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 9)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtTable.setStatus("current")
_TmnxOamPmCfgTwampLtEntry_Object = MibTableRow
tmnxOamPmCfgTwampLtEntry = _TmnxOamPmCfgTwampLtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 9, 1)
)
tmnxOamPmCfgTwampLtEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtEntry.setStatus("current")
_TmnxOamPmCfgTwampLtRowStatus_Type = RowStatus
_TmnxOamPmCfgTwampLtRowStatus_Object = MibTableColumn
tmnxOamPmCfgTwampLtRowStatus = _TmnxOamPmCfgTwampLtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 9, 1, 1),
    _TmnxOamPmCfgTwampLtRowStatus_Type()
)
tmnxOamPmCfgTwampLtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtRowStatus.setStatus("current")


class _TmnxOamPmCfgTwampLtAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type tmnxOamPmCfgTwampLtAdminStatus based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxOamPmCfgTwampLtAdminStatus_Type.__name__ = "TmnxEnabledDisabled"
_TmnxOamPmCfgTwampLtAdminStatus_Object = MibTableColumn
tmnxOamPmCfgTwampLtAdminStatus = _TmnxOamPmCfgTwampLtAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 9, 1, 2),
    _TmnxOamPmCfgTwampLtAdminStatus_Type()
)
tmnxOamPmCfgTwampLtAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtAdminStatus.setStatus("current")
_TmnxOamPmCfgTwampLtOnDmndStatus_Type = TmnxEnabledDisabledOrNA
_TmnxOamPmCfgTwampLtOnDmndStatus_Object = MibTableColumn
tmnxOamPmCfgTwampLtOnDmndStatus = _TmnxOamPmCfgTwampLtOnDmndStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 9, 1, 3),
    _TmnxOamPmCfgTwampLtOnDmndStatus_Type()
)
tmnxOamPmCfgTwampLtOnDmndStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtOnDmndStatus.setStatus("current")


class _TmnxOamPmCfgTwampLtTestId_Type(Unsigned32):
    """Custom type tmnxOamPmCfgTwampLtTestId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxOamPmCfgTwampLtTestId_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgTwampLtTestId_Object = MibTableColumn
tmnxOamPmCfgTwampLtTestId = _TmnxOamPmCfgTwampLtTestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 9, 1, 4),
    _TmnxOamPmCfgTwampLtTestId_Type()
)
tmnxOamPmCfgTwampLtTestId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtTestId.setStatus("current")


class _TmnxOamPmCfgTwampLtInterval_Type(Unsigned32):
    """Custom type tmnxOamPmCfgTwampLtInterval based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(1000, 1000),
    )


_TmnxOamPmCfgTwampLtInterval_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgTwampLtInterval_Object = MibTableColumn
tmnxOamPmCfgTwampLtInterval = _TmnxOamPmCfgTwampLtInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 9, 1, 5),
    _TmnxOamPmCfgTwampLtInterval_Type()
)
tmnxOamPmCfgTwampLtInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtInterval.setUnits("milliseconds")


class _TmnxOamPmCfgTwampLtPadSize_Type(Unsigned32):
    """Custom type tmnxOamPmCfgTwampLtPadSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_TmnxOamPmCfgTwampLtPadSize_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgTwampLtPadSize_Object = MibTableColumn
tmnxOamPmCfgTwampLtPadSize = _TmnxOamPmCfgTwampLtPadSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 9, 1, 6),
    _TmnxOamPmCfgTwampLtPadSize_Type()
)
tmnxOamPmCfgTwampLtPadSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtPadSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtPadSize.setUnits("octets")


class _TmnxOamPmCfgTwampLtTestDuration_Type(Unsigned32):
    """Custom type tmnxOamPmCfgTwampLtTestDuration based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TmnxOamPmCfgTwampLtTestDuration_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgTwampLtTestDuration_Object = MibTableColumn
tmnxOamPmCfgTwampLtTestDuration = _TmnxOamPmCfgTwampLtTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 9, 1, 7),
    _TmnxOamPmCfgTwampLtTestDuration_Type()
)
tmnxOamPmCfgTwampLtTestDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtTestDuration.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtTestDuration.setUnits("seconds")


class _TmnxOamPmCfgTwampLtRunTimeLeft_Type(Unsigned32):
    """Custom type tmnxOamPmCfgTwampLtRunTimeLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TmnxOamPmCfgTwampLtRunTimeLeft_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgTwampLtRunTimeLeft_Object = MibTableColumn
tmnxOamPmCfgTwampLtRunTimeLeft = _TmnxOamPmCfgTwampLtRunTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 9, 1, 8),
    _TmnxOamPmCfgTwampLtRunTimeLeft_Type()
)
tmnxOamPmCfgTwampLtRunTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtRunTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtRunTimeLeft.setUnits("seconds")
_TmnxOamPmCfgTwlRflTable_Object = MibTable
tmnxOamPmCfgTwlRflTable = _TmnxOamPmCfgTwlRflTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 10)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflTable.setStatus("current")
_TmnxOamPmCfgTwlRflEntry_Object = MibTableRow
tmnxOamPmCfgTwlRflEntry = _TmnxOamPmCfgTwlRflEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 10, 1)
)
tmnxOamPmCfgTwlRflEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflEntry.setStatus("current")
_TmnxOamPmCfgTwlRflRowStatus_Type = RowStatus
_TmnxOamPmCfgTwlRflRowStatus_Object = MibTableColumn
tmnxOamPmCfgTwlRflRowStatus = _TmnxOamPmCfgTwlRflRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 10, 1, 1),
    _TmnxOamPmCfgTwlRflRowStatus_Type()
)
tmnxOamPmCfgTwlRflRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflRowStatus.setStatus("current")


class _TmnxOamPmCfgTwlRflAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type tmnxOamPmCfgTwlRflAdminStatus based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxOamPmCfgTwlRflAdminStatus_Type.__name__ = "TmnxEnabledDisabled"
_TmnxOamPmCfgTwlRflAdminStatus_Object = MibTableColumn
tmnxOamPmCfgTwlRflAdminStatus = _TmnxOamPmCfgTwlRflAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 10, 1, 2),
    _TmnxOamPmCfgTwlRflAdminStatus_Type()
)
tmnxOamPmCfgTwlRflAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflAdminStatus.setStatus("current")


class _TmnxOamPmCfgTwlRflDescription_Type(TItemDescription):
    """Custom type tmnxOamPmCfgTwlRflDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxOamPmCfgTwlRflDescription_Type.__name__ = "TItemDescription"
_TmnxOamPmCfgTwlRflDescription_Object = MibTableColumn
tmnxOamPmCfgTwlRflDescription = _TmnxOamPmCfgTwlRflDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 10, 1, 3),
    _TmnxOamPmCfgTwlRflDescription_Type()
)
tmnxOamPmCfgTwlRflDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflDescription.setStatus("current")


class _TmnxOamPmCfgTwlRflListenUdpPort_Type(Unsigned32):
    """Custom type tmnxOamPmCfgTwlRflListenUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_TmnxOamPmCfgTwlRflListenUdpPort_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgTwlRflListenUdpPort_Object = MibTableColumn
tmnxOamPmCfgTwlRflListenUdpPort = _TmnxOamPmCfgTwlRflListenUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 10, 1, 4),
    _TmnxOamPmCfgTwlRflListenUdpPort_Type()
)
tmnxOamPmCfgTwlRflListenUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflListenUdpPort.setStatus("current")
_TmnxOamPmCfgTwlRflPfxTable_Object = MibTable
tmnxOamPmCfgTwlRflPfxTable = _TmnxOamPmCfgTwlRflPfxTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 11)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflPfxTable.setStatus("current")
_TmnxOamPmCfgTwlRflPfxEntry_Object = MibTableRow
tmnxOamPmCfgTwlRflPfxEntry = _TmnxOamPmCfgTwlRflPfxEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 11, 1)
)
tmnxOamPmCfgTwlRflPfxEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwlRflPfxPrefixType"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwlRflPfxPrefix"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwlRflPfxPrefixLen"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflPfxEntry.setStatus("current")


class _TmnxOamPmCfgTwlRflPfxPrefixType_Type(InetAddressType):
    """Custom type tmnxOamPmCfgTwlRflPfxPrefixType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_TmnxOamPmCfgTwlRflPfxPrefixType_Type.__name__ = "InetAddressType"
_TmnxOamPmCfgTwlRflPfxPrefixType_Object = MibTableColumn
tmnxOamPmCfgTwlRflPfxPrefixType = _TmnxOamPmCfgTwlRflPfxPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 11, 1, 1),
    _TmnxOamPmCfgTwlRflPfxPrefixType_Type()
)
tmnxOamPmCfgTwlRflPfxPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflPfxPrefixType.setStatus("current")


class _TmnxOamPmCfgTwlRflPfxPrefix_Type(InetAddress):
    """Custom type tmnxOamPmCfgTwlRflPfxPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamPmCfgTwlRflPfxPrefix_Type.__name__ = "InetAddress"
_TmnxOamPmCfgTwlRflPfxPrefix_Object = MibTableColumn
tmnxOamPmCfgTwlRflPfxPrefix = _TmnxOamPmCfgTwlRflPfxPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 11, 1, 2),
    _TmnxOamPmCfgTwlRflPfxPrefix_Type()
)
tmnxOamPmCfgTwlRflPfxPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflPfxPrefix.setStatus("current")


class _TmnxOamPmCfgTwlRflPfxPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxOamPmCfgTwlRflPfxPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxOamPmCfgTwlRflPfxPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxOamPmCfgTwlRflPfxPrefixLen_Object = MibTableColumn
tmnxOamPmCfgTwlRflPfxPrefixLen = _TmnxOamPmCfgTwlRflPfxPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 11, 1, 3),
    _TmnxOamPmCfgTwlRflPfxPrefixLen_Type()
)
tmnxOamPmCfgTwlRflPfxPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflPfxPrefixLen.setStatus("current")
_TmnxOamPmCfgTwlRflPfxRowStatus_Type = RowStatus
_TmnxOamPmCfgTwlRflPfxRowStatus_Object = MibTableColumn
tmnxOamPmCfgTwlRflPfxRowStatus = _TmnxOamPmCfgTwlRflPfxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 11, 1, 4),
    _TmnxOamPmCfgTwlRflPfxRowStatus_Type()
)
tmnxOamPmCfgTwlRflPfxRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflPfxRowStatus.setStatus("current")


class _TmnxOamPmCfgTwlRflPfxDescription_Type(TItemDescription):
    """Custom type tmnxOamPmCfgTwlRflPfxDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxOamPmCfgTwlRflPfxDescription_Type.__name__ = "TItemDescription"
_TmnxOamPmCfgTwlRflPfxDescription_Object = MibTableColumn
tmnxOamPmCfgTwlRflPfxDescription = _TmnxOamPmCfgTwlRflPfxDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 11, 1, 5),
    _TmnxOamPmCfgTwlRflPfxDescription_Type()
)
tmnxOamPmCfgTwlRflPfxDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflPfxDescription.setStatus("current")
_TmnxOamPmCfgLossLmmTable_Object = MibTable
tmnxOamPmCfgLossLmmTable = _TmnxOamPmCfgLossLmmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 12)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmTable.setStatus("current")
_TmnxOamPmCfgLossLmmEntry_Object = MibTableRow
tmnxOamPmCfgLossLmmEntry = _TmnxOamPmCfgLossLmmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 12, 1)
)
tmnxOamPmCfgLossLmmEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmEntry.setStatus("current")
_TmnxOamPmCfgLossLmmRowStatus_Type = RowStatus
_TmnxOamPmCfgLossLmmRowStatus_Object = MibTableColumn
tmnxOamPmCfgLossLmmRowStatus = _TmnxOamPmCfgLossLmmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 12, 1, 1),
    _TmnxOamPmCfgLossLmmRowStatus_Type()
)
tmnxOamPmCfgLossLmmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmRowStatus.setStatus("current")


class _TmnxOamPmCfgLossLmmAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type tmnxOamPmCfgLossLmmAdminStatus based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxOamPmCfgLossLmmAdminStatus_Type.__name__ = "TmnxEnabledDisabled"
_TmnxOamPmCfgLossLmmAdminStatus_Object = MibTableColumn
tmnxOamPmCfgLossLmmAdminStatus = _TmnxOamPmCfgLossLmmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 12, 1, 2),
    _TmnxOamPmCfgLossLmmAdminStatus_Type()
)
tmnxOamPmCfgLossLmmAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmAdminStatus.setStatus("current")
_TmnxOamPmCfgLossLmmOnDmndStatus_Type = TmnxEnabledDisabledOrNA
_TmnxOamPmCfgLossLmmOnDmndStatus_Object = MibTableColumn
tmnxOamPmCfgLossLmmOnDmndStatus = _TmnxOamPmCfgLossLmmOnDmndStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 12, 1, 3),
    _TmnxOamPmCfgLossLmmOnDmndStatus_Type()
)
tmnxOamPmCfgLossLmmOnDmndStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmOnDmndStatus.setStatus("current")


class _TmnxOamPmCfgLossLmmTestId_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossLmmTestId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxOamPmCfgLossLmmTestId_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossLmmTestId_Object = MibTableColumn
tmnxOamPmCfgLossLmmTestId = _TmnxOamPmCfgLossLmmTestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 12, 1, 4),
    _TmnxOamPmCfgLossLmmTestId_Type()
)
tmnxOamPmCfgLossLmmTestId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmTestId.setStatus("current")


class _TmnxOamPmCfgLossLmmInterval_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossLmmInterval based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(1000, 1000),
        ValueRangeConstraint(10000, 10000),
    )


_TmnxOamPmCfgLossLmmInterval_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossLmmInterval_Object = MibTableColumn
tmnxOamPmCfgLossLmmInterval = _TmnxOamPmCfgLossLmmInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 12, 1, 5),
    _TmnxOamPmCfgLossLmmInterval_Type()
)
tmnxOamPmCfgLossLmmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmInterval.setUnits("milliseconds")


class _TmnxOamPmCfgLossLmmTestDuration_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossLmmTestDuration based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TmnxOamPmCfgLossLmmTestDuration_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossLmmTestDuration_Object = MibTableColumn
tmnxOamPmCfgLossLmmTestDuration = _TmnxOamPmCfgLossLmmTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 12, 1, 6),
    _TmnxOamPmCfgLossLmmTestDuration_Type()
)
tmnxOamPmCfgLossLmmTestDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmTestDuration.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmTestDuration.setUnits("seconds")


class _TmnxOamPmCfgLossLmmRunTimeLeft_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossLmmRunTimeLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TmnxOamPmCfgLossLmmRunTimeLeft_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossLmmRunTimeLeft_Object = MibTableColumn
tmnxOamPmCfgLossLmmRunTimeLeft = _TmnxOamPmCfgLossLmmRunTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 12, 1, 7),
    _TmnxOamPmCfgLossLmmRunTimeLeft_Type()
)
tmnxOamPmCfgLossLmmRunTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmRunTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmRunTimeLeft.setUnits("seconds")
_TmnxOamPmStatsObjs_ObjectIdentity = ObjectIdentity
tmnxOamPmStatsObjs = _TmnxOamPmStatsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2)
)
_TmnxOamPmStatsScalarObjs_ObjectIdentity = ObjectIdentity
tmnxOamPmStatsScalarObjs = _TmnxOamPmStatsScalarObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 1)
)
_TmnxOamPmStatsTableObjs_ObjectIdentity = ObjectIdentity
tmnxOamPmStatsTableObjs = _TmnxOamPmStatsTableObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2)
)
_TmnxOamPmStsBaseTable_Object = MibTable
tmnxOamPmStsBaseTable = _TmnxOamPmStsBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsBaseTable.setStatus("current")
_TmnxOamPmStsBaseEntry_Object = MibTableRow
tmnxOamPmStsBaseEntry = _TmnxOamPmStsBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 1, 1)
)
tmnxOamPmStsBaseEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsBaseTestType"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsMeasIntvlDuration"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsIntvlNum"),
)
if mibBuilder.loadTexts:
    tmnxOamPmStsBaseEntry.setStatus("current")
_TmnxOamPmStsBaseTestType_Type = TmnxOamPmTestType
_TmnxOamPmStsBaseTestType_Object = MibTableColumn
tmnxOamPmStsBaseTestType = _TmnxOamPmStsBaseTestType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 1, 1, 1),
    _TmnxOamPmStsBaseTestType_Type()
)
tmnxOamPmStsBaseTestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmStsBaseTestType.setStatus("current")
_TmnxOamPmStsMeasIntvlDuration_Type = TmnxOamPmMeasIntervalDuration
_TmnxOamPmStsMeasIntvlDuration_Object = MibTableColumn
tmnxOamPmStsMeasIntvlDuration = _TmnxOamPmStsMeasIntvlDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 1, 1, 2),
    _TmnxOamPmStsMeasIntvlDuration_Type()
)
tmnxOamPmStsMeasIntvlDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmStsMeasIntvlDuration.setStatus("current")
_TmnxOamPmStsIntvlNum_Type = TmnxOamPmStsIntvlNum
_TmnxOamPmStsIntvlNum_Object = MibTableColumn
tmnxOamPmStsIntvlNum = _TmnxOamPmStsIntvlNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 1, 1, 3),
    _TmnxOamPmStsIntvlNum_Type()
)
tmnxOamPmStsIntvlNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmStsIntvlNum.setStatus("current")


class _TmnxOamPmStsBaseOperStatus_Type(Integer32):
    """Custom type tmnxOamPmStsBaseOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 1),
          ("completed", 2))
    )


_TmnxOamPmStsBaseOperStatus_Type.__name__ = "Integer32"
_TmnxOamPmStsBaseOperStatus_Object = MibTableColumn
tmnxOamPmStsBaseOperStatus = _TmnxOamPmStsBaseOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 1, 1, 4),
    _TmnxOamPmStsBaseOperStatus_Type()
)
tmnxOamPmStsBaseOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsBaseOperStatus.setStatus("current")
_TmnxOamPmStsBaseSuspect_Type = TruthValue
_TmnxOamPmStsBaseSuspect_Object = MibTableColumn
tmnxOamPmStsBaseSuspect = _TmnxOamPmStsBaseSuspect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 1, 1, 5),
    _TmnxOamPmStsBaseSuspect_Type()
)
tmnxOamPmStsBaseSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsBaseSuspect.setStatus("current")


class _TmnxOamPmStsBaseStartTime_Type(DateAndTime):
    """Custom type tmnxOamPmStsBaseStartTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TmnxOamPmStsBaseStartTime_Type.__name__ = "DateAndTime"
_TmnxOamPmStsBaseStartTime_Object = MibTableColumn
tmnxOamPmStsBaseStartTime = _TmnxOamPmStsBaseStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 1, 1, 6),
    _TmnxOamPmStsBaseStartTime_Type()
)
tmnxOamPmStsBaseStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsBaseStartTime.setStatus("current")
_TmnxOamPmStsBaseElapsedTime_Type = Unsigned32
_TmnxOamPmStsBaseElapsedTime_Object = MibTableColumn
tmnxOamPmStsBaseElapsedTime = _TmnxOamPmStsBaseElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 1, 1, 7),
    _TmnxOamPmStsBaseElapsedTime_Type()
)
tmnxOamPmStsBaseElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsBaseElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsBaseElapsedTime.setUnits("seconds")
_TmnxOamPmStsBaseTestFramesTx_Type = Unsigned32
_TmnxOamPmStsBaseTestFramesTx_Object = MibTableColumn
tmnxOamPmStsBaseTestFramesTx = _TmnxOamPmStsBaseTestFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 1, 1, 8),
    _TmnxOamPmStsBaseTestFramesTx_Type()
)
tmnxOamPmStsBaseTestFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsBaseTestFramesTx.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsBaseTestFramesTx.setUnits("frames")
_TmnxOamPmStsBaseTestFramesRx_Type = Unsigned32
_TmnxOamPmStsBaseTestFramesRx_Object = MibTableColumn
tmnxOamPmStsBaseTestFramesRx = _TmnxOamPmStsBaseTestFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 1, 1, 9),
    _TmnxOamPmStsBaseTestFramesRx_Type()
)
tmnxOamPmStsBaseTestFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsBaseTestFramesRx.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsBaseTestFramesRx.setUnits("frames")
_TmnxOamPmStsMeasIntvlIndexTable_Object = MibTable
tmnxOamPmStsMeasIntvlIndexTable = _TmnxOamPmStsMeasIntvlIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsMeasIntvlIndexTable.setStatus("current")
_TmnxOamPmStsMeasIntvlIndexEntry_Object = MibTableRow
tmnxOamPmStsMeasIntvlIndexEntry = _TmnxOamPmStsMeasIntvlIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 2, 1)
)
tmnxOamPmStsMeasIntvlIndexEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsBaseTestType"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsMeasIntvlDuration"),
)
if mibBuilder.loadTexts:
    tmnxOamPmStsMeasIntvlIndexEntry.setStatus("current")
_TmnxOamPmStsMeasIntvlIndexNewest_Type = TmnxOamPmStsIntvlNum
_TmnxOamPmStsMeasIntvlIndexNewest_Object = MibTableColumn
tmnxOamPmStsMeasIntvlIndexNewest = _TmnxOamPmStsMeasIntvlIndexNewest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 2, 1, 1),
    _TmnxOamPmStsMeasIntvlIndexNewest_Type()
)
tmnxOamPmStsMeasIntvlIndexNewest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsMeasIntvlIndexNewest.setStatus("current")
_TmnxOamPmStsLossSlmTable_Object = MibTable
tmnxOamPmStsLossSlmTable = _TmnxOamPmStsLossSlmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmTable.setStatus("current")
_TmnxOamPmStsLossSlmEntry_Object = MibTableRow
tmnxOamPmStsLossSlmEntry = _TmnxOamPmStsLossSlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1)
)
tmnxOamPmStsLossSlmEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsMeasIntvlDuration"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsIntvlNum"),
)
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmEntry.setStatus("current")
_TmnxOamPmStsLossSlmTxFwd_Type = Unsigned32
_TmnxOamPmStsLossSlmTxFwd_Object = MibTableColumn
tmnxOamPmStsLossSlmTxFwd = _TmnxOamPmStsLossSlmTxFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 1),
    _TmnxOamPmStsLossSlmTxFwd_Type()
)
tmnxOamPmStsLossSlmTxFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmTxFwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmTxFwd.setUnits("SLM frames")
_TmnxOamPmStsLossSlmRxFwd_Type = Unsigned32
_TmnxOamPmStsLossSlmRxFwd_Object = MibTableColumn
tmnxOamPmStsLossSlmRxFwd = _TmnxOamPmStsLossSlmRxFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 2),
    _TmnxOamPmStsLossSlmRxFwd_Type()
)
tmnxOamPmStsLossSlmRxFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmRxFwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmRxFwd.setUnits("SLM frames")
_TmnxOamPmStsLossSlmTxBwd_Type = Unsigned32
_TmnxOamPmStsLossSlmTxBwd_Object = MibTableColumn
tmnxOamPmStsLossSlmTxBwd = _TmnxOamPmStsLossSlmTxBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 3),
    _TmnxOamPmStsLossSlmTxBwd_Type()
)
tmnxOamPmStsLossSlmTxBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmTxBwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmTxBwd.setUnits("SLR frames")
_TmnxOamPmStsLossSlmRxBwd_Type = Unsigned32
_TmnxOamPmStsLossSlmRxBwd_Object = MibTableColumn
tmnxOamPmStsLossSlmRxBwd = _TmnxOamPmStsLossSlmRxBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 4),
    _TmnxOamPmStsLossSlmRxBwd_Type()
)
tmnxOamPmStsLossSlmRxBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmRxBwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmRxBwd.setUnits("SLR frames")
_TmnxOamPmStsLossSlmAvailIndFwd_Type = Unsigned32
_TmnxOamPmStsLossSlmAvailIndFwd_Object = MibTableColumn
tmnxOamPmStsLossSlmAvailIndFwd = _TmnxOamPmStsLossSlmAvailIndFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 5),
    _TmnxOamPmStsLossSlmAvailIndFwd_Type()
)
tmnxOamPmStsLossSlmAvailIndFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmAvailIndFwd.setStatus("current")
_TmnxOamPmStsLossSlmAvailIndBwd_Type = Unsigned32
_TmnxOamPmStsLossSlmAvailIndBwd_Object = MibTableColumn
tmnxOamPmStsLossSlmAvailIndBwd = _TmnxOamPmStsLossSlmAvailIndBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 6),
    _TmnxOamPmStsLossSlmAvailIndBwd_Type()
)
tmnxOamPmStsLossSlmAvailIndBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmAvailIndBwd.setStatus("current")
_TmnxOamPmStsLossSlmUnavlIndFwd_Type = Unsigned32
_TmnxOamPmStsLossSlmUnavlIndFwd_Object = MibTableColumn
tmnxOamPmStsLossSlmUnavlIndFwd = _TmnxOamPmStsLossSlmUnavlIndFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 7),
    _TmnxOamPmStsLossSlmUnavlIndFwd_Type()
)
tmnxOamPmStsLossSlmUnavlIndFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmUnavlIndFwd.setStatus("current")
_TmnxOamPmStsLossSlmUnavlIndBwd_Type = Unsigned32
_TmnxOamPmStsLossSlmUnavlIndBwd_Object = MibTableColumn
tmnxOamPmStsLossSlmUnavlIndBwd = _TmnxOamPmStsLossSlmUnavlIndBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 8),
    _TmnxOamPmStsLossSlmUnavlIndBwd_Type()
)
tmnxOamPmStsLossSlmUnavlIndBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmUnavlIndBwd.setStatus("current")
_TmnxOamPmStsLossSlmUndtAvlFwd_Type = Unsigned32
_TmnxOamPmStsLossSlmUndtAvlFwd_Object = MibTableColumn
tmnxOamPmStsLossSlmUndtAvlFwd = _TmnxOamPmStsLossSlmUndtAvlFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 9),
    _TmnxOamPmStsLossSlmUndtAvlFwd_Type()
)
tmnxOamPmStsLossSlmUndtAvlFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmUndtAvlFwd.setStatus("current")
_TmnxOamPmStsLossSlmUndtUnavlFwd_Type = Unsigned32
_TmnxOamPmStsLossSlmUndtUnavlFwd_Object = MibTableColumn
tmnxOamPmStsLossSlmUndtUnavlFwd = _TmnxOamPmStsLossSlmUndtUnavlFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 10),
    _TmnxOamPmStsLossSlmUndtUnavlFwd_Type()
)
tmnxOamPmStsLossSlmUndtUnavlFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmUndtUnavlFwd.setStatus("current")
_TmnxOamPmStsLossSlmUndtAvlBwd_Type = Unsigned32
_TmnxOamPmStsLossSlmUndtAvlBwd_Object = MibTableColumn
tmnxOamPmStsLossSlmUndtAvlBwd = _TmnxOamPmStsLossSlmUndtAvlBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 11),
    _TmnxOamPmStsLossSlmUndtAvlBwd_Type()
)
tmnxOamPmStsLossSlmUndtAvlBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmUndtAvlBwd.setStatus("current")
_TmnxOamPmStsLossSlmUndtUnavlBwd_Type = Unsigned32
_TmnxOamPmStsLossSlmUndtUnavlBwd_Object = MibTableColumn
tmnxOamPmStsLossSlmUndtUnavlBwd = _TmnxOamPmStsLossSlmUndtUnavlBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 12),
    _TmnxOamPmStsLossSlmUndtUnavlBwd_Type()
)
tmnxOamPmStsLossSlmUndtUnavlBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmUndtUnavlBwd.setStatus("current")
_TmnxOamPmStsLossSlmHliFwd_Type = Unsigned32
_TmnxOamPmStsLossSlmHliFwd_Object = MibTableColumn
tmnxOamPmStsLossSlmHliFwd = _TmnxOamPmStsLossSlmHliFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 13),
    _TmnxOamPmStsLossSlmHliFwd_Type()
)
tmnxOamPmStsLossSlmHliFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmHliFwd.setStatus("current")
_TmnxOamPmStsLossSlmHliBwd_Type = Unsigned32
_TmnxOamPmStsLossSlmHliBwd_Object = MibTableColumn
tmnxOamPmStsLossSlmHliBwd = _TmnxOamPmStsLossSlmHliBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 14),
    _TmnxOamPmStsLossSlmHliBwd_Type()
)
tmnxOamPmStsLossSlmHliBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmHliBwd.setStatus("current")
_TmnxOamPmStsLossSlmChliFwd_Type = Unsigned32
_TmnxOamPmStsLossSlmChliFwd_Object = MibTableColumn
tmnxOamPmStsLossSlmChliFwd = _TmnxOamPmStsLossSlmChliFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 15),
    _TmnxOamPmStsLossSlmChliFwd_Type()
)
tmnxOamPmStsLossSlmChliFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmChliFwd.setStatus("current")
_TmnxOamPmStsLossSlmChliBwd_Type = Unsigned32
_TmnxOamPmStsLossSlmChliBwd_Object = MibTableColumn
tmnxOamPmStsLossSlmChliBwd = _TmnxOamPmStsLossSlmChliBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 16),
    _TmnxOamPmStsLossSlmChliBwd_Type()
)
tmnxOamPmStsLossSlmChliBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmChliBwd.setStatus("current")


class _TmnxOamPmStsLossSlmMinFlrFwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossSlmMinFlrFwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossSlmMinFlrFwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossSlmMinFlrFwd_Object = MibTableColumn
tmnxOamPmStsLossSlmMinFlrFwd = _TmnxOamPmStsLossSlmMinFlrFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 17),
    _TmnxOamPmStsLossSlmMinFlrFwd_Type()
)
tmnxOamPmStsLossSlmMinFlrFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmMinFlrFwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmMinFlrFwd.setUnits("milli-percent")


class _TmnxOamPmStsLossSlmMaxFlrFwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossSlmMaxFlrFwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossSlmMaxFlrFwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossSlmMaxFlrFwd_Object = MibTableColumn
tmnxOamPmStsLossSlmMaxFlrFwd = _TmnxOamPmStsLossSlmMaxFlrFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 18),
    _TmnxOamPmStsLossSlmMaxFlrFwd_Type()
)
tmnxOamPmStsLossSlmMaxFlrFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmMaxFlrFwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmMaxFlrFwd.setUnits("milli-percent")


class _TmnxOamPmStsLossSlmAvgFlrFwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossSlmAvgFlrFwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossSlmAvgFlrFwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossSlmAvgFlrFwd_Object = MibTableColumn
tmnxOamPmStsLossSlmAvgFlrFwd = _TmnxOamPmStsLossSlmAvgFlrFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 19),
    _TmnxOamPmStsLossSlmAvgFlrFwd_Type()
)
tmnxOamPmStsLossSlmAvgFlrFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmAvgFlrFwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmAvgFlrFwd.setUnits("milli-percent")


class _TmnxOamPmStsLossSlmMinFlrBwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossSlmMinFlrBwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossSlmMinFlrBwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossSlmMinFlrBwd_Object = MibTableColumn
tmnxOamPmStsLossSlmMinFlrBwd = _TmnxOamPmStsLossSlmMinFlrBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 20),
    _TmnxOamPmStsLossSlmMinFlrBwd_Type()
)
tmnxOamPmStsLossSlmMinFlrBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmMinFlrBwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmMinFlrBwd.setUnits("milli-percent")


class _TmnxOamPmStsLossSlmMaxFlrBwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossSlmMaxFlrBwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossSlmMaxFlrBwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossSlmMaxFlrBwd_Object = MibTableColumn
tmnxOamPmStsLossSlmMaxFlrBwd = _TmnxOamPmStsLossSlmMaxFlrBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 21),
    _TmnxOamPmStsLossSlmMaxFlrBwd_Type()
)
tmnxOamPmStsLossSlmMaxFlrBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmMaxFlrBwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmMaxFlrBwd.setUnits("milli-percent")


class _TmnxOamPmStsLossSlmAvgFlrBwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossSlmAvgFlrBwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossSlmAvgFlrBwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossSlmAvgFlrBwd_Object = MibTableColumn
tmnxOamPmStsLossSlmAvgFlrBwd = _TmnxOamPmStsLossSlmAvgFlrBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 22),
    _TmnxOamPmStsLossSlmAvgFlrBwd_Type()
)
tmnxOamPmStsLossSlmAvgFlrBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmAvgFlrBwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmAvgFlrBwd.setUnits("milli-percent")
_TmnxOamPmStsDelayDmmTable_Object = MibTable
tmnxOamPmStsDelayDmmTable = _TmnxOamPmStsDelayDmmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 4)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmTable.setStatus("current")
_TmnxOamPmStsDelayDmmEntry_Object = MibTableRow
tmnxOamPmStsDelayDmmEntry = _TmnxOamPmStsDelayDmmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 4, 1)
)
tmnxOamPmStsDelayDmmEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsMeasIntvlDuration"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsIntvlNum"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinType"),
)
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmEntry.setStatus("current")
_TmnxOamPmStsDelayDmmFwdMin_Type = Unsigned32
_TmnxOamPmStsDelayDmmFwdMin_Object = MibTableColumn
tmnxOamPmStsDelayDmmFwdMin = _TmnxOamPmStsDelayDmmFwdMin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 4, 1, 1),
    _TmnxOamPmStsDelayDmmFwdMin_Type()
)
tmnxOamPmStsDelayDmmFwdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmFwdMin.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmFwdMin.setUnits("microseconds")
_TmnxOamPmStsDelayDmmFwdMax_Type = Unsigned32
_TmnxOamPmStsDelayDmmFwdMax_Object = MibTableColumn
tmnxOamPmStsDelayDmmFwdMax = _TmnxOamPmStsDelayDmmFwdMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 4, 1, 2),
    _TmnxOamPmStsDelayDmmFwdMax_Type()
)
tmnxOamPmStsDelayDmmFwdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmFwdMax.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmFwdMax.setUnits("microseconds")
_TmnxOamPmStsDelayDmmFwdAvg_Type = Unsigned32
_TmnxOamPmStsDelayDmmFwdAvg_Object = MibTableColumn
tmnxOamPmStsDelayDmmFwdAvg = _TmnxOamPmStsDelayDmmFwdAvg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 4, 1, 3),
    _TmnxOamPmStsDelayDmmFwdAvg_Type()
)
tmnxOamPmStsDelayDmmFwdAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmFwdAvg.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmFwdAvg.setUnits("microseconds")
_TmnxOamPmStsDelayDmmBwdMin_Type = Unsigned32
_TmnxOamPmStsDelayDmmBwdMin_Object = MibTableColumn
tmnxOamPmStsDelayDmmBwdMin = _TmnxOamPmStsDelayDmmBwdMin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 4, 1, 4),
    _TmnxOamPmStsDelayDmmBwdMin_Type()
)
tmnxOamPmStsDelayDmmBwdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmBwdMin.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmBwdMin.setUnits("microseconds")
_TmnxOamPmStsDelayDmmBwdMax_Type = Unsigned32
_TmnxOamPmStsDelayDmmBwdMax_Object = MibTableColumn
tmnxOamPmStsDelayDmmBwdMax = _TmnxOamPmStsDelayDmmBwdMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 4, 1, 5),
    _TmnxOamPmStsDelayDmmBwdMax_Type()
)
tmnxOamPmStsDelayDmmBwdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmBwdMax.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmBwdMax.setUnits("microseconds")
_TmnxOamPmStsDelayDmmBwdAvg_Type = Unsigned32
_TmnxOamPmStsDelayDmmBwdAvg_Object = MibTableColumn
tmnxOamPmStsDelayDmmBwdAvg = _TmnxOamPmStsDelayDmmBwdAvg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 4, 1, 6),
    _TmnxOamPmStsDelayDmmBwdAvg_Type()
)
tmnxOamPmStsDelayDmmBwdAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmBwdAvg.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmBwdAvg.setUnits("microseconds")
_TmnxOamPmStsDelayDmm2wyMin_Type = Unsigned32
_TmnxOamPmStsDelayDmm2wyMin_Object = MibTableColumn
tmnxOamPmStsDelayDmm2wyMin = _TmnxOamPmStsDelayDmm2wyMin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 4, 1, 7),
    _TmnxOamPmStsDelayDmm2wyMin_Type()
)
tmnxOamPmStsDelayDmm2wyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmm2wyMin.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmm2wyMin.setUnits("microseconds")
_TmnxOamPmStsDelayDmm2wyMax_Type = Unsigned32
_TmnxOamPmStsDelayDmm2wyMax_Object = MibTableColumn
tmnxOamPmStsDelayDmm2wyMax = _TmnxOamPmStsDelayDmm2wyMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 4, 1, 8),
    _TmnxOamPmStsDelayDmm2wyMax_Type()
)
tmnxOamPmStsDelayDmm2wyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmm2wyMax.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmm2wyMax.setUnits("microseconds")
_TmnxOamPmStsDelayDmm2wyAvg_Type = Unsigned32
_TmnxOamPmStsDelayDmm2wyAvg_Object = MibTableColumn
tmnxOamPmStsDelayDmm2wyAvg = _TmnxOamPmStsDelayDmm2wyAvg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 4, 1, 9),
    _TmnxOamPmStsDelayDmm2wyAvg_Type()
)
tmnxOamPmStsDelayDmm2wyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmm2wyAvg.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmm2wyAvg.setUnits("microseconds")
_TmnxOamPmStsDelayDmmBinTable_Object = MibTable
tmnxOamPmStsDelayDmmBinTable = _TmnxOamPmStsDelayDmmBinTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 5)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmBinTable.setStatus("current")
_TmnxOamPmStsDelayDmmBinEntry_Object = MibTableRow
tmnxOamPmStsDelayDmmBinEntry = _TmnxOamPmStsDelayDmmBinEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 5, 1)
)
tmnxOamPmStsDelayDmmBinEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsMeasIntvlDuration"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsIntvlNum"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinType"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayDmmBinNum"),
)
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmBinEntry.setStatus("current")


class _TmnxOamPmStsDelayDmmBinNum_Type(Unsigned32):
    """Custom type tmnxOamPmStsDelayDmmBinNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_TmnxOamPmStsDelayDmmBinNum_Type.__name__ = "Unsigned32"
_TmnxOamPmStsDelayDmmBinNum_Object = MibTableColumn
tmnxOamPmStsDelayDmmBinNum = _TmnxOamPmStsDelayDmmBinNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 5, 1, 1),
    _TmnxOamPmStsDelayDmmBinNum_Type()
)
tmnxOamPmStsDelayDmmBinNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmBinNum.setStatus("current")
_TmnxOamPmStsDelayDmmBinFwdCount_Type = Unsigned32
_TmnxOamPmStsDelayDmmBinFwdCount_Object = MibTableColumn
tmnxOamPmStsDelayDmmBinFwdCount = _TmnxOamPmStsDelayDmmBinFwdCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 5, 1, 2),
    _TmnxOamPmStsDelayDmmBinFwdCount_Type()
)
tmnxOamPmStsDelayDmmBinFwdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmBinFwdCount.setStatus("current")
_TmnxOamPmStsDelayDmmBinBwdCount_Type = Unsigned32
_TmnxOamPmStsDelayDmmBinBwdCount_Object = MibTableColumn
tmnxOamPmStsDelayDmmBinBwdCount = _TmnxOamPmStsDelayDmmBinBwdCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 5, 1, 3),
    _TmnxOamPmStsDelayDmmBinBwdCount_Type()
)
tmnxOamPmStsDelayDmmBinBwdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmBinBwdCount.setStatus("current")
_TmnxOamPmStsDelayDmmBin2wyCount_Type = Unsigned32
_TmnxOamPmStsDelayDmmBin2wyCount_Object = MibTableColumn
tmnxOamPmStsDelayDmmBin2wyCount = _TmnxOamPmStsDelayDmmBin2wyCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 5, 1, 4),
    _TmnxOamPmStsDelayDmmBin2wyCount_Type()
)
tmnxOamPmStsDelayDmmBin2wyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmBin2wyCount.setStatus("current")
_TmnxOamPmStsTwlRflTable_Object = MibTable
tmnxOamPmStsTwlRflTable = _TmnxOamPmStsTwlRflTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 6)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsTwlRflTable.setStatus("current")
_TmnxOamPmStsTwlRflEntry_Object = MibTableRow
tmnxOamPmStsTwlRflEntry = _TmnxOamPmStsTwlRflEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 6, 1)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsTwlRflEntry.setStatus("current")
_TmnxOamPmStsTwlRflUpTime_Type = Unsigned32
_TmnxOamPmStsTwlRflUpTime_Object = MibTableColumn
tmnxOamPmStsTwlRflUpTime = _TmnxOamPmStsTwlRflUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 6, 1, 1),
    _TmnxOamPmStsTwlRflUpTime_Type()
)
tmnxOamPmStsTwlRflUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsTwlRflUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsTwlRflUpTime.setUnits("seconds")
_TmnxOamPmStsTwlRflFramesRx_Type = Unsigned32
_TmnxOamPmStsTwlRflFramesRx_Object = MibTableColumn
tmnxOamPmStsTwlRflFramesRx = _TmnxOamPmStsTwlRflFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 6, 1, 2),
    _TmnxOamPmStsTwlRflFramesRx_Type()
)
tmnxOamPmStsTwlRflFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsTwlRflFramesRx.setStatus("current")
_TmnxOamPmStsTwlRflFramesTx_Type = Unsigned32
_TmnxOamPmStsTwlRflFramesTx_Object = MibTableColumn
tmnxOamPmStsTwlRflFramesTx = _TmnxOamPmStsTwlRflFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 6, 1, 3),
    _TmnxOamPmStsTwlRflFramesTx_Type()
)
tmnxOamPmStsTwlRflFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsTwlRflFramesTx.setStatus("current")
_TmnxOamPmStsDelayTwlTable_Object = MibTable
tmnxOamPmStsDelayTwlTable = _TmnxOamPmStsDelayTwlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 7)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlTable.setStatus("current")
_TmnxOamPmStsDelayTwlEntry_Object = MibTableRow
tmnxOamPmStsDelayTwlEntry = _TmnxOamPmStsDelayTwlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 7, 1)
)
tmnxOamPmStsDelayTwlEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsMeasIntvlDuration"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsIntvlNum"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinType"),
)
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlEntry.setStatus("current")
_TmnxOamPmStsDelayTwlFwdMin_Type = Unsigned32
_TmnxOamPmStsDelayTwlFwdMin_Object = MibTableColumn
tmnxOamPmStsDelayTwlFwdMin = _TmnxOamPmStsDelayTwlFwdMin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 7, 1, 1),
    _TmnxOamPmStsDelayTwlFwdMin_Type()
)
tmnxOamPmStsDelayTwlFwdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlFwdMin.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlFwdMin.setUnits("microseconds")
_TmnxOamPmStsDelayTwlFwdMax_Type = Unsigned32
_TmnxOamPmStsDelayTwlFwdMax_Object = MibTableColumn
tmnxOamPmStsDelayTwlFwdMax = _TmnxOamPmStsDelayTwlFwdMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 7, 1, 2),
    _TmnxOamPmStsDelayTwlFwdMax_Type()
)
tmnxOamPmStsDelayTwlFwdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlFwdMax.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlFwdMax.setUnits("microseconds")
_TmnxOamPmStsDelayTwlFwdAvg_Type = Unsigned32
_TmnxOamPmStsDelayTwlFwdAvg_Object = MibTableColumn
tmnxOamPmStsDelayTwlFwdAvg = _TmnxOamPmStsDelayTwlFwdAvg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 7, 1, 3),
    _TmnxOamPmStsDelayTwlFwdAvg_Type()
)
tmnxOamPmStsDelayTwlFwdAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlFwdAvg.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlFwdAvg.setUnits("microseconds")
_TmnxOamPmStsDelayTwlBwdMin_Type = Unsigned32
_TmnxOamPmStsDelayTwlBwdMin_Object = MibTableColumn
tmnxOamPmStsDelayTwlBwdMin = _TmnxOamPmStsDelayTwlBwdMin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 7, 1, 4),
    _TmnxOamPmStsDelayTwlBwdMin_Type()
)
tmnxOamPmStsDelayTwlBwdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlBwdMin.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlBwdMin.setUnits("microseconds")
_TmnxOamPmStsDelayTwlBwdMax_Type = Unsigned32
_TmnxOamPmStsDelayTwlBwdMax_Object = MibTableColumn
tmnxOamPmStsDelayTwlBwdMax = _TmnxOamPmStsDelayTwlBwdMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 7, 1, 5),
    _TmnxOamPmStsDelayTwlBwdMax_Type()
)
tmnxOamPmStsDelayTwlBwdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlBwdMax.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlBwdMax.setUnits("microseconds")
_TmnxOamPmStsDelayTwlBwdAvg_Type = Unsigned32
_TmnxOamPmStsDelayTwlBwdAvg_Object = MibTableColumn
tmnxOamPmStsDelayTwlBwdAvg = _TmnxOamPmStsDelayTwlBwdAvg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 7, 1, 6),
    _TmnxOamPmStsDelayTwlBwdAvg_Type()
)
tmnxOamPmStsDelayTwlBwdAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlBwdAvg.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlBwdAvg.setUnits("microseconds")
_TmnxOamPmStsDelayTwl2wyMin_Type = Unsigned32
_TmnxOamPmStsDelayTwl2wyMin_Object = MibTableColumn
tmnxOamPmStsDelayTwl2wyMin = _TmnxOamPmStsDelayTwl2wyMin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 7, 1, 7),
    _TmnxOamPmStsDelayTwl2wyMin_Type()
)
tmnxOamPmStsDelayTwl2wyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwl2wyMin.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwl2wyMin.setUnits("microseconds")
_TmnxOamPmStsDelayTwl2wyMax_Type = Unsigned32
_TmnxOamPmStsDelayTwl2wyMax_Object = MibTableColumn
tmnxOamPmStsDelayTwl2wyMax = _TmnxOamPmStsDelayTwl2wyMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 7, 1, 8),
    _TmnxOamPmStsDelayTwl2wyMax_Type()
)
tmnxOamPmStsDelayTwl2wyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwl2wyMax.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwl2wyMax.setUnits("microseconds")
_TmnxOamPmStsDelayTwl2wyAvg_Type = Unsigned32
_TmnxOamPmStsDelayTwl2wyAvg_Object = MibTableColumn
tmnxOamPmStsDelayTwl2wyAvg = _TmnxOamPmStsDelayTwl2wyAvg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 7, 1, 9),
    _TmnxOamPmStsDelayTwl2wyAvg_Type()
)
tmnxOamPmStsDelayTwl2wyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwl2wyAvg.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwl2wyAvg.setUnits("microseconds")
_TmnxOamPmStsDelayTwlBinTable_Object = MibTable
tmnxOamPmStsDelayTwlBinTable = _TmnxOamPmStsDelayTwlBinTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 8)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlBinTable.setStatus("current")
_TmnxOamPmStsDelayTwlBinEntry_Object = MibTableRow
tmnxOamPmStsDelayTwlBinEntry = _TmnxOamPmStsDelayTwlBinEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 8, 1)
)
tmnxOamPmStsDelayTwlBinEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsMeasIntvlDuration"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsIntvlNum"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinType"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayTwlBinNum"),
)
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlBinEntry.setStatus("current")


class _TmnxOamPmStsDelayTwlBinNum_Type(Unsigned32):
    """Custom type tmnxOamPmStsDelayTwlBinNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_TmnxOamPmStsDelayTwlBinNum_Type.__name__ = "Unsigned32"
_TmnxOamPmStsDelayTwlBinNum_Object = MibTableColumn
tmnxOamPmStsDelayTwlBinNum = _TmnxOamPmStsDelayTwlBinNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 8, 1, 1),
    _TmnxOamPmStsDelayTwlBinNum_Type()
)
tmnxOamPmStsDelayTwlBinNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlBinNum.setStatus("current")
_TmnxOamPmStsDelayTwlBinFwdCount_Type = Unsigned32
_TmnxOamPmStsDelayTwlBinFwdCount_Object = MibTableColumn
tmnxOamPmStsDelayTwlBinFwdCount = _TmnxOamPmStsDelayTwlBinFwdCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 8, 1, 2),
    _TmnxOamPmStsDelayTwlBinFwdCount_Type()
)
tmnxOamPmStsDelayTwlBinFwdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlBinFwdCount.setStatus("current")
_TmnxOamPmStsDelayTwlBinBwdCount_Type = Unsigned32
_TmnxOamPmStsDelayTwlBinBwdCount_Object = MibTableColumn
tmnxOamPmStsDelayTwlBinBwdCount = _TmnxOamPmStsDelayTwlBinBwdCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 8, 1, 3),
    _TmnxOamPmStsDelayTwlBinBwdCount_Type()
)
tmnxOamPmStsDelayTwlBinBwdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlBinBwdCount.setStatus("current")
_TmnxOamPmStsDelayTwlBin2wyCount_Type = Unsigned32
_TmnxOamPmStsDelayTwlBin2wyCount_Object = MibTableColumn
tmnxOamPmStsDelayTwlBin2wyCount = _TmnxOamPmStsDelayTwlBin2wyCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 8, 1, 4),
    _TmnxOamPmStsDelayTwlBin2wyCount_Type()
)
tmnxOamPmStsDelayTwlBin2wyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlBin2wyCount.setStatus("current")
_TmnxOamPmStsLossLmmTable_Object = MibTable
tmnxOamPmStsLossLmmTable = _TmnxOamPmStsLossLmmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmTable.setStatus("current")
_TmnxOamPmStsLossLmmEntry_Object = MibTableRow
tmnxOamPmStsLossLmmEntry = _TmnxOamPmStsLossLmmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1)
)
tmnxOamPmStsLossLmmEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsMeasIntvlDuration"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsIntvlNum"),
)
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmEntry.setStatus("current")
_TmnxOamPmStsLossLmmTxFwd_Type = Counter64
_TmnxOamPmStsLossLmmTxFwd_Object = MibTableColumn
tmnxOamPmStsLossLmmTxFwd = _TmnxOamPmStsLossLmmTxFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 1),
    _TmnxOamPmStsLossLmmTxFwd_Type()
)
tmnxOamPmStsLossLmmTxFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmTxFwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmTxFwd.setUnits("frames")
_TmnxOamPmStsLossLmmRxFwd_Type = Counter64
_TmnxOamPmStsLossLmmRxFwd_Object = MibTableColumn
tmnxOamPmStsLossLmmRxFwd = _TmnxOamPmStsLossLmmRxFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 2),
    _TmnxOamPmStsLossLmmRxFwd_Type()
)
tmnxOamPmStsLossLmmRxFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmRxFwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmRxFwd.setUnits("frames")
_TmnxOamPmStsLossLmmTxBwd_Type = Counter64
_TmnxOamPmStsLossLmmTxBwd_Object = MibTableColumn
tmnxOamPmStsLossLmmTxBwd = _TmnxOamPmStsLossLmmTxBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 3),
    _TmnxOamPmStsLossLmmTxBwd_Type()
)
tmnxOamPmStsLossLmmTxBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmTxBwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmTxBwd.setUnits("frames")
_TmnxOamPmStsLossLmmRxBwd_Type = Counter64
_TmnxOamPmStsLossLmmRxBwd_Object = MibTableColumn
tmnxOamPmStsLossLmmRxBwd = _TmnxOamPmStsLossLmmRxBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 4),
    _TmnxOamPmStsLossLmmRxBwd_Type()
)
tmnxOamPmStsLossLmmRxBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmRxBwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmRxBwd.setUnits("frames")


class _TmnxOamPmStsLossLmmMinFlrFwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossLmmMinFlrFwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossLmmMinFlrFwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossLmmMinFlrFwd_Object = MibTableColumn
tmnxOamPmStsLossLmmMinFlrFwd = _TmnxOamPmStsLossLmmMinFlrFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 5),
    _TmnxOamPmStsLossLmmMinFlrFwd_Type()
)
tmnxOamPmStsLossLmmMinFlrFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmMinFlrFwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmMinFlrFwd.setUnits("milli-percent")


class _TmnxOamPmStsLossLmmMaxFlrFwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossLmmMaxFlrFwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossLmmMaxFlrFwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossLmmMaxFlrFwd_Object = MibTableColumn
tmnxOamPmStsLossLmmMaxFlrFwd = _TmnxOamPmStsLossLmmMaxFlrFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 6),
    _TmnxOamPmStsLossLmmMaxFlrFwd_Type()
)
tmnxOamPmStsLossLmmMaxFlrFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmMaxFlrFwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmMaxFlrFwd.setUnits("milli-percent")


class _TmnxOamPmStsLossLmmAvgFlrFwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossLmmAvgFlrFwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossLmmAvgFlrFwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossLmmAvgFlrFwd_Object = MibTableColumn
tmnxOamPmStsLossLmmAvgFlrFwd = _TmnxOamPmStsLossLmmAvgFlrFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 7),
    _TmnxOamPmStsLossLmmAvgFlrFwd_Type()
)
tmnxOamPmStsLossLmmAvgFlrFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmAvgFlrFwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmAvgFlrFwd.setUnits("milli-percent")


class _TmnxOamPmStsLossLmmMinFlrBwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossLmmMinFlrBwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossLmmMinFlrBwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossLmmMinFlrBwd_Object = MibTableColumn
tmnxOamPmStsLossLmmMinFlrBwd = _TmnxOamPmStsLossLmmMinFlrBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 8),
    _TmnxOamPmStsLossLmmMinFlrBwd_Type()
)
tmnxOamPmStsLossLmmMinFlrBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmMinFlrBwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmMinFlrBwd.setUnits("milli-percent")


class _TmnxOamPmStsLossLmmMaxFlrBwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossLmmMaxFlrBwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossLmmMaxFlrBwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossLmmMaxFlrBwd_Object = MibTableColumn
tmnxOamPmStsLossLmmMaxFlrBwd = _TmnxOamPmStsLossLmmMaxFlrBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 9),
    _TmnxOamPmStsLossLmmMaxFlrBwd_Type()
)
tmnxOamPmStsLossLmmMaxFlrBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmMaxFlrBwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmMaxFlrBwd.setUnits("milli-percent")


class _TmnxOamPmStsLossLmmAvgFlrBwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossLmmAvgFlrBwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossLmmAvgFlrBwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossLmmAvgFlrBwd_Object = MibTableColumn
tmnxOamPmStsLossLmmAvgFlrBwd = _TmnxOamPmStsLossLmmAvgFlrBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 10),
    _TmnxOamPmStsLossLmmAvgFlrBwd_Type()
)
tmnxOamPmStsLossLmmAvgFlrBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmAvgFlrBwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmAvgFlrBwd.setUnits("milli-percent")
_TmnxOamPmNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxOamPmNotificationObjs = _TmnxOamPmNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 3)
)
_TmnxOamPmNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxOamPmNotifyPrefix = _TmnxOamPmNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 92)
)
_TmnxOamPmNotifications_ObjectIdentity = ObjectIdentity
tmnxOamPmNotifications = _TmnxOamPmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 92, 0)
)
tmnxOamPmCfgTwlRflEntry.registerAugmentions(
    ("TIMETRA-OAM-PM-MIB",
     "tmnxOamPmStsTwlRflEntry")
)
tmnxOamPmStsTwlRflEntry.setIndexNames(*tmnxOamPmCfgTwlRflEntry.getIndexNames())

# Managed Objects groups

tmnxOamPmV12v0ObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 2, 1, 1)
)
tmnxOamPmV12v0ObjGroup.setObjects(
      *(("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinGroupAdminStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinGroupDescription"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinGroupFdBinCount"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinGroupFdrBinCount"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinGroupIfdvBinCount"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinGroupRowStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinGroupTableLastChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinLowerBound"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinTableLastChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayDmmAdminStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayDmmDataTlvSize"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayDmmInterval"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayDmmOnDmndStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayDmmRowStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayDmmRunTimeLeft"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayDmmTableLastChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayDmmTestDuration"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayDmmTestId"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossSlmAdminStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossSlmChliThreshold"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossSlmConsecDeltaTs"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossSlmDataTlvSize"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossSlmFlrThreshold"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossSlmInterval"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossSlmOnDmndStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossSlmRowStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossSlmRunTimeLeft"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossSlmTableLastChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossSlmTestDuration"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossSlmTestId"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossSlmTxFrmsPerDelT"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgMeasIntvlAccntPolicy"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgMeasIntvlBoundaryTyp"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgMeasIntvlClockOffset"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgMeasIntvlRowStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgMeasIntvlTableLstChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgMeasIntvlsStored"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessBinGroupId"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessDescription"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessEthDestMacAddr"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessEthPriority"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessEthSrcMaIndex"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessEthSrcMdIndex"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessEthSrcMepId"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessEthTableLastChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessRowStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessTableLastChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessTestFamily"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessType"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsBaseElapsedTime"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsBaseOperStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsBaseStartTime"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsBaseSuspect"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsBaseTestFramesRx"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsBaseTestFramesTx"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayDmm2wyAvg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayDmm2wyMax"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayDmm2wyMin"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayDmmBin2wyCount"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayDmmBinBwdCount"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayDmmBinFwdCount"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayDmmBwdAvg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayDmmBwdMax"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayDmmBwdMin"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayDmmFwdAvg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayDmmFwdMax"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayDmmFwdMin"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmAvailIndBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmAvailIndFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmAvgFlrBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmAvgFlrFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmChliBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmChliFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmHliBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmHliFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmMaxFlrBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmMaxFlrFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmMinFlrBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmMinFlrFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmRxBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmRxFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmTxBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmTxFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmUnavlIndBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmUnavlIndFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmUndtAvlBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmUndtAvlFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmUndtUnavlBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmUndtUnavlFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsMeasIntvlIndexNewest"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpBypassRouting"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpDstAddress"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpDstAddressType"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpDstUdpPort"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpEgressIfName"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpForwardClass"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpNhAddress"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpNhAddressType"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpProfile"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpServiceId"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpSrcAddress"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpSrcAddressType"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpTableLastChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpTtl"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwampLtAdminStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwampLtInterval"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwampLtOnDmndStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwampLtPadSize"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwampLtRowStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwampLtRunTimeLeft"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwampLtTableLastChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwampLtTestDuration"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwampLtTestId"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwlRflAdminStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwlRflDescription"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwlRflInactTimer"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwlRflListenUdpPort"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwlRflPfxDescription"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwlRflPfxRowStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwlRflPfxTableLstChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwlRflRowStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwlRflTableLastChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayTwl2wyAvg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayTwl2wyMax"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayTwl2wyMin"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayTwlBin2wyCount"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayTwlBinBwdCount"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayTwlBinFwdCount"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayTwlBwdAvg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayTwlBwdMax"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayTwlBwdMin"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayTwlFwdAvg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayTwlFwdMax"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayTwlFwdMin"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsTwlRflFramesRx"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsTwlRflFramesTx"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsTwlRflUpTime"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossLmmAdminStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossLmmInterval"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossLmmOnDmndStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossLmmRowStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossLmmRunTimeLeft"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossLmmTableLastChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossLmmTestDuration"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossLmmTestId"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmAvgFlrBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmAvgFlrFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmMaxFlrBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmMaxFlrFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmMinFlrBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmMinFlrFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmRxBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmRxFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmTxBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmTxFwd"))
)
if mibBuilder.loadTexts:
    tmnxOamPmV12v0ObjGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tmnxOamPmV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 1, 1)
)
tmnxOamPmV12v0Compliance.setObjects(
    ("TIMETRA-OAM-PM-MIB", "tmnxOamPmV12v0ObjGroup")
)
if mibBuilder.loadTexts:
    tmnxOamPmV12v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-OAM-PM-MIB",
    **{"TmnxOamPmBinGroupId": TmnxOamPmBinGroupId,
       "TmnxOamPmBinType": TmnxOamPmBinType,
       "TmnxOamPmMeasIntervalDuration": TmnxOamPmMeasIntervalDuration,
       "TmnxOamPmCfgMeasIntervalDuration": TmnxOamPmCfgMeasIntervalDuration,
       "TmnxOamPmSessionType": TmnxOamPmSessionType,
       "TmnxOamPmStsIntvlNum": TmnxOamPmStsIntvlNum,
       "TmnxOamPmTestFamily": TmnxOamPmTestFamily,
       "TmnxOamPmTestType": TmnxOamPmTestType,
       "timetraOamPmMIBModule": timetraOamPmMIBModule,
       "tmnxOamPmConformance": tmnxOamPmConformance,
       "tmnxOamPmCompliances": tmnxOamPmCompliances,
       "tmnxOamPmV12v0Compliance": tmnxOamPmV12v0Compliance,
       "tmnxOamPmObjGroups": tmnxOamPmObjGroups,
       "tmnxOamPmV12v0ObjGroups": tmnxOamPmV12v0ObjGroups,
       "tmnxOamPmV12v0ObjGroup": tmnxOamPmV12v0ObjGroup,
       "tmnxOamPmNotifGroups": tmnxOamPmNotifGroups,
       "tmnxOamPmV12v0NotifGroups": tmnxOamPmV12v0NotifGroups,
       "tmnxOamPmObjs": tmnxOamPmObjs,
       "tmnxOamPmCfgObjs": tmnxOamPmCfgObjs,
       "tmnxOamPmCfgScalarObjs": tmnxOamPmCfgScalarObjs,
       "tmnxOamPmCfgTwlRflInactTimer": tmnxOamPmCfgTwlRflInactTimer,
       "tmnxOamPmTableLastChgObjs": tmnxOamPmTableLastChgObjs,
       "tmnxOamPmCfgBinGroupTableLastChg": tmnxOamPmCfgBinGroupTableLastChg,
       "tmnxOamPmCfgBinTableLastChg": tmnxOamPmCfgBinTableLastChg,
       "tmnxOamPmCfgSessTableLastChg": tmnxOamPmCfgSessTableLastChg,
       "tmnxOamPmCfgSessEthTableLastChg": tmnxOamPmCfgSessEthTableLastChg,
       "tmnxOamPmCfgDelayDmmTableLastChg": tmnxOamPmCfgDelayDmmTableLastChg,
       "tmnxOamPmCfgLossSlmTableLastChg": tmnxOamPmCfgLossSlmTableLastChg,
       "tmnxOamPmCfgMeasIntvlTableLstChg": tmnxOamPmCfgMeasIntvlTableLstChg,
       "tmnxOamPmCfgSessIpTableLastChg": tmnxOamPmCfgSessIpTableLastChg,
       "tmnxOamPmCfgTwampLtTableLastChg": tmnxOamPmCfgTwampLtTableLastChg,
       "tmnxOamPmCfgTwlRflTableLastChg": tmnxOamPmCfgTwlRflTableLastChg,
       "tmnxOamPmCfgTwlRflPfxTableLstChg": tmnxOamPmCfgTwlRflPfxTableLstChg,
       "tmnxOamPmCfgLossLmmTableLastChg": tmnxOamPmCfgLossLmmTableLastChg,
       "tmnxOamPmCfgTableObjs": tmnxOamPmCfgTableObjs,
       "tmnxOamPmCfgBinGroupTable": tmnxOamPmCfgBinGroupTable,
       "tmnxOamPmCfgBinGroupEntry": tmnxOamPmCfgBinGroupEntry,
       "tmnxOamPmCfgBinGroupId": tmnxOamPmCfgBinGroupId,
       "tmnxOamPmCfgBinGroupRowStatus": tmnxOamPmCfgBinGroupRowStatus,
       "tmnxOamPmCfgBinGroupAdminStatus": tmnxOamPmCfgBinGroupAdminStatus,
       "tmnxOamPmCfgBinGroupDescription": tmnxOamPmCfgBinGroupDescription,
       "tmnxOamPmCfgBinGroupFdBinCount": tmnxOamPmCfgBinGroupFdBinCount,
       "tmnxOamPmCfgBinGroupFdrBinCount": tmnxOamPmCfgBinGroupFdrBinCount,
       "tmnxOamPmCfgBinGroupIfdvBinCount": tmnxOamPmCfgBinGroupIfdvBinCount,
       "tmnxOamPmCfgBinTable": tmnxOamPmCfgBinTable,
       "tmnxOamPmCfgBinEntry": tmnxOamPmCfgBinEntry,
       "tmnxOamPmCfgBinType": tmnxOamPmCfgBinType,
       "tmnxOamPmCfgBinNum": tmnxOamPmCfgBinNum,
       "tmnxOamPmCfgBinLowerBound": tmnxOamPmCfgBinLowerBound,
       "tmnxOamPmCfgSessTable": tmnxOamPmCfgSessTable,
       "tmnxOamPmCfgSessEntry": tmnxOamPmCfgSessEntry,
       "tmnxOamPmCfgSessName": tmnxOamPmCfgSessName,
       "tmnxOamPmCfgSessRowStatus": tmnxOamPmCfgSessRowStatus,
       "tmnxOamPmCfgSessTestFamily": tmnxOamPmCfgSessTestFamily,
       "tmnxOamPmCfgSessType": tmnxOamPmCfgSessType,
       "tmnxOamPmCfgSessBinGroupId": tmnxOamPmCfgSessBinGroupId,
       "tmnxOamPmCfgSessDescription": tmnxOamPmCfgSessDescription,
       "tmnxOamPmCfgSessEthTable": tmnxOamPmCfgSessEthTable,
       "tmnxOamPmCfgSessEthEntry": tmnxOamPmCfgSessEthEntry,
       "tmnxOamPmCfgSessEthSrcMepId": tmnxOamPmCfgSessEthSrcMepId,
       "tmnxOamPmCfgSessEthSrcMdIndex": tmnxOamPmCfgSessEthSrcMdIndex,
       "tmnxOamPmCfgSessEthSrcMaIndex": tmnxOamPmCfgSessEthSrcMaIndex,
       "tmnxOamPmCfgSessEthPriority": tmnxOamPmCfgSessEthPriority,
       "tmnxOamPmCfgSessEthDestMacAddr": tmnxOamPmCfgSessEthDestMacAddr,
       "tmnxOamPmCfgDelayDmmTable": tmnxOamPmCfgDelayDmmTable,
       "tmnxOamPmCfgDelayDmmEntry": tmnxOamPmCfgDelayDmmEntry,
       "tmnxOamPmCfgDelayDmmRowStatus": tmnxOamPmCfgDelayDmmRowStatus,
       "tmnxOamPmCfgDelayDmmAdminStatus": tmnxOamPmCfgDelayDmmAdminStatus,
       "tmnxOamPmCfgDelayDmmOnDmndStatus": tmnxOamPmCfgDelayDmmOnDmndStatus,
       "tmnxOamPmCfgDelayDmmTestId": tmnxOamPmCfgDelayDmmTestId,
       "tmnxOamPmCfgDelayDmmInterval": tmnxOamPmCfgDelayDmmInterval,
       "tmnxOamPmCfgDelayDmmDataTlvSize": tmnxOamPmCfgDelayDmmDataTlvSize,
       "tmnxOamPmCfgDelayDmmTestDuration": tmnxOamPmCfgDelayDmmTestDuration,
       "tmnxOamPmCfgDelayDmmRunTimeLeft": tmnxOamPmCfgDelayDmmRunTimeLeft,
       "tmnxOamPmCfgLossSlmTable": tmnxOamPmCfgLossSlmTable,
       "tmnxOamPmCfgLossSlmEntry": tmnxOamPmCfgLossSlmEntry,
       "tmnxOamPmCfgLossSlmRowStatus": tmnxOamPmCfgLossSlmRowStatus,
       "tmnxOamPmCfgLossSlmAdminStatus": tmnxOamPmCfgLossSlmAdminStatus,
       "tmnxOamPmCfgLossSlmOnDmndStatus": tmnxOamPmCfgLossSlmOnDmndStatus,
       "tmnxOamPmCfgLossSlmTestId": tmnxOamPmCfgLossSlmTestId,
       "tmnxOamPmCfgLossSlmInterval": tmnxOamPmCfgLossSlmInterval,
       "tmnxOamPmCfgLossSlmDataTlvSize": tmnxOamPmCfgLossSlmDataTlvSize,
       "tmnxOamPmCfgLossSlmTxFrmsPerDelT": tmnxOamPmCfgLossSlmTxFrmsPerDelT,
       "tmnxOamPmCfgLossSlmConsecDeltaTs": tmnxOamPmCfgLossSlmConsecDeltaTs,
       "tmnxOamPmCfgLossSlmChliThreshold": tmnxOamPmCfgLossSlmChliThreshold,
       "tmnxOamPmCfgLossSlmFlrThreshold": tmnxOamPmCfgLossSlmFlrThreshold,
       "tmnxOamPmCfgLossSlmTestDuration": tmnxOamPmCfgLossSlmTestDuration,
       "tmnxOamPmCfgLossSlmRunTimeLeft": tmnxOamPmCfgLossSlmRunTimeLeft,
       "tmnxOamPmCfgMeasIntvlTable": tmnxOamPmCfgMeasIntvlTable,
       "tmnxOamPmCfgMeasIntvlEntry": tmnxOamPmCfgMeasIntvlEntry,
       "tmnxOamPmCfgMeasIntvlDuration": tmnxOamPmCfgMeasIntvlDuration,
       "tmnxOamPmCfgMeasIntvlRowStatus": tmnxOamPmCfgMeasIntvlRowStatus,
       "tmnxOamPmCfgMeasIntvlAccntPolicy": tmnxOamPmCfgMeasIntvlAccntPolicy,
       "tmnxOamPmCfgMeasIntvlsStored": tmnxOamPmCfgMeasIntvlsStored,
       "tmnxOamPmCfgMeasIntvlBoundaryTyp": tmnxOamPmCfgMeasIntvlBoundaryTyp,
       "tmnxOamPmCfgMeasIntvlClockOffset": tmnxOamPmCfgMeasIntvlClockOffset,
       "tmnxOamPmCfgSessIpTable": tmnxOamPmCfgSessIpTable,
       "tmnxOamPmCfgSessIpEntry": tmnxOamPmCfgSessIpEntry,
       "tmnxOamPmCfgSessIpServiceId": tmnxOamPmCfgSessIpServiceId,
       "tmnxOamPmCfgSessIpSrcAddressType": tmnxOamPmCfgSessIpSrcAddressType,
       "tmnxOamPmCfgSessIpSrcAddress": tmnxOamPmCfgSessIpSrcAddress,
       "tmnxOamPmCfgSessIpDstAddressType": tmnxOamPmCfgSessIpDstAddressType,
       "tmnxOamPmCfgSessIpDstAddress": tmnxOamPmCfgSessIpDstAddress,
       "tmnxOamPmCfgSessIpDstUdpPort": tmnxOamPmCfgSessIpDstUdpPort,
       "tmnxOamPmCfgSessIpBypassRouting": tmnxOamPmCfgSessIpBypassRouting,
       "tmnxOamPmCfgSessIpEgressIfName": tmnxOamPmCfgSessIpEgressIfName,
       "tmnxOamPmCfgSessIpNhAddressType": tmnxOamPmCfgSessIpNhAddressType,
       "tmnxOamPmCfgSessIpNhAddress": tmnxOamPmCfgSessIpNhAddress,
       "tmnxOamPmCfgSessIpForwardClass": tmnxOamPmCfgSessIpForwardClass,
       "tmnxOamPmCfgSessIpProfile": tmnxOamPmCfgSessIpProfile,
       "tmnxOamPmCfgSessIpTtl": tmnxOamPmCfgSessIpTtl,
       "tmnxOamPmCfgTwampLtTable": tmnxOamPmCfgTwampLtTable,
       "tmnxOamPmCfgTwampLtEntry": tmnxOamPmCfgTwampLtEntry,
       "tmnxOamPmCfgTwampLtRowStatus": tmnxOamPmCfgTwampLtRowStatus,
       "tmnxOamPmCfgTwampLtAdminStatus": tmnxOamPmCfgTwampLtAdminStatus,
       "tmnxOamPmCfgTwampLtOnDmndStatus": tmnxOamPmCfgTwampLtOnDmndStatus,
       "tmnxOamPmCfgTwampLtTestId": tmnxOamPmCfgTwampLtTestId,
       "tmnxOamPmCfgTwampLtInterval": tmnxOamPmCfgTwampLtInterval,
       "tmnxOamPmCfgTwampLtPadSize": tmnxOamPmCfgTwampLtPadSize,
       "tmnxOamPmCfgTwampLtTestDuration": tmnxOamPmCfgTwampLtTestDuration,
       "tmnxOamPmCfgTwampLtRunTimeLeft": tmnxOamPmCfgTwampLtRunTimeLeft,
       "tmnxOamPmCfgTwlRflTable": tmnxOamPmCfgTwlRflTable,
       "tmnxOamPmCfgTwlRflEntry": tmnxOamPmCfgTwlRflEntry,
       "tmnxOamPmCfgTwlRflRowStatus": tmnxOamPmCfgTwlRflRowStatus,
       "tmnxOamPmCfgTwlRflAdminStatus": tmnxOamPmCfgTwlRflAdminStatus,
       "tmnxOamPmCfgTwlRflDescription": tmnxOamPmCfgTwlRflDescription,
       "tmnxOamPmCfgTwlRflListenUdpPort": tmnxOamPmCfgTwlRflListenUdpPort,
       "tmnxOamPmCfgTwlRflPfxTable": tmnxOamPmCfgTwlRflPfxTable,
       "tmnxOamPmCfgTwlRflPfxEntry": tmnxOamPmCfgTwlRflPfxEntry,
       "tmnxOamPmCfgTwlRflPfxPrefixType": tmnxOamPmCfgTwlRflPfxPrefixType,
       "tmnxOamPmCfgTwlRflPfxPrefix": tmnxOamPmCfgTwlRflPfxPrefix,
       "tmnxOamPmCfgTwlRflPfxPrefixLen": tmnxOamPmCfgTwlRflPfxPrefixLen,
       "tmnxOamPmCfgTwlRflPfxRowStatus": tmnxOamPmCfgTwlRflPfxRowStatus,
       "tmnxOamPmCfgTwlRflPfxDescription": tmnxOamPmCfgTwlRflPfxDescription,
       "tmnxOamPmCfgLossLmmTable": tmnxOamPmCfgLossLmmTable,
       "tmnxOamPmCfgLossLmmEntry": tmnxOamPmCfgLossLmmEntry,
       "tmnxOamPmCfgLossLmmRowStatus": tmnxOamPmCfgLossLmmRowStatus,
       "tmnxOamPmCfgLossLmmAdminStatus": tmnxOamPmCfgLossLmmAdminStatus,
       "tmnxOamPmCfgLossLmmOnDmndStatus": tmnxOamPmCfgLossLmmOnDmndStatus,
       "tmnxOamPmCfgLossLmmTestId": tmnxOamPmCfgLossLmmTestId,
       "tmnxOamPmCfgLossLmmInterval": tmnxOamPmCfgLossLmmInterval,
       "tmnxOamPmCfgLossLmmTestDuration": tmnxOamPmCfgLossLmmTestDuration,
       "tmnxOamPmCfgLossLmmRunTimeLeft": tmnxOamPmCfgLossLmmRunTimeLeft,
       "tmnxOamPmStatsObjs": tmnxOamPmStatsObjs,
       "tmnxOamPmStatsScalarObjs": tmnxOamPmStatsScalarObjs,
       "tmnxOamPmStatsTableObjs": tmnxOamPmStatsTableObjs,
       "tmnxOamPmStsBaseTable": tmnxOamPmStsBaseTable,
       "tmnxOamPmStsBaseEntry": tmnxOamPmStsBaseEntry,
       "tmnxOamPmStsBaseTestType": tmnxOamPmStsBaseTestType,
       "tmnxOamPmStsMeasIntvlDuration": tmnxOamPmStsMeasIntvlDuration,
       "tmnxOamPmStsIntvlNum": tmnxOamPmStsIntvlNum,
       "tmnxOamPmStsBaseOperStatus": tmnxOamPmStsBaseOperStatus,
       "tmnxOamPmStsBaseSuspect": tmnxOamPmStsBaseSuspect,
       "tmnxOamPmStsBaseStartTime": tmnxOamPmStsBaseStartTime,
       "tmnxOamPmStsBaseElapsedTime": tmnxOamPmStsBaseElapsedTime,
       "tmnxOamPmStsBaseTestFramesTx": tmnxOamPmStsBaseTestFramesTx,
       "tmnxOamPmStsBaseTestFramesRx": tmnxOamPmStsBaseTestFramesRx,
       "tmnxOamPmStsMeasIntvlIndexTable": tmnxOamPmStsMeasIntvlIndexTable,
       "tmnxOamPmStsMeasIntvlIndexEntry": tmnxOamPmStsMeasIntvlIndexEntry,
       "tmnxOamPmStsMeasIntvlIndexNewest": tmnxOamPmStsMeasIntvlIndexNewest,
       "tmnxOamPmStsLossSlmTable": tmnxOamPmStsLossSlmTable,
       "tmnxOamPmStsLossSlmEntry": tmnxOamPmStsLossSlmEntry,
       "tmnxOamPmStsLossSlmTxFwd": tmnxOamPmStsLossSlmTxFwd,
       "tmnxOamPmStsLossSlmRxFwd": tmnxOamPmStsLossSlmRxFwd,
       "tmnxOamPmStsLossSlmTxBwd": tmnxOamPmStsLossSlmTxBwd,
       "tmnxOamPmStsLossSlmRxBwd": tmnxOamPmStsLossSlmRxBwd,
       "tmnxOamPmStsLossSlmAvailIndFwd": tmnxOamPmStsLossSlmAvailIndFwd,
       "tmnxOamPmStsLossSlmAvailIndBwd": tmnxOamPmStsLossSlmAvailIndBwd,
       "tmnxOamPmStsLossSlmUnavlIndFwd": tmnxOamPmStsLossSlmUnavlIndFwd,
       "tmnxOamPmStsLossSlmUnavlIndBwd": tmnxOamPmStsLossSlmUnavlIndBwd,
       "tmnxOamPmStsLossSlmUndtAvlFwd": tmnxOamPmStsLossSlmUndtAvlFwd,
       "tmnxOamPmStsLossSlmUndtUnavlFwd": tmnxOamPmStsLossSlmUndtUnavlFwd,
       "tmnxOamPmStsLossSlmUndtAvlBwd": tmnxOamPmStsLossSlmUndtAvlBwd,
       "tmnxOamPmStsLossSlmUndtUnavlBwd": tmnxOamPmStsLossSlmUndtUnavlBwd,
       "tmnxOamPmStsLossSlmHliFwd": tmnxOamPmStsLossSlmHliFwd,
       "tmnxOamPmStsLossSlmHliBwd": tmnxOamPmStsLossSlmHliBwd,
       "tmnxOamPmStsLossSlmChliFwd": tmnxOamPmStsLossSlmChliFwd,
       "tmnxOamPmStsLossSlmChliBwd": tmnxOamPmStsLossSlmChliBwd,
       "tmnxOamPmStsLossSlmMinFlrFwd": tmnxOamPmStsLossSlmMinFlrFwd,
       "tmnxOamPmStsLossSlmMaxFlrFwd": tmnxOamPmStsLossSlmMaxFlrFwd,
       "tmnxOamPmStsLossSlmAvgFlrFwd": tmnxOamPmStsLossSlmAvgFlrFwd,
       "tmnxOamPmStsLossSlmMinFlrBwd": tmnxOamPmStsLossSlmMinFlrBwd,
       "tmnxOamPmStsLossSlmMaxFlrBwd": tmnxOamPmStsLossSlmMaxFlrBwd,
       "tmnxOamPmStsLossSlmAvgFlrBwd": tmnxOamPmStsLossSlmAvgFlrBwd,
       "tmnxOamPmStsDelayDmmTable": tmnxOamPmStsDelayDmmTable,
       "tmnxOamPmStsDelayDmmEntry": tmnxOamPmStsDelayDmmEntry,
       "tmnxOamPmStsDelayDmmFwdMin": tmnxOamPmStsDelayDmmFwdMin,
       "tmnxOamPmStsDelayDmmFwdMax": tmnxOamPmStsDelayDmmFwdMax,
       "tmnxOamPmStsDelayDmmFwdAvg": tmnxOamPmStsDelayDmmFwdAvg,
       "tmnxOamPmStsDelayDmmBwdMin": tmnxOamPmStsDelayDmmBwdMin,
       "tmnxOamPmStsDelayDmmBwdMax": tmnxOamPmStsDelayDmmBwdMax,
       "tmnxOamPmStsDelayDmmBwdAvg": tmnxOamPmStsDelayDmmBwdAvg,
       "tmnxOamPmStsDelayDmm2wyMin": tmnxOamPmStsDelayDmm2wyMin,
       "tmnxOamPmStsDelayDmm2wyMax": tmnxOamPmStsDelayDmm2wyMax,
       "tmnxOamPmStsDelayDmm2wyAvg": tmnxOamPmStsDelayDmm2wyAvg,
       "tmnxOamPmStsDelayDmmBinTable": tmnxOamPmStsDelayDmmBinTable,
       "tmnxOamPmStsDelayDmmBinEntry": tmnxOamPmStsDelayDmmBinEntry,
       "tmnxOamPmStsDelayDmmBinNum": tmnxOamPmStsDelayDmmBinNum,
       "tmnxOamPmStsDelayDmmBinFwdCount": tmnxOamPmStsDelayDmmBinFwdCount,
       "tmnxOamPmStsDelayDmmBinBwdCount": tmnxOamPmStsDelayDmmBinBwdCount,
       "tmnxOamPmStsDelayDmmBin2wyCount": tmnxOamPmStsDelayDmmBin2wyCount,
       "tmnxOamPmStsTwlRflTable": tmnxOamPmStsTwlRflTable,
       "tmnxOamPmStsTwlRflEntry": tmnxOamPmStsTwlRflEntry,
       "tmnxOamPmStsTwlRflUpTime": tmnxOamPmStsTwlRflUpTime,
       "tmnxOamPmStsTwlRflFramesRx": tmnxOamPmStsTwlRflFramesRx,
       "tmnxOamPmStsTwlRflFramesTx": tmnxOamPmStsTwlRflFramesTx,
       "tmnxOamPmStsDelayTwlTable": tmnxOamPmStsDelayTwlTable,
       "tmnxOamPmStsDelayTwlEntry": tmnxOamPmStsDelayTwlEntry,
       "tmnxOamPmStsDelayTwlFwdMin": tmnxOamPmStsDelayTwlFwdMin,
       "tmnxOamPmStsDelayTwlFwdMax": tmnxOamPmStsDelayTwlFwdMax,
       "tmnxOamPmStsDelayTwlFwdAvg": tmnxOamPmStsDelayTwlFwdAvg,
       "tmnxOamPmStsDelayTwlBwdMin": tmnxOamPmStsDelayTwlBwdMin,
       "tmnxOamPmStsDelayTwlBwdMax": tmnxOamPmStsDelayTwlBwdMax,
       "tmnxOamPmStsDelayTwlBwdAvg": tmnxOamPmStsDelayTwlBwdAvg,
       "tmnxOamPmStsDelayTwl2wyMin": tmnxOamPmStsDelayTwl2wyMin,
       "tmnxOamPmStsDelayTwl2wyMax": tmnxOamPmStsDelayTwl2wyMax,
       "tmnxOamPmStsDelayTwl2wyAvg": tmnxOamPmStsDelayTwl2wyAvg,
       "tmnxOamPmStsDelayTwlBinTable": tmnxOamPmStsDelayTwlBinTable,
       "tmnxOamPmStsDelayTwlBinEntry": tmnxOamPmStsDelayTwlBinEntry,
       "tmnxOamPmStsDelayTwlBinNum": tmnxOamPmStsDelayTwlBinNum,
       "tmnxOamPmStsDelayTwlBinFwdCount": tmnxOamPmStsDelayTwlBinFwdCount,
       "tmnxOamPmStsDelayTwlBinBwdCount": tmnxOamPmStsDelayTwlBinBwdCount,
       "tmnxOamPmStsDelayTwlBin2wyCount": tmnxOamPmStsDelayTwlBin2wyCount,
       "tmnxOamPmStsLossLmmTable": tmnxOamPmStsLossLmmTable,
       "tmnxOamPmStsLossLmmEntry": tmnxOamPmStsLossLmmEntry,
       "tmnxOamPmStsLossLmmTxFwd": tmnxOamPmStsLossLmmTxFwd,
       "tmnxOamPmStsLossLmmRxFwd": tmnxOamPmStsLossLmmRxFwd,
       "tmnxOamPmStsLossLmmTxBwd": tmnxOamPmStsLossLmmTxBwd,
       "tmnxOamPmStsLossLmmRxBwd": tmnxOamPmStsLossLmmRxBwd,
       "tmnxOamPmStsLossLmmMinFlrFwd": tmnxOamPmStsLossLmmMinFlrFwd,
       "tmnxOamPmStsLossLmmMaxFlrFwd": tmnxOamPmStsLossLmmMaxFlrFwd,
       "tmnxOamPmStsLossLmmAvgFlrFwd": tmnxOamPmStsLossLmmAvgFlrFwd,
       "tmnxOamPmStsLossLmmMinFlrBwd": tmnxOamPmStsLossLmmMinFlrBwd,
       "tmnxOamPmStsLossLmmMaxFlrBwd": tmnxOamPmStsLossLmmMaxFlrBwd,
       "tmnxOamPmStsLossLmmAvgFlrBwd": tmnxOamPmStsLossLmmAvgFlrBwd,
       "tmnxOamPmNotificationObjs": tmnxOamPmNotificationObjs,
       "tmnxOamPmNotifyPrefix": tmnxOamPmNotifyPrefix,
       "tmnxOamPmNotifications": tmnxOamPmNotifications}
)
