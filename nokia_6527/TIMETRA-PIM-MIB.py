# SNMP MIB module (TIMETRA-PIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-PIM-MIB.mib
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

(timetraSRMIBModules,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(IpAddressPrefixLength,
 TNamedItemOrEmpty,
 TmnxAdminState,
 TmnxOperState) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "IpAddressPrefixLength",
    "TNamedItemOrEmpty",
    "TmnxAdminState",
    "TmnxOperState")

(vRtrID,
 vRtrIfIndex) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrIfIndex")


# MODULE-IDENTITY

timetraPimMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 24)
)
if mibBuilder.loadTexts:
    timetraPimMIBModule.setRevisions(
        ("1904-01-15 00:00",
         "1903-10-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxPimObjs_ObjectIdentity = ObjectIdentity
tmnxPimObjs = _TmnxPimObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24)
)
_VRtrPimProtocolObjs_ObjectIdentity = ObjectIdentity
vRtrPimProtocolObjs = _VRtrPimProtocolObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1)
)
_VRtrPimGeneralTable_Object = MibTable
vRtrPimGeneralTable = _VRtrPimGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 1)
)
if mibBuilder.loadTexts:
    vRtrPimGeneralTable.setStatus("current")
_VRtrPimGeneralEntry_Object = MibTableRow
vRtrPimGeneralEntry = _VRtrPimGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 1, 1)
)
vRtrPimGeneralEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    vRtrPimGeneralEntry.setStatus("current")


class _VRtrPimGenAdminState_Type(TmnxAdminState):
    """Custom type vRtrPimGenAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrPimGenAdminState_Type.__name__ = "TmnxAdminState"
_VRtrPimGenAdminState_Object = MibTableColumn
vRtrPimGenAdminState = _VRtrPimGenAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 1, 1, 1),
    _VRtrPimGenAdminState_Type()
)
vRtrPimGenAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimGenAdminState.setStatus("current")
_VRtrPimGenOperState_Type = TmnxOperState
_VRtrPimGenOperState_Object = MibTableColumn
vRtrPimGenOperState = _VRtrPimGenOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 1, 1, 2),
    _VRtrPimGenOperState_Type()
)
vRtrPimGenOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGenOperState.setStatus("current")


class _VRtrPimGenCBSRPriority_Type(Integer32):
    """Custom type vRtrPimGenCBSRPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrPimGenCBSRPriority_Type.__name__ = "Integer32"
_VRtrPimGenCBSRPriority_Object = MibTableColumn
vRtrPimGenCBSRPriority = _VRtrPimGenCBSRPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 1, 1, 3),
    _VRtrPimGenCBSRPriority_Type()
)
vRtrPimGenCBSRPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimGenCBSRPriority.setStatus("current")


class _VRtrPimGenCBSRAddress_Type(IpAddress):
    """Custom type vRtrPimGenCBSRAddress based on IpAddress"""
    defaultHexValue = "00000000"


_VRtrPimGenCBSRAddress_Type.__name__ = "IpAddress"
_VRtrPimGenCBSRAddress_Object = MibTableColumn
vRtrPimGenCBSRAddress = _VRtrPimGenCBSRAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 1, 1, 4),
    _VRtrPimGenCBSRAddress_Type()
)
vRtrPimGenCBSRAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimGenCBSRAddress.setStatus("current")
_VRtrPimGenCBSRAdminState_Type = TmnxAdminState
_VRtrPimGenCBSRAdminState_Object = MibTableColumn
vRtrPimGenCBSRAdminState = _VRtrPimGenCBSRAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 1, 1, 5),
    _VRtrPimGenCBSRAdminState_Type()
)
vRtrPimGenCBSRAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimGenCBSRAdminState.setStatus("current")
_VRtrPimGenCBSROperState_Type = TmnxOperState
_VRtrPimGenCBSROperState_Object = MibTableColumn
vRtrPimGenCBSROperState = _VRtrPimGenCBSROperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 1, 1, 6),
    _VRtrPimGenCBSROperState_Type()
)
vRtrPimGenCBSROperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGenCBSROperState.setStatus("current")
_VRtrPimGenBSRAddress_Type = IpAddress
_VRtrPimGenBSRAddress_Object = MibTableColumn
vRtrPimGenBSRAddress = _VRtrPimGenBSRAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 1, 1, 7),
    _VRtrPimGenBSRAddress_Type()
)
vRtrPimGenBSRAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGenBSRAddress.setStatus("current")


class _VRtrPimGenBSRPriority_Type(Integer32):
    """Custom type vRtrPimGenBSRPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrPimGenBSRPriority_Type.__name__ = "Integer32"
_VRtrPimGenBSRPriority_Object = MibTableColumn
vRtrPimGenBSRPriority = _VRtrPimGenBSRPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 1, 1, 8),
    _VRtrPimGenBSRPriority_Type()
)
vRtrPimGenBSRPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGenBSRPriority.setStatus("current")
_VRtrPimGenBSRExpiryTime_Type = Unsigned32
_VRtrPimGenBSRExpiryTime_Object = MibTableColumn
vRtrPimGenBSRExpiryTime = _VRtrPimGenBSRExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 1, 1, 9),
    _VRtrPimGenBSRExpiryTime_Type()
)
vRtrPimGenBSRExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGenBSRExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimGenBSRExpiryTime.setUnits("seconds")


class _VRtrPimGenBSRState_Type(Integer32):
    """Custom type vRtrPimGenBSRState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("candidateBSR", 1),
          ("pendingBSR", 2),
          ("electedBSR", 3),
          ("acceptAny", 4),
          ("acceptPreferred", 5))
    )


_VRtrPimGenBSRState_Type.__name__ = "Integer32"
_VRtrPimGenBSRState_Object = MibTableColumn
vRtrPimGenBSRState = _VRtrPimGenBSRState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 1, 1, 10),
    _VRtrPimGenBSRState_Type()
)
vRtrPimGenBSRState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGenBSRState.setStatus("current")
_VRtrPimGenBSRUpTime_Type = Unsigned32
_VRtrPimGenBSRUpTime_Object = MibTableColumn
vRtrPimGenBSRUpTime = _VRtrPimGenBSRUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 1, 1, 11),
    _VRtrPimGenBSRUpTime_Type()
)
vRtrPimGenBSRUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGenBSRUpTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimGenBSRUpTime.setUnits("seconds")
_VRtrPimGenCRPAddress_Type = IpAddress
_VRtrPimGenCRPAddress_Object = MibTableColumn
vRtrPimGenCRPAddress = _VRtrPimGenCRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 1, 1, 12),
    _VRtrPimGenCRPAddress_Type()
)
vRtrPimGenCRPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimGenCRPAddress.setStatus("current")
_VRtrPimGenCRPAdminState_Type = TmnxAdminState
_VRtrPimGenCRPAdminState_Object = MibTableColumn
vRtrPimGenCRPAdminState = _VRtrPimGenCRPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 1, 1, 13),
    _VRtrPimGenCRPAdminState_Type()
)
vRtrPimGenCRPAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimGenCRPAdminState.setStatus("current")
_VRtrPimGenCRPOperState_Type = TmnxOperState
_VRtrPimGenCRPOperState_Object = MibTableColumn
vRtrPimGenCRPOperState = _VRtrPimGenCRPOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 1, 1, 14),
    _VRtrPimGenCRPOperState_Type()
)
vRtrPimGenCRPOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGenCRPOperState.setStatus("current")


class _VRtrPimGenCRPHoldtime_Type(Integer32):
    """Custom type vRtrPimGenCRPHoldtime based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_VRtrPimGenCRPHoldtime_Type.__name__ = "Integer32"
_VRtrPimGenCRPHoldtime_Object = MibTableColumn
vRtrPimGenCRPHoldtime = _VRtrPimGenCRPHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 1, 1, 15),
    _VRtrPimGenCRPHoldtime_Type()
)
vRtrPimGenCRPHoldtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimGenCRPHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimGenCRPHoldtime.setUnits("seconds")


class _VRtrPimGenCRPPriority_Type(Integer32):
    """Custom type vRtrPimGenCRPPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrPimGenCRPPriority_Type.__name__ = "Integer32"
_VRtrPimGenCRPPriority_Object = MibTableColumn
vRtrPimGenCRPPriority = _VRtrPimGenCRPPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 1, 1, 16),
    _VRtrPimGenCRPPriority_Type()
)
vRtrPimGenCRPPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimGenCRPPriority.setStatus("current")
_VRtrPimGenLastChange_Type = TimeStamp
_VRtrPimGenLastChange_Object = MibTableColumn
vRtrPimGenLastChange = _VRtrPimGenLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 1, 1, 17),
    _VRtrPimGenLastChange_Type()
)
vRtrPimGenLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGenLastChange.setStatus("current")
_VRtrPimStaticGrpToRPTable_Object = MibTable
vRtrPimStaticGrpToRPTable = _VRtrPimStaticGrpToRPTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 2)
)
if mibBuilder.loadTexts:
    vRtrPimStaticGrpToRPTable.setStatus("current")
_VRtrPimStaticGrpToRPEntry_Object = MibTableRow
vRtrPimStaticGrpToRPEntry = _VRtrPimStaticGrpToRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 2, 1)
)
vRtrPimStaticGrpToRPEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-MIB", "vRtrPimStaticGrpToRPRPAddress"),
    (0, "TIMETRA-PIM-MIB", "vRtrPimStaticGroupAddr"),
    (0, "TIMETRA-PIM-MIB", "vRtrPimStaticGroupMask"),
)
if mibBuilder.loadTexts:
    vRtrPimStaticGrpToRPEntry.setStatus("current")
_VRtrPimStaticGrpToRPRPAddress_Type = IpAddress
_VRtrPimStaticGrpToRPRPAddress_Object = MibTableColumn
vRtrPimStaticGrpToRPRPAddress = _VRtrPimStaticGrpToRPRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 2, 1, 1),
    _VRtrPimStaticGrpToRPRPAddress_Type()
)
vRtrPimStaticGrpToRPRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimStaticGrpToRPRPAddress.setStatus("current")
_VRtrPimStaticGroupAddr_Type = IpAddress
_VRtrPimStaticGroupAddr_Object = MibTableColumn
vRtrPimStaticGroupAddr = _VRtrPimStaticGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 2, 1, 2),
    _VRtrPimStaticGroupAddr_Type()
)
vRtrPimStaticGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimStaticGroupAddr.setStatus("current")
_VRtrPimStaticGroupMask_Type = IpAddressPrefixLength
_VRtrPimStaticGroupMask_Object = MibTableColumn
vRtrPimStaticGroupMask = _VRtrPimStaticGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 2, 1, 3),
    _VRtrPimStaticGroupMask_Type()
)
vRtrPimStaticGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimStaticGroupMask.setStatus("current")
_VRtrPimStaticGrpToRPRowStatus_Type = RowStatus
_VRtrPimStaticGrpToRPRowStatus_Object = MibTableColumn
vRtrPimStaticGrpToRPRowStatus = _VRtrPimStaticGrpToRPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 2, 1, 4),
    _VRtrPimStaticGrpToRPRowStatus_Type()
)
vRtrPimStaticGrpToRPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimStaticGrpToRPRowStatus.setStatus("current")
_VRtrPimGrpSrcTable_Object = MibTable
vRtrPimGrpSrcTable = _VRtrPimGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 3)
)
if mibBuilder.loadTexts:
    vRtrPimGrpSrcTable.setStatus("current")
_VRtrPimGrpSrcEntry_Object = MibTableRow
vRtrPimGrpSrcEntry = _VRtrPimGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 3, 1)
)
vRtrPimGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-MIB", "vRtrPimGrpSrcGroupAddress"),
    (0, "TIMETRA-PIM-MIB", "vRtrPimGrpSrcSourceAddress"),
)
if mibBuilder.loadTexts:
    vRtrPimGrpSrcEntry.setStatus("current")
_VRtrPimGrpSrcGroupAddress_Type = IpAddress
_VRtrPimGrpSrcGroupAddress_Object = MibTableColumn
vRtrPimGrpSrcGroupAddress = _VRtrPimGrpSrcGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 3, 1, 1),
    _VRtrPimGrpSrcGroupAddress_Type()
)
vRtrPimGrpSrcGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcGroupAddress.setStatus("current")
_VRtrPimGrpSrcSourceAddress_Type = IpAddress
_VRtrPimGrpSrcSourceAddress_Object = MibTableColumn
vRtrPimGrpSrcSourceAddress = _VRtrPimGrpSrcSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 3, 1, 2),
    _VRtrPimGrpSrcSourceAddress_Type()
)
vRtrPimGrpSrcSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcSourceAddress.setStatus("current")


class _VRtrPimGrpSrcType_Type(Integer32):
    """Custom type vRtrPimGrpSrcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("starStarRP", 0),
          ("starG", 1),
          ("sg", 2))
    )


_VRtrPimGrpSrcType_Type.__name__ = "Integer32"
_VRtrPimGrpSrcType_Object = MibTableColumn
vRtrPimGrpSrcType = _VRtrPimGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 3, 1, 3),
    _VRtrPimGrpSrcType_Type()
)
vRtrPimGrpSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcType.setStatus("current")
_VRtrPimGrpSrcRPAddr_Type = IpAddress
_VRtrPimGrpSrcRPAddr_Object = MibTableColumn
vRtrPimGrpSrcRPAddr = _VRtrPimGrpSrcRPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 3, 1, 4),
    _VRtrPimGrpSrcRPAddr_Type()
)
vRtrPimGrpSrcRPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcRPAddr.setStatus("current")
_VRtrPimGrpSrcRpfNbrAddr_Type = IpAddress
_VRtrPimGrpSrcRpfNbrAddr_Object = MibTableColumn
vRtrPimGrpSrcRpfNbrAddr = _VRtrPimGrpSrcRpfNbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 3, 1, 5),
    _VRtrPimGrpSrcRpfNbrAddr_Type()
)
vRtrPimGrpSrcRpfNbrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcRpfNbrAddr.setStatus("current")
_VRtrPimGrpSrcRpfIfIndex_Type = InterfaceIndexOrZero
_VRtrPimGrpSrcRpfIfIndex_Object = MibTableColumn
vRtrPimGrpSrcRpfIfIndex = _VRtrPimGrpSrcRpfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 3, 1, 6),
    _VRtrPimGrpSrcRpfIfIndex_Type()
)
vRtrPimGrpSrcRpfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcRpfIfIndex.setStatus("current")
_VRtrPimGrpSrcRptRpfNbrAddr_Type = IpAddress
_VRtrPimGrpSrcRptRpfNbrAddr_Object = MibTableColumn
vRtrPimGrpSrcRptRpfNbrAddr = _VRtrPimGrpSrcRptRpfNbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 3, 1, 7),
    _VRtrPimGrpSrcRptRpfNbrAddr_Type()
)
vRtrPimGrpSrcRptRpfNbrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcRptRpfNbrAddr.setStatus("current")
_VRtrPimGrpSrcMRIBNextHopAddr_Type = IpAddress
_VRtrPimGrpSrcMRIBNextHopAddr_Object = MibTableColumn
vRtrPimGrpSrcMRIBNextHopAddr = _VRtrPimGrpSrcMRIBNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 3, 1, 8),
    _VRtrPimGrpSrcMRIBNextHopAddr_Type()
)
vRtrPimGrpSrcMRIBNextHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcMRIBNextHopAddr.setStatus("current")


class _VRtrPimGrpSrcMRIBSrcFlags_Type(Bits):
    """Custom type vRtrPimGrpSrcMRIBSrcFlags based on Bits"""
    namedValues = NamedValues(
        *(("self", 0),
          ("direct", 1),
          ("remote", 2))
    )

_VRtrPimGrpSrcMRIBSrcFlags_Type.__name__ = "Bits"
_VRtrPimGrpSrcMRIBSrcFlags_Object = MibTableColumn
vRtrPimGrpSrcMRIBSrcFlags = _VRtrPimGrpSrcMRIBSrcFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 3, 1, 9),
    _VRtrPimGrpSrcMRIBSrcFlags_Type()
)
vRtrPimGrpSrcMRIBSrcFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcMRIBSrcFlags.setStatus("current")


class _VRtrPimGrpSrcFlags_Type(Bits):
    """Custom type vRtrPimGrpSrcFlags based on Bits"""
    namedValues = NamedValues(
        *(("sptBit", 0),
          ("rptPruneDesired", 1))
    )

_VRtrPimGrpSrcFlags_Type.__name__ = "Bits"
_VRtrPimGrpSrcFlags_Object = MibTableColumn
vRtrPimGrpSrcFlags = _VRtrPimGrpSrcFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 3, 1, 10),
    _VRtrPimGrpSrcFlags_Type()
)
vRtrPimGrpSrcFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcFlags.setStatus("current")


class _VRtrPimGrpSrcUpstreamJpState_Type(Integer32):
    """Custom type vRtrPimGrpSrcUpstreamJpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notJoined", 0),
          ("joined", 1))
    )


_VRtrPimGrpSrcUpstreamJpState_Type.__name__ = "Integer32"
_VRtrPimGrpSrcUpstreamJpState_Object = MibTableColumn
vRtrPimGrpSrcUpstreamJpState = _VRtrPimGrpSrcUpstreamJpState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 3, 1, 11),
    _VRtrPimGrpSrcUpstreamJpState_Type()
)
vRtrPimGrpSrcUpstreamJpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcUpstreamJpState.setStatus("current")
_VRtrPimGrpSrcUpstreamJpTimer_Type = Unsigned32
_VRtrPimGrpSrcUpstreamJpTimer_Object = MibTableColumn
vRtrPimGrpSrcUpstreamJpTimer = _VRtrPimGrpSrcUpstreamJpTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 3, 1, 12),
    _VRtrPimGrpSrcUpstreamJpTimer_Type()
)
vRtrPimGrpSrcUpstreamJpTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcUpstreamJpTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcUpstreamJpTimer.setUnits("seconds")


class _VRtrPimGrpSrcUpstreamRptJpState_Type(Integer32):
    """Custom type vRtrPimGrpSrcUpstreamRptJpState based on Integer32"""
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


_VRtrPimGrpSrcUpstreamRptJpState_Type.__name__ = "Integer32"
_VRtrPimGrpSrcUpstreamRptJpState_Object = MibTableColumn
vRtrPimGrpSrcUpstreamRptJpState = _VRtrPimGrpSrcUpstreamRptJpState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 3, 1, 13),
    _VRtrPimGrpSrcUpstreamRptJpState_Type()
)
vRtrPimGrpSrcUpstreamRptJpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcUpstreamRptJpState.setStatus("current")
_VRtrPimGrpSrcUpstreamRptOverrideTimer_Type = Unsigned32
_VRtrPimGrpSrcUpstreamRptOverrideTimer_Object = MibTableColumn
vRtrPimGrpSrcUpstreamRptOverrideTimer = _VRtrPimGrpSrcUpstreamRptOverrideTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 3, 1, 14),
    _VRtrPimGrpSrcUpstreamRptOverrideTimer_Type()
)
vRtrPimGrpSrcUpstreamRptOverrideTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcUpstreamRptOverrideTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcUpstreamRptOverrideTimer.setUnits("seconds")


class _VRtrPimGrpSrcRegisterState_Type(Integer32):
    """Custom type vRtrPimGrpSrcRegisterState based on Integer32"""
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
          ("joinPending", 2),
          ("prune", 3))
    )


_VRtrPimGrpSrcRegisterState_Type.__name__ = "Integer32"
_VRtrPimGrpSrcRegisterState_Object = MibTableColumn
vRtrPimGrpSrcRegisterState = _VRtrPimGrpSrcRegisterState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 3, 1, 15),
    _VRtrPimGrpSrcRegisterState_Type()
)
vRtrPimGrpSrcRegisterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcRegisterState.setStatus("current")
_VRtrPimGrpSrcRegisterStopTimer_Type = Unsigned32
_VRtrPimGrpSrcRegisterStopTimer_Object = MibTableColumn
vRtrPimGrpSrcRegisterStopTimer = _VRtrPimGrpSrcRegisterStopTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 3, 1, 16),
    _VRtrPimGrpSrcRegisterStopTimer_Type()
)
vRtrPimGrpSrcRegisterStopTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcRegisterStopTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcRegisterStopTimer.setUnits("seconds")
_VRtrPimGrpSrcKeepaliveTimer_Type = Unsigned32
_VRtrPimGrpSrcKeepaliveTimer_Object = MibTableColumn
vRtrPimGrpSrcKeepaliveTimer = _VRtrPimGrpSrcKeepaliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 3, 1, 17),
    _VRtrPimGrpSrcKeepaliveTimer_Type()
)
vRtrPimGrpSrcKeepaliveTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcKeepaliveTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcKeepaliveTimer.setUnits("seconds")
_VRtrPimGrpSrcNumImmediateOif_Type = Gauge32
_VRtrPimGrpSrcNumImmediateOif_Object = MibTableColumn
vRtrPimGrpSrcNumImmediateOif = _VRtrPimGrpSrcNumImmediateOif_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 3, 1, 18),
    _VRtrPimGrpSrcNumImmediateOif_Type()
)
vRtrPimGrpSrcNumImmediateOif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcNumImmediateOif.setStatus("current")
_VRtrPimGrpSrcNumInheritedOif_Type = Gauge32
_VRtrPimGrpSrcNumInheritedOif_Object = MibTableColumn
vRtrPimGrpSrcNumInheritedOif = _VRtrPimGrpSrcNumInheritedOif_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 3, 1, 19),
    _VRtrPimGrpSrcNumInheritedOif_Type()
)
vRtrPimGrpSrcNumInheritedOif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcNumInheritedOif.setStatus("current")
_VRtrPimGrpSrcNumInheritedRptOif_Type = Gauge32
_VRtrPimGrpSrcNumInheritedRptOif_Object = MibTableColumn
vRtrPimGrpSrcNumInheritedRptOif = _VRtrPimGrpSrcNumInheritedRptOif_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 3, 1, 20),
    _VRtrPimGrpSrcNumInheritedRptOif_Type()
)
vRtrPimGrpSrcNumInheritedRptOif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcNumInheritedRptOif.setStatus("current")
_VRtrPimGrpSrcNumLocalRxIncludeIf_Type = Gauge32
_VRtrPimGrpSrcNumLocalRxIncludeIf_Object = MibTableColumn
vRtrPimGrpSrcNumLocalRxIncludeIf = _VRtrPimGrpSrcNumLocalRxIncludeIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 3, 1, 21),
    _VRtrPimGrpSrcNumLocalRxIncludeIf_Type()
)
vRtrPimGrpSrcNumLocalRxIncludeIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcNumLocalRxIncludeIf.setStatus("current")
_VRtrPimGrpSrcNumLocalRxExcludeIf_Type = Gauge32
_VRtrPimGrpSrcNumLocalRxExcludeIf_Object = MibTableColumn
vRtrPimGrpSrcNumLocalRxExcludeIf = _VRtrPimGrpSrcNumLocalRxExcludeIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 3, 1, 22),
    _VRtrPimGrpSrcNumLocalRxExcludeIf_Type()
)
vRtrPimGrpSrcNumLocalRxExcludeIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcNumLocalRxExcludeIf.setStatus("current")
_VRtrPimGrpSrcNumJoinPruneIf_Type = Gauge32
_VRtrPimGrpSrcNumJoinPruneIf_Object = MibTableColumn
vRtrPimGrpSrcNumJoinPruneIf = _VRtrPimGrpSrcNumJoinPruneIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 3, 1, 23),
    _VRtrPimGrpSrcNumJoinPruneIf_Type()
)
vRtrPimGrpSrcNumJoinPruneIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcNumJoinPruneIf.setStatus("current")
_VRtrPimGrpSrcNumLostAssertIf_Type = Gauge32
_VRtrPimGrpSrcNumLostAssertIf_Object = MibTableColumn
vRtrPimGrpSrcNumLostAssertIf = _VRtrPimGrpSrcNumLostAssertIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 3, 1, 24),
    _VRtrPimGrpSrcNumLostAssertIf_Type()
)
vRtrPimGrpSrcNumLostAssertIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcNumLostAssertIf.setStatus("current")
_VRtrPimGrpSrcUpTime_Type = Unsigned32
_VRtrPimGrpSrcUpTime_Object = MibTableColumn
vRtrPimGrpSrcUpTime = _VRtrPimGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 3, 1, 25),
    _VRtrPimGrpSrcUpTime_Type()
)
vRtrPimGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcUpTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcUpTime.setUnits("seconds")
_VRtrPimGrpSrcIfTable_Object = MibTable
vRtrPimGrpSrcIfTable = _VRtrPimGrpSrcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 4)
)
if mibBuilder.loadTexts:
    vRtrPimGrpSrcIfTable.setStatus("current")
_VRtrPimGrpSrcIfEntry_Object = MibTableRow
vRtrPimGrpSrcIfEntry = _VRtrPimGrpSrcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 4, 1)
)
vRtrPimGrpSrcIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-MIB", "vRtrPimGrpSrcGroupAddress"),
    (0, "TIMETRA-PIM-MIB", "vRtrPimGrpSrcSourceAddress"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrPimGrpSrcIfEntry.setStatus("current")


class _VRtrPimGrpSrcIfFlags_Type(Bits):
    """Custom type vRtrPimGrpSrcIfFlags based on Bits"""
    namedValues = NamedValues(
        *(("immediateOifList", 0),
          ("inheritedOifList", 1),
          ("inheritedRptOifList", 2),
          ("localRxInclude", 3),
          ("localRxExclude", 4),
          ("joinPruneList", 5),
          ("lostAssertList", 6))
    )

_VRtrPimGrpSrcIfFlags_Type.__name__ = "Bits"
_VRtrPimGrpSrcIfFlags_Object = MibTableColumn
vRtrPimGrpSrcIfFlags = _VRtrPimGrpSrcIfFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 4, 1, 1),
    _VRtrPimGrpSrcIfFlags_Type()
)
vRtrPimGrpSrcIfFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcIfFlags.setStatus("current")
_VRtrPimCRPGrpPrefixTable_Object = MibTable
vRtrPimCRPGrpPrefixTable = _VRtrPimCRPGrpPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 5)
)
if mibBuilder.loadTexts:
    vRtrPimCRPGrpPrefixTable.setStatus("current")
_VRtrPimCRPGrpPrefixEntry_Object = MibTableRow
vRtrPimCRPGrpPrefixEntry = _VRtrPimCRPGrpPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 5, 1)
)
vRtrPimCRPGrpPrefixEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-MIB", "vRtrPimCRPGrpPrefixGrpAddr"),
    (0, "TIMETRA-PIM-MIB", "vRtrPimCRPGrpPrefixGrpMask"),
)
if mibBuilder.loadTexts:
    vRtrPimCRPGrpPrefixEntry.setStatus("current")
_VRtrPimCRPGrpPrefixGrpAddr_Type = IpAddress
_VRtrPimCRPGrpPrefixGrpAddr_Object = MibTableColumn
vRtrPimCRPGrpPrefixGrpAddr = _VRtrPimCRPGrpPrefixGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 5, 1, 1),
    _VRtrPimCRPGrpPrefixGrpAddr_Type()
)
vRtrPimCRPGrpPrefixGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimCRPGrpPrefixGrpAddr.setStatus("current")
_VRtrPimCRPGrpPrefixGrpMask_Type = IpAddressPrefixLength
_VRtrPimCRPGrpPrefixGrpMask_Object = MibTableColumn
vRtrPimCRPGrpPrefixGrpMask = _VRtrPimCRPGrpPrefixGrpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 5, 1, 2),
    _VRtrPimCRPGrpPrefixGrpMask_Type()
)
vRtrPimCRPGrpPrefixGrpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimCRPGrpPrefixGrpMask.setStatus("current")
_VRtrPimCRPGrpPrefixRowStatus_Type = RowStatus
_VRtrPimCRPGrpPrefixRowStatus_Object = MibTableColumn
vRtrPimCRPGrpPrefixRowStatus = _VRtrPimCRPGrpPrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 5, 1, 3),
    _VRtrPimCRPGrpPrefixRowStatus_Type()
)
vRtrPimCRPGrpPrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimCRPGrpPrefixRowStatus.setStatus("current")
_VRtrPimCRPTable_Object = MibTable
vRtrPimCRPTable = _VRtrPimCRPTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 6)
)
if mibBuilder.loadTexts:
    vRtrPimCRPTable.setStatus("current")
_VRtrPimCRPEntry_Object = MibTableRow
vRtrPimCRPEntry = _VRtrPimCRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 6, 1)
)
vRtrPimCRPEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-MIB", "vRtrPimCRPAddress"),
    (0, "TIMETRA-PIM-MIB", "vRtrPimCRPGrpAddr"),
    (0, "TIMETRA-PIM-MIB", "vRtrPimCRPGrpMask"),
)
if mibBuilder.loadTexts:
    vRtrPimCRPEntry.setStatus("current")
_VRtrPimCRPAddress_Type = IpAddress
_VRtrPimCRPAddress_Object = MibTableColumn
vRtrPimCRPAddress = _VRtrPimCRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 6, 1, 1),
    _VRtrPimCRPAddress_Type()
)
vRtrPimCRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimCRPAddress.setStatus("current")
_VRtrPimCRPGrpAddr_Type = IpAddress
_VRtrPimCRPGrpAddr_Object = MibTableColumn
vRtrPimCRPGrpAddr = _VRtrPimCRPGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 6, 1, 2),
    _VRtrPimCRPGrpAddr_Type()
)
vRtrPimCRPGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimCRPGrpAddr.setStatus("current")
_VRtrPimCRPGrpMask_Type = IpAddressPrefixLength
_VRtrPimCRPGrpMask_Object = MibTableColumn
vRtrPimCRPGrpMask = _VRtrPimCRPGrpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 6, 1, 3),
    _VRtrPimCRPGrpMask_Type()
)
vRtrPimCRPGrpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimCRPGrpMask.setStatus("current")
_VRtrPimCRPHoldtime_Type = Integer32
_VRtrPimCRPHoldtime_Object = MibTableColumn
vRtrPimCRPHoldtime = _VRtrPimCRPHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 6, 1, 4),
    _VRtrPimCRPHoldtime_Type()
)
vRtrPimCRPHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimCRPHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimCRPHoldtime.setUnits("seconds")
_VRtrPimCRPPriority_Type = Integer32
_VRtrPimCRPPriority_Object = MibTableColumn
vRtrPimCRPPriority = _VRtrPimCRPPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 6, 1, 5),
    _VRtrPimCRPPriority_Type()
)
vRtrPimCRPPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimCRPPriority.setStatus("current")
_VRtrPimCRPExpiryTime_Type = Integer32
_VRtrPimCRPExpiryTime_Object = MibTableColumn
vRtrPimCRPExpiryTime = _VRtrPimCRPExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 6, 1, 6),
    _VRtrPimCRPExpiryTime_Type()
)
vRtrPimCRPExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimCRPExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimCRPExpiryTime.setUnits("seconds")
_VRtrPimRPSetTable_Object = MibTable
vRtrPimRPSetTable = _VRtrPimRPSetTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 7)
)
if mibBuilder.loadTexts:
    vRtrPimRPSetTable.setStatus("current")
_VRtrPimRPSetEntry_Object = MibTableRow
vRtrPimRPSetEntry = _VRtrPimRPSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 7, 1)
)
vRtrPimRPSetEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PIM-MIB", "vRtrPimRPSetType"),
    (0, "TIMETRA-PIM-MIB", "vRtrPimRPSetGrpAddr"),
    (0, "TIMETRA-PIM-MIB", "vRtrPimRPSetGrpMask"),
    (0, "TIMETRA-PIM-MIB", "vRtrPimRPSetCRPAddress"),
)
if mibBuilder.loadTexts:
    vRtrPimRPSetEntry.setStatus("current")


class _VRtrPimRPSetType_Type(Integer32):
    """Custom type vRtrPimRPSetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_VRtrPimRPSetType_Type.__name__ = "Integer32"
_VRtrPimRPSetType_Object = MibTableColumn
vRtrPimRPSetType = _VRtrPimRPSetType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 7, 1, 1),
    _VRtrPimRPSetType_Type()
)
vRtrPimRPSetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimRPSetType.setStatus("current")
_VRtrPimRPSetGrpAddr_Type = IpAddress
_VRtrPimRPSetGrpAddr_Object = MibTableColumn
vRtrPimRPSetGrpAddr = _VRtrPimRPSetGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 7, 1, 2),
    _VRtrPimRPSetGrpAddr_Type()
)
vRtrPimRPSetGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimRPSetGrpAddr.setStatus("current")
_VRtrPimRPSetGrpMask_Type = IpAddressPrefixLength
_VRtrPimRPSetGrpMask_Object = MibTableColumn
vRtrPimRPSetGrpMask = _VRtrPimRPSetGrpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 7, 1, 3),
    _VRtrPimRPSetGrpMask_Type()
)
vRtrPimRPSetGrpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimRPSetGrpMask.setStatus("current")
_VRtrPimRPSetCRPAddress_Type = IpAddress
_VRtrPimRPSetCRPAddress_Object = MibTableColumn
vRtrPimRPSetCRPAddress = _VRtrPimRPSetCRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 7, 1, 4),
    _VRtrPimRPSetCRPAddress_Type()
)
vRtrPimRPSetCRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimRPSetCRPAddress.setStatus("current")
_VRtrPimRPSetHoldtime_Type = Integer32
_VRtrPimRPSetHoldtime_Object = MibTableColumn
vRtrPimRPSetHoldtime = _VRtrPimRPSetHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 7, 1, 5),
    _VRtrPimRPSetHoldtime_Type()
)
vRtrPimRPSetHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimRPSetHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimRPSetHoldtime.setUnits("seconds")
_VRtrPimRPSetPriority_Type = Integer32
_VRtrPimRPSetPriority_Object = MibTableColumn
vRtrPimRPSetPriority = _VRtrPimRPSetPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 7, 1, 6),
    _VRtrPimRPSetPriority_Type()
)
vRtrPimRPSetPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimRPSetPriority.setStatus("current")
_VRtrPimGenStatsTable_Object = MibTable
vRtrPimGenStatsTable = _VRtrPimGenStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 8)
)
if mibBuilder.loadTexts:
    vRtrPimGenStatsTable.setStatus("current")
_VRtrPimGenStatsEntry_Object = MibTableRow
vRtrPimGenStatsEntry = _VRtrPimGenStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 8, 1)
)
if mibBuilder.loadTexts:
    vRtrPimGenStatsEntry.setStatus("current")
_VRtrPimGenStatsTxCrpaPdus_Type = Counter32
_VRtrPimGenStatsTxCrpaPdus_Object = MibTableColumn
vRtrPimGenStatsTxCrpaPdus = _VRtrPimGenStatsTxCrpaPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 8, 1, 1),
    _VRtrPimGenStatsTxCrpaPdus_Type()
)
vRtrPimGenStatsTxCrpaPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGenStatsTxCrpaPdus.setStatus("current")
_VRtrPimGenStatsTxCrpaPduErrs_Type = Counter32
_VRtrPimGenStatsTxCrpaPduErrs_Object = MibTableColumn
vRtrPimGenStatsTxCrpaPduErrs = _VRtrPimGenStatsTxCrpaPduErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 8, 1, 2),
    _VRtrPimGenStatsTxCrpaPduErrs_Type()
)
vRtrPimGenStatsTxCrpaPduErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGenStatsTxCrpaPduErrs.setStatus("current")
_VRtrPimGenStatsRxCrpaPdus_Type = Counter32
_VRtrPimGenStatsRxCrpaPdus_Object = MibTableColumn
vRtrPimGenStatsRxCrpaPdus = _VRtrPimGenStatsRxCrpaPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 8, 1, 3),
    _VRtrPimGenStatsRxCrpaPdus_Type()
)
vRtrPimGenStatsRxCrpaPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGenStatsRxCrpaPdus.setStatus("current")
_VRtrPimGenStatsRxCrpaPduDrops_Type = Counter32
_VRtrPimGenStatsRxCrpaPduDrops_Object = MibTableColumn
vRtrPimGenStatsRxCrpaPduDrops = _VRtrPimGenStatsRxCrpaPduDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 8, 1, 4),
    _VRtrPimGenStatsRxCrpaPduDrops_Type()
)
vRtrPimGenStatsRxCrpaPduDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGenStatsRxCrpaPduDrops.setStatus("current")
_VRtrPimGenStatsStarStarRPTypes_Type = Gauge32
_VRtrPimGenStatsStarStarRPTypes_Object = MibTableColumn
vRtrPimGenStatsStarStarRPTypes = _VRtrPimGenStatsStarStarRPTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 8, 1, 5),
    _VRtrPimGenStatsStarStarRPTypes_Type()
)
vRtrPimGenStatsStarStarRPTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGenStatsStarStarRPTypes.setStatus("current")
_VRtrPimGenStatsStarGTypes_Type = Gauge32
_VRtrPimGenStatsStarGTypes_Object = MibTableColumn
vRtrPimGenStatsStarGTypes = _VRtrPimGenStatsStarGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 8, 1, 6),
    _VRtrPimGenStatsStarGTypes_Type()
)
vRtrPimGenStatsStarGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGenStatsStarGTypes.setStatus("current")
_VRtrPimGenStatsSGTypes_Type = Gauge32
_VRtrPimGenStatsSGTypes_Object = MibTableColumn
vRtrPimGenStatsSGTypes = _VRtrPimGenStatsSGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 8, 1, 7),
    _VRtrPimGenStatsSGTypes_Type()
)
vRtrPimGenStatsSGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGenStatsSGTypes.setStatus("current")
_VRtrPimGrpSrcStatsTable_Object = MibTable
vRtrPimGrpSrcStatsTable = _VRtrPimGrpSrcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 9)
)
if mibBuilder.loadTexts:
    vRtrPimGrpSrcStatsTable.setStatus("current")
_VRtrPimGrpSrcStatsEntry_Object = MibTableRow
vRtrPimGrpSrcStatsEntry = _VRtrPimGrpSrcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 9, 1)
)
if mibBuilder.loadTexts:
    vRtrPimGrpSrcStatsEntry.setStatus("current")
_VRtrPimGrpSrcStatsForwardedPkts_Type = Counter64
_VRtrPimGrpSrcStatsForwardedPkts_Object = MibTableColumn
vRtrPimGrpSrcStatsForwardedPkts = _VRtrPimGrpSrcStatsForwardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 9, 1, 1),
    _VRtrPimGrpSrcStatsForwardedPkts_Type()
)
vRtrPimGrpSrcStatsForwardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcStatsForwardedPkts.setStatus("current")
_VRtrPimGrpSrcStatsDiscardedPkts_Type = Counter64
_VRtrPimGrpSrcStatsDiscardedPkts_Object = MibTableColumn
vRtrPimGrpSrcStatsDiscardedPkts = _VRtrPimGrpSrcStatsDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 9, 1, 2),
    _VRtrPimGrpSrcStatsDiscardedPkts_Type()
)
vRtrPimGrpSrcStatsDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcStatsDiscardedPkts.setStatus("current")
_VRtrPimGrpSrcStatsRPFMismatches_Type = Counter64
_VRtrPimGrpSrcStatsRPFMismatches_Object = MibTableColumn
vRtrPimGrpSrcStatsRPFMismatches = _VRtrPimGrpSrcStatsRPFMismatches_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 9, 1, 3),
    _VRtrPimGrpSrcStatsRPFMismatches_Type()
)
vRtrPimGrpSrcStatsRPFMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimGrpSrcStatsRPFMismatches.setStatus("current")
_VRtrPimGenPolicyTable_Object = MibTable
vRtrPimGenPolicyTable = _VRtrPimGenPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 10)
)
if mibBuilder.loadTexts:
    vRtrPimGenPolicyTable.setStatus("current")
_VRtrPimGenPolicyEntry_Object = MibTableRow
vRtrPimGenPolicyEntry = _VRtrPimGenPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 10, 1)
)
if mibBuilder.loadTexts:
    vRtrPimGenPolicyEntry.setStatus("current")


class _VRtrPimImportJoinPrunePolicy1_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimImportJoinPrunePolicy1 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimImportJoinPrunePolicy1_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimImportJoinPrunePolicy1_Object = MibTableColumn
vRtrPimImportJoinPrunePolicy1 = _VRtrPimImportJoinPrunePolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 10, 1, 1),
    _VRtrPimImportJoinPrunePolicy1_Type()
)
vRtrPimImportJoinPrunePolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimImportJoinPrunePolicy1.setStatus("current")


class _VRtrPimImportJoinPrunePolicy2_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimImportJoinPrunePolicy2 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimImportJoinPrunePolicy2_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimImportJoinPrunePolicy2_Object = MibTableColumn
vRtrPimImportJoinPrunePolicy2 = _VRtrPimImportJoinPrunePolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 10, 1, 2),
    _VRtrPimImportJoinPrunePolicy2_Type()
)
vRtrPimImportJoinPrunePolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimImportJoinPrunePolicy2.setStatus("current")


class _VRtrPimImportJoinPrunePolicy3_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimImportJoinPrunePolicy3 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimImportJoinPrunePolicy3_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimImportJoinPrunePolicy3_Object = MibTableColumn
vRtrPimImportJoinPrunePolicy3 = _VRtrPimImportJoinPrunePolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 10, 1, 3),
    _VRtrPimImportJoinPrunePolicy3_Type()
)
vRtrPimImportJoinPrunePolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimImportJoinPrunePolicy3.setStatus("current")


class _VRtrPimImportJoinPrunePolicy4_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimImportJoinPrunePolicy4 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimImportJoinPrunePolicy4_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimImportJoinPrunePolicy4_Object = MibTableColumn
vRtrPimImportJoinPrunePolicy4 = _VRtrPimImportJoinPrunePolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 10, 1, 4),
    _VRtrPimImportJoinPrunePolicy4_Type()
)
vRtrPimImportJoinPrunePolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimImportJoinPrunePolicy4.setStatus("current")


class _VRtrPimImportJoinPrunePolicy5_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimImportJoinPrunePolicy5 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimImportJoinPrunePolicy5_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimImportJoinPrunePolicy5_Object = MibTableColumn
vRtrPimImportJoinPrunePolicy5 = _VRtrPimImportJoinPrunePolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 10, 1, 5),
    _VRtrPimImportJoinPrunePolicy5_Type()
)
vRtrPimImportJoinPrunePolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimImportJoinPrunePolicy5.setStatus("current")


class _VRtrPimImportRegisterPolicy1_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimImportRegisterPolicy1 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimImportRegisterPolicy1_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimImportRegisterPolicy1_Object = MibTableColumn
vRtrPimImportRegisterPolicy1 = _VRtrPimImportRegisterPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 10, 1, 6),
    _VRtrPimImportRegisterPolicy1_Type()
)
vRtrPimImportRegisterPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimImportRegisterPolicy1.setStatus("current")


class _VRtrPimImportRegisterPolicy2_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimImportRegisterPolicy2 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimImportRegisterPolicy2_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimImportRegisterPolicy2_Object = MibTableColumn
vRtrPimImportRegisterPolicy2 = _VRtrPimImportRegisterPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 10, 1, 7),
    _VRtrPimImportRegisterPolicy2_Type()
)
vRtrPimImportRegisterPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimImportRegisterPolicy2.setStatus("current")


class _VRtrPimImportRegisterPolicy3_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimImportRegisterPolicy3 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimImportRegisterPolicy3_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimImportRegisterPolicy3_Object = MibTableColumn
vRtrPimImportRegisterPolicy3 = _VRtrPimImportRegisterPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 10, 1, 8),
    _VRtrPimImportRegisterPolicy3_Type()
)
vRtrPimImportRegisterPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimImportRegisterPolicy3.setStatus("current")


class _VRtrPimImportRegisterPolicy4_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimImportRegisterPolicy4 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimImportRegisterPolicy4_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimImportRegisterPolicy4_Object = MibTableColumn
vRtrPimImportRegisterPolicy4 = _VRtrPimImportRegisterPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 10, 1, 9),
    _VRtrPimImportRegisterPolicy4_Type()
)
vRtrPimImportRegisterPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimImportRegisterPolicy4.setStatus("current")


class _VRtrPimImportRegisterPolicy5_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimImportRegisterPolicy5 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimImportRegisterPolicy5_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimImportRegisterPolicy5_Object = MibTableColumn
vRtrPimImportRegisterPolicy5 = _VRtrPimImportRegisterPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 10, 1, 10),
    _VRtrPimImportRegisterPolicy5_Type()
)
vRtrPimImportRegisterPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimImportRegisterPolicy5.setStatus("current")


class _VRtrPimImportBootstrapPolicy1_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimImportBootstrapPolicy1 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimImportBootstrapPolicy1_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimImportBootstrapPolicy1_Object = MibTableColumn
vRtrPimImportBootstrapPolicy1 = _VRtrPimImportBootstrapPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 10, 1, 11),
    _VRtrPimImportBootstrapPolicy1_Type()
)
vRtrPimImportBootstrapPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimImportBootstrapPolicy1.setStatus("current")


class _VRtrPimImportBootstrapPolicy2_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimImportBootstrapPolicy2 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimImportBootstrapPolicy2_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimImportBootstrapPolicy2_Object = MibTableColumn
vRtrPimImportBootstrapPolicy2 = _VRtrPimImportBootstrapPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 10, 1, 12),
    _VRtrPimImportBootstrapPolicy2_Type()
)
vRtrPimImportBootstrapPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimImportBootstrapPolicy2.setStatus("current")


class _VRtrPimImportBootstrapPolicy3_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimImportBootstrapPolicy3 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimImportBootstrapPolicy3_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimImportBootstrapPolicy3_Object = MibTableColumn
vRtrPimImportBootstrapPolicy3 = _VRtrPimImportBootstrapPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 10, 1, 13),
    _VRtrPimImportBootstrapPolicy3_Type()
)
vRtrPimImportBootstrapPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimImportBootstrapPolicy3.setStatus("current")


class _VRtrPimImportBootstrapPolicy4_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimImportBootstrapPolicy4 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimImportBootstrapPolicy4_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimImportBootstrapPolicy4_Object = MibTableColumn
vRtrPimImportBootstrapPolicy4 = _VRtrPimImportBootstrapPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 10, 1, 14),
    _VRtrPimImportBootstrapPolicy4_Type()
)
vRtrPimImportBootstrapPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimImportBootstrapPolicy4.setStatus("current")


class _VRtrPimImportBootstrapPolicy5_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimImportBootstrapPolicy5 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimImportBootstrapPolicy5_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimImportBootstrapPolicy5_Object = MibTableColumn
vRtrPimImportBootstrapPolicy5 = _VRtrPimImportBootstrapPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 10, 1, 15),
    _VRtrPimImportBootstrapPolicy5_Type()
)
vRtrPimImportBootstrapPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimImportBootstrapPolicy5.setStatus("current")


class _VRtrPimExportBootstrapPolicy1_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimExportBootstrapPolicy1 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimExportBootstrapPolicy1_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimExportBootstrapPolicy1_Object = MibTableColumn
vRtrPimExportBootstrapPolicy1 = _VRtrPimExportBootstrapPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 10, 1, 16),
    _VRtrPimExportBootstrapPolicy1_Type()
)
vRtrPimExportBootstrapPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimExportBootstrapPolicy1.setStatus("current")


class _VRtrPimExportBootstrapPolicy2_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimExportBootstrapPolicy2 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimExportBootstrapPolicy2_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimExportBootstrapPolicy2_Object = MibTableColumn
vRtrPimExportBootstrapPolicy2 = _VRtrPimExportBootstrapPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 10, 1, 17),
    _VRtrPimExportBootstrapPolicy2_Type()
)
vRtrPimExportBootstrapPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimExportBootstrapPolicy2.setStatus("current")


class _VRtrPimExportBootstrapPolicy3_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimExportBootstrapPolicy3 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimExportBootstrapPolicy3_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimExportBootstrapPolicy3_Object = MibTableColumn
vRtrPimExportBootstrapPolicy3 = _VRtrPimExportBootstrapPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 10, 1, 18),
    _VRtrPimExportBootstrapPolicy3_Type()
)
vRtrPimExportBootstrapPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimExportBootstrapPolicy3.setStatus("current")


class _VRtrPimExportBootstrapPolicy4_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimExportBootstrapPolicy4 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimExportBootstrapPolicy4_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimExportBootstrapPolicy4_Object = MibTableColumn
vRtrPimExportBootstrapPolicy4 = _VRtrPimExportBootstrapPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 10, 1, 19),
    _VRtrPimExportBootstrapPolicy4_Type()
)
vRtrPimExportBootstrapPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimExportBootstrapPolicy4.setStatus("current")


class _VRtrPimExportBootstrapPolicy5_Type(TNamedItemOrEmpty):
    """Custom type vRtrPimExportBootstrapPolicy5 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrPimExportBootstrapPolicy5_Type.__name__ = "TNamedItemOrEmpty"
_VRtrPimExportBootstrapPolicy5_Object = MibTableColumn
vRtrPimExportBootstrapPolicy5 = _VRtrPimExportBootstrapPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 1, 10, 1, 20),
    _VRtrPimExportBootstrapPolicy5_Type()
)
vRtrPimExportBootstrapPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimExportBootstrapPolicy5.setStatus("current")
_VRtrPimIfObjs_ObjectIdentity = ObjectIdentity
vRtrPimIfObjs = _VRtrPimIfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2)
)
_VRtrPimIfTable_Object = MibTable
vRtrPimIfTable = _VRtrPimIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 1)
)
if mibBuilder.loadTexts:
    vRtrPimIfTable.setStatus("current")
_VRtrPimIfEntry_Object = MibTableRow
vRtrPimIfEntry = _VRtrPimIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 1, 1)
)
vRtrPimIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrPimIfEntry.setStatus("current")
_VRtrPimIfRowStatus_Type = RowStatus
_VRtrPimIfRowStatus_Object = MibTableColumn
vRtrPimIfRowStatus = _VRtrPimIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 1, 1, 1),
    _VRtrPimIfRowStatus_Type()
)
vRtrPimIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimIfRowStatus.setStatus("current")
_VRtrPimIfLastChangeTime_Type = TimeStamp
_VRtrPimIfLastChangeTime_Object = MibTableColumn
vRtrPimIfLastChangeTime = _VRtrPimIfLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 1, 1, 2),
    _VRtrPimIfLastChangeTime_Type()
)
vRtrPimIfLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfLastChangeTime.setStatus("current")
_VRtrPimIfAdminState_Type = TmnxAdminState
_VRtrPimIfAdminState_Object = MibTableColumn
vRtrPimIfAdminState = _VRtrPimIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 1, 1, 3),
    _VRtrPimIfAdminState_Type()
)
vRtrPimIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimIfAdminState.setStatus("current")
_VRtrPimIfOperState_Type = TmnxOperState
_VRtrPimIfOperState_Object = MibTableColumn
vRtrPimIfOperState = _VRtrPimIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 1, 1, 4),
    _VRtrPimIfOperState_Type()
)
vRtrPimIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfOperState.setStatus("current")
_VRtrPimIfDR_Type = IpAddress
_VRtrPimIfDR_Object = MibTableColumn
vRtrPimIfDR = _VRtrPimIfDR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 1, 1, 5),
    _VRtrPimIfDR_Type()
)
vRtrPimIfDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfDR.setStatus("current")


class _VRtrPimIfDRPriority_Type(Unsigned32):
    """Custom type vRtrPimIfDRPriority based on Unsigned32"""
    defaultValue = 1


_VRtrPimIfDRPriority_Type.__name__ = "Unsigned32"
_VRtrPimIfDRPriority_Object = MibTableColumn
vRtrPimIfDRPriority = _VRtrPimIfDRPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 1, 1, 6),
    _VRtrPimIfDRPriority_Type()
)
vRtrPimIfDRPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimIfDRPriority.setStatus("current")


class _VRtrPimIfHelloInterval_Type(Integer32):
    """Custom type vRtrPimIfHelloInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrPimIfHelloInterval_Type.__name__ = "Integer32"
_VRtrPimIfHelloInterval_Object = MibTableColumn
vRtrPimIfHelloInterval = _VRtrPimIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 1, 1, 7),
    _VRtrPimIfHelloInterval_Type()
)
vRtrPimIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimIfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimIfHelloInterval.setUnits("seconds")


class _VRtrPimIfTrackingSupport_Type(TruthValue):
    """Custom type vRtrPimIfTrackingSupport based on TruthValue"""
    defaultValue = 2


_VRtrPimIfTrackingSupport_Type.__name__ = "TruthValue"
_VRtrPimIfTrackingSupport_Object = MibTableColumn
vRtrPimIfTrackingSupport = _VRtrPimIfTrackingSupport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 1, 1, 8),
    _VRtrPimIfTrackingSupport_Type()
)
vRtrPimIfTrackingSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimIfTrackingSupport.setStatus("current")


class _VRtrPimIfMulticastSenders_Type(Integer32):
    """Custom type vRtrPimIfMulticastSenders based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("always", 1),
          ("never", 2))
    )


_VRtrPimIfMulticastSenders_Type.__name__ = "Integer32"
_VRtrPimIfMulticastSenders_Object = MibTableColumn
vRtrPimIfMulticastSenders = _VRtrPimIfMulticastSenders_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 1, 1, 9),
    _VRtrPimIfMulticastSenders_Type()
)
vRtrPimIfMulticastSenders.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimIfMulticastSenders.setStatus("current")
_VRtrPimIfNeighborTable_Object = MibTable
vRtrPimIfNeighborTable = _VRtrPimIfNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 2)
)
if mibBuilder.loadTexts:
    vRtrPimIfNeighborTable.setStatus("current")
_VRtrPimIfNeighborEntry_Object = MibTableRow
vRtrPimIfNeighborEntry = _VRtrPimIfNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 2, 1)
)
vRtrPimIfNeighborEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-PIM-MIB", "vRtrPimIfNeighborAddress"),
)
if mibBuilder.loadTexts:
    vRtrPimIfNeighborEntry.setStatus("current")
_VRtrPimIfNeighborAddress_Type = IpAddress
_VRtrPimIfNeighborAddress_Object = MibTableColumn
vRtrPimIfNeighborAddress = _VRtrPimIfNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 2, 1, 1),
    _VRtrPimIfNeighborAddress_Type()
)
vRtrPimIfNeighborAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimIfNeighborAddress.setStatus("current")
_VRtrPimIfNeighborUpTime_Type = Unsigned32
_VRtrPimIfNeighborUpTime_Object = MibTableColumn
vRtrPimIfNeighborUpTime = _VRtrPimIfNeighborUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 2, 1, 2),
    _VRtrPimIfNeighborUpTime_Type()
)
vRtrPimIfNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfNeighborUpTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimIfNeighborUpTime.setUnits("seconds")
_VRtrPimIfNeighborExpiryTime_Type = Unsigned32
_VRtrPimIfNeighborExpiryTime_Object = MibTableColumn
vRtrPimIfNeighborExpiryTime = _VRtrPimIfNeighborExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 2, 1, 3),
    _VRtrPimIfNeighborExpiryTime_Type()
)
vRtrPimIfNeighborExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfNeighborExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimIfNeighborExpiryTime.setUnits("seconds")
_VRtrPimIfNeighborGenId_Type = Unsigned32
_VRtrPimIfNeighborGenId_Object = MibTableColumn
vRtrPimIfNeighborGenId = _VRtrPimIfNeighborGenId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 2, 1, 4),
    _VRtrPimIfNeighborGenId_Type()
)
vRtrPimIfNeighborGenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfNeighborGenId.setStatus("current")
_VRtrPimIfNeighborDrPriority_Type = Unsigned32
_VRtrPimIfNeighborDrPriority_Object = MibTableColumn
vRtrPimIfNeighborDrPriority = _VRtrPimIfNeighborDrPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 2, 1, 5),
    _VRtrPimIfNeighborDrPriority_Type()
)
vRtrPimIfNeighborDrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfNeighborDrPriority.setStatus("current")
_VRtrPimIfNeighborDrPriorityPresent_Type = TruthValue
_VRtrPimIfNeighborDrPriorityPresent_Object = MibTableColumn
vRtrPimIfNeighborDrPriorityPresent = _VRtrPimIfNeighborDrPriorityPresent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 2, 1, 6),
    _VRtrPimIfNeighborDrPriorityPresent_Type()
)
vRtrPimIfNeighborDrPriorityPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfNeighborDrPriorityPresent.setStatus("current")
_VRtrPimIfNeighborLanDelay_Type = Unsigned32
_VRtrPimIfNeighborLanDelay_Object = MibTableColumn
vRtrPimIfNeighborLanDelay = _VRtrPimIfNeighborLanDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 2, 1, 7),
    _VRtrPimIfNeighborLanDelay_Type()
)
vRtrPimIfNeighborLanDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfNeighborLanDelay.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimIfNeighborLanDelay.setUnits("milliseconds")
_VRtrPimIfNeighborLanDelayPresent_Type = TruthValue
_VRtrPimIfNeighborLanDelayPresent_Object = MibTableColumn
vRtrPimIfNeighborLanDelayPresent = _VRtrPimIfNeighborLanDelayPresent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 2, 1, 8),
    _VRtrPimIfNeighborLanDelayPresent_Type()
)
vRtrPimIfNeighborLanDelayPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfNeighborLanDelayPresent.setStatus("current")
_VRtrPimIfNeighborTrackingSupport_Type = TruthValue
_VRtrPimIfNeighborTrackingSupport_Object = MibTableColumn
vRtrPimIfNeighborTrackingSupport = _VRtrPimIfNeighborTrackingSupport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 2, 1, 9),
    _VRtrPimIfNeighborTrackingSupport_Type()
)
vRtrPimIfNeighborTrackingSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfNeighborTrackingSupport.setStatus("current")
_VRtrPimIfNeighborHoldTime_Type = Unsigned32
_VRtrPimIfNeighborHoldTime_Object = MibTableColumn
vRtrPimIfNeighborHoldTime = _VRtrPimIfNeighborHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 2, 1, 10),
    _VRtrPimIfNeighborHoldTime_Type()
)
vRtrPimIfNeighborHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfNeighborHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimIfNeighborHoldTime.setUnits("seconds")
_VRtrPimIfNeighborOverrideInterval_Type = Unsigned32
_VRtrPimIfNeighborOverrideInterval_Object = MibTableColumn
vRtrPimIfNeighborOverrideInterval = _VRtrPimIfNeighborOverrideInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 2, 1, 11),
    _VRtrPimIfNeighborOverrideInterval_Type()
)
vRtrPimIfNeighborOverrideInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfNeighborOverrideInterval.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimIfNeighborOverrideInterval.setUnits("milliseconds")
_VRtrPimIfGrpSrcTable_Object = MibTable
vRtrPimIfGrpSrcTable = _VRtrPimIfGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 3)
)
if mibBuilder.loadTexts:
    vRtrPimIfGrpSrcTable.setStatus("current")
_VRtrPimIfGrpSrcEntry_Object = MibTableRow
vRtrPimIfGrpSrcEntry = _VRtrPimIfGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 3, 1)
)
vRtrPimIfGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-PIM-MIB", "vRtrPimIfGrpSrcType"),
    (0, "TIMETRA-PIM-MIB", "vRtrPimIfGrpSrcGroupAddress"),
    (0, "TIMETRA-PIM-MIB", "vRtrPimIfGrpSrcSourceAddress"),
)
if mibBuilder.loadTexts:
    vRtrPimIfGrpSrcEntry.setStatus("current")


class _VRtrPimIfGrpSrcType_Type(Integer32):
    """Custom type vRtrPimIfGrpSrcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("starStarRP", 0),
          ("starG", 1),
          ("sg", 2))
    )


_VRtrPimIfGrpSrcType_Type.__name__ = "Integer32"
_VRtrPimIfGrpSrcType_Object = MibTableColumn
vRtrPimIfGrpSrcType = _VRtrPimIfGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 3, 1, 1),
    _VRtrPimIfGrpSrcType_Type()
)
vRtrPimIfGrpSrcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimIfGrpSrcType.setStatus("current")
_VRtrPimIfGrpSrcGroupAddress_Type = IpAddress
_VRtrPimIfGrpSrcGroupAddress_Object = MibTableColumn
vRtrPimIfGrpSrcGroupAddress = _VRtrPimIfGrpSrcGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 3, 1, 2),
    _VRtrPimIfGrpSrcGroupAddress_Type()
)
vRtrPimIfGrpSrcGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimIfGrpSrcGroupAddress.setStatus("current")
_VRtrPimIfGrpSrcSourceAddress_Type = IpAddress
_VRtrPimIfGrpSrcSourceAddress_Object = MibTableColumn
vRtrPimIfGrpSrcSourceAddress = _VRtrPimIfGrpSrcSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 3, 1, 3),
    _VRtrPimIfGrpSrcSourceAddress_Type()
)
vRtrPimIfGrpSrcSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrPimIfGrpSrcSourceAddress.setStatus("current")
_VRtrPimIfGrpSrcRPAddress_Type = IpAddress
_VRtrPimIfGrpSrcRPAddress_Object = MibTableColumn
vRtrPimIfGrpSrcRPAddress = _VRtrPimIfGrpSrcRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 3, 1, 4),
    _VRtrPimIfGrpSrcRPAddress_Type()
)
vRtrPimIfGrpSrcRPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfGrpSrcRPAddress.setStatus("current")


class _VRtrPimIfGrpSrcJPState_Type(Integer32):
    """Custom type vRtrPimIfGrpSrcJPState based on Integer32"""
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


_VRtrPimIfGrpSrcJPState_Type.__name__ = "Integer32"
_VRtrPimIfGrpSrcJPState_Object = MibTableColumn
vRtrPimIfGrpSrcJPState = _VRtrPimIfGrpSrcJPState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 3, 1, 5),
    _VRtrPimIfGrpSrcJPState_Type()
)
vRtrPimIfGrpSrcJPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfGrpSrcJPState.setStatus("current")
_VRtrPimIfGrpSrcPrunePendTimer_Type = Unsigned32
_VRtrPimIfGrpSrcPrunePendTimer_Object = MibTableColumn
vRtrPimIfGrpSrcPrunePendTimer = _VRtrPimIfGrpSrcPrunePendTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 3, 1, 6),
    _VRtrPimIfGrpSrcPrunePendTimer_Type()
)
vRtrPimIfGrpSrcPrunePendTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfGrpSrcPrunePendTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimIfGrpSrcPrunePendTimer.setUnits("seconds")
_VRtrPimIfGrpSrcJoinPruneTimer_Type = Unsigned32
_VRtrPimIfGrpSrcJoinPruneTimer_Object = MibTableColumn
vRtrPimIfGrpSrcJoinPruneTimer = _VRtrPimIfGrpSrcJoinPruneTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 3, 1, 7),
    _VRtrPimIfGrpSrcJoinPruneTimer_Type()
)
vRtrPimIfGrpSrcJoinPruneTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfGrpSrcJoinPruneTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimIfGrpSrcJoinPruneTimer.setUnits("seconds")


class _VRtrPimIfGrpSrcJPRptState_Type(Integer32):
    """Custom type vRtrPimIfGrpSrcJPRptState based on Integer32"""
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


_VRtrPimIfGrpSrcJPRptState_Type.__name__ = "Integer32"
_VRtrPimIfGrpSrcJPRptState_Object = MibTableColumn
vRtrPimIfGrpSrcJPRptState = _VRtrPimIfGrpSrcJPRptState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 3, 1, 8),
    _VRtrPimIfGrpSrcJPRptState_Type()
)
vRtrPimIfGrpSrcJPRptState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfGrpSrcJPRptState.setStatus("current")
_VRtrPimIfGrpSrcRptPrunePendTimer_Type = Unsigned32
_VRtrPimIfGrpSrcRptPrunePendTimer_Object = MibTableColumn
vRtrPimIfGrpSrcRptPrunePendTimer = _VRtrPimIfGrpSrcRptPrunePendTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 3, 1, 9),
    _VRtrPimIfGrpSrcRptPrunePendTimer_Type()
)
vRtrPimIfGrpSrcRptPrunePendTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfGrpSrcRptPrunePendTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimIfGrpSrcRptPrunePendTimer.setUnits("seconds")
_VRtrPimIfGrpSrcRptJoinPruneTimer_Type = Unsigned32
_VRtrPimIfGrpSrcRptJoinPruneTimer_Object = MibTableColumn
vRtrPimIfGrpSrcRptJoinPruneTimer = _VRtrPimIfGrpSrcRptJoinPruneTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 3, 1, 10),
    _VRtrPimIfGrpSrcRptJoinPruneTimer_Type()
)
vRtrPimIfGrpSrcRptJoinPruneTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfGrpSrcRptJoinPruneTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimIfGrpSrcRptJoinPruneTimer.setUnits("seconds")


class _VRtrPimIfGrpSrcAssertState_Type(Integer32):
    """Custom type vRtrPimIfGrpSrcAssertState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noInfo", 0),
          ("lostAssert", 1),
          ("wonAssert", 2))
    )


_VRtrPimIfGrpSrcAssertState_Type.__name__ = "Integer32"
_VRtrPimIfGrpSrcAssertState_Object = MibTableColumn
vRtrPimIfGrpSrcAssertState = _VRtrPimIfGrpSrcAssertState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 3, 1, 11),
    _VRtrPimIfGrpSrcAssertState_Type()
)
vRtrPimIfGrpSrcAssertState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfGrpSrcAssertState.setStatus("current")
_VRtrPimIfGrpSrcAssertTimer_Type = Unsigned32
_VRtrPimIfGrpSrcAssertTimer_Object = MibTableColumn
vRtrPimIfGrpSrcAssertTimer = _VRtrPimIfGrpSrcAssertTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 3, 1, 12),
    _VRtrPimIfGrpSrcAssertTimer_Type()
)
vRtrPimIfGrpSrcAssertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfGrpSrcAssertTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrPimIfGrpSrcAssertTimer.setUnits("seconds")
_VRtrPimIfGrpSrcAssertMetric_Type = Unsigned32
_VRtrPimIfGrpSrcAssertMetric_Object = MibTableColumn
vRtrPimIfGrpSrcAssertMetric = _VRtrPimIfGrpSrcAssertMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 3, 1, 13),
    _VRtrPimIfGrpSrcAssertMetric_Type()
)
vRtrPimIfGrpSrcAssertMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfGrpSrcAssertMetric.setStatus("current")
_VRtrPimIfGrpSrcAssertMetricPref_Type = Unsigned32
_VRtrPimIfGrpSrcAssertMetricPref_Object = MibTableColumn
vRtrPimIfGrpSrcAssertMetricPref = _VRtrPimIfGrpSrcAssertMetricPref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 3, 1, 14),
    _VRtrPimIfGrpSrcAssertMetricPref_Type()
)
vRtrPimIfGrpSrcAssertMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfGrpSrcAssertMetricPref.setStatus("current")
_VRtrPimIfGrpSrcAssertRPTBit_Type = TruthValue
_VRtrPimIfGrpSrcAssertRPTBit_Object = MibTableColumn
vRtrPimIfGrpSrcAssertRPTBit = _VRtrPimIfGrpSrcAssertRPTBit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 3, 1, 15),
    _VRtrPimIfGrpSrcAssertRPTBit_Type()
)
vRtrPimIfGrpSrcAssertRPTBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfGrpSrcAssertRPTBit.setStatus("current")
_VRtrPimIfGrpSrcAssertWinnerMetric_Type = Unsigned32
_VRtrPimIfGrpSrcAssertWinnerMetric_Object = MibTableColumn
vRtrPimIfGrpSrcAssertWinnerMetric = _VRtrPimIfGrpSrcAssertWinnerMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 3, 1, 16),
    _VRtrPimIfGrpSrcAssertWinnerMetric_Type()
)
vRtrPimIfGrpSrcAssertWinnerMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfGrpSrcAssertWinnerMetric.setStatus("current")
_VRtrPimIfGrpSrcAssertWinnerMetricPref_Type = Unsigned32
_VRtrPimIfGrpSrcAssertWinnerMetricPref_Object = MibTableColumn
vRtrPimIfGrpSrcAssertWinnerMetricPref = _VRtrPimIfGrpSrcAssertWinnerMetricPref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 3, 1, 17),
    _VRtrPimIfGrpSrcAssertWinnerMetricPref_Type()
)
vRtrPimIfGrpSrcAssertWinnerMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfGrpSrcAssertWinnerMetricPref.setStatus("current")
_VRtrPimIfGrpSrcAssertWinnerRPTBit_Type = TruthValue
_VRtrPimIfGrpSrcAssertWinnerRPTBit_Object = MibTableColumn
vRtrPimIfGrpSrcAssertWinnerRPTBit = _VRtrPimIfGrpSrcAssertWinnerRPTBit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 3, 1, 18),
    _VRtrPimIfGrpSrcAssertWinnerRPTBit_Type()
)
vRtrPimIfGrpSrcAssertWinnerRPTBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfGrpSrcAssertWinnerRPTBit.setStatus("current")
_VRtrPimIfGrpSrcAssertWinnerAddr_Type = IpAddress
_VRtrPimIfGrpSrcAssertWinnerAddr_Object = MibTableColumn
vRtrPimIfGrpSrcAssertWinnerAddr = _VRtrPimIfGrpSrcAssertWinnerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 3, 1, 19),
    _VRtrPimIfGrpSrcAssertWinnerAddr_Type()
)
vRtrPimIfGrpSrcAssertWinnerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfGrpSrcAssertWinnerAddr.setStatus("current")
_VRtrPimIfStatsTable_Object = MibTable
vRtrPimIfStatsTable = _VRtrPimIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4)
)
if mibBuilder.loadTexts:
    vRtrPimIfStatsTable.setStatus("current")
_VRtrPimIfStatsEntry_Object = MibTableRow
vRtrPimIfStatsEntry = _VRtrPimIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1)
)
if mibBuilder.loadTexts:
    vRtrPimIfStatsEntry.setStatus("current")
_VRtrPimIfTxPkts_Type = Counter32
_VRtrPimIfTxPkts_Object = MibTableColumn
vRtrPimIfTxPkts = _VRtrPimIfTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 1),
    _VRtrPimIfTxPkts_Type()
)
vRtrPimIfTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfTxPkts.setStatus("current")
_VRtrPimIfTxHellos_Type = Counter32
_VRtrPimIfTxHellos_Object = MibTableColumn
vRtrPimIfTxHellos = _VRtrPimIfTxHellos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 2),
    _VRtrPimIfTxHellos_Type()
)
vRtrPimIfTxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfTxHellos.setStatus("current")
_VRtrPimIfTxAsserts_Type = Counter32
_VRtrPimIfTxAsserts_Object = MibTableColumn
vRtrPimIfTxAsserts = _VRtrPimIfTxAsserts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 3),
    _VRtrPimIfTxAsserts_Type()
)
vRtrPimIfTxAsserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfTxAsserts.setStatus("current")
_VRtrPimIfTxRegisters_Type = Counter32
_VRtrPimIfTxRegisters_Object = MibTableColumn
vRtrPimIfTxRegisters = _VRtrPimIfTxRegisters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 4),
    _VRtrPimIfTxRegisters_Type()
)
vRtrPimIfTxRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfTxRegisters.setStatus("current")
_VRtrPimIfTxRegisterErrs_Type = Counter32
_VRtrPimIfTxRegisterErrs_Object = MibTableColumn
vRtrPimIfTxRegisterErrs = _VRtrPimIfTxRegisterErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 5),
    _VRtrPimIfTxRegisterErrs_Type()
)
vRtrPimIfTxRegisterErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfTxRegisterErrs.setStatus("current")
_VRtrPimIfTxNullRegisters_Type = Counter32
_VRtrPimIfTxNullRegisters_Object = MibTableColumn
vRtrPimIfTxNullRegisters = _VRtrPimIfTxNullRegisters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 6),
    _VRtrPimIfTxNullRegisters_Type()
)
vRtrPimIfTxNullRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfTxNullRegisters.setStatus("current")
_VRtrPimIfTxRegisterStops_Type = Counter32
_VRtrPimIfTxRegisterStops_Object = MibTableColumn
vRtrPimIfTxRegisterStops = _VRtrPimIfTxRegisterStops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 7),
    _VRtrPimIfTxRegisterStops_Type()
)
vRtrPimIfTxRegisterStops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfTxRegisterStops.setStatus("current")
_VRtrPimIfTxRegisterStopErrs_Type = Counter32
_VRtrPimIfTxRegisterStopErrs_Object = MibTableColumn
vRtrPimIfTxRegisterStopErrs = _VRtrPimIfTxRegisterStopErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 8),
    _VRtrPimIfTxRegisterStopErrs_Type()
)
vRtrPimIfTxRegisterStopErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfTxRegisterStopErrs.setStatus("current")
_VRtrPimIfTxRegisterTTLDrops_Type = Counter32
_VRtrPimIfTxRegisterTTLDrops_Object = MibTableColumn
vRtrPimIfTxRegisterTTLDrops = _VRtrPimIfTxRegisterTTLDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 9),
    _VRtrPimIfTxRegisterTTLDrops_Type()
)
vRtrPimIfTxRegisterTTLDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfTxRegisterTTLDrops.setStatus("current")
_VRtrPimIfTxRegisterMtuDrops_Type = Counter32
_VRtrPimIfTxRegisterMtuDrops_Object = MibTableColumn
vRtrPimIfTxRegisterMtuDrops = _VRtrPimIfTxRegisterMtuDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 10),
    _VRtrPimIfTxRegisterMtuDrops_Type()
)
vRtrPimIfTxRegisterMtuDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfTxRegisterMtuDrops.setStatus("current")
_VRtrPimIfTxBsmPdus_Type = Counter32
_VRtrPimIfTxBsmPdus_Object = MibTableColumn
vRtrPimIfTxBsmPdus = _VRtrPimIfTxBsmPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 11),
    _VRtrPimIfTxBsmPdus_Type()
)
vRtrPimIfTxBsmPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfTxBsmPdus.setStatus("current")
_VRtrPimIfTxBsmErrs_Type = Counter32
_VRtrPimIfTxBsmErrs_Object = MibTableColumn
vRtrPimIfTxBsmErrs = _VRtrPimIfTxBsmErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 12),
    _VRtrPimIfTxBsmErrs_Type()
)
vRtrPimIfTxBsmErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfTxBsmErrs.setStatus("current")
_VRtrPimIfRxPkts_Type = Counter32
_VRtrPimIfRxPkts_Object = MibTableColumn
vRtrPimIfRxPkts = _VRtrPimIfRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 13),
    _VRtrPimIfRxPkts_Type()
)
vRtrPimIfRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfRxPkts.setStatus("current")
_VRtrPimIfRxHellos_Type = Counter32
_VRtrPimIfRxHellos_Object = MibTableColumn
vRtrPimIfRxHellos = _VRtrPimIfRxHellos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 14),
    _VRtrPimIfRxHellos_Type()
)
vRtrPimIfRxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfRxHellos.setStatus("current")
_VRtrPimIfRxHellosDropped_Type = Counter32
_VRtrPimIfRxHellosDropped_Object = MibTableColumn
vRtrPimIfRxHellosDropped = _VRtrPimIfRxHellosDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 15),
    _VRtrPimIfRxHellosDropped_Type()
)
vRtrPimIfRxHellosDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfRxHellosDropped.setStatus("current")
_VRtrPimIfRxNbrUnknown_Type = Counter32
_VRtrPimIfRxNbrUnknown_Object = MibTableColumn
vRtrPimIfRxNbrUnknown = _VRtrPimIfRxNbrUnknown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 16),
    _VRtrPimIfRxNbrUnknown_Type()
)
vRtrPimIfRxNbrUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfRxNbrUnknown.setStatus("current")
_VRtrPimIfRxBadChecksumDiscards_Type = Counter32
_VRtrPimIfRxBadChecksumDiscards_Object = MibTableColumn
vRtrPimIfRxBadChecksumDiscards = _VRtrPimIfRxBadChecksumDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 17),
    _VRtrPimIfRxBadChecksumDiscards_Type()
)
vRtrPimIfRxBadChecksumDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfRxBadChecksumDiscards.setStatus("current")
_VRtrPimIfRxBadVersionDiscards_Type = Counter32
_VRtrPimIfRxBadVersionDiscards_Object = MibTableColumn
vRtrPimIfRxBadVersionDiscards = _VRtrPimIfRxBadVersionDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 18),
    _VRtrPimIfRxBadVersionDiscards_Type()
)
vRtrPimIfRxBadVersionDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfRxBadVersionDiscards.setStatus("current")
_VRtrPimIfRxBadEncodings_Type = Counter32
_VRtrPimIfRxBadEncodings_Object = MibTableColumn
vRtrPimIfRxBadEncodings = _VRtrPimIfRxBadEncodings_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 19),
    _VRtrPimIfRxBadEncodings_Type()
)
vRtrPimIfRxBadEncodings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfRxBadEncodings.setStatus("current")
_VRtrPimIfRxAsserts_Type = Counter32
_VRtrPimIfRxAsserts_Object = MibTableColumn
vRtrPimIfRxAsserts = _VRtrPimIfRxAsserts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 20),
    _VRtrPimIfRxAsserts_Type()
)
vRtrPimIfRxAsserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfRxAsserts.setStatus("current")
_VRtrPimIfRxAssertErrs_Type = Counter32
_VRtrPimIfRxAssertErrs_Object = MibTableColumn
vRtrPimIfRxAssertErrs = _VRtrPimIfRxAssertErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 21),
    _VRtrPimIfRxAssertErrs_Type()
)
vRtrPimIfRxAssertErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfRxAssertErrs.setStatus("current")
_VRtrPimIfRxRegisters_Type = Counter32
_VRtrPimIfRxRegisters_Object = MibTableColumn
vRtrPimIfRxRegisters = _VRtrPimIfRxRegisters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 22),
    _VRtrPimIfRxRegisters_Type()
)
vRtrPimIfRxRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfRxRegisters.setStatus("current")
_VRtrPimIfRxRegisterErrs_Type = Counter32
_VRtrPimIfRxRegisterErrs_Object = MibTableColumn
vRtrPimIfRxRegisterErrs = _VRtrPimIfRxRegisterErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 23),
    _VRtrPimIfRxRegisterErrs_Type()
)
vRtrPimIfRxRegisterErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfRxRegisterErrs.setStatus("current")
_VRtrPimIfRxNullRegisters_Type = Counter32
_VRtrPimIfRxNullRegisters_Object = MibTableColumn
vRtrPimIfRxNullRegisters = _VRtrPimIfRxNullRegisters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 24),
    _VRtrPimIfRxNullRegisters_Type()
)
vRtrPimIfRxNullRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfRxNullRegisters.setStatus("current")
_VRtrPimIfRxRegisterStops_Type = Counter32
_VRtrPimIfRxRegisterStops_Object = MibTableColumn
vRtrPimIfRxRegisterStops = _VRtrPimIfRxRegisterStops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 25),
    _VRtrPimIfRxRegisterStops_Type()
)
vRtrPimIfRxRegisterStops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfRxRegisterStops.setStatus("current")
_VRtrPimIfRxRegisterStopErrs_Type = Counter32
_VRtrPimIfRxRegisterStopErrs_Object = MibTableColumn
vRtrPimIfRxRegisterStopErrs = _VRtrPimIfRxRegisterStopErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 26),
    _VRtrPimIfRxRegisterStopErrs_Type()
)
vRtrPimIfRxRegisterStopErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfRxRegisterStopErrs.setStatus("current")
_VRtrPimIfRxCRPAdvNoRouterAlert_Type = Counter32
_VRtrPimIfRxCRPAdvNoRouterAlert_Object = MibTableColumn
vRtrPimIfRxCRPAdvNoRouterAlert = _VRtrPimIfRxCRPAdvNoRouterAlert_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 27),
    _VRtrPimIfRxCRPAdvNoRouterAlert_Type()
)
vRtrPimIfRxCRPAdvNoRouterAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfRxCRPAdvNoRouterAlert.setStatus("current")
_VRtrPimIfRxBsmPdus_Type = Counter32
_VRtrPimIfRxBsmPdus_Object = MibTableColumn
vRtrPimIfRxBsmPdus = _VRtrPimIfRxBsmPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 28),
    _VRtrPimIfRxBsmPdus_Type()
)
vRtrPimIfRxBsmPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfRxBsmPdus.setStatus("current")
_VRtrPimIfRxBsmPduDrops_Type = Counter32
_VRtrPimIfRxBsmPduDrops_Object = MibTableColumn
vRtrPimIfRxBsmPduDrops = _VRtrPimIfRxBsmPduDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 29),
    _VRtrPimIfRxBsmPduDrops_Type()
)
vRtrPimIfRxBsmPduDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfRxBsmPduDrops.setStatus("current")
_VRtrPimIfStarStarRPTypes_Type = Gauge32
_VRtrPimIfStarStarRPTypes_Object = MibTableColumn
vRtrPimIfStarStarRPTypes = _VRtrPimIfStarStarRPTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 30),
    _VRtrPimIfStarStarRPTypes_Type()
)
vRtrPimIfStarStarRPTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfStarStarRPTypes.setStatus("current")
_VRtrPimIfStarGTypes_Type = Gauge32
_VRtrPimIfStarGTypes_Object = MibTableColumn
vRtrPimIfStarGTypes = _VRtrPimIfStarGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 31),
    _VRtrPimIfStarGTypes_Type()
)
vRtrPimIfStarGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfStarGTypes.setStatus("current")
_VRtrPimIfSGTypes_Type = Gauge32
_VRtrPimIfSGTypes_Object = MibTableColumn
vRtrPimIfSGTypes = _VRtrPimIfSGTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 32),
    _VRtrPimIfSGTypes_Type()
)
vRtrPimIfSGTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfSGTypes.setStatus("current")
_VRtrPimIfJoinPolicyDrops_Type = Counter32
_VRtrPimIfJoinPolicyDrops_Object = MibTableColumn
vRtrPimIfJoinPolicyDrops = _VRtrPimIfJoinPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 33),
    _VRtrPimIfJoinPolicyDrops_Type()
)
vRtrPimIfJoinPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfJoinPolicyDrops.setStatus("current")
_VRtrPimIfRegisterPolicyDrops_Type = Counter32
_VRtrPimIfRegisterPolicyDrops_Object = MibTableColumn
vRtrPimIfRegisterPolicyDrops = _VRtrPimIfRegisterPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 34),
    _VRtrPimIfRegisterPolicyDrops_Type()
)
vRtrPimIfRegisterPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfRegisterPolicyDrops.setStatus("current")
_VRtrPimIfBootstrapImpPolicyDrops_Type = Counter32
_VRtrPimIfBootstrapImpPolicyDrops_Object = MibTableColumn
vRtrPimIfBootstrapImpPolicyDrops = _VRtrPimIfBootstrapImpPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 35),
    _VRtrPimIfBootstrapImpPolicyDrops_Type()
)
vRtrPimIfBootstrapImpPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfBootstrapImpPolicyDrops.setStatus("current")
_VRtrPimIfBootstrapExpPolicyDrops_Type = Counter32
_VRtrPimIfBootstrapExpPolicyDrops_Object = MibTableColumn
vRtrPimIfBootstrapExpPolicyDrops = _VRtrPimIfBootstrapExpPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 2, 4, 1, 36),
    _VRtrPimIfBootstrapExpPolicyDrops_Type()
)
vRtrPimIfBootstrapExpPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrPimIfBootstrapExpPolicyDrops.setStatus("current")
_VRtrPimNotificationObjs_ObjectIdentity = ObjectIdentity
vRtrPimNotificationObjs = _VRtrPimNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 24, 3)
)
_VRtrPimNotifications_ObjectIdentity = ObjectIdentity
vRtrPimNotifications = _VRtrPimNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 24, 0)
)
vRtrPimGeneralEntry.registerAugmentions(
    ("TIMETRA-PIM-MIB",
     "vRtrPimGenStatsEntry")
)
vRtrPimGenStatsEntry.setIndexNames(*vRtrPimGeneralEntry.getIndexNames())
vRtrPimGrpSrcEntry.registerAugmentions(
    ("TIMETRA-PIM-MIB",
     "vRtrPimGrpSrcStatsEntry")
)
vRtrPimGrpSrcStatsEntry.setIndexNames(*vRtrPimGrpSrcEntry.getIndexNames())
vRtrPimGeneralEntry.registerAugmentions(
    ("TIMETRA-PIM-MIB",
     "vRtrPimGenPolicyEntry")
)
vRtrPimGenPolicyEntry.setIndexNames(*vRtrPimGeneralEntry.getIndexNames())
vRtrPimIfEntry.registerAugmentions(
    ("TIMETRA-PIM-MIB",
     "vRtrPimIfStatsEntry")
)
vRtrPimIfStatsEntry.setIndexNames(*vRtrPimIfEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-PIM-MIB",
    **{"timetraPimMIBModule": timetraPimMIBModule,
       "tmnxPimObjs": tmnxPimObjs,
       "vRtrPimProtocolObjs": vRtrPimProtocolObjs,
       "vRtrPimGeneralTable": vRtrPimGeneralTable,
       "vRtrPimGeneralEntry": vRtrPimGeneralEntry,
       "vRtrPimGenAdminState": vRtrPimGenAdminState,
       "vRtrPimGenOperState": vRtrPimGenOperState,
       "vRtrPimGenCBSRPriority": vRtrPimGenCBSRPriority,
       "vRtrPimGenCBSRAddress": vRtrPimGenCBSRAddress,
       "vRtrPimGenCBSRAdminState": vRtrPimGenCBSRAdminState,
       "vRtrPimGenCBSROperState": vRtrPimGenCBSROperState,
       "vRtrPimGenBSRAddress": vRtrPimGenBSRAddress,
       "vRtrPimGenBSRPriority": vRtrPimGenBSRPriority,
       "vRtrPimGenBSRExpiryTime": vRtrPimGenBSRExpiryTime,
       "vRtrPimGenBSRState": vRtrPimGenBSRState,
       "vRtrPimGenBSRUpTime": vRtrPimGenBSRUpTime,
       "vRtrPimGenCRPAddress": vRtrPimGenCRPAddress,
       "vRtrPimGenCRPAdminState": vRtrPimGenCRPAdminState,
       "vRtrPimGenCRPOperState": vRtrPimGenCRPOperState,
       "vRtrPimGenCRPHoldtime": vRtrPimGenCRPHoldtime,
       "vRtrPimGenCRPPriority": vRtrPimGenCRPPriority,
       "vRtrPimGenLastChange": vRtrPimGenLastChange,
       "vRtrPimStaticGrpToRPTable": vRtrPimStaticGrpToRPTable,
       "vRtrPimStaticGrpToRPEntry": vRtrPimStaticGrpToRPEntry,
       "vRtrPimStaticGrpToRPRPAddress": vRtrPimStaticGrpToRPRPAddress,
       "vRtrPimStaticGroupAddr": vRtrPimStaticGroupAddr,
       "vRtrPimStaticGroupMask": vRtrPimStaticGroupMask,
       "vRtrPimStaticGrpToRPRowStatus": vRtrPimStaticGrpToRPRowStatus,
       "vRtrPimGrpSrcTable": vRtrPimGrpSrcTable,
       "vRtrPimGrpSrcEntry": vRtrPimGrpSrcEntry,
       "vRtrPimGrpSrcGroupAddress": vRtrPimGrpSrcGroupAddress,
       "vRtrPimGrpSrcSourceAddress": vRtrPimGrpSrcSourceAddress,
       "vRtrPimGrpSrcType": vRtrPimGrpSrcType,
       "vRtrPimGrpSrcRPAddr": vRtrPimGrpSrcRPAddr,
       "vRtrPimGrpSrcRpfNbrAddr": vRtrPimGrpSrcRpfNbrAddr,
       "vRtrPimGrpSrcRpfIfIndex": vRtrPimGrpSrcRpfIfIndex,
       "vRtrPimGrpSrcRptRpfNbrAddr": vRtrPimGrpSrcRptRpfNbrAddr,
       "vRtrPimGrpSrcMRIBNextHopAddr": vRtrPimGrpSrcMRIBNextHopAddr,
       "vRtrPimGrpSrcMRIBSrcFlags": vRtrPimGrpSrcMRIBSrcFlags,
       "vRtrPimGrpSrcFlags": vRtrPimGrpSrcFlags,
       "vRtrPimGrpSrcUpstreamJpState": vRtrPimGrpSrcUpstreamJpState,
       "vRtrPimGrpSrcUpstreamJpTimer": vRtrPimGrpSrcUpstreamJpTimer,
       "vRtrPimGrpSrcUpstreamRptJpState": vRtrPimGrpSrcUpstreamRptJpState,
       "vRtrPimGrpSrcUpstreamRptOverrideTimer": vRtrPimGrpSrcUpstreamRptOverrideTimer,
       "vRtrPimGrpSrcRegisterState": vRtrPimGrpSrcRegisterState,
       "vRtrPimGrpSrcRegisterStopTimer": vRtrPimGrpSrcRegisterStopTimer,
       "vRtrPimGrpSrcKeepaliveTimer": vRtrPimGrpSrcKeepaliveTimer,
       "vRtrPimGrpSrcNumImmediateOif": vRtrPimGrpSrcNumImmediateOif,
       "vRtrPimGrpSrcNumInheritedOif": vRtrPimGrpSrcNumInheritedOif,
       "vRtrPimGrpSrcNumInheritedRptOif": vRtrPimGrpSrcNumInheritedRptOif,
       "vRtrPimGrpSrcNumLocalRxIncludeIf": vRtrPimGrpSrcNumLocalRxIncludeIf,
       "vRtrPimGrpSrcNumLocalRxExcludeIf": vRtrPimGrpSrcNumLocalRxExcludeIf,
       "vRtrPimGrpSrcNumJoinPruneIf": vRtrPimGrpSrcNumJoinPruneIf,
       "vRtrPimGrpSrcNumLostAssertIf": vRtrPimGrpSrcNumLostAssertIf,
       "vRtrPimGrpSrcUpTime": vRtrPimGrpSrcUpTime,
       "vRtrPimGrpSrcIfTable": vRtrPimGrpSrcIfTable,
       "vRtrPimGrpSrcIfEntry": vRtrPimGrpSrcIfEntry,
       "vRtrPimGrpSrcIfFlags": vRtrPimGrpSrcIfFlags,
       "vRtrPimCRPGrpPrefixTable": vRtrPimCRPGrpPrefixTable,
       "vRtrPimCRPGrpPrefixEntry": vRtrPimCRPGrpPrefixEntry,
       "vRtrPimCRPGrpPrefixGrpAddr": vRtrPimCRPGrpPrefixGrpAddr,
       "vRtrPimCRPGrpPrefixGrpMask": vRtrPimCRPGrpPrefixGrpMask,
       "vRtrPimCRPGrpPrefixRowStatus": vRtrPimCRPGrpPrefixRowStatus,
       "vRtrPimCRPTable": vRtrPimCRPTable,
       "vRtrPimCRPEntry": vRtrPimCRPEntry,
       "vRtrPimCRPAddress": vRtrPimCRPAddress,
       "vRtrPimCRPGrpAddr": vRtrPimCRPGrpAddr,
       "vRtrPimCRPGrpMask": vRtrPimCRPGrpMask,
       "vRtrPimCRPHoldtime": vRtrPimCRPHoldtime,
       "vRtrPimCRPPriority": vRtrPimCRPPriority,
       "vRtrPimCRPExpiryTime": vRtrPimCRPExpiryTime,
       "vRtrPimRPSetTable": vRtrPimRPSetTable,
       "vRtrPimRPSetEntry": vRtrPimRPSetEntry,
       "vRtrPimRPSetType": vRtrPimRPSetType,
       "vRtrPimRPSetGrpAddr": vRtrPimRPSetGrpAddr,
       "vRtrPimRPSetGrpMask": vRtrPimRPSetGrpMask,
       "vRtrPimRPSetCRPAddress": vRtrPimRPSetCRPAddress,
       "vRtrPimRPSetHoldtime": vRtrPimRPSetHoldtime,
       "vRtrPimRPSetPriority": vRtrPimRPSetPriority,
       "vRtrPimGenStatsTable": vRtrPimGenStatsTable,
       "vRtrPimGenStatsEntry": vRtrPimGenStatsEntry,
       "vRtrPimGenStatsTxCrpaPdus": vRtrPimGenStatsTxCrpaPdus,
       "vRtrPimGenStatsTxCrpaPduErrs": vRtrPimGenStatsTxCrpaPduErrs,
       "vRtrPimGenStatsRxCrpaPdus": vRtrPimGenStatsRxCrpaPdus,
       "vRtrPimGenStatsRxCrpaPduDrops": vRtrPimGenStatsRxCrpaPduDrops,
       "vRtrPimGenStatsStarStarRPTypes": vRtrPimGenStatsStarStarRPTypes,
       "vRtrPimGenStatsStarGTypes": vRtrPimGenStatsStarGTypes,
       "vRtrPimGenStatsSGTypes": vRtrPimGenStatsSGTypes,
       "vRtrPimGrpSrcStatsTable": vRtrPimGrpSrcStatsTable,
       "vRtrPimGrpSrcStatsEntry": vRtrPimGrpSrcStatsEntry,
       "vRtrPimGrpSrcStatsForwardedPkts": vRtrPimGrpSrcStatsForwardedPkts,
       "vRtrPimGrpSrcStatsDiscardedPkts": vRtrPimGrpSrcStatsDiscardedPkts,
       "vRtrPimGrpSrcStatsRPFMismatches": vRtrPimGrpSrcStatsRPFMismatches,
       "vRtrPimGenPolicyTable": vRtrPimGenPolicyTable,
       "vRtrPimGenPolicyEntry": vRtrPimGenPolicyEntry,
       "vRtrPimImportJoinPrunePolicy1": vRtrPimImportJoinPrunePolicy1,
       "vRtrPimImportJoinPrunePolicy2": vRtrPimImportJoinPrunePolicy2,
       "vRtrPimImportJoinPrunePolicy3": vRtrPimImportJoinPrunePolicy3,
       "vRtrPimImportJoinPrunePolicy4": vRtrPimImportJoinPrunePolicy4,
       "vRtrPimImportJoinPrunePolicy5": vRtrPimImportJoinPrunePolicy5,
       "vRtrPimImportRegisterPolicy1": vRtrPimImportRegisterPolicy1,
       "vRtrPimImportRegisterPolicy2": vRtrPimImportRegisterPolicy2,
       "vRtrPimImportRegisterPolicy3": vRtrPimImportRegisterPolicy3,
       "vRtrPimImportRegisterPolicy4": vRtrPimImportRegisterPolicy4,
       "vRtrPimImportRegisterPolicy5": vRtrPimImportRegisterPolicy5,
       "vRtrPimImportBootstrapPolicy1": vRtrPimImportBootstrapPolicy1,
       "vRtrPimImportBootstrapPolicy2": vRtrPimImportBootstrapPolicy2,
       "vRtrPimImportBootstrapPolicy3": vRtrPimImportBootstrapPolicy3,
       "vRtrPimImportBootstrapPolicy4": vRtrPimImportBootstrapPolicy4,
       "vRtrPimImportBootstrapPolicy5": vRtrPimImportBootstrapPolicy5,
       "vRtrPimExportBootstrapPolicy1": vRtrPimExportBootstrapPolicy1,
       "vRtrPimExportBootstrapPolicy2": vRtrPimExportBootstrapPolicy2,
       "vRtrPimExportBootstrapPolicy3": vRtrPimExportBootstrapPolicy3,
       "vRtrPimExportBootstrapPolicy4": vRtrPimExportBootstrapPolicy4,
       "vRtrPimExportBootstrapPolicy5": vRtrPimExportBootstrapPolicy5,
       "vRtrPimIfObjs": vRtrPimIfObjs,
       "vRtrPimIfTable": vRtrPimIfTable,
       "vRtrPimIfEntry": vRtrPimIfEntry,
       "vRtrPimIfRowStatus": vRtrPimIfRowStatus,
       "vRtrPimIfLastChangeTime": vRtrPimIfLastChangeTime,
       "vRtrPimIfAdminState": vRtrPimIfAdminState,
       "vRtrPimIfOperState": vRtrPimIfOperState,
       "vRtrPimIfDR": vRtrPimIfDR,
       "vRtrPimIfDRPriority": vRtrPimIfDRPriority,
       "vRtrPimIfHelloInterval": vRtrPimIfHelloInterval,
       "vRtrPimIfTrackingSupport": vRtrPimIfTrackingSupport,
       "vRtrPimIfMulticastSenders": vRtrPimIfMulticastSenders,
       "vRtrPimIfNeighborTable": vRtrPimIfNeighborTable,
       "vRtrPimIfNeighborEntry": vRtrPimIfNeighborEntry,
       "vRtrPimIfNeighborAddress": vRtrPimIfNeighborAddress,
       "vRtrPimIfNeighborUpTime": vRtrPimIfNeighborUpTime,
       "vRtrPimIfNeighborExpiryTime": vRtrPimIfNeighborExpiryTime,
       "vRtrPimIfNeighborGenId": vRtrPimIfNeighborGenId,
       "vRtrPimIfNeighborDrPriority": vRtrPimIfNeighborDrPriority,
       "vRtrPimIfNeighborDrPriorityPresent": vRtrPimIfNeighborDrPriorityPresent,
       "vRtrPimIfNeighborLanDelay": vRtrPimIfNeighborLanDelay,
       "vRtrPimIfNeighborLanDelayPresent": vRtrPimIfNeighborLanDelayPresent,
       "vRtrPimIfNeighborTrackingSupport": vRtrPimIfNeighborTrackingSupport,
       "vRtrPimIfNeighborHoldTime": vRtrPimIfNeighborHoldTime,
       "vRtrPimIfNeighborOverrideInterval": vRtrPimIfNeighborOverrideInterval,
       "vRtrPimIfGrpSrcTable": vRtrPimIfGrpSrcTable,
       "vRtrPimIfGrpSrcEntry": vRtrPimIfGrpSrcEntry,
       "vRtrPimIfGrpSrcType": vRtrPimIfGrpSrcType,
       "vRtrPimIfGrpSrcGroupAddress": vRtrPimIfGrpSrcGroupAddress,
       "vRtrPimIfGrpSrcSourceAddress": vRtrPimIfGrpSrcSourceAddress,
       "vRtrPimIfGrpSrcRPAddress": vRtrPimIfGrpSrcRPAddress,
       "vRtrPimIfGrpSrcJPState": vRtrPimIfGrpSrcJPState,
       "vRtrPimIfGrpSrcPrunePendTimer": vRtrPimIfGrpSrcPrunePendTimer,
       "vRtrPimIfGrpSrcJoinPruneTimer": vRtrPimIfGrpSrcJoinPruneTimer,
       "vRtrPimIfGrpSrcJPRptState": vRtrPimIfGrpSrcJPRptState,
       "vRtrPimIfGrpSrcRptPrunePendTimer": vRtrPimIfGrpSrcRptPrunePendTimer,
       "vRtrPimIfGrpSrcRptJoinPruneTimer": vRtrPimIfGrpSrcRptJoinPruneTimer,
       "vRtrPimIfGrpSrcAssertState": vRtrPimIfGrpSrcAssertState,
       "vRtrPimIfGrpSrcAssertTimer": vRtrPimIfGrpSrcAssertTimer,
       "vRtrPimIfGrpSrcAssertMetric": vRtrPimIfGrpSrcAssertMetric,
       "vRtrPimIfGrpSrcAssertMetricPref": vRtrPimIfGrpSrcAssertMetricPref,
       "vRtrPimIfGrpSrcAssertRPTBit": vRtrPimIfGrpSrcAssertRPTBit,
       "vRtrPimIfGrpSrcAssertWinnerMetric": vRtrPimIfGrpSrcAssertWinnerMetric,
       "vRtrPimIfGrpSrcAssertWinnerMetricPref": vRtrPimIfGrpSrcAssertWinnerMetricPref,
       "vRtrPimIfGrpSrcAssertWinnerRPTBit": vRtrPimIfGrpSrcAssertWinnerRPTBit,
       "vRtrPimIfGrpSrcAssertWinnerAddr": vRtrPimIfGrpSrcAssertWinnerAddr,
       "vRtrPimIfStatsTable": vRtrPimIfStatsTable,
       "vRtrPimIfStatsEntry": vRtrPimIfStatsEntry,
       "vRtrPimIfTxPkts": vRtrPimIfTxPkts,
       "vRtrPimIfTxHellos": vRtrPimIfTxHellos,
       "vRtrPimIfTxAsserts": vRtrPimIfTxAsserts,
       "vRtrPimIfTxRegisters": vRtrPimIfTxRegisters,
       "vRtrPimIfTxRegisterErrs": vRtrPimIfTxRegisterErrs,
       "vRtrPimIfTxNullRegisters": vRtrPimIfTxNullRegisters,
       "vRtrPimIfTxRegisterStops": vRtrPimIfTxRegisterStops,
       "vRtrPimIfTxRegisterStopErrs": vRtrPimIfTxRegisterStopErrs,
       "vRtrPimIfTxRegisterTTLDrops": vRtrPimIfTxRegisterTTLDrops,
       "vRtrPimIfTxRegisterMtuDrops": vRtrPimIfTxRegisterMtuDrops,
       "vRtrPimIfTxBsmPdus": vRtrPimIfTxBsmPdus,
       "vRtrPimIfTxBsmErrs": vRtrPimIfTxBsmErrs,
       "vRtrPimIfRxPkts": vRtrPimIfRxPkts,
       "vRtrPimIfRxHellos": vRtrPimIfRxHellos,
       "vRtrPimIfRxHellosDropped": vRtrPimIfRxHellosDropped,
       "vRtrPimIfRxNbrUnknown": vRtrPimIfRxNbrUnknown,
       "vRtrPimIfRxBadChecksumDiscards": vRtrPimIfRxBadChecksumDiscards,
       "vRtrPimIfRxBadVersionDiscards": vRtrPimIfRxBadVersionDiscards,
       "vRtrPimIfRxBadEncodings": vRtrPimIfRxBadEncodings,
       "vRtrPimIfRxAsserts": vRtrPimIfRxAsserts,
       "vRtrPimIfRxAssertErrs": vRtrPimIfRxAssertErrs,
       "vRtrPimIfRxRegisters": vRtrPimIfRxRegisters,
       "vRtrPimIfRxRegisterErrs": vRtrPimIfRxRegisterErrs,
       "vRtrPimIfRxNullRegisters": vRtrPimIfRxNullRegisters,
       "vRtrPimIfRxRegisterStops": vRtrPimIfRxRegisterStops,
       "vRtrPimIfRxRegisterStopErrs": vRtrPimIfRxRegisterStopErrs,
       "vRtrPimIfRxCRPAdvNoRouterAlert": vRtrPimIfRxCRPAdvNoRouterAlert,
       "vRtrPimIfRxBsmPdus": vRtrPimIfRxBsmPdus,
       "vRtrPimIfRxBsmPduDrops": vRtrPimIfRxBsmPduDrops,
       "vRtrPimIfStarStarRPTypes": vRtrPimIfStarStarRPTypes,
       "vRtrPimIfStarGTypes": vRtrPimIfStarGTypes,
       "vRtrPimIfSGTypes": vRtrPimIfSGTypes,
       "vRtrPimIfJoinPolicyDrops": vRtrPimIfJoinPolicyDrops,
       "vRtrPimIfRegisterPolicyDrops": vRtrPimIfRegisterPolicyDrops,
       "vRtrPimIfBootstrapImpPolicyDrops": vRtrPimIfBootstrapImpPolicyDrops,
       "vRtrPimIfBootstrapExpPolicyDrops": vRtrPimIfBootstrapExpPolicyDrops,
       "vRtrPimNotificationObjs": vRtrPimNotificationObjs,
       "vRtrPimNotifications": vRtrPimNotifications}
)
