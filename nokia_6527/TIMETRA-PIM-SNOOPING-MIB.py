# SNMP MIB module (TIMETRA-PIM-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-PIM-SNOOPING-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:37:40 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tmnxCardHwIndex,) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "tmnxCardHwIndex")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(vRtrPimNgAFGenAFType,) = mibBuilder.importSymbols(
    "TIMETRA-PIM-NG-MIB",
    "vRtrPimNgAFGenAFType")

(svcId,) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "svcId")

(ServiceOperStatus,
 TNamedItemOrEmpty,
 TmnxAdminState,
 TmnxEncapVal,
 TmnxPortID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "ServiceOperStatus",
    "TNamedItemOrEmpty",
    "TmnxAdminState",
    "TmnxEncapVal",
    "TmnxPortID")


# MODULE-IDENTITY

timetraPimSnoopingMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 53)
)
if mibBuilder.loadTexts:
    timetraPimSnoopingMIBModule.setRevisions(
        ("1909-02-28 00:00",
         "1908-01-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxPimSnpgOperState(TextualConvention, Integer32):
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
        *(("down", 1),
          ("snoop", 2),
          ("proxy", 3))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxPimSnpgConformance_ObjectIdentity = ObjectIdentity
tmnxPimSnpgConformance = _TmnxPimSnpgConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53)
)
_TmnxPimSnpgCompliances_ObjectIdentity = ObjectIdentity
tmnxPimSnpgCompliances = _TmnxPimSnpgCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53, 1)
)
_TmnxPimSnpgGroups_ObjectIdentity = ObjectIdentity
tmnxPimSnpgGroups = _TmnxPimSnpgGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53, 2)
)
_TmnxPimSnpgObjs_ObjectIdentity = ObjectIdentity
tmnxPimSnpgObjs = _TmnxPimSnpgObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53)
)
_TmnxPimSnpgProtocolObjs_ObjectIdentity = ObjectIdentity
tmnxPimSnpgProtocolObjs = _TmnxPimSnpgProtocolObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1)
)
_TmnxPimSnpgGenTableLstChanged_Type = TimeStamp
_TmnxPimSnpgGenTableLstChanged_Object = MibScalar
tmnxPimSnpgGenTableLstChanged = _TmnxPimSnpgGenTableLstChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 1),
    _TmnxPimSnpgGenTableLstChanged_Type()
)
tmnxPimSnpgGenTableLstChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenTableLstChanged.setStatus("current")
_TmnxPimSnpgGeneralTable_Object = MibTable
tmnxPimSnpgGeneralTable = _TmnxPimSnpgGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxPimSnpgGeneralTable.setStatus("current")
_TmnxPimSnpgGeneralEntry_Object = MibTableRow
tmnxPimSnpgGeneralEntry = _TmnxPimSnpgGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1)
)
tmnxPimSnpgGeneralEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenAFType"),
)
if mibBuilder.loadTexts:
    tmnxPimSnpgGeneralEntry.setStatus("current")
_TmnxPimSnpgGenRowStatus_Type = RowStatus
_TmnxPimSnpgGenRowStatus_Object = MibTableColumn
tmnxPimSnpgGenRowStatus = _TmnxPimSnpgGenRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 1),
    _TmnxPimSnpgGenRowStatus_Type()
)
tmnxPimSnpgGenRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenRowStatus.setStatus("current")
_TmnxPimSnpgGenRowLastChanged_Type = TimeStamp
_TmnxPimSnpgGenRowLastChanged_Object = MibTableColumn
tmnxPimSnpgGenRowLastChanged = _TmnxPimSnpgGenRowLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 2),
    _TmnxPimSnpgGenRowLastChanged_Type()
)
tmnxPimSnpgGenRowLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenRowLastChanged.setStatus("current")


class _TmnxPimSnpgGenAdminState_Type(TmnxAdminState):
    """Custom type tmnxPimSnpgGenAdminState based on TmnxAdminState"""
    defaultValue = 2


_TmnxPimSnpgGenAdminState_Type.__name__ = "TmnxAdminState"
_TmnxPimSnpgGenAdminState_Object = MibTableColumn
tmnxPimSnpgGenAdminState = _TmnxPimSnpgGenAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 3),
    _TmnxPimSnpgGenAdminState_Type()
)
tmnxPimSnpgGenAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenAdminState.setStatus("current")


class _TmnxPimSnpgGenOperState_Type(TmnxPimSnpgOperState):
    """Custom type tmnxPimSnpgGenOperState based on TmnxPimSnpgOperState"""
    defaultValue = 1


_TmnxPimSnpgGenOperState_Type.__name__ = "TmnxPimSnpgOperState"
_TmnxPimSnpgGenOperState_Object = MibTableColumn
tmnxPimSnpgGenOperState = _TmnxPimSnpgGenOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 4),
    _TmnxPimSnpgGenOperState_Type()
)
tmnxPimSnpgGenOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenOperState.setStatus("current")


class _TmnxPimSnpgGenHoldTime_Type(Unsigned32):
    """Custom type tmnxPimSnpgGenHoldTime based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_TmnxPimSnpgGenHoldTime_Type.__name__ = "Unsigned32"
_TmnxPimSnpgGenHoldTime_Object = MibTableColumn
tmnxPimSnpgGenHoldTime = _TmnxPimSnpgGenHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 5),
    _TmnxPimSnpgGenHoldTime_Type()
)
tmnxPimSnpgGenHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenHoldTime.setUnits("seconds")
_TmnxPimSnpgGenDRType_Type = InetAddressType
_TmnxPimSnpgGenDRType_Object = MibTableColumn
tmnxPimSnpgGenDRType = _TmnxPimSnpgGenDRType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 6),
    _TmnxPimSnpgGenDRType_Type()
)
tmnxPimSnpgGenDRType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenDRType.setStatus("current")


class _TmnxPimSnpgGenDR_Type(InetAddress):
    """Custom type tmnxPimSnpgGenDR based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPimSnpgGenDR_Type.__name__ = "InetAddress"
_TmnxPimSnpgGenDR_Object = MibTableColumn
tmnxPimSnpgGenDR = _TmnxPimSnpgGenDR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 7),
    _TmnxPimSnpgGenDR_Type()
)
tmnxPimSnpgGenDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenDR.setStatus("current")
_TmnxPimSnpgGenTrackingSupport_Type = TruthValue
_TmnxPimSnpgGenTrackingSupport_Object = MibTableColumn
tmnxPimSnpgGenTrackingSupport = _TmnxPimSnpgGenTrackingSupport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 8),
    _TmnxPimSnpgGenTrackingSupport_Type()
)
tmnxPimSnpgGenTrackingSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenTrackingSupport.setStatus("current")
_TmnxPimSnpgGenUpTime_Type = Unsigned32
_TmnxPimSnpgGenUpTime_Object = MibTableColumn
tmnxPimSnpgGenUpTime = _TmnxPimSnpgGenUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 9),
    _TmnxPimSnpgGenUpTime_Type()
)
tmnxPimSnpgGenUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenUpTime.setUnits("seconds")


class _TmnxPimSnpgGenMode_Type(Integer32):
    """Custom type tmnxPimSnpgGenMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("proxy", 1),
          ("snoop", 2))
    )


_TmnxPimSnpgGenMode_Type.__name__ = "Integer32"
_TmnxPimSnpgGenMode_Object = MibTableColumn
tmnxPimSnpgGenMode = _TmnxPimSnpgGenMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 10),
    _TmnxPimSnpgGenMode_Type()
)
tmnxPimSnpgGenMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenMode.setStatus("current")


class _TmnxPimSnpgGenGroupPolicy1_Type(TNamedItemOrEmpty):
    """Custom type tmnxPimSnpgGenGroupPolicy1 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxPimSnpgGenGroupPolicy1_Type.__name__ = "TNamedItemOrEmpty"
_TmnxPimSnpgGenGroupPolicy1_Object = MibTableColumn
tmnxPimSnpgGenGroupPolicy1 = _TmnxPimSnpgGenGroupPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 11),
    _TmnxPimSnpgGenGroupPolicy1_Type()
)
tmnxPimSnpgGenGroupPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenGroupPolicy1.setStatus("current")


class _TmnxPimSnpgGenGroupPolicy2_Type(TNamedItemOrEmpty):
    """Custom type tmnxPimSnpgGenGroupPolicy2 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxPimSnpgGenGroupPolicy2_Type.__name__ = "TNamedItemOrEmpty"
_TmnxPimSnpgGenGroupPolicy2_Object = MibTableColumn
tmnxPimSnpgGenGroupPolicy2 = _TmnxPimSnpgGenGroupPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 12),
    _TmnxPimSnpgGenGroupPolicy2_Type()
)
tmnxPimSnpgGenGroupPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenGroupPolicy2.setStatus("current")


class _TmnxPimSnpgGenGroupPolicy3_Type(TNamedItemOrEmpty):
    """Custom type tmnxPimSnpgGenGroupPolicy3 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxPimSnpgGenGroupPolicy3_Type.__name__ = "TNamedItemOrEmpty"
_TmnxPimSnpgGenGroupPolicy3_Object = MibTableColumn
tmnxPimSnpgGenGroupPolicy3 = _TmnxPimSnpgGenGroupPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 13),
    _TmnxPimSnpgGenGroupPolicy3_Type()
)
tmnxPimSnpgGenGroupPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenGroupPolicy3.setStatus("current")


class _TmnxPimSnpgGenGroupPolicy4_Type(TNamedItemOrEmpty):
    """Custom type tmnxPimSnpgGenGroupPolicy4 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxPimSnpgGenGroupPolicy4_Type.__name__ = "TNamedItemOrEmpty"
_TmnxPimSnpgGenGroupPolicy4_Object = MibTableColumn
tmnxPimSnpgGenGroupPolicy4 = _TmnxPimSnpgGenGroupPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 14),
    _TmnxPimSnpgGenGroupPolicy4_Type()
)
tmnxPimSnpgGenGroupPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenGroupPolicy4.setStatus("current")


class _TmnxPimSnpgGenGroupPolicy5_Type(TNamedItemOrEmpty):
    """Custom type tmnxPimSnpgGenGroupPolicy5 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxPimSnpgGenGroupPolicy5_Type.__name__ = "TNamedItemOrEmpty"
_TmnxPimSnpgGenGroupPolicy5_Object = MibTableColumn
tmnxPimSnpgGenGroupPolicy5 = _TmnxPimSnpgGenGroupPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 2, 1, 15),
    _TmnxPimSnpgGenGroupPolicy5_Type()
)
tmnxPimSnpgGenGroupPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenGroupPolicy5.setStatus("current")
_TmnxPimSnpgGrpSrcTable_Object = MibTable
tmnxPimSnpgGrpSrcTable = _TmnxPimSnpgGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcTable.setStatus("current")
_TmnxPimSnpgGrpSrcEntry_Object = MibTableRow
tmnxPimSnpgGrpSrcEntry = _TmnxPimSnpgGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1)
)
tmnxPimSnpgGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcGrpAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcGroupAddress"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcSrcAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcSourceAddress"),
)
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcEntry.setStatus("current")
_TmnxPimSnpgGrpSrcGrpAddrType_Type = InetAddressType
_TmnxPimSnpgGrpSrcGrpAddrType_Object = MibTableColumn
tmnxPimSnpgGrpSrcGrpAddrType = _TmnxPimSnpgGrpSrcGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 1),
    _TmnxPimSnpgGrpSrcGrpAddrType_Type()
)
tmnxPimSnpgGrpSrcGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcGrpAddrType.setStatus("current")


class _TmnxPimSnpgGrpSrcGroupAddress_Type(InetAddress):
    """Custom type tmnxPimSnpgGrpSrcGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPimSnpgGrpSrcGroupAddress_Type.__name__ = "InetAddress"
_TmnxPimSnpgGrpSrcGroupAddress_Object = MibTableColumn
tmnxPimSnpgGrpSrcGroupAddress = _TmnxPimSnpgGrpSrcGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 2),
    _TmnxPimSnpgGrpSrcGroupAddress_Type()
)
tmnxPimSnpgGrpSrcGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcGroupAddress.setStatus("current")
_TmnxPimSnpgGrpSrcSrcAddrType_Type = InetAddressType
_TmnxPimSnpgGrpSrcSrcAddrType_Object = MibTableColumn
tmnxPimSnpgGrpSrcSrcAddrType = _TmnxPimSnpgGrpSrcSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 3),
    _TmnxPimSnpgGrpSrcSrcAddrType_Type()
)
tmnxPimSnpgGrpSrcSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcSrcAddrType.setStatus("current")


class _TmnxPimSnpgGrpSrcSourceAddress_Type(InetAddress):
    """Custom type tmnxPimSnpgGrpSrcSourceAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPimSnpgGrpSrcSourceAddress_Type.__name__ = "InetAddress"
_TmnxPimSnpgGrpSrcSourceAddress_Object = MibTableColumn
tmnxPimSnpgGrpSrcSourceAddress = _TmnxPimSnpgGrpSrcSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 4),
    _TmnxPimSnpgGrpSrcSourceAddress_Type()
)
tmnxPimSnpgGrpSrcSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcSourceAddress.setStatus("current")
_TmnxPimSnpgGrpSrcRpfNbrAddrType_Type = InetAddressType
_TmnxPimSnpgGrpSrcRpfNbrAddrType_Object = MibTableColumn
tmnxPimSnpgGrpSrcRpfNbrAddrType = _TmnxPimSnpgGrpSrcRpfNbrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 5),
    _TmnxPimSnpgGrpSrcRpfNbrAddrType_Type()
)
tmnxPimSnpgGrpSrcRpfNbrAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcRpfNbrAddrType.setStatus("current")


class _TmnxPimSnpgGrpSrcRpfNbrAddr_Type(InetAddress):
    """Custom type tmnxPimSnpgGrpSrcRpfNbrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPimSnpgGrpSrcRpfNbrAddr_Type.__name__ = "InetAddress"
_TmnxPimSnpgGrpSrcRpfNbrAddr_Object = MibTableColumn
tmnxPimSnpgGrpSrcRpfNbrAddr = _TmnxPimSnpgGrpSrcRpfNbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 6),
    _TmnxPimSnpgGrpSrcRpfNbrAddr_Type()
)
tmnxPimSnpgGrpSrcRpfNbrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcRpfNbrAddr.setStatus("current")
_TmnxPimSnpgGrpSrcRpfIfIndex_Type = InterfaceIndexOrZero
_TmnxPimSnpgGrpSrcRpfIfIndex_Object = MibTableColumn
tmnxPimSnpgGrpSrcRpfIfIndex = _TmnxPimSnpgGrpSrcRpfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 7),
    _TmnxPimSnpgGrpSrcRpfIfIndex_Type()
)
tmnxPimSnpgGrpSrcRpfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcRpfIfIndex.setStatus("current")
_TmnxPimSnpgGrpSrcRptRpfNbrAdrTp_Type = InetAddressType
_TmnxPimSnpgGrpSrcRptRpfNbrAdrTp_Object = MibTableColumn
tmnxPimSnpgGrpSrcRptRpfNbrAdrTp = _TmnxPimSnpgGrpSrcRptRpfNbrAdrTp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 8),
    _TmnxPimSnpgGrpSrcRptRpfNbrAdrTp_Type()
)
tmnxPimSnpgGrpSrcRptRpfNbrAdrTp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcRptRpfNbrAdrTp.setStatus("current")


class _TmnxPimSnpgGrpSrcRptRpfNbrAddr_Type(InetAddress):
    """Custom type tmnxPimSnpgGrpSrcRptRpfNbrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPimSnpgGrpSrcRptRpfNbrAddr_Type.__name__ = "InetAddress"
_TmnxPimSnpgGrpSrcRptRpfNbrAddr_Object = MibTableColumn
tmnxPimSnpgGrpSrcRptRpfNbrAddr = _TmnxPimSnpgGrpSrcRptRpfNbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 9),
    _TmnxPimSnpgGrpSrcRptRpfNbrAddr_Type()
)
tmnxPimSnpgGrpSrcRptRpfNbrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcRptRpfNbrAddr.setStatus("current")


class _TmnxPimSnpgGrpSrcUstrmJpState_Type(Integer32):
    """Custom type tmnxPimSnpgGrpSrcUstrmJpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-info", 0),
          ("joined", 1),
          ("prune-pend", 2),
          ("pruned", 3))
    )


_TmnxPimSnpgGrpSrcUstrmJpState_Type.__name__ = "Integer32"
_TmnxPimSnpgGrpSrcUstrmJpState_Object = MibTableColumn
tmnxPimSnpgGrpSrcUstrmJpState = _TmnxPimSnpgGrpSrcUstrmJpState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 10),
    _TmnxPimSnpgGrpSrcUstrmJpState_Type()
)
tmnxPimSnpgGrpSrcUstrmJpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcUstrmJpState.setStatus("current")
_TmnxPimSnpgGrpSrcUstrmJpTimer_Type = Unsigned32
_TmnxPimSnpgGrpSrcUstrmJpTimer_Object = MibTableColumn
tmnxPimSnpgGrpSrcUstrmJpTimer = _TmnxPimSnpgGrpSrcUstrmJpTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 11),
    _TmnxPimSnpgGrpSrcUstrmJpTimer_Type()
)
tmnxPimSnpgGrpSrcUstrmJpTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcUstrmJpTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcUstrmJpTimer.setUnits("seconds")


class _TmnxPimSnpgGrpSrcUstrmRptJpSt_Type(Integer32):
    """Custom type tmnxPimSnpgGrpSrcUstrmRptJpSt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notJoinedStarG", 0),
          ("notPruned", 1),
          ("pruned", 2))
    )


_TmnxPimSnpgGrpSrcUstrmRptJpSt_Type.__name__ = "Integer32"
_TmnxPimSnpgGrpSrcUstrmRptJpSt_Object = MibTableColumn
tmnxPimSnpgGrpSrcUstrmRptJpSt = _TmnxPimSnpgGrpSrcUstrmRptJpSt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 12),
    _TmnxPimSnpgGrpSrcUstrmRptJpSt_Type()
)
tmnxPimSnpgGrpSrcUstrmRptJpSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcUstrmRptJpSt.setStatus("current")
_TmnxPimSnpgGrpSrcUstrmRptOvdTmr_Type = Unsigned32
_TmnxPimSnpgGrpSrcUstrmRptOvdTmr_Object = MibTableColumn
tmnxPimSnpgGrpSrcUstrmRptOvdTmr = _TmnxPimSnpgGrpSrcUstrmRptOvdTmr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 13),
    _TmnxPimSnpgGrpSrcUstrmRptOvdTmr_Type()
)
tmnxPimSnpgGrpSrcUstrmRptOvdTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcUstrmRptOvdTmr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcUstrmRptOvdTmr.setUnits("seconds")
_TmnxPimSnpgGrpSrcNumJoinOif_Type = Gauge32
_TmnxPimSnpgGrpSrcNumJoinOif_Object = MibTableColumn
tmnxPimSnpgGrpSrcNumJoinOif = _TmnxPimSnpgGrpSrcNumJoinOif_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 14),
    _TmnxPimSnpgGrpSrcNumJoinOif_Type()
)
tmnxPimSnpgGrpSrcNumJoinOif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcNumJoinOif.setStatus("current")
_TmnxPimSnpgGrpSrcNumImdiateOif_Type = Gauge32
_TmnxPimSnpgGrpSrcNumImdiateOif_Object = MibTableColumn
tmnxPimSnpgGrpSrcNumImdiateOif = _TmnxPimSnpgGrpSrcNumImdiateOif_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 15),
    _TmnxPimSnpgGrpSrcNumImdiateOif_Type()
)
tmnxPimSnpgGrpSrcNumImdiateOif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcNumImdiateOif.setStatus("current")
_TmnxPimSnpgGrpSrcNumInhritedOif_Type = Gauge32
_TmnxPimSnpgGrpSrcNumInhritedOif_Object = MibTableColumn
tmnxPimSnpgGrpSrcNumInhritedOif = _TmnxPimSnpgGrpSrcNumInhritedOif_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 16),
    _TmnxPimSnpgGrpSrcNumInhritedOif_Type()
)
tmnxPimSnpgGrpSrcNumInhritedOif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcNumInhritedOif.setStatus("current")
_TmnxPimSnpgGrpSrcNumInherRptOif_Type = Gauge32
_TmnxPimSnpgGrpSrcNumInherRptOif_Object = MibTableColumn
tmnxPimSnpgGrpSrcNumInherRptOif = _TmnxPimSnpgGrpSrcNumInherRptOif_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 17),
    _TmnxPimSnpgGrpSrcNumInherRptOif_Type()
)
tmnxPimSnpgGrpSrcNumInherRptOif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcNumInherRptOif.setStatus("current")
_TmnxPimSnpgGrpSrcNumIif_Type = Gauge32
_TmnxPimSnpgGrpSrcNumIif_Object = MibTableColumn
tmnxPimSnpgGrpSrcNumIif = _TmnxPimSnpgGrpSrcNumIif_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 18),
    _TmnxPimSnpgGrpSrcNumIif_Type()
)
tmnxPimSnpgGrpSrcNumIif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcNumIif.setStatus("current")
_TmnxPimSnpgGrpSrcUpTime_Type = Unsigned32
_TmnxPimSnpgGrpSrcUpTime_Object = MibTableColumn
tmnxPimSnpgGrpSrcUpTime = _TmnxPimSnpgGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 3, 1, 19),
    _TmnxPimSnpgGrpSrcUpTime_Type()
)
tmnxPimSnpgGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcUpTime.setUnits("seconds")
_TmnxPimSnpgGrpSrcIfTable_Object = MibTable
tmnxPimSnpgGrpSrcIfTable = _TmnxPimSnpgGrpSrcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcIfTable.setStatus("current")
_TmnxPimSnpgGrpSrcIfEntry_Object = MibTableRow
tmnxPimSnpgGrpSrcIfEntry = _TmnxPimSnpgGrpSrcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 4, 1)
)
tmnxPimSnpgGrpSrcIfEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcGrpAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcGroupAddress"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcSrcAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcSourceAddress"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgPortId"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgEncapValue"),
)
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcIfEntry.setStatus("current")
_TmnxPimSnpgPortId_Type = TmnxPortID
_TmnxPimSnpgPortId_Object = MibTableColumn
tmnxPimSnpgPortId = _TmnxPimSnpgPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 4, 1, 1),
    _TmnxPimSnpgPortId_Type()
)
tmnxPimSnpgPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPimSnpgPortId.setStatus("current")
_TmnxPimSnpgEncapValue_Type = TmnxEncapVal
_TmnxPimSnpgEncapValue_Object = MibTableColumn
tmnxPimSnpgEncapValue = _TmnxPimSnpgEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 4, 1, 2),
    _TmnxPimSnpgEncapValue_Type()
)
tmnxPimSnpgEncapValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPimSnpgEncapValue.setStatus("current")


class _TmnxPimSnpgGrpSrcIfFlags_Type(Bits):
    """Custom type tmnxPimSnpgGrpSrcIfFlags based on Bits"""
    namedValues = NamedValues(
        *(("immediateOifList", 0),
          ("inheritedOifList", 1),
          ("inheritedRptOifList", 2),
          ("joined", 3),
          ("rpfPort", 4))
    )

_TmnxPimSnpgGrpSrcIfFlags_Type.__name__ = "Bits"
_TmnxPimSnpgGrpSrcIfFlags_Object = MibTableColumn
tmnxPimSnpgGrpSrcIfFlags = _TmnxPimSnpgGrpSrcIfFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 4, 1, 3),
    _TmnxPimSnpgGrpSrcIfFlags_Type()
)
tmnxPimSnpgGrpSrcIfFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcIfFlags.setStatus("current")
_TmnxPimSnpgGenStatsTable_Object = MibTable
tmnxPimSnpgGenStatsTable = _TmnxPimSnpgGenStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxPimSnpgGenStatsTable.setStatus("current")
_TmnxPimSnpgGenStatsEntry_Object = MibTableRow
tmnxPimSnpgGenStatsEntry = _TmnxPimSnpgGenStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxPimSnpgGenStatsEntry.setStatus("current")
_TmnxPimSnpgGenStatsStarGTypes_Type = Gauge32
_TmnxPimSnpgGenStatsStarGTypes_Object = MibTableColumn
tmnxPimSnpgGenStatsStarGTypes = _TmnxPimSnpgGenStatsStarGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 5, 1, 1),
    _TmnxPimSnpgGenStatsStarGTypes_Type()
)
tmnxPimSnpgGenStatsStarGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenStatsStarGTypes.setStatus("current")
_TmnxPimSnpgGenStatsSGTypes_Type = Gauge32
_TmnxPimSnpgGenStatsSGTypes_Object = MibTableColumn
tmnxPimSnpgGenStatsSGTypes = _TmnxPimSnpgGenStatsSGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 5, 1, 2),
    _TmnxPimSnpgGenStatsSGTypes_Type()
)
tmnxPimSnpgGenStatsSGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGenStatsSGTypes.setStatus("current")
_TmnxPimSnpgGrpSrcStatsTable_Object = MibTable
tmnxPimSnpgGrpSrcStatsTable = _TmnxPimSnpgGrpSrcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcStatsTable.setStatus("current")
_TmnxPimSnpgGrpSrcStatsEntry_Object = MibTableRow
tmnxPimSnpgGrpSrcStatsEntry = _TmnxPimSnpgGrpSrcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 6, 1)
)
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcStatsEntry.setStatus("current")
_TmnxPimSnpgGrpSrcStatsFwdedPkts_Type = Counter32
_TmnxPimSnpgGrpSrcStatsFwdedPkts_Object = MibTableColumn
tmnxPimSnpgGrpSrcStatsFwdedPkts = _TmnxPimSnpgGrpSrcStatsFwdedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 6, 1, 1),
    _TmnxPimSnpgGrpSrcStatsFwdedPkts_Type()
)
tmnxPimSnpgGrpSrcStatsFwdedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcStatsFwdedPkts.setStatus("current")
_TmnxPimSnpgGrpSrcStatsFwdedOct_Type = Counter32
_TmnxPimSnpgGrpSrcStatsFwdedOct_Object = MibTableColumn
tmnxPimSnpgGrpSrcStatsFwdedOct = _TmnxPimSnpgGrpSrcStatsFwdedOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 1, 6, 1, 2),
    _TmnxPimSnpgGrpSrcStatsFwdedOct_Type()
)
tmnxPimSnpgGrpSrcStatsFwdedOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgGrpSrcStatsFwdedOct.setStatus("current")
_TmnxPimSnpgIfObjs_ObjectIdentity = ObjectIdentity
tmnxPimSnpgIfObjs = _TmnxPimSnpgIfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2)
)
_TmnxPimSnpgIfTableLastChanged_Type = TimeStamp
_TmnxPimSnpgIfTableLastChanged_Object = MibScalar
tmnxPimSnpgIfTableLastChanged = _TmnxPimSnpgIfTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 1),
    _TmnxPimSnpgIfTableLastChanged_Type()
)
tmnxPimSnpgIfTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfTableLastChanged.setStatus("current")
_TmnxPimSnpgIfTable_Object = MibTable
tmnxPimSnpgIfTable = _TmnxPimSnpgIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfTable.setStatus("current")
_TmnxPimSnpgIfEntry_Object = MibTableRow
tmnxPimSnpgIfEntry = _TmnxPimSnpgIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 2, 1)
)
tmnxPimSnpgIfEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgPortId"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgEncapValue"),
    (0, "TIMETRA-PIM-NG-MIB", "vRtrPimNgAFGenAFType"),
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfEntry.setStatus("current")
_TmnxPimSnpgIfLastChangeTime_Type = TimeStamp
_TmnxPimSnpgIfLastChangeTime_Object = MibTableColumn
tmnxPimSnpgIfLastChangeTime = _TmnxPimSnpgIfLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 2, 1, 1),
    _TmnxPimSnpgIfLastChangeTime_Type()
)
tmnxPimSnpgIfLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfLastChangeTime.setStatus("current")
_TmnxPimSnpgIfOperState_Type = ServiceOperStatus
_TmnxPimSnpgIfOperState_Object = MibTableColumn
tmnxPimSnpgIfOperState = _TmnxPimSnpgIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 2, 1, 2),
    _TmnxPimSnpgIfOperState_Type()
)
tmnxPimSnpgIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfOperState.setStatus("current")
_TmnxPimSnpgIfUpTime_Type = Unsigned32
_TmnxPimSnpgIfUpTime_Object = MibTableColumn
tmnxPimSnpgIfUpTime = _TmnxPimSnpgIfUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 2, 1, 3),
    _TmnxPimSnpgIfUpTime_Type()
)
tmnxPimSnpgIfUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfUpTime.setUnits("seconds")


class _TmnxPimSnpgIfMaxGroups_Type(Unsigned32):
    """Custom type tmnxPimSnpgIfMaxGroups based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16000),
    )


_TmnxPimSnpgIfMaxGroups_Type.__name__ = "Unsigned32"
_TmnxPimSnpgIfMaxGroups_Object = MibTableColumn
tmnxPimSnpgIfMaxGroups = _TmnxPimSnpgIfMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 2, 1, 4),
    _TmnxPimSnpgIfMaxGroups_Type()
)
tmnxPimSnpgIfMaxGroups.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfMaxGroups.setStatus("current")
_TmnxPimSnpgIfCurrentGroups_Type = Gauge32
_TmnxPimSnpgIfCurrentGroups_Object = MibTableColumn
tmnxPimSnpgIfCurrentGroups = _TmnxPimSnpgIfCurrentGroups_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 2, 1, 5),
    _TmnxPimSnpgIfCurrentGroups_Type()
)
tmnxPimSnpgIfCurrentGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfCurrentGroups.setStatus("current")
_TmnxPimSnpgIfMaxGroupsTillNow_Type = Counter32
_TmnxPimSnpgIfMaxGroupsTillNow_Object = MibTableColumn
tmnxPimSnpgIfMaxGroupsTillNow = _TmnxPimSnpgIfMaxGroupsTillNow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 2, 1, 6),
    _TmnxPimSnpgIfMaxGroupsTillNow_Type()
)
tmnxPimSnpgIfMaxGroupsTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfMaxGroupsTillNow.setStatus("current")
_TmnxPimSnpgIfNbrTable_Object = MibTable
tmnxPimSnpgIfNbrTable = _TmnxPimSnpgIfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 3)
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrTable.setStatus("current")
_TmnxPimSnpgIfNbrEntry_Object = MibTableRow
tmnxPimSnpgIfNbrEntry = _TmnxPimSnpgIfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 3, 1)
)
tmnxPimSnpgIfNbrEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgPortId"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgEncapValue"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrAddress"),
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrEntry.setStatus("current")
_TmnxPimSnpgIfNbrAddrType_Type = InetAddressType
_TmnxPimSnpgIfNbrAddrType_Object = MibTableColumn
tmnxPimSnpgIfNbrAddrType = _TmnxPimSnpgIfNbrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 3, 1, 1),
    _TmnxPimSnpgIfNbrAddrType_Type()
)
tmnxPimSnpgIfNbrAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrAddrType.setStatus("current")


class _TmnxPimSnpgIfNbrAddress_Type(InetAddress):
    """Custom type tmnxPimSnpgIfNbrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPimSnpgIfNbrAddress_Type.__name__ = "InetAddress"
_TmnxPimSnpgIfNbrAddress_Object = MibTableColumn
tmnxPimSnpgIfNbrAddress = _TmnxPimSnpgIfNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 3, 1, 2),
    _TmnxPimSnpgIfNbrAddress_Type()
)
tmnxPimSnpgIfNbrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrAddress.setStatus("current")
_TmnxPimSnpgIfNbrUpTime_Type = Unsigned32
_TmnxPimSnpgIfNbrUpTime_Object = MibTableColumn
tmnxPimSnpgIfNbrUpTime = _TmnxPimSnpgIfNbrUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 3, 1, 3),
    _TmnxPimSnpgIfNbrUpTime_Type()
)
tmnxPimSnpgIfNbrUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrUpTime.setUnits("seconds")
_TmnxPimSnpgIfNbrExpiryTime_Type = Unsigned32
_TmnxPimSnpgIfNbrExpiryTime_Object = MibTableColumn
tmnxPimSnpgIfNbrExpiryTime = _TmnxPimSnpgIfNbrExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 3, 1, 4),
    _TmnxPimSnpgIfNbrExpiryTime_Type()
)
tmnxPimSnpgIfNbrExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrExpiryTime.setUnits("seconds")
_TmnxPimSnpgIfNbrGenId_Type = Unsigned32
_TmnxPimSnpgIfNbrGenId_Object = MibTableColumn
tmnxPimSnpgIfNbrGenId = _TmnxPimSnpgIfNbrGenId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 3, 1, 5),
    _TmnxPimSnpgIfNbrGenId_Type()
)
tmnxPimSnpgIfNbrGenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrGenId.setStatus("current")
_TmnxPimSnpgIfNbrDrPriority_Type = Unsigned32
_TmnxPimSnpgIfNbrDrPriority_Object = MibTableColumn
tmnxPimSnpgIfNbrDrPriority = _TmnxPimSnpgIfNbrDrPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 3, 1, 6),
    _TmnxPimSnpgIfNbrDrPriority_Type()
)
tmnxPimSnpgIfNbrDrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrDrPriority.setStatus("current")
_TmnxPimSnpgIfNbrDrPriorPresent_Type = TruthValue
_TmnxPimSnpgIfNbrDrPriorPresent_Object = MibTableColumn
tmnxPimSnpgIfNbrDrPriorPresent = _TmnxPimSnpgIfNbrDrPriorPresent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 3, 1, 7),
    _TmnxPimSnpgIfNbrDrPriorPresent_Type()
)
tmnxPimSnpgIfNbrDrPriorPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrDrPriorPresent.setStatus("current")
_TmnxPimSnpgIfNbrLanDelay_Type = Unsigned32
_TmnxPimSnpgIfNbrLanDelay_Object = MibTableColumn
tmnxPimSnpgIfNbrLanDelay = _TmnxPimSnpgIfNbrLanDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 3, 1, 8),
    _TmnxPimSnpgIfNbrLanDelay_Type()
)
tmnxPimSnpgIfNbrLanDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrLanDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrLanDelay.setUnits("milliseconds")
_TmnxPimSnpgIfNbrLanDlayPrsnt_Type = TruthValue
_TmnxPimSnpgIfNbrLanDlayPrsnt_Object = MibTableColumn
tmnxPimSnpgIfNbrLanDlayPrsnt = _TmnxPimSnpgIfNbrLanDlayPrsnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 3, 1, 9),
    _TmnxPimSnpgIfNbrLanDlayPrsnt_Type()
)
tmnxPimSnpgIfNbrLanDlayPrsnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrLanDlayPrsnt.setStatus("current")
_TmnxPimSnpgIfNbrTrckngSpprt_Type = TruthValue
_TmnxPimSnpgIfNbrTrckngSpprt_Object = MibTableColumn
tmnxPimSnpgIfNbrTrckngSpprt = _TmnxPimSnpgIfNbrTrckngSpprt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 3, 1, 10),
    _TmnxPimSnpgIfNbrTrckngSpprt_Type()
)
tmnxPimSnpgIfNbrTrckngSpprt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrTrckngSpprt.setStatus("current")
_TmnxPimSnpgIfNbrHoldTime_Type = Unsigned32
_TmnxPimSnpgIfNbrHoldTime_Object = MibTableColumn
tmnxPimSnpgIfNbrHoldTime = _TmnxPimSnpgIfNbrHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 3, 1, 11),
    _TmnxPimSnpgIfNbrHoldTime_Type()
)
tmnxPimSnpgIfNbrHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrHoldTime.setUnits("seconds")
_TmnxPimSnpgIfNbrOvrdeIntrvl_Type = Unsigned32
_TmnxPimSnpgIfNbrOvrdeIntrvl_Object = MibTableColumn
tmnxPimSnpgIfNbrOvrdeIntrvl = _TmnxPimSnpgIfNbrOvrdeIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 3, 1, 12),
    _TmnxPimSnpgIfNbrOvrdeIntrvl_Type()
)
tmnxPimSnpgIfNbrOvrdeIntrvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrOvrdeIntrvl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNbrOvrdeIntrvl.setUnits("milliseconds")
_TmnxPimSnpgIfGrpSrcTable_Object = MibTable
tmnxPimSnpgIfGrpSrcTable = _TmnxPimSnpgIfGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 4)
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcTable.setStatus("current")
_TmnxPimSnpgIfGrpSrcEntry_Object = MibTableRow
tmnxPimSnpgIfGrpSrcEntry = _TmnxPimSnpgIfGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 4, 1)
)
tmnxPimSnpgIfGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgPortId"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgEncapValue"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfGrpSrcGrpAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfGrpSrcGroupAddr"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfGrpSrcSrcAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfGrpSrcSourceAddr"),
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcEntry.setStatus("current")
_TmnxPimSnpgIfGrpSrcGrpAddrType_Type = InetAddressType
_TmnxPimSnpgIfGrpSrcGrpAddrType_Object = MibTableColumn
tmnxPimSnpgIfGrpSrcGrpAddrType = _TmnxPimSnpgIfGrpSrcGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 4, 1, 1),
    _TmnxPimSnpgIfGrpSrcGrpAddrType_Type()
)
tmnxPimSnpgIfGrpSrcGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcGrpAddrType.setStatus("current")


class _TmnxPimSnpgIfGrpSrcGroupAddr_Type(InetAddress):
    """Custom type tmnxPimSnpgIfGrpSrcGroupAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPimSnpgIfGrpSrcGroupAddr_Type.__name__ = "InetAddress"
_TmnxPimSnpgIfGrpSrcGroupAddr_Object = MibTableColumn
tmnxPimSnpgIfGrpSrcGroupAddr = _TmnxPimSnpgIfGrpSrcGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 4, 1, 2),
    _TmnxPimSnpgIfGrpSrcGroupAddr_Type()
)
tmnxPimSnpgIfGrpSrcGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcGroupAddr.setStatus("current")
_TmnxPimSnpgIfGrpSrcSrcAddrType_Type = InetAddressType
_TmnxPimSnpgIfGrpSrcSrcAddrType_Object = MibTableColumn
tmnxPimSnpgIfGrpSrcSrcAddrType = _TmnxPimSnpgIfGrpSrcSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 4, 1, 3),
    _TmnxPimSnpgIfGrpSrcSrcAddrType_Type()
)
tmnxPimSnpgIfGrpSrcSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcSrcAddrType.setStatus("current")


class _TmnxPimSnpgIfGrpSrcSourceAddr_Type(InetAddress):
    """Custom type tmnxPimSnpgIfGrpSrcSourceAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPimSnpgIfGrpSrcSourceAddr_Type.__name__ = "InetAddress"
_TmnxPimSnpgIfGrpSrcSourceAddr_Object = MibTableColumn
tmnxPimSnpgIfGrpSrcSourceAddr = _TmnxPimSnpgIfGrpSrcSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 4, 1, 4),
    _TmnxPimSnpgIfGrpSrcSourceAddr_Type()
)
tmnxPimSnpgIfGrpSrcSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcSourceAddr.setStatus("current")


class _TmnxPimSnpgIfGrpSrcJPState_Type(Integer32):
    """Custom type tmnxPimSnpgIfGrpSrcJPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noInfo", 0),
          ("join", 1),
          ("prunePend", 2),
          ("pruned", 3))
    )


_TmnxPimSnpgIfGrpSrcJPState_Type.__name__ = "Integer32"
_TmnxPimSnpgIfGrpSrcJPState_Object = MibTableColumn
tmnxPimSnpgIfGrpSrcJPState = _TmnxPimSnpgIfGrpSrcJPState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 4, 1, 5),
    _TmnxPimSnpgIfGrpSrcJPState_Type()
)
tmnxPimSnpgIfGrpSrcJPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcJPState.setStatus("current")
_TmnxPimSnpgIfGrpSrcPrunePendTmr_Type = Unsigned32
_TmnxPimSnpgIfGrpSrcPrunePendTmr_Object = MibTableColumn
tmnxPimSnpgIfGrpSrcPrunePendTmr = _TmnxPimSnpgIfGrpSrcPrunePendTmr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 4, 1, 6),
    _TmnxPimSnpgIfGrpSrcPrunePendTmr_Type()
)
tmnxPimSnpgIfGrpSrcPrunePendTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcPrunePendTmr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcPrunePendTmr.setUnits("seconds")
_TmnxPimSnpgIfGrpSrcJPTimer_Type = Unsigned32
_TmnxPimSnpgIfGrpSrcJPTimer_Object = MibTableColumn
tmnxPimSnpgIfGrpSrcJPTimer = _TmnxPimSnpgIfGrpSrcJPTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 4, 1, 7),
    _TmnxPimSnpgIfGrpSrcJPTimer_Type()
)
tmnxPimSnpgIfGrpSrcJPTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcJPTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcJPTimer.setUnits("seconds")


class _TmnxPimSnpgIfGrpSrcJPRptState_Type(Integer32):
    """Custom type tmnxPimSnpgIfGrpSrcJPRptState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noInfo", 0),
          ("join", 1),
          ("prunePend", 2),
          ("pruned", 3))
    )


_TmnxPimSnpgIfGrpSrcJPRptState_Type.__name__ = "Integer32"
_TmnxPimSnpgIfGrpSrcJPRptState_Object = MibTableColumn
tmnxPimSnpgIfGrpSrcJPRptState = _TmnxPimSnpgIfGrpSrcJPRptState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 4, 1, 8),
    _TmnxPimSnpgIfGrpSrcJPRptState_Type()
)
tmnxPimSnpgIfGrpSrcJPRptState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcJPRptState.setStatus("current")
_TmnxPimSnpgIfGrpSrcRptPrnPndTmr_Type = Unsigned32
_TmnxPimSnpgIfGrpSrcRptPrnPndTmr_Object = MibTableColumn
tmnxPimSnpgIfGrpSrcRptPrnPndTmr = _TmnxPimSnpgIfGrpSrcRptPrnPndTmr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 4, 1, 9),
    _TmnxPimSnpgIfGrpSrcRptPrnPndTmr_Type()
)
tmnxPimSnpgIfGrpSrcRptPrnPndTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcRptPrnPndTmr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcRptPrnPndTmr.setUnits("seconds")
_TmnxPimSnpgIfGrpSrcRptJPTimer_Type = Unsigned32
_TmnxPimSnpgIfGrpSrcRptJPTimer_Object = MibTableColumn
tmnxPimSnpgIfGrpSrcRptJPTimer = _TmnxPimSnpgIfGrpSrcRptJPTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 4, 1, 10),
    _TmnxPimSnpgIfGrpSrcRptJPTimer_Type()
)
tmnxPimSnpgIfGrpSrcRptJPTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcRptJPTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcRptJPTimer.setUnits("seconds")
_TmnxPimSnpgIfGrpSrcUpTime_Type = Unsigned32
_TmnxPimSnpgIfGrpSrcUpTime_Object = MibTableColumn
tmnxPimSnpgIfGrpSrcUpTime = _TmnxPimSnpgIfGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 4, 1, 11),
    _TmnxPimSnpgIfGrpSrcUpTime_Type()
)
tmnxPimSnpgIfGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGrpSrcUpTime.setUnits("seconds")
_TmnxPimSnpgIfStatsTable_Object = MibTable
tmnxPimSnpgIfStatsTable = _TmnxPimSnpgIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5)
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfStatsTable.setStatus("current")
_TmnxPimSnpgIfStatsEntry_Object = MibTableRow
tmnxPimSnpgIfStatsEntry = _TmnxPimSnpgIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfStatsEntry.setStatus("current")
_TmnxPimSnpgIfTxPkts_Type = Counter32
_TmnxPimSnpgIfTxPkts_Object = MibTableColumn
tmnxPimSnpgIfTxPkts = _TmnxPimSnpgIfTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1, 1),
    _TmnxPimSnpgIfTxPkts_Type()
)
tmnxPimSnpgIfTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfTxPkts.setStatus("current")
_TmnxPimSnpgIfRxPkts_Type = Counter32
_TmnxPimSnpgIfRxPkts_Object = MibTableColumn
tmnxPimSnpgIfRxPkts = _TmnxPimSnpgIfRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1, 2),
    _TmnxPimSnpgIfRxPkts_Type()
)
tmnxPimSnpgIfRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfRxPkts.setStatus("current")
_TmnxPimSnpgIfRxHellos_Type = Counter32
_TmnxPimSnpgIfRxHellos_Object = MibTableColumn
tmnxPimSnpgIfRxHellos = _TmnxPimSnpgIfRxHellos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1, 3),
    _TmnxPimSnpgIfRxHellos_Type()
)
tmnxPimSnpgIfRxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfRxHellos.setStatus("current")
_TmnxPimSnpgIfRxHellosDropped_Type = Counter32
_TmnxPimSnpgIfRxHellosDropped_Object = MibTableColumn
tmnxPimSnpgIfRxHellosDropped = _TmnxPimSnpgIfRxHellosDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1, 4),
    _TmnxPimSnpgIfRxHellosDropped_Type()
)
tmnxPimSnpgIfRxHellosDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfRxHellosDropped.setStatus("current")
_TmnxPimSnpgIfRxNbrUnknown_Type = Counter32
_TmnxPimSnpgIfRxNbrUnknown_Object = MibTableColumn
tmnxPimSnpgIfRxNbrUnknown = _TmnxPimSnpgIfRxNbrUnknown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1, 5),
    _TmnxPimSnpgIfRxNbrUnknown_Type()
)
tmnxPimSnpgIfRxNbrUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfRxNbrUnknown.setStatus("current")
_TmnxPimSnpgIfRxBadChecksumDscrd_Type = Counter32
_TmnxPimSnpgIfRxBadChecksumDscrd_Object = MibTableColumn
tmnxPimSnpgIfRxBadChecksumDscrd = _TmnxPimSnpgIfRxBadChecksumDscrd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1, 6),
    _TmnxPimSnpgIfRxBadChecksumDscrd_Type()
)
tmnxPimSnpgIfRxBadChecksumDscrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfRxBadChecksumDscrd.setStatus("current")
_TmnxPimSnpgIfRxBadVersionDscrd_Type = Counter32
_TmnxPimSnpgIfRxBadVersionDscrd_Object = MibTableColumn
tmnxPimSnpgIfRxBadVersionDscrd = _TmnxPimSnpgIfRxBadVersionDscrd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1, 7),
    _TmnxPimSnpgIfRxBadVersionDscrd_Type()
)
tmnxPimSnpgIfRxBadVersionDscrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfRxBadVersionDscrd.setStatus("current")
_TmnxPimSnpgIfRxBadEncodings_Type = Counter32
_TmnxPimSnpgIfRxBadEncodings_Object = MibTableColumn
tmnxPimSnpgIfRxBadEncodings = _TmnxPimSnpgIfRxBadEncodings_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1, 8),
    _TmnxPimSnpgIfRxBadEncodings_Type()
)
tmnxPimSnpgIfRxBadEncodings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfRxBadEncodings.setStatus("current")
_TmnxPimSnpgIfStarGTypes_Type = Gauge32
_TmnxPimSnpgIfStarGTypes_Object = MibTableColumn
tmnxPimSnpgIfStarGTypes = _TmnxPimSnpgIfStarGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1, 9),
    _TmnxPimSnpgIfStarGTypes_Type()
)
tmnxPimSnpgIfStarGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfStarGTypes.setStatus("current")
_TmnxPimSnpgIfSGTypes_Type = Gauge32
_TmnxPimSnpgIfSGTypes_Object = MibTableColumn
tmnxPimSnpgIfSGTypes = _TmnxPimSnpgIfSGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1, 10),
    _TmnxPimSnpgIfSGTypes_Type()
)
tmnxPimSnpgIfSGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfSGTypes.setStatus("current")
_TmnxPimSnpgIfJoinPolicyDrops_Type = Counter32
_TmnxPimSnpgIfJoinPolicyDrops_Object = MibTableColumn
tmnxPimSnpgIfJoinPolicyDrops = _TmnxPimSnpgIfJoinPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1, 11),
    _TmnxPimSnpgIfJoinPolicyDrops_Type()
)
tmnxPimSnpgIfJoinPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfJoinPolicyDrops.setStatus("current")
_TmnxPimSnpgIfTxJoinPrunes_Type = Counter32
_TmnxPimSnpgIfTxJoinPrunes_Object = MibTableColumn
tmnxPimSnpgIfTxJoinPrunes = _TmnxPimSnpgIfTxJoinPrunes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1, 12),
    _TmnxPimSnpgIfTxJoinPrunes_Type()
)
tmnxPimSnpgIfTxJoinPrunes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfTxJoinPrunes.setStatus("current")
_TmnxPimSnpgIfRxJoinPrunes_Type = Counter32
_TmnxPimSnpgIfRxJoinPrunes_Object = MibTableColumn
tmnxPimSnpgIfRxJoinPrunes = _TmnxPimSnpgIfRxJoinPrunes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1, 13),
    _TmnxPimSnpgIfRxJoinPrunes_Type()
)
tmnxPimSnpgIfRxJoinPrunes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfRxJoinPrunes.setStatus("current")
_TmnxPimSnpgIfRxJoinPruneErrs_Type = Counter32
_TmnxPimSnpgIfRxJoinPruneErrs_Object = MibTableColumn
tmnxPimSnpgIfRxJoinPruneErrs = _TmnxPimSnpgIfRxJoinPruneErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 5, 1, 14),
    _TmnxPimSnpgIfRxJoinPruneErrs_Type()
)
tmnxPimSnpgIfRxJoinPruneErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfRxJoinPruneErrs.setStatus("current")
_TmnxPimSnpgIfSecNbrTblLstChanged_Type = TimeStamp
_TmnxPimSnpgIfSecNbrTblLstChanged_Object = MibScalar
tmnxPimSnpgIfSecNbrTblLstChanged = _TmnxPimSnpgIfSecNbrTblLstChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 6),
    _TmnxPimSnpgIfSecNbrTblLstChanged_Type()
)
tmnxPimSnpgIfSecNbrTblLstChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfSecNbrTblLstChanged.setStatus("current")
_TmnxPimSnpgIfSecNbrTable_Object = MibTable
tmnxPimSnpgIfSecNbrTable = _TmnxPimSnpgIfSecNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 7)
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfSecNbrTable.setStatus("current")
_TmnxPimSnpgIfSecNbrEntry_Object = MibTableRow
tmnxPimSnpgIfSecNbrEntry = _TmnxPimSnpgIfSecNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 7, 1)
)
tmnxPimSnpgIfSecNbrEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgPortId"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgEncapValue"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrAddress"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfSecNbrAddrType"),
    (0, "TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfSecNbrAddress"),
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfSecNbrEntry.setStatus("current")
_TmnxPimSnpgIfSecNbrAddrType_Type = InetAddressType
_TmnxPimSnpgIfSecNbrAddrType_Object = MibTableColumn
tmnxPimSnpgIfSecNbrAddrType = _TmnxPimSnpgIfSecNbrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 7, 1, 1),
    _TmnxPimSnpgIfSecNbrAddrType_Type()
)
tmnxPimSnpgIfSecNbrAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfSecNbrAddrType.setStatus("current")


class _TmnxPimSnpgIfSecNbrAddress_Type(InetAddress):
    """Custom type tmnxPimSnpgIfSecNbrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPimSnpgIfSecNbrAddress_Type.__name__ = "InetAddress"
_TmnxPimSnpgIfSecNbrAddress_Object = MibTableColumn
tmnxPimSnpgIfSecNbrAddress = _TmnxPimSnpgIfSecNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 2, 7, 1, 2),
    _TmnxPimSnpgIfSecNbrAddress_Type()
)
tmnxPimSnpgIfSecNbrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPimSnpgIfSecNbrAddress.setStatus("current")
_TmnxPimSnpgNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxPimSnpgNotificationObjs = _TmnxPimSnpgNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 53, 3)
)
_TmnxPimSnpgNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxPimSnpgNotifyPrefix = _TmnxPimSnpgNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 53)
)
_TmnxPimSnpgNotifications_ObjectIdentity = ObjectIdentity
tmnxPimSnpgNotifications = _TmnxPimSnpgNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 53, 0)
)
tmnxPimSnpgGeneralEntry.registerAugmentions(
    ("TIMETRA-PIM-SNOOPING-MIB",
     "tmnxPimSnpgGenStatsEntry")
)
tmnxPimSnpgGenStatsEntry.setIndexNames(*tmnxPimSnpgGeneralEntry.getIndexNames())
tmnxPimSnpgGrpSrcEntry.registerAugmentions(
    ("TIMETRA-PIM-SNOOPING-MIB",
     "tmnxPimSnpgGrpSrcStatsEntry")
)
tmnxPimSnpgGrpSrcStatsEntry.setIndexNames(*tmnxPimSnpgGrpSrcEntry.getIndexNames())
tmnxPimSnpgIfEntry.registerAugmentions(
    ("TIMETRA-PIM-SNOOPING-MIB",
     "tmnxPimSnpgIfStatsEntry")
)
tmnxPimSnpgIfStatsEntry.setIndexNames(*tmnxPimSnpgIfEntry.getIndexNames())

# Managed Objects groups

tmnxPimSnpgGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53, 2, 1)
)
tmnxPimSnpgGlobalGroup.setObjects(
      *(("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenTableLstChanged"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenRowStatus"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenRowLastChanged"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenAdminState"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenOperState"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenHoldTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenDRType"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenDR"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenTrackingSupport"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenUpTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenMode"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenGroupPolicy1"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenGroupPolicy2"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenGroupPolicy3"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenGroupPolicy4"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenGroupPolicy5"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcRpfNbrAddrType"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcRpfNbrAddr"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcRpfIfIndex"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcRptRpfNbrAdrTp"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcRptRpfNbrAddr"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcUstrmJpState"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcUstrmJpTimer"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcUstrmRptJpSt"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcUstrmRptOvdTmr"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcNumJoinOif"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcNumImdiateOif"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcNumInhritedOif"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcNumInherRptOif"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcNumIif"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcUpTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcIfFlags"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenStatsStarGTypes"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenStatsSGTypes"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcStatsFwdedPkts"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGrpSrcStatsFwdedOct"))
)
if mibBuilder.loadTexts:
    tmnxPimSnpgGlobalGroup.setStatus("current")

tmnxPimSnpgIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53, 2, 2)
)
tmnxPimSnpgIfGroup.setObjects(
      *(("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfTableLastChanged"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfLastChangeTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfOperState"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfUpTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfMaxGroups"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfCurrentGroups"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfMaxGroupsTillNow"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrUpTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrExpiryTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrGenId"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrDrPriority"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrDrPriorPresent"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrLanDelay"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrLanDlayPrsnt"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrTrckngSpprt"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrHoldTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrOvrdeIntrvl"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfGrpSrcJPState"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfGrpSrcPrunePendTmr"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfGrpSrcJPTimer"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfGrpSrcJPRptState"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfGrpSrcRptPrnPndTmr"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfGrpSrcRptJPTimer"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfGrpSrcUpTime"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfTxPkts"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfRxPkts"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfRxHellos"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfRxHellosDropped"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfRxNbrUnknown"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfRxBadChecksumDscrd"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfRxBadVersionDscrd"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfRxBadEncodings"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfStarGTypes"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfSGTypes"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfJoinPolicyDrops"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfTxJoinPrunes"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfRxJoinPrunes"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfRxJoinPruneErrs"))
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfGroup.setStatus("current")

tmnxPimSnpgIfSecNbrV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53, 2, 4)
)
tmnxPimSnpgIfSecNbrV6v0Group.setObjects(
      *(("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfSecNbrTblLstChanged"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfSecNbrAddrType"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfSecNbrAddress"))
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfSecNbrV6v0Group.setStatus("current")


# Notification objects

tmnxPimSnpgIfNeighborLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 53, 0, 1)
)
tmnxPimSnpgIfNeighborLoss.setObjects(
    ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrUpTime")
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNeighborLoss.setStatus(
        "current"
    )

tmnxPimSnpgIfNeighborUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 53, 0, 2)
)
tmnxPimSnpgIfNeighborUp.setObjects(
    ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNbrUpTime")
)
if mibBuilder.loadTexts:
    tmnxPimSnpgIfNeighborUp.setStatus(
        "current"
    )

tmnxPimSnpgSGLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 53, 0, 3)
)
tmnxPimSnpgSGLimitExceeded.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxCardHwIndex")
)
if mibBuilder.loadTexts:
    tmnxPimSnpgSGLimitExceeded.setStatus(
        "current"
    )

tmnxPimSnpgSnoopModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 53, 0, 4)
)
tmnxPimSnpgSnoopModeChanged.setObjects(
      *(("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenOperState"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGenMode"))
)
if mibBuilder.loadTexts:
    tmnxPimSnpgSnoopModeChanged.setStatus(
        "current"
    )


# Notifications groups

tmnxPimSnpgNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53, 2, 3)
)
tmnxPimSnpgNotificationGroup.setObjects(
      *(("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNeighborLoss"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfNeighborUp"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgSGLimitExceeded"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgSnoopModeChanged"))
)
if mibBuilder.loadTexts:
    tmnxPimSnpgNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxPimSnpgCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 53, 1, 1)
)
tmnxPimSnpgCompliance.setObjects(
      *(("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgGlobalGroup"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfGroup"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgNotificationGroup"),
        ("TIMETRA-PIM-SNOOPING-MIB", "tmnxPimSnpgIfSecNbrV6v0Group"))
)
if mibBuilder.loadTexts:
    tmnxPimSnpgCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-PIM-SNOOPING-MIB",
    **{"TmnxPimSnpgOperState": TmnxPimSnpgOperState,
       "timetraPimSnoopingMIBModule": timetraPimSnoopingMIBModule,
       "tmnxPimSnpgConformance": tmnxPimSnpgConformance,
       "tmnxPimSnpgCompliances": tmnxPimSnpgCompliances,
       "tmnxPimSnpgCompliance": tmnxPimSnpgCompliance,
       "tmnxPimSnpgGroups": tmnxPimSnpgGroups,
       "tmnxPimSnpgGlobalGroup": tmnxPimSnpgGlobalGroup,
       "tmnxPimSnpgIfGroup": tmnxPimSnpgIfGroup,
       "tmnxPimSnpgNotificationGroup": tmnxPimSnpgNotificationGroup,
       "tmnxPimSnpgIfSecNbrV6v0Group": tmnxPimSnpgIfSecNbrV6v0Group,
       "tmnxPimSnpgObjs": tmnxPimSnpgObjs,
       "tmnxPimSnpgProtocolObjs": tmnxPimSnpgProtocolObjs,
       "tmnxPimSnpgGenTableLstChanged": tmnxPimSnpgGenTableLstChanged,
       "tmnxPimSnpgGeneralTable": tmnxPimSnpgGeneralTable,
       "tmnxPimSnpgGeneralEntry": tmnxPimSnpgGeneralEntry,
       "tmnxPimSnpgGenRowStatus": tmnxPimSnpgGenRowStatus,
       "tmnxPimSnpgGenRowLastChanged": tmnxPimSnpgGenRowLastChanged,
       "tmnxPimSnpgGenAdminState": tmnxPimSnpgGenAdminState,
       "tmnxPimSnpgGenOperState": tmnxPimSnpgGenOperState,
       "tmnxPimSnpgGenHoldTime": tmnxPimSnpgGenHoldTime,
       "tmnxPimSnpgGenDRType": tmnxPimSnpgGenDRType,
       "tmnxPimSnpgGenDR": tmnxPimSnpgGenDR,
       "tmnxPimSnpgGenTrackingSupport": tmnxPimSnpgGenTrackingSupport,
       "tmnxPimSnpgGenUpTime": tmnxPimSnpgGenUpTime,
       "tmnxPimSnpgGenMode": tmnxPimSnpgGenMode,
       "tmnxPimSnpgGenGroupPolicy1": tmnxPimSnpgGenGroupPolicy1,
       "tmnxPimSnpgGenGroupPolicy2": tmnxPimSnpgGenGroupPolicy2,
       "tmnxPimSnpgGenGroupPolicy3": tmnxPimSnpgGenGroupPolicy3,
       "tmnxPimSnpgGenGroupPolicy4": tmnxPimSnpgGenGroupPolicy4,
       "tmnxPimSnpgGenGroupPolicy5": tmnxPimSnpgGenGroupPolicy5,
       "tmnxPimSnpgGrpSrcTable": tmnxPimSnpgGrpSrcTable,
       "tmnxPimSnpgGrpSrcEntry": tmnxPimSnpgGrpSrcEntry,
       "tmnxPimSnpgGrpSrcGrpAddrType": tmnxPimSnpgGrpSrcGrpAddrType,
       "tmnxPimSnpgGrpSrcGroupAddress": tmnxPimSnpgGrpSrcGroupAddress,
       "tmnxPimSnpgGrpSrcSrcAddrType": tmnxPimSnpgGrpSrcSrcAddrType,
       "tmnxPimSnpgGrpSrcSourceAddress": tmnxPimSnpgGrpSrcSourceAddress,
       "tmnxPimSnpgGrpSrcRpfNbrAddrType": tmnxPimSnpgGrpSrcRpfNbrAddrType,
       "tmnxPimSnpgGrpSrcRpfNbrAddr": tmnxPimSnpgGrpSrcRpfNbrAddr,
       "tmnxPimSnpgGrpSrcRpfIfIndex": tmnxPimSnpgGrpSrcRpfIfIndex,
       "tmnxPimSnpgGrpSrcRptRpfNbrAdrTp": tmnxPimSnpgGrpSrcRptRpfNbrAdrTp,
       "tmnxPimSnpgGrpSrcRptRpfNbrAddr": tmnxPimSnpgGrpSrcRptRpfNbrAddr,
       "tmnxPimSnpgGrpSrcUstrmJpState": tmnxPimSnpgGrpSrcUstrmJpState,
       "tmnxPimSnpgGrpSrcUstrmJpTimer": tmnxPimSnpgGrpSrcUstrmJpTimer,
       "tmnxPimSnpgGrpSrcUstrmRptJpSt": tmnxPimSnpgGrpSrcUstrmRptJpSt,
       "tmnxPimSnpgGrpSrcUstrmRptOvdTmr": tmnxPimSnpgGrpSrcUstrmRptOvdTmr,
       "tmnxPimSnpgGrpSrcNumJoinOif": tmnxPimSnpgGrpSrcNumJoinOif,
       "tmnxPimSnpgGrpSrcNumImdiateOif": tmnxPimSnpgGrpSrcNumImdiateOif,
       "tmnxPimSnpgGrpSrcNumInhritedOif": tmnxPimSnpgGrpSrcNumInhritedOif,
       "tmnxPimSnpgGrpSrcNumInherRptOif": tmnxPimSnpgGrpSrcNumInherRptOif,
       "tmnxPimSnpgGrpSrcNumIif": tmnxPimSnpgGrpSrcNumIif,
       "tmnxPimSnpgGrpSrcUpTime": tmnxPimSnpgGrpSrcUpTime,
       "tmnxPimSnpgGrpSrcIfTable": tmnxPimSnpgGrpSrcIfTable,
       "tmnxPimSnpgGrpSrcIfEntry": tmnxPimSnpgGrpSrcIfEntry,
       "tmnxPimSnpgPortId": tmnxPimSnpgPortId,
       "tmnxPimSnpgEncapValue": tmnxPimSnpgEncapValue,
       "tmnxPimSnpgGrpSrcIfFlags": tmnxPimSnpgGrpSrcIfFlags,
       "tmnxPimSnpgGenStatsTable": tmnxPimSnpgGenStatsTable,
       "tmnxPimSnpgGenStatsEntry": tmnxPimSnpgGenStatsEntry,
       "tmnxPimSnpgGenStatsStarGTypes": tmnxPimSnpgGenStatsStarGTypes,
       "tmnxPimSnpgGenStatsSGTypes": tmnxPimSnpgGenStatsSGTypes,
       "tmnxPimSnpgGrpSrcStatsTable": tmnxPimSnpgGrpSrcStatsTable,
       "tmnxPimSnpgGrpSrcStatsEntry": tmnxPimSnpgGrpSrcStatsEntry,
       "tmnxPimSnpgGrpSrcStatsFwdedPkts": tmnxPimSnpgGrpSrcStatsFwdedPkts,
       "tmnxPimSnpgGrpSrcStatsFwdedOct": tmnxPimSnpgGrpSrcStatsFwdedOct,
       "tmnxPimSnpgIfObjs": tmnxPimSnpgIfObjs,
       "tmnxPimSnpgIfTableLastChanged": tmnxPimSnpgIfTableLastChanged,
       "tmnxPimSnpgIfTable": tmnxPimSnpgIfTable,
       "tmnxPimSnpgIfEntry": tmnxPimSnpgIfEntry,
       "tmnxPimSnpgIfLastChangeTime": tmnxPimSnpgIfLastChangeTime,
       "tmnxPimSnpgIfOperState": tmnxPimSnpgIfOperState,
       "tmnxPimSnpgIfUpTime": tmnxPimSnpgIfUpTime,
       "tmnxPimSnpgIfMaxGroups": tmnxPimSnpgIfMaxGroups,
       "tmnxPimSnpgIfCurrentGroups": tmnxPimSnpgIfCurrentGroups,
       "tmnxPimSnpgIfMaxGroupsTillNow": tmnxPimSnpgIfMaxGroupsTillNow,
       "tmnxPimSnpgIfNbrTable": tmnxPimSnpgIfNbrTable,
       "tmnxPimSnpgIfNbrEntry": tmnxPimSnpgIfNbrEntry,
       "tmnxPimSnpgIfNbrAddrType": tmnxPimSnpgIfNbrAddrType,
       "tmnxPimSnpgIfNbrAddress": tmnxPimSnpgIfNbrAddress,
       "tmnxPimSnpgIfNbrUpTime": tmnxPimSnpgIfNbrUpTime,
       "tmnxPimSnpgIfNbrExpiryTime": tmnxPimSnpgIfNbrExpiryTime,
       "tmnxPimSnpgIfNbrGenId": tmnxPimSnpgIfNbrGenId,
       "tmnxPimSnpgIfNbrDrPriority": tmnxPimSnpgIfNbrDrPriority,
       "tmnxPimSnpgIfNbrDrPriorPresent": tmnxPimSnpgIfNbrDrPriorPresent,
       "tmnxPimSnpgIfNbrLanDelay": tmnxPimSnpgIfNbrLanDelay,
       "tmnxPimSnpgIfNbrLanDlayPrsnt": tmnxPimSnpgIfNbrLanDlayPrsnt,
       "tmnxPimSnpgIfNbrTrckngSpprt": tmnxPimSnpgIfNbrTrckngSpprt,
       "tmnxPimSnpgIfNbrHoldTime": tmnxPimSnpgIfNbrHoldTime,
       "tmnxPimSnpgIfNbrOvrdeIntrvl": tmnxPimSnpgIfNbrOvrdeIntrvl,
       "tmnxPimSnpgIfGrpSrcTable": tmnxPimSnpgIfGrpSrcTable,
       "tmnxPimSnpgIfGrpSrcEntry": tmnxPimSnpgIfGrpSrcEntry,
       "tmnxPimSnpgIfGrpSrcGrpAddrType": tmnxPimSnpgIfGrpSrcGrpAddrType,
       "tmnxPimSnpgIfGrpSrcGroupAddr": tmnxPimSnpgIfGrpSrcGroupAddr,
       "tmnxPimSnpgIfGrpSrcSrcAddrType": tmnxPimSnpgIfGrpSrcSrcAddrType,
       "tmnxPimSnpgIfGrpSrcSourceAddr": tmnxPimSnpgIfGrpSrcSourceAddr,
       "tmnxPimSnpgIfGrpSrcJPState": tmnxPimSnpgIfGrpSrcJPState,
       "tmnxPimSnpgIfGrpSrcPrunePendTmr": tmnxPimSnpgIfGrpSrcPrunePendTmr,
       "tmnxPimSnpgIfGrpSrcJPTimer": tmnxPimSnpgIfGrpSrcJPTimer,
       "tmnxPimSnpgIfGrpSrcJPRptState": tmnxPimSnpgIfGrpSrcJPRptState,
       "tmnxPimSnpgIfGrpSrcRptPrnPndTmr": tmnxPimSnpgIfGrpSrcRptPrnPndTmr,
       "tmnxPimSnpgIfGrpSrcRptJPTimer": tmnxPimSnpgIfGrpSrcRptJPTimer,
       "tmnxPimSnpgIfGrpSrcUpTime": tmnxPimSnpgIfGrpSrcUpTime,
       "tmnxPimSnpgIfStatsTable": tmnxPimSnpgIfStatsTable,
       "tmnxPimSnpgIfStatsEntry": tmnxPimSnpgIfStatsEntry,
       "tmnxPimSnpgIfTxPkts": tmnxPimSnpgIfTxPkts,
       "tmnxPimSnpgIfRxPkts": tmnxPimSnpgIfRxPkts,
       "tmnxPimSnpgIfRxHellos": tmnxPimSnpgIfRxHellos,
       "tmnxPimSnpgIfRxHellosDropped": tmnxPimSnpgIfRxHellosDropped,
       "tmnxPimSnpgIfRxNbrUnknown": tmnxPimSnpgIfRxNbrUnknown,
       "tmnxPimSnpgIfRxBadChecksumDscrd": tmnxPimSnpgIfRxBadChecksumDscrd,
       "tmnxPimSnpgIfRxBadVersionDscrd": tmnxPimSnpgIfRxBadVersionDscrd,
       "tmnxPimSnpgIfRxBadEncodings": tmnxPimSnpgIfRxBadEncodings,
       "tmnxPimSnpgIfStarGTypes": tmnxPimSnpgIfStarGTypes,
       "tmnxPimSnpgIfSGTypes": tmnxPimSnpgIfSGTypes,
       "tmnxPimSnpgIfJoinPolicyDrops": tmnxPimSnpgIfJoinPolicyDrops,
       "tmnxPimSnpgIfTxJoinPrunes": tmnxPimSnpgIfTxJoinPrunes,
       "tmnxPimSnpgIfRxJoinPrunes": tmnxPimSnpgIfRxJoinPrunes,
       "tmnxPimSnpgIfRxJoinPruneErrs": tmnxPimSnpgIfRxJoinPruneErrs,
       "tmnxPimSnpgIfSecNbrTblLstChanged": tmnxPimSnpgIfSecNbrTblLstChanged,
       "tmnxPimSnpgIfSecNbrTable": tmnxPimSnpgIfSecNbrTable,
       "tmnxPimSnpgIfSecNbrEntry": tmnxPimSnpgIfSecNbrEntry,
       "tmnxPimSnpgIfSecNbrAddrType": tmnxPimSnpgIfSecNbrAddrType,
       "tmnxPimSnpgIfSecNbrAddress": tmnxPimSnpgIfSecNbrAddress,
       "tmnxPimSnpgNotificationObjs": tmnxPimSnpgNotificationObjs,
       "tmnxPimSnpgNotifyPrefix": tmnxPimSnpgNotifyPrefix,
       "tmnxPimSnpgNotifications": tmnxPimSnpgNotifications,
       "tmnxPimSnpgIfNeighborLoss": tmnxPimSnpgIfNeighborLoss,
       "tmnxPimSnpgIfNeighborUp": tmnxPimSnpgIfNeighborUp,
       "tmnxPimSnpgSGLimitExceeded": tmnxPimSnpgSGLimitExceeded,
       "tmnxPimSnpgSnoopModeChanged": tmnxPimSnpgSnoopModeChanged}
)
