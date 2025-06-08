# SNMP MIB module (MPOA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/atmforum_353/MPOA-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:06:53 2025
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

(AtmAddr,) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmAddr")

(atmForumNetworkManagement,
 lecIndex) = mibBuilder.importSymbols(
    "LAN-EMULATION-CLIENT-MIB",
    "atmForumNetworkManagement",
    "lecIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions



class LecIndex(Integer32):
    """Custom type LecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )





class AtmConfigAddr(OctetString):
    """Custom type AtmConfigAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )





class InternetworkAddrType(Integer32):
    """Custom type InternetworkAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("ipV4", 1),
          ("ipV6", 2),
          ("nsap", 3),
          ("hdlc", 4),
          ("bbn1822", 5),
          ("ieee802", 6),
          ("e163", 7),
          ("e164", 8),
          ("f69", 9),
          ("x121", 10),
          ("ipx", 11),
          ("appleTalk", 12),
          ("decnetIV", 13),
          ("banyanVines", 14),
          ("e164WithNsap", 15))
    )





class InternetworkAddr(OctetString):
    """Custom type InternetworkAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )





class MpcIndex(Integer32):
    """Custom type MpcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )





class MpsIndex(Integer32):
    """Custom type MpsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtmfMpoa_ObjectIdentity = ObjectIdentity
atmfMpoa = _AtmfMpoa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8)
)
_MpoaMIB_ObjectIdentity = ObjectIdentity
mpoaMIB = _MpoaMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1)
)
_MpoaMIBObjects_ObjectIdentity = ObjectIdentity
mpoaMIBObjects = _MpoaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1)
)
_MpoaCommonObjects_ObjectIdentity = ObjectIdentity
mpoaCommonObjects = _MpoaCommonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 1)
)
_DeviceTypeTable_Object = MibTable
deviceTypeTable = _DeviceTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    deviceTypeTable.setStatus("mandatory")
_DeviceTypeEntry_Object = MibTableRow
deviceTypeEntry = _DeviceTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 1, 1, 1)
)
deviceTypeEntry.setIndexNames(
    (0, "MPOA-MIB", "deviceTypeIndex"),
)
if mibBuilder.loadTexts:
    deviceTypeEntry.setStatus("mandatory")


class _DeviceTypeIndex_Type(Integer32):
    """Custom type deviceTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DeviceTypeIndex_Type.__name__ = "Integer32"
_DeviceTypeIndex_Object = MibTableColumn
deviceTypeIndex = _DeviceTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 1, 1, 1, 1),
    _DeviceTypeIndex_Type()
)
deviceTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTypeIndex.setStatus("mandatory")
_DeviceTypeLecIndex_Type = LecIndex
_DeviceTypeLecIndex_Object = MibTableColumn
deviceTypeLecIndex = _DeviceTypeLecIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 1, 1, 1, 2),
    _DeviceTypeLecIndex_Type()
)
deviceTypeLecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTypeLecIndex.setStatus("mandatory")
_DeviceTypeRemoteLecAtmAddress_Type = AtmAddr
_DeviceTypeRemoteLecAtmAddress_Object = MibTableColumn
deviceTypeRemoteLecAtmAddress = _DeviceTypeRemoteLecAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 1, 1, 1, 3),
    _DeviceTypeRemoteLecAtmAddress_Type()
)
deviceTypeRemoteLecAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTypeRemoteLecAtmAddress.setStatus("mandatory")


class _DeviceTypeType_Type(Integer32):
    """Custom type deviceTypeType based on Integer32"""
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
        *(("nonMpoa", 1),
          ("mps", 2),
          ("mpc", 3),
          ("mpsAndMpc", 4))
    )


_DeviceTypeType_Type.__name__ = "Integer32"
_DeviceTypeType_Object = MibTableColumn
deviceTypeType = _DeviceTypeType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 1, 1, 1, 4),
    _DeviceTypeType_Type()
)
deviceTypeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTypeType.setStatus("mandatory")
_DeviceTypeMpsAtmAddress_Type = AtmAddr
_DeviceTypeMpsAtmAddress_Object = MibTableColumn
deviceTypeMpsAtmAddress = _DeviceTypeMpsAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 1, 1, 1, 5),
    _DeviceTypeMpsAtmAddress_Type()
)
deviceTypeMpsAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTypeMpsAtmAddress.setStatus("mandatory")
_DeviceTypeMpcAtmAddress_Type = AtmAddr
_DeviceTypeMpcAtmAddress_Object = MibTableColumn
deviceTypeMpcAtmAddress = _DeviceTypeMpcAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 1, 1, 1, 6),
    _DeviceTypeMpcAtmAddress_Type()
)
deviceTypeMpcAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTypeMpcAtmAddress.setStatus("mandatory")
_DeviceTypeMpsMacAddressTable_Object = MibTable
deviceTypeMpsMacAddressTable = _DeviceTypeMpsMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    deviceTypeMpsMacAddressTable.setStatus("mandatory")
_DeviceTypeMpsMacAddressEntry_Object = MibTableRow
deviceTypeMpsMacAddressEntry = _DeviceTypeMpsMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 1, 2, 1)
)
deviceTypeMpsMacAddressEntry.setIndexNames(
    (0, "MPOA-MIB", "deviceTypeIndex"),
    (0, "MPOA-MIB", "deviceTypeMpsMacAddress"),
)
if mibBuilder.loadTexts:
    deviceTypeMpsMacAddressEntry.setStatus("mandatory")
_DeviceTypeMpsMacAddress_Type = MacAddress
_DeviceTypeMpsMacAddress_Object = MibTableColumn
deviceTypeMpsMacAddress = _DeviceTypeMpsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 1, 2, 1, 1),
    _DeviceTypeMpsMacAddress_Type()
)
deviceTypeMpsMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTypeMpsMacAddress.setStatus("mandatory")
_MpcObjects_ObjectIdentity = ObjectIdentity
mpcObjects = _MpcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2)
)


class _MpcNextIndex_Type(Integer32):
    """Custom type mpcNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MpcNextIndex_Type.__name__ = "Integer32"
_MpcNextIndex_Object = MibScalar
mpcNextIndex = _MpcNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 1),
    _MpcNextIndex_Type()
)
mpcNextIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpcNextIndex.setStatus("mandatory")
_MpcConfigTable_Object = MibTable
mpcConfigTable = _MpcConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mpcConfigTable.setStatus("mandatory")
_MpcConfigEntry_Object = MibTableRow
mpcConfigEntry = _MpcConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 2, 1)
)
mpcConfigEntry.setIndexNames(
    (0, "MPOA-MIB", "mpcIndex"),
)
if mibBuilder.loadTexts:
    mpcConfigEntry.setStatus("mandatory")
_MpcIndex_Type = MpcIndex
_MpcIndex_Object = MibTableColumn
mpcIndex = _MpcIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 2, 1, 1),
    _MpcIndex_Type()
)
mpcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIndex.setStatus("mandatory")
_MpcRowStatus_Type = RowStatus
_MpcRowStatus_Object = MibTableColumn
mpcRowStatus = _MpcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 2, 1, 2),
    _MpcRowStatus_Type()
)
mpcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpcRowStatus.setStatus("mandatory")


class _MpcConfigMode_Type(Integer32):
    """Custom type mpcConfigMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_MpcConfigMode_Type.__name__ = "Integer32"
_MpcConfigMode_Object = MibTableColumn
mpcConfigMode = _MpcConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 2, 1, 3),
    _MpcConfigMode_Type()
)
mpcConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpcConfigMode.setStatus("mandatory")
_MpcCtrlAtmAddr_Type = AtmConfigAddr
_MpcCtrlAtmAddr_Object = MibTableColumn
mpcCtrlAtmAddr = _MpcCtrlAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 2, 1, 4),
    _MpcCtrlAtmAddr_Type()
)
mpcCtrlAtmAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpcCtrlAtmAddr.setStatus("mandatory")


class _MpcSCSetupFrameCount_Type(Integer32):
    """Custom type mpcSCSetupFrameCount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MpcSCSetupFrameCount_Type.__name__ = "Integer32"
_MpcSCSetupFrameCount_Object = MibTableColumn
mpcSCSetupFrameCount = _MpcSCSetupFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 2, 1, 5),
    _MpcSCSetupFrameCount_Type()
)
mpcSCSetupFrameCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpcSCSetupFrameCount.setStatus("mandatory")


class _MpcSCSetupFrameTime_Type(Integer32):
    """Custom type mpcSCSetupFrameTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_MpcSCSetupFrameTime_Type.__name__ = "Integer32"
_MpcSCSetupFrameTime_Object = MibTableColumn
mpcSCSetupFrameTime = _MpcSCSetupFrameTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 2, 1, 6),
    _MpcSCSetupFrameTime_Type()
)
mpcSCSetupFrameTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpcSCSetupFrameTime.setStatus("mandatory")


class _MpcInitialRetryTime_Type(Integer32):
    """Custom type mpcInitialRetryTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_MpcInitialRetryTime_Type.__name__ = "Integer32"
_MpcInitialRetryTime_Object = MibTableColumn
mpcInitialRetryTime = _MpcInitialRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 2, 1, 7),
    _MpcInitialRetryTime_Type()
)
mpcInitialRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpcInitialRetryTime.setStatus("mandatory")


class _MpcRetryTimeMaximum_Type(Integer32):
    """Custom type mpcRetryTimeMaximum based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_MpcRetryTimeMaximum_Type.__name__ = "Integer32"
_MpcRetryTimeMaximum_Object = MibTableColumn
mpcRetryTimeMaximum = _MpcRetryTimeMaximum_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 2, 1, 8),
    _MpcRetryTimeMaximum_Type()
)
mpcRetryTimeMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpcRetryTimeMaximum.setStatus("mandatory")


class _MpcHoldDownTime_Type(Integer32):
    """Custom type mpcHoldDownTime based on Integer32"""
    defaultValue = 160

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1200),
    )


_MpcHoldDownTime_Type.__name__ = "Integer32"
_MpcHoldDownTime_Object = MibTableColumn
mpcHoldDownTime = _MpcHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 2, 1, 9),
    _MpcHoldDownTime_Type()
)
mpcHoldDownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpcHoldDownTime.setStatus("mandatory")
_MpcActualTable_Object = MibTable
mpcActualTable = _MpcActualTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mpcActualTable.setStatus("mandatory")
_MpcActualEntry_Object = MibTableRow
mpcActualEntry = _MpcActualEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 3, 1)
)
mpcActualEntry.setIndexNames(
    (0, "MPOA-MIB", "mpcIndex"),
)
if mibBuilder.loadTexts:
    mpcActualEntry.setStatus("mandatory")


class _MpcActualState_Type(Integer32):
    """Custom type mpcActualState based on Integer32"""
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
          ("initialState", 2),
          ("up", 3),
          ("down", 4))
    )


_MpcActualState_Type.__name__ = "Integer32"
_MpcActualState_Object = MibTableColumn
mpcActualState = _MpcActualState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 3, 1, 1),
    _MpcActualState_Type()
)
mpcActualState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcActualState.setStatus("mandatory")
_MpcDiscontinuityTime_Type = TimeStamp
_MpcDiscontinuityTime_Object = MibTableColumn
mpcDiscontinuityTime = _MpcDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 3, 1, 2),
    _MpcDiscontinuityTime_Type()
)
mpcDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcDiscontinuityTime.setStatus("mandatory")


class _MpcActualConfigMode_Type(Integer32):
    """Custom type mpcActualConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_MpcActualConfigMode_Type.__name__ = "Integer32"
_MpcActualConfigMode_Object = MibTableColumn
mpcActualConfigMode = _MpcActualConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 3, 1, 3),
    _MpcActualConfigMode_Type()
)
mpcActualConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcActualConfigMode.setStatus("mandatory")


class _MpcActualSCSetupFrameCount_Type(Integer32):
    """Custom type mpcActualSCSetupFrameCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MpcActualSCSetupFrameCount_Type.__name__ = "Integer32"
_MpcActualSCSetupFrameCount_Object = MibTableColumn
mpcActualSCSetupFrameCount = _MpcActualSCSetupFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 3, 1, 4),
    _MpcActualSCSetupFrameCount_Type()
)
mpcActualSCSetupFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcActualSCSetupFrameCount.setStatus("mandatory")


class _MpcActualSCSetupFrameTime_Type(Integer32):
    """Custom type mpcActualSCSetupFrameTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_MpcActualSCSetupFrameTime_Type.__name__ = "Integer32"
_MpcActualSCSetupFrameTime_Object = MibTableColumn
mpcActualSCSetupFrameTime = _MpcActualSCSetupFrameTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 3, 1, 5),
    _MpcActualSCSetupFrameTime_Type()
)
mpcActualSCSetupFrameTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcActualSCSetupFrameTime.setStatus("mandatory")


class _MpcActualInitialRetryTime_Type(Integer32):
    """Custom type mpcActualInitialRetryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_MpcActualInitialRetryTime_Type.__name__ = "Integer32"
_MpcActualInitialRetryTime_Object = MibTableColumn
mpcActualInitialRetryTime = _MpcActualInitialRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 3, 1, 6),
    _MpcActualInitialRetryTime_Type()
)
mpcActualInitialRetryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcActualInitialRetryTime.setStatus("mandatory")


class _MpcActualRetryTimeMaximum_Type(Integer32):
    """Custom type mpcActualRetryTimeMaximum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_MpcActualRetryTimeMaximum_Type.__name__ = "Integer32"
_MpcActualRetryTimeMaximum_Object = MibTableColumn
mpcActualRetryTimeMaximum = _MpcActualRetryTimeMaximum_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 3, 1, 7),
    _MpcActualRetryTimeMaximum_Type()
)
mpcActualRetryTimeMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcActualRetryTimeMaximum.setStatus("mandatory")


class _MpcActualHoldDownTime_Type(Integer32):
    """Custom type mpcActualHoldDownTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1200),
    )


_MpcActualHoldDownTime_Type.__name__ = "Integer32"
_MpcActualHoldDownTime_Object = MibTableColumn
mpcActualHoldDownTime = _MpcActualHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 3, 1, 8),
    _MpcActualHoldDownTime_Type()
)
mpcActualHoldDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcActualHoldDownTime.setStatus("mandatory")
_MpcDataAtmAddressTable_Object = MibTable
mpcDataAtmAddressTable = _MpcDataAtmAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    mpcDataAtmAddressTable.setStatus("mandatory")
_MpcDataAtmAddressEntry_Object = MibTableRow
mpcDataAtmAddressEntry = _MpcDataAtmAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 4, 1)
)
mpcDataAtmAddressEntry.setIndexNames(
    (0, "MPOA-MIB", "mpcIndex"),
    (0, "MPOA-MIB", "mpcDataAtmAddress"),
)
if mibBuilder.loadTexts:
    mpcDataAtmAddressEntry.setStatus("mandatory")
_MpcDataAtmAddress_Type = AtmAddr
_MpcDataAtmAddress_Object = MibTableColumn
mpcDataAtmAddress = _MpcDataAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 4, 1, 1),
    _MpcDataAtmAddress_Type()
)
mpcDataAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcDataAtmAddress.setStatus("mandatory")
_MpcDataAtmAddressRowStatus_Type = RowStatus
_MpcDataAtmAddressRowStatus_Object = MibTableColumn
mpcDataAtmAddressRowStatus = _MpcDataAtmAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 4, 1, 2),
    _MpcDataAtmAddressRowStatus_Type()
)
mpcDataAtmAddressRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpcDataAtmAddressRowStatus.setStatus("mandatory")
_MpcStatisticsTable_Object = MibTable
mpcStatisticsTable = _MpcStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    mpcStatisticsTable.setStatus("mandatory")
_MpcStatisticsEntry_Object = MibTableRow
mpcStatisticsEntry = _MpcStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1)
)
mpcStatisticsEntry.setIndexNames(
    (0, "MPOA-MIB", "mpcIndex"),
)
if mibBuilder.loadTexts:
    mpcStatisticsEntry.setStatus("mandatory")
_MpcStatTxMpoaResolveRequests_Type = Counter32
_MpcStatTxMpoaResolveRequests_Object = MibTableColumn
mpcStatTxMpoaResolveRequests = _MpcStatTxMpoaResolveRequests_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 1),
    _MpcStatTxMpoaResolveRequests_Type()
)
mpcStatTxMpoaResolveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatTxMpoaResolveRequests.setStatus("mandatory")
_MpcStatRxMpoaResolveReplyAcks_Type = Counter32
_MpcStatRxMpoaResolveReplyAcks_Object = MibTableColumn
mpcStatRxMpoaResolveReplyAcks = _MpcStatRxMpoaResolveReplyAcks_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 2),
    _MpcStatRxMpoaResolveReplyAcks_Type()
)
mpcStatRxMpoaResolveReplyAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxMpoaResolveReplyAcks.setStatus("mandatory")
_MpcStatRxMpoaResolveReplyInsufECResources_Type = Counter32
_MpcStatRxMpoaResolveReplyInsufECResources_Object = MibTableColumn
mpcStatRxMpoaResolveReplyInsufECResources = _MpcStatRxMpoaResolveReplyInsufECResources_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 3),
    _MpcStatRxMpoaResolveReplyInsufECResources_Type()
)
mpcStatRxMpoaResolveReplyInsufECResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxMpoaResolveReplyInsufECResources.setStatus("mandatory")
_MpcStatRxMpoaResolveReplyInsufSCResources_Type = Counter32
_MpcStatRxMpoaResolveReplyInsufSCResources_Object = MibTableColumn
mpcStatRxMpoaResolveReplyInsufSCResources = _MpcStatRxMpoaResolveReplyInsufSCResources_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 4),
    _MpcStatRxMpoaResolveReplyInsufSCResources_Type()
)
mpcStatRxMpoaResolveReplyInsufSCResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxMpoaResolveReplyInsufSCResources.setStatus("mandatory")
_MpcStatRxMpoaResolveReplyInsufEitherResources_Type = Counter32
_MpcStatRxMpoaResolveReplyInsufEitherResources_Object = MibTableColumn
mpcStatRxMpoaResolveReplyInsufEitherResources = _MpcStatRxMpoaResolveReplyInsufEitherResources_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 5),
    _MpcStatRxMpoaResolveReplyInsufEitherResources_Type()
)
mpcStatRxMpoaResolveReplyInsufEitherResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxMpoaResolveReplyInsufEitherResources.setStatus("mandatory")
_MpcStatRxMpoaResolveReplyUnsupportedInetProt_Type = Counter32
_MpcStatRxMpoaResolveReplyUnsupportedInetProt_Object = MibTableColumn
mpcStatRxMpoaResolveReplyUnsupportedInetProt = _MpcStatRxMpoaResolveReplyUnsupportedInetProt_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 6),
    _MpcStatRxMpoaResolveReplyUnsupportedInetProt_Type()
)
mpcStatRxMpoaResolveReplyUnsupportedInetProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxMpoaResolveReplyUnsupportedInetProt.setStatus("mandatory")
_MpcStatRxMpoaResolveReplyUnsupportedMacEncaps_Type = Counter32
_MpcStatRxMpoaResolveReplyUnsupportedMacEncaps_Object = MibTableColumn
mpcStatRxMpoaResolveReplyUnsupportedMacEncaps = _MpcStatRxMpoaResolveReplyUnsupportedMacEncaps_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 7),
    _MpcStatRxMpoaResolveReplyUnsupportedMacEncaps_Type()
)
mpcStatRxMpoaResolveReplyUnsupportedMacEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxMpoaResolveReplyUnsupportedMacEncaps.setStatus("mandatory")
_MpcStatRxMpoaResolveReplyUnspecifiedOther_Type = Counter32
_MpcStatRxMpoaResolveReplyUnspecifiedOther_Object = MibTableColumn
mpcStatRxMpoaResolveReplyUnspecifiedOther = _MpcStatRxMpoaResolveReplyUnspecifiedOther_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 8),
    _MpcStatRxMpoaResolveReplyUnspecifiedOther_Type()
)
mpcStatRxMpoaResolveReplyUnspecifiedOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxMpoaResolveReplyUnspecifiedOther.setStatus("mandatory")
_MpcStatRxMpoaImpRequests_Type = Counter32
_MpcStatRxMpoaImpRequests_Object = MibTableColumn
mpcStatRxMpoaImpRequests = _MpcStatRxMpoaImpRequests_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 9),
    _MpcStatRxMpoaImpRequests_Type()
)
mpcStatRxMpoaImpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxMpoaImpRequests.setStatus("mandatory")
_MpcStatTxMpoaImpReplyAcks_Type = Counter32
_MpcStatTxMpoaImpReplyAcks_Object = MibTableColumn
mpcStatTxMpoaImpReplyAcks = _MpcStatTxMpoaImpReplyAcks_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 10),
    _MpcStatTxMpoaImpReplyAcks_Type()
)
mpcStatTxMpoaImpReplyAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatTxMpoaImpReplyAcks.setStatus("mandatory")
_MpcStatTxMpoaImpReplyInsufECResources_Type = Counter32
_MpcStatTxMpoaImpReplyInsufECResources_Object = MibTableColumn
mpcStatTxMpoaImpReplyInsufECResources = _MpcStatTxMpoaImpReplyInsufECResources_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 11),
    _MpcStatTxMpoaImpReplyInsufECResources_Type()
)
mpcStatTxMpoaImpReplyInsufECResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatTxMpoaImpReplyInsufECResources.setStatus("mandatory")
_MpcStatTxMpoaImpReplyInsufSCResources_Type = Counter32
_MpcStatTxMpoaImpReplyInsufSCResources_Object = MibTableColumn
mpcStatTxMpoaImpReplyInsufSCResources = _MpcStatTxMpoaImpReplyInsufSCResources_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 12),
    _MpcStatTxMpoaImpReplyInsufSCResources_Type()
)
mpcStatTxMpoaImpReplyInsufSCResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatTxMpoaImpReplyInsufSCResources.setStatus("mandatory")
_MpcStatTxMpoaImpReplyInsufEitherResources_Type = Counter32
_MpcStatTxMpoaImpReplyInsufEitherResources_Object = MibTableColumn
mpcStatTxMpoaImpReplyInsufEitherResources = _MpcStatTxMpoaImpReplyInsufEitherResources_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 13),
    _MpcStatTxMpoaImpReplyInsufEitherResources_Type()
)
mpcStatTxMpoaImpReplyInsufEitherResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatTxMpoaImpReplyInsufEitherResources.setStatus("mandatory")
_MpcStatTxMpoaImpReplyUnsupportedInetProt_Type = Counter32
_MpcStatTxMpoaImpReplyUnsupportedInetProt_Object = MibTableColumn
mpcStatTxMpoaImpReplyUnsupportedInetProt = _MpcStatTxMpoaImpReplyUnsupportedInetProt_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 14),
    _MpcStatTxMpoaImpReplyUnsupportedInetProt_Type()
)
mpcStatTxMpoaImpReplyUnsupportedInetProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatTxMpoaImpReplyUnsupportedInetProt.setStatus("mandatory")
_MpcStatTxMpoaImpReplyUnsupportedMacEncaps_Type = Counter32
_MpcStatTxMpoaImpReplyUnsupportedMacEncaps_Object = MibTableColumn
mpcStatTxMpoaImpReplyUnsupportedMacEncaps = _MpcStatTxMpoaImpReplyUnsupportedMacEncaps_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 15),
    _MpcStatTxMpoaImpReplyUnsupportedMacEncaps_Type()
)
mpcStatTxMpoaImpReplyUnsupportedMacEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatTxMpoaImpReplyUnsupportedMacEncaps.setStatus("mandatory")
_MpcStatTxMpoaImpReplyUnspecifiedOther_Type = Counter32
_MpcStatTxMpoaImpReplyUnspecifiedOther_Object = MibTableColumn
mpcStatTxMpoaImpReplyUnspecifiedOther = _MpcStatTxMpoaImpReplyUnspecifiedOther_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 16),
    _MpcStatTxMpoaImpReplyUnspecifiedOther_Type()
)
mpcStatTxMpoaImpReplyUnspecifiedOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatTxMpoaImpReplyUnspecifiedOther.setStatus("mandatory")
_MpcStatTxMpoaEgressCachePurgeRequests_Type = Counter32
_MpcStatTxMpoaEgressCachePurgeRequests_Object = MibTableColumn
mpcStatTxMpoaEgressCachePurgeRequests = _MpcStatTxMpoaEgressCachePurgeRequests_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 17),
    _MpcStatTxMpoaEgressCachePurgeRequests_Type()
)
mpcStatTxMpoaEgressCachePurgeRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatTxMpoaEgressCachePurgeRequests.setStatus("mandatory")
_MpcStatRxMpoaEgressCachePurgeReplies_Type = Counter32
_MpcStatRxMpoaEgressCachePurgeReplies_Object = MibTableColumn
mpcStatRxMpoaEgressCachePurgeReplies = _MpcStatRxMpoaEgressCachePurgeReplies_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 18),
    _MpcStatRxMpoaEgressCachePurgeReplies_Type()
)
mpcStatRxMpoaEgressCachePurgeReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxMpoaEgressCachePurgeReplies.setStatus("mandatory")
_MpcStatRxMpoaKeepAlives_Type = Counter32
_MpcStatRxMpoaKeepAlives_Object = MibTableColumn
mpcStatRxMpoaKeepAlives = _MpcStatRxMpoaKeepAlives_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 19),
    _MpcStatRxMpoaKeepAlives_Type()
)
mpcStatRxMpoaKeepAlives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxMpoaKeepAlives.setStatus("mandatory")
_MpcStatRxMpoaTriggers_Type = Counter32
_MpcStatRxMpoaTriggers_Object = MibTableColumn
mpcStatRxMpoaTriggers = _MpcStatRxMpoaTriggers_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 20),
    _MpcStatRxMpoaTriggers_Type()
)
mpcStatRxMpoaTriggers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxMpoaTriggers.setStatus("mandatory")
_MpcStatRxMpoaDataPlanePurges_Type = Counter32
_MpcStatRxMpoaDataPlanePurges_Object = MibTableColumn
mpcStatRxMpoaDataPlanePurges = _MpcStatRxMpoaDataPlanePurges_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 21),
    _MpcStatRxMpoaDataPlanePurges_Type()
)
mpcStatRxMpoaDataPlanePurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxMpoaDataPlanePurges.setStatus("mandatory")
_MpcStatTxMpoaDataPlanePurges_Type = Counter32
_MpcStatTxMpoaDataPlanePurges_Object = MibTableColumn
mpcStatTxMpoaDataPlanePurges = _MpcStatTxMpoaDataPlanePurges_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 22),
    _MpcStatTxMpoaDataPlanePurges_Type()
)
mpcStatTxMpoaDataPlanePurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatTxMpoaDataPlanePurges.setStatus("mandatory")
_MpcStatRxNhrpPurgeRequests_Type = Counter32
_MpcStatRxNhrpPurgeRequests_Object = MibTableColumn
mpcStatRxNhrpPurgeRequests = _MpcStatRxNhrpPurgeRequests_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 23),
    _MpcStatRxNhrpPurgeRequests_Type()
)
mpcStatRxNhrpPurgeRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxNhrpPurgeRequests.setStatus("mandatory")
_MpcStatTxNhrpPurgeReplies_Type = Counter32
_MpcStatTxNhrpPurgeReplies_Object = MibTableColumn
mpcStatTxNhrpPurgeReplies = _MpcStatTxNhrpPurgeReplies_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 24),
    _MpcStatTxNhrpPurgeReplies_Type()
)
mpcStatTxNhrpPurgeReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatTxNhrpPurgeReplies.setStatus("mandatory")
_MpcStatRxErrUnrecognizedExtensions_Type = Counter32
_MpcStatRxErrUnrecognizedExtensions_Object = MibTableColumn
mpcStatRxErrUnrecognizedExtensions = _MpcStatRxErrUnrecognizedExtensions_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 25),
    _MpcStatRxErrUnrecognizedExtensions_Type()
)
mpcStatRxErrUnrecognizedExtensions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxErrUnrecognizedExtensions.setStatus("mandatory")
_MpcStatRxErrLoopDetecteds_Type = Counter32
_MpcStatRxErrLoopDetecteds_Object = MibTableColumn
mpcStatRxErrLoopDetecteds = _MpcStatRxErrLoopDetecteds_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 26),
    _MpcStatRxErrLoopDetecteds_Type()
)
mpcStatRxErrLoopDetecteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxErrLoopDetecteds.setStatus("mandatory")
_MpcStatRxErrProtoAddrUnreachables_Type = Counter32
_MpcStatRxErrProtoAddrUnreachables_Object = MibTableColumn
mpcStatRxErrProtoAddrUnreachables = _MpcStatRxErrProtoAddrUnreachables_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 27),
    _MpcStatRxErrProtoAddrUnreachables_Type()
)
mpcStatRxErrProtoAddrUnreachables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxErrProtoAddrUnreachables.setStatus("mandatory")
_MpcStatRxErrProtoErrors_Type = Counter32
_MpcStatRxErrProtoErrors_Object = MibTableColumn
mpcStatRxErrProtoErrors = _MpcStatRxErrProtoErrors_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 28),
    _MpcStatRxErrProtoErrors_Type()
)
mpcStatRxErrProtoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxErrProtoErrors.setStatus("mandatory")
_MpcStatRxErrSduSizeExceededs_Type = Counter32
_MpcStatRxErrSduSizeExceededs_Object = MibTableColumn
mpcStatRxErrSduSizeExceededs = _MpcStatRxErrSduSizeExceededs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 29),
    _MpcStatRxErrSduSizeExceededs_Type()
)
mpcStatRxErrSduSizeExceededs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxErrSduSizeExceededs.setStatus("mandatory")
_MpcStatRxErrInvalidExtensions_Type = Counter32
_MpcStatRxErrInvalidExtensions_Object = MibTableColumn
mpcStatRxErrInvalidExtensions = _MpcStatRxErrInvalidExtensions_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 30),
    _MpcStatRxErrInvalidExtensions_Type()
)
mpcStatRxErrInvalidExtensions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxErrInvalidExtensions.setStatus("mandatory")
_MpcStatRxErrInvalidReplies_Type = Counter32
_MpcStatRxErrInvalidReplies_Object = MibTableColumn
mpcStatRxErrInvalidReplies = _MpcStatRxErrInvalidReplies_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 31),
    _MpcStatRxErrInvalidReplies_Type()
)
mpcStatRxErrInvalidReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxErrInvalidReplies.setStatus("mandatory")
_MpcStatRxErrAuthenticationFailures_Type = Counter32
_MpcStatRxErrAuthenticationFailures_Object = MibTableColumn
mpcStatRxErrAuthenticationFailures = _MpcStatRxErrAuthenticationFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 32),
    _MpcStatRxErrAuthenticationFailures_Type()
)
mpcStatRxErrAuthenticationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxErrAuthenticationFailures.setStatus("mandatory")
_MpcStatRxErrHopCountExceededs_Type = Counter32
_MpcStatRxErrHopCountExceededs_Object = MibTableColumn
mpcStatRxErrHopCountExceededs = _MpcStatRxErrHopCountExceededs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 33),
    _MpcStatRxErrHopCountExceededs_Type()
)
mpcStatRxErrHopCountExceededs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxErrHopCountExceededs.setStatus("mandatory")
_MpcProtocolTable_Object = MibTable
mpcProtocolTable = _MpcProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    mpcProtocolTable.setStatus("mandatory")
_MpcProtocolEntry_Object = MibTableRow
mpcProtocolEntry = _MpcProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 6, 1)
)
mpcProtocolEntry.setIndexNames(
    (0, "MPOA-MIB", "mpcIndex"),
    (0, "MPOA-MIB", "mpcFlowDetectProtocol"),
)
if mibBuilder.loadTexts:
    mpcProtocolEntry.setStatus("mandatory")
_MpcFlowDetectProtocol_Type = InternetworkAddrType
_MpcFlowDetectProtocol_Object = MibTableColumn
mpcFlowDetectProtocol = _MpcFlowDetectProtocol_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 6, 1, 1),
    _MpcFlowDetectProtocol_Type()
)
mpcFlowDetectProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcFlowDetectProtocol.setStatus("mandatory")
_MpcLECSValue_Type = TruthValue
_MpcLECSValue_Object = MibTableColumn
mpcLECSValue = _MpcLECSValue_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 6, 1, 2),
    _MpcLECSValue_Type()
)
mpcLECSValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcLECSValue.setStatus("mandatory")
_MpcProtocolRowStatus_Type = RowStatus
_MpcProtocolRowStatus_Object = MibTableColumn
mpcProtocolRowStatus = _MpcProtocolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 6, 1, 3),
    _MpcProtocolRowStatus_Type()
)
mpcProtocolRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpcProtocolRowStatus.setStatus("mandatory")
_MpcMappingTable_Object = MibTable
mpcMappingTable = _MpcMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 7)
)
if mibBuilder.loadTexts:
    mpcMappingTable.setStatus("mandatory")
_MpcMappingEntry_Object = MibTableRow
mpcMappingEntry = _MpcMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 7, 1)
)
mpcMappingEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"),
)
if mibBuilder.loadTexts:
    mpcMappingEntry.setStatus("mandatory")
_MpcMappingRowStatus_Type = RowStatus
_MpcMappingRowStatus_Object = MibTableColumn
mpcMappingRowStatus = _MpcMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 7, 1, 1),
    _MpcMappingRowStatus_Type()
)
mpcMappingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpcMappingRowStatus.setStatus("mandatory")
_MpcMappingIndex_Type = MpcIndex
_MpcMappingIndex_Object = MibTableColumn
mpcMappingIndex = _MpcMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 7, 1, 2),
    _MpcMappingIndex_Type()
)
mpcMappingIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpcMappingIndex.setStatus("mandatory")
_MpcMpsTable_Object = MibTable
mpcMpsTable = _MpcMpsTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 8)
)
if mibBuilder.loadTexts:
    mpcMpsTable.setStatus("mandatory")
_MpcMpsEntry_Object = MibTableRow
mpcMpsEntry = _MpcMpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 8, 1)
)
mpcMpsEntry.setIndexNames(
    (0, "MPOA-MIB", "mpcMpsIndex"),
)
if mibBuilder.loadTexts:
    mpcMpsEntry.setStatus("mandatory")
_MpcMpsIndex_Type = MpsIndex
_MpcMpsIndex_Object = MibTableColumn
mpcMpsIndex = _MpcMpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 8, 1, 1),
    _MpcMpsIndex_Type()
)
mpcMpsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcMpsIndex.setStatus("mandatory")
_MpcMpsAtmAddr_Type = AtmAddr
_MpcMpsAtmAddr_Object = MibTableColumn
mpcMpsAtmAddr = _MpcMpsAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 8, 1, 2),
    _MpcMpsAtmAddr_Type()
)
mpcMpsAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcMpsAtmAddr.setStatus("mandatory")
_MpcMpsMacAddressTable_Object = MibTable
mpcMpsMacAddressTable = _MpcMpsMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 9)
)
if mibBuilder.loadTexts:
    mpcMpsMacAddressTable.setStatus("mandatory")
_MpcMpsMacAddressEntry_Object = MibTableRow
mpcMpsMacAddressEntry = _MpcMpsMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 9, 1)
)
mpcMpsMacAddressEntry.setIndexNames(
    (0, "MPOA-MIB", "mpcMpsIndex"),
    (0, "MPOA-MIB", "mpcLecIndex"),
)
if mibBuilder.loadTexts:
    mpcMpsMacAddressEntry.setStatus("mandatory")
_MpcLecIndex_Type = LecIndex
_MpcLecIndex_Object = MibTableColumn
mpcLecIndex = _MpcLecIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 9, 1, 1),
    _MpcLecIndex_Type()
)
mpcLecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcLecIndex.setStatus("mandatory")
_MpcMpsMacAddress_Type = MacAddress
_MpcMpsMacAddress_Object = MibTableColumn
mpcMpsMacAddress = _MpcMpsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 9, 1, 2),
    _MpcMpsMacAddress_Type()
)
mpcMpsMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcMpsMacAddress.setStatus("mandatory")
_MpcIngressCacheTxTotalPackets_Type = Counter32
_MpcIngressCacheTxTotalPackets_Object = MibScalar
mpcIngressCacheTxTotalPackets = _MpcIngressCacheTxTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 10),
    _MpcIngressCacheTxTotalPackets_Type()
)
mpcIngressCacheTxTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCacheTxTotalPackets.setStatus("mandatory")
_MpcIngressCacheTxTotalOctets_Type = Counter64
_MpcIngressCacheTxTotalOctets_Object = MibScalar
mpcIngressCacheTxTotalOctets = _MpcIngressCacheTxTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 11),
    _MpcIngressCacheTxTotalOctets_Type()
)
mpcIngressCacheTxTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCacheTxTotalOctets.setStatus("mandatory")
_MpcIngressCacheTable_Object = MibTable
mpcIngressCacheTable = _MpcIngressCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12)
)
if mibBuilder.loadTexts:
    mpcIngressCacheTable.setStatus("mandatory")
_MpcIngressCacheEntry_Object = MibTableRow
mpcIngressCacheEntry = _MpcIngressCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1)
)
mpcIngressCacheEntry.setIndexNames(
    (0, "MPOA-MIB", "mpcIngressCacheDestInetworkAddrType"),
    (0, "MPOA-MIB", "mpcIngressCacheDestAddr"),
    (0, "MPOA-MIB", "mpcIndex"),
    (0, "MPOA-MIB", "mpcMpsIndex"),
)
if mibBuilder.loadTexts:
    mpcIngressCacheEntry.setStatus("mandatory")
_MpcIngressCacheDestInetworkAddrType_Type = InternetworkAddrType
_MpcIngressCacheDestInetworkAddrType_Object = MibTableColumn
mpcIngressCacheDestInetworkAddrType = _MpcIngressCacheDestInetworkAddrType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1, 1),
    _MpcIngressCacheDestInetworkAddrType_Type()
)
mpcIngressCacheDestInetworkAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCacheDestInetworkAddrType.setStatus("mandatory")
_MpcIngressCacheDestAddr_Type = InternetworkAddr
_MpcIngressCacheDestAddr_Object = MibTableColumn
mpcIngressCacheDestAddr = _MpcIngressCacheDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1, 2),
    _MpcIngressCacheDestAddr_Type()
)
mpcIngressCacheDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCacheDestAddr.setStatus("mandatory")
_MpcIngressCachePrefixLen_Type = Integer32
_MpcIngressCachePrefixLen_Object = MibTableColumn
mpcIngressCachePrefixLen = _MpcIngressCachePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1, 3),
    _MpcIngressCachePrefixLen_Type()
)
mpcIngressCachePrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCachePrefixLen.setStatus("mandatory")
_MpcIngressCacheDestAtmAddr_Type = AtmAddr
_MpcIngressCacheDestAtmAddr_Object = MibTableColumn
mpcIngressCacheDestAtmAddr = _MpcIngressCacheDestAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1, 4),
    _MpcIngressCacheDestAtmAddr_Type()
)
mpcIngressCacheDestAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCacheDestAtmAddr.setStatus("mandatory")
_MpcIngressCacheSrcAtmAddr_Type = AtmAddr
_MpcIngressCacheSrcAtmAddr_Object = MibTableColumn
mpcIngressCacheSrcAtmAddr = _MpcIngressCacheSrcAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1, 5),
    _MpcIngressCacheSrcAtmAddr_Type()
)
mpcIngressCacheSrcAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCacheSrcAtmAddr.setStatus("mandatory")


class _MpcIngressCacheEntryState_Type(Integer32):
    """Custom type mpcIngressCacheEntryState based on Integer32"""
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
        *(("doesNotExist", 1),
          ("inactive", 2),
          ("active", 3),
          ("negative", 4))
    )


_MpcIngressCacheEntryState_Type.__name__ = "Integer32"
_MpcIngressCacheEntryState_Object = MibTableColumn
mpcIngressCacheEntryState = _MpcIngressCacheEntryState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1, 6),
    _MpcIngressCacheEntryState_Type()
)
mpcIngressCacheEntryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCacheEntryState.setStatus("mandatory")
_MpcIngressCacheEgressCacheTagValid_Type = TruthValue
_MpcIngressCacheEgressCacheTagValid_Object = MibTableColumn
mpcIngressCacheEgressCacheTagValid = _MpcIngressCacheEgressCacheTagValid_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1, 7),
    _MpcIngressCacheEgressCacheTagValid_Type()
)
mpcIngressCacheEgressCacheTagValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCacheEgressCacheTagValid.setStatus("mandatory")
_MpcIngressCacheEgressCacheTag_Type = Integer32
_MpcIngressCacheEgressCacheTag_Object = MibTableColumn
mpcIngressCacheEgressCacheTag = _MpcIngressCacheEgressCacheTag_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1, 8),
    _MpcIngressCacheEgressCacheTag_Type()
)
mpcIngressCacheEgressCacheTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCacheEgressCacheTag.setStatus("mandatory")


class _MpcIngressCacheLastNhrpCieCode_Type(Integer32):
    """Custom type mpcIngressCacheLastNhrpCieCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MpcIngressCacheLastNhrpCieCode_Type.__name__ = "Integer32"
_MpcIngressCacheLastNhrpCieCode_Object = MibTableColumn
mpcIngressCacheLastNhrpCieCode = _MpcIngressCacheLastNhrpCieCode_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1, 9),
    _MpcIngressCacheLastNhrpCieCode_Type()
)
mpcIngressCacheLastNhrpCieCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCacheLastNhrpCieCode.setStatus("mandatory")
_MpcIngressCacheSigErrCode_Type = Integer32
_MpcIngressCacheSigErrCode_Object = MibTableColumn
mpcIngressCacheSigErrCode = _MpcIngressCacheSigErrCode_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1, 10),
    _MpcIngressCacheSigErrCode_Type()
)
mpcIngressCacheSigErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCacheSigErrCode.setStatus("mandatory")
_MpcIngressCacheRetries_Type = Counter32
_MpcIngressCacheRetries_Object = MibTableColumn
mpcIngressCacheRetries = _MpcIngressCacheRetries_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1, 11),
    _MpcIngressCacheRetries_Type()
)
mpcIngressCacheRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCacheRetries.setStatus("mandatory")
_MpcIngressCacheTimeUntilNextResolutionRequest_Type = TimeInterval
_MpcIngressCacheTimeUntilNextResolutionRequest_Object = MibTableColumn
mpcIngressCacheTimeUntilNextResolutionRequest = _MpcIngressCacheTimeUntilNextResolutionRequest_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1, 12),
    _MpcIngressCacheTimeUntilNextResolutionRequest_Type()
)
mpcIngressCacheTimeUntilNextResolutionRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCacheTimeUntilNextResolutionRequest.setStatus("mandatory")
_MpcIngressCacheHoldingTime_Type = TimeInterval
_MpcIngressCacheHoldingTime_Object = MibTableColumn
mpcIngressCacheHoldingTime = _MpcIngressCacheHoldingTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1, 13),
    _MpcIngressCacheHoldingTime_Type()
)
mpcIngressCacheHoldingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCacheHoldingTime.setStatus("mandatory")


class _MpcIngressCacheServiceCategory_Type(Integer32):
    """Custom type mpcIngressCacheServiceCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpcIngressCacheServiceCategory_Type.__name__ = "Integer32"
_MpcIngressCacheServiceCategory_Object = MibTableColumn
mpcIngressCacheServiceCategory = _MpcIngressCacheServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1, 14),
    _MpcIngressCacheServiceCategory_Type()
)
mpcIngressCacheServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCacheServiceCategory.setStatus("mandatory")
_MpcEgressCacheRxTotalPackets_Type = Counter32
_MpcEgressCacheRxTotalPackets_Object = MibScalar
mpcEgressCacheRxTotalPackets = _MpcEgressCacheRxTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 13),
    _MpcEgressCacheRxTotalPackets_Type()
)
mpcEgressCacheRxTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcEgressCacheRxTotalPackets.setStatus("mandatory")
_MpcEgressCacheRxTotalOctets_Type = Counter64
_MpcEgressCacheRxTotalOctets_Object = MibScalar
mpcEgressCacheRxTotalOctets = _MpcEgressCacheRxTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 14),
    _MpcEgressCacheRxTotalOctets_Type()
)
mpcEgressCacheRxTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcEgressCacheRxTotalOctets.setStatus("mandatory")
_MpcEgressCacheTable_Object = MibTable
mpcEgressCacheTable = _MpcEgressCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 15)
)
if mibBuilder.loadTexts:
    mpcEgressCacheTable.setStatus("mandatory")
_MpcEgressCacheEntry_Object = MibTableRow
mpcEgressCacheEntry = _MpcEgressCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 15, 1)
)
mpcEgressCacheEntry.setIndexNames(
    (0, "MPOA-MIB", "mpcEgressCacheId"),
    (0, "MPOA-MIB", "mpcIndex"),
    (0, "MPOA-MIB", "mpcMpsIndex"),
)
if mibBuilder.loadTexts:
    mpcEgressCacheEntry.setStatus("mandatory")


class _MpcEgressCacheId_Type(Integer32):
    """Custom type mpcEgressCacheId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MpcEgressCacheId_Type.__name__ = "Integer32"
_MpcEgressCacheId_Object = MibTableColumn
mpcEgressCacheId = _MpcEgressCacheId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 15, 1, 1),
    _MpcEgressCacheId_Type()
)
mpcEgressCacheId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcEgressCacheId.setStatus("mandatory")
_MpcEgressCacheInetworkAddrType_Type = InternetworkAddrType
_MpcEgressCacheInetworkAddrType_Object = MibTableColumn
mpcEgressCacheInetworkAddrType = _MpcEgressCacheInetworkAddrType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 15, 1, 2),
    _MpcEgressCacheInetworkAddrType_Type()
)
mpcEgressCacheInetworkAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcEgressCacheInetworkAddrType.setStatus("mandatory")
_MpcEgressCacheIDestAddr_Type = InternetworkAddr
_MpcEgressCacheIDestAddr_Object = MibTableColumn
mpcEgressCacheIDestAddr = _MpcEgressCacheIDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 15, 1, 3),
    _MpcEgressCacheIDestAddr_Type()
)
mpcEgressCacheIDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcEgressCacheIDestAddr.setStatus("mandatory")
_MpcEgressCachePrefixLen_Type = Integer32
_MpcEgressCachePrefixLen_Object = MibTableColumn
mpcEgressCachePrefixLen = _MpcEgressCachePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 15, 1, 4),
    _MpcEgressCachePrefixLen_Type()
)
mpcEgressCachePrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcEgressCachePrefixLen.setStatus("mandatory")


class _MpcEgressCacheEntryState_Type(Integer32):
    """Custom type mpcEgressCacheEntryState based on Integer32"""
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
        *(("doesNotExist", 1),
          ("inactive", 2),
          ("active", 3),
          ("negative", 4))
    )


_MpcEgressCacheEntryState_Type.__name__ = "Integer32"
_MpcEgressCacheEntryState_Object = MibTableColumn
mpcEgressCacheEntryState = _MpcEgressCacheEntryState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 15, 1, 5),
    _MpcEgressCacheEntryState_Type()
)
mpcEgressCacheEntryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcEgressCacheEntryState.setStatus("mandatory")
_MpcEgressCacheEgressCacheTagValid_Type = TruthValue
_MpcEgressCacheEgressCacheTagValid_Object = MibTableColumn
mpcEgressCacheEgressCacheTagValid = _MpcEgressCacheEgressCacheTagValid_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 15, 1, 6),
    _MpcEgressCacheEgressCacheTagValid_Type()
)
mpcEgressCacheEgressCacheTagValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcEgressCacheEgressCacheTagValid.setStatus("mandatory")
_MpcEgressCacheEgressCacheTag_Type = Integer32
_MpcEgressCacheEgressCacheTag_Object = MibTableColumn
mpcEgressCacheEgressCacheTag = _MpcEgressCacheEgressCacheTag_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 15, 1, 7),
    _MpcEgressCacheEgressCacheTag_Type()
)
mpcEgressCacheEgressCacheTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcEgressCacheEgressCacheTag.setStatus("mandatory")
_MpcEgressCacheHoldTime_Type = TimeInterval
_MpcEgressCacheHoldTime_Object = MibTableColumn
mpcEgressCacheHoldTime = _MpcEgressCacheHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 15, 1, 8),
    _MpcEgressCacheHoldTime_Type()
)
mpcEgressCacheHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcEgressCacheHoldTime.setStatus("mandatory")


class _MpcEgressCacheDataLinkHeader_Type(OctetString):
    """Custom type mpcEgressCacheDataLinkHeader based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpcEgressCacheDataLinkHeader_Type.__name__ = "OctetString"
_MpcEgressCacheDataLinkHeader_Object = MibTableColumn
mpcEgressCacheDataLinkHeader = _MpcEgressCacheDataLinkHeader_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 15, 1, 9),
    _MpcEgressCacheDataLinkHeader_Type()
)
mpcEgressCacheDataLinkHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcEgressCacheDataLinkHeader.setStatus("mandatory")
_MpcEgressCacheIngressMpcDataAtmAddr_Type = AtmAddr
_MpcEgressCacheIngressMpcDataAtmAddr_Object = MibTableColumn
mpcEgressCacheIngressMpcDataAtmAddr = _MpcEgressCacheIngressMpcDataAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 15, 1, 10),
    _MpcEgressCacheIngressMpcDataAtmAddr_Type()
)
mpcEgressCacheIngressMpcDataAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcEgressCacheIngressMpcDataAtmAddr.setStatus("mandatory")
_MpcEgressCacheLecIndex_Type = LecIndex
_MpcEgressCacheLecIndex_Object = MibTableColumn
mpcEgressCacheLecIndex = _MpcEgressCacheLecIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 15, 1, 11),
    _MpcEgressCacheLecIndex_Type()
)
mpcEgressCacheLecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcEgressCacheLecIndex.setStatus("mandatory")


class _MpcEgressCacheServiceCategory_Type(Integer32):
    """Custom type mpcEgressCacheServiceCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpcEgressCacheServiceCategory_Type.__name__ = "Integer32"
_MpcEgressCacheServiceCategory_Object = MibTableColumn
mpcEgressCacheServiceCategory = _MpcEgressCacheServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 15, 1, 12),
    _MpcEgressCacheServiceCategory_Type()
)
mpcEgressCacheServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcEgressCacheServiceCategory.setStatus("mandatory")
_MpsObjects_ObjectIdentity = ObjectIdentity
mpsObjects = _MpsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3)
)


class _MpsNextIndex_Type(Integer32):
    """Custom type mpsNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MpsNextIndex_Type.__name__ = "Integer32"
_MpsNextIndex_Object = MibScalar
mpsNextIndex = _MpsNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 1),
    _MpsNextIndex_Type()
)
mpsNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsNextIndex.setStatus("mandatory")
_MpsConfigTable_Object = MibTable
mpsConfigTable = _MpsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    mpsConfigTable.setStatus("mandatory")
_MpsConfigEntry_Object = MibTableRow
mpsConfigEntry = _MpsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 2, 1)
)
mpsConfigEntry.setIndexNames(
    (0, "MPOA-MIB", "mpsIndex"),
)
if mibBuilder.loadTexts:
    mpsConfigEntry.setStatus("mandatory")
_MpsIndex_Type = MpsIndex
_MpsIndex_Object = MibTableColumn
mpsIndex = _MpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 2, 1, 1),
    _MpsIndex_Type()
)
mpsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsIndex.setStatus("mandatory")
_MpsRowStatus_Type = RowStatus
_MpsRowStatus_Object = MibTableColumn
mpsRowStatus = _MpsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 2, 1, 2),
    _MpsRowStatus_Type()
)
mpsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpsRowStatus.setStatus("mandatory")


class _MpsConfigMode_Type(Integer32):
    """Custom type mpsConfigMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_MpsConfigMode_Type.__name__ = "Integer32"
_MpsConfigMode_Object = MibTableColumn
mpsConfigMode = _MpsConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 2, 1, 3),
    _MpsConfigMode_Type()
)
mpsConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpsConfigMode.setStatus("mandatory")
_MpsCtrlAtmAddr_Type = AtmConfigAddr
_MpsCtrlAtmAddr_Object = MibTableColumn
mpsCtrlAtmAddr = _MpsCtrlAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 2, 1, 4),
    _MpsCtrlAtmAddr_Type()
)
mpsCtrlAtmAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpsCtrlAtmAddr.setStatus("mandatory")


class _MpsKeepAliveTime_Type(Integer32):
    """Custom type mpsKeepAliveTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_MpsKeepAliveTime_Type.__name__ = "Integer32"
_MpsKeepAliveTime_Object = MibTableColumn
mpsKeepAliveTime = _MpsKeepAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 2, 1, 5),
    _MpsKeepAliveTime_Type()
)
mpsKeepAliveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpsKeepAliveTime.setStatus("mandatory")


class _MpsKeepAliveLifeTime_Type(Integer32):
    """Custom type mpsKeepAliveLifeTime based on Integer32"""
    defaultValue = 35

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1000),
    )


_MpsKeepAliveLifeTime_Type.__name__ = "Integer32"
_MpsKeepAliveLifeTime_Object = MibTableColumn
mpsKeepAliveLifeTime = _MpsKeepAliveLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 2, 1, 6),
    _MpsKeepAliveLifeTime_Type()
)
mpsKeepAliveLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpsKeepAliveLifeTime.setStatus("mandatory")


class _MpsInitialRetryTime_Type(Integer32):
    """Custom type mpsInitialRetryTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_MpsInitialRetryTime_Type.__name__ = "Integer32"
_MpsInitialRetryTime_Object = MibTableColumn
mpsInitialRetryTime = _MpsInitialRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 2, 1, 7),
    _MpsInitialRetryTime_Type()
)
mpsInitialRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpsInitialRetryTime.setStatus("mandatory")


class _MpsRetryTimeMaximum_Type(Integer32):
    """Custom type mpsRetryTimeMaximum based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_MpsRetryTimeMaximum_Type.__name__ = "Integer32"
_MpsRetryTimeMaximum_Object = MibTableColumn
mpsRetryTimeMaximum = _MpsRetryTimeMaximum_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 2, 1, 8),
    _MpsRetryTimeMaximum_Type()
)
mpsRetryTimeMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpsRetryTimeMaximum.setStatus("mandatory")


class _MpsGiveupTime_Type(Integer32):
    """Custom type mpsGiveupTime based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_MpsGiveupTime_Type.__name__ = "Integer32"
_MpsGiveupTime_Object = MibTableColumn
mpsGiveupTime = _MpsGiveupTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 2, 1, 9),
    _MpsGiveupTime_Type()
)
mpsGiveupTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpsGiveupTime.setStatus("mandatory")


class _MpsDefaultHoldingTime_Type(Integer32):
    """Custom type mpsDefaultHoldingTime based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_MpsDefaultHoldingTime_Type.__name__ = "Integer32"
_MpsDefaultHoldingTime_Object = MibTableColumn
mpsDefaultHoldingTime = _MpsDefaultHoldingTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 2, 1, 10),
    _MpsDefaultHoldingTime_Type()
)
mpsDefaultHoldingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpsDefaultHoldingTime.setStatus("mandatory")
_MpsActualTable_Object = MibTable
mpsActualTable = _MpsActualTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    mpsActualTable.setStatus("mandatory")
_MpsActualEntry_Object = MibTableRow
mpsActualEntry = _MpsActualEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 3, 1)
)
mpsActualEntry.setIndexNames(
    (0, "MPOA-MIB", "mpsIndex"),
)
if mibBuilder.loadTexts:
    mpsActualEntry.setStatus("mandatory")


class _MpsActualState_Type(Integer32):
    """Custom type mpsActualState based on Integer32"""
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
          ("initialState", 2),
          ("up", 3),
          ("down", 4))
    )


_MpsActualState_Type.__name__ = "Integer32"
_MpsActualState_Object = MibTableColumn
mpsActualState = _MpsActualState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 3, 1, 1),
    _MpsActualState_Type()
)
mpsActualState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsActualState.setStatus("mandatory")
_MpsDiscontinuityTime_Type = TimeStamp
_MpsDiscontinuityTime_Object = MibTableColumn
mpsDiscontinuityTime = _MpsDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 3, 1, 2),
    _MpsDiscontinuityTime_Type()
)
mpsDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsDiscontinuityTime.setStatus("mandatory")


class _MpsActualConfigMode_Type(Integer32):
    """Custom type mpsActualConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_MpsActualConfigMode_Type.__name__ = "Integer32"
_MpsActualConfigMode_Object = MibTableColumn
mpsActualConfigMode = _MpsActualConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 3, 1, 3),
    _MpsActualConfigMode_Type()
)
mpsActualConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsActualConfigMode.setStatus("mandatory")
_MpsActualKeepAlive_Type = Integer32
_MpsActualKeepAlive_Object = MibTableColumn
mpsActualKeepAlive = _MpsActualKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 3, 1, 5),
    _MpsActualKeepAlive_Type()
)
mpsActualKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsActualKeepAlive.setStatus("mandatory")
_MpsActualKeepAliveLifeTime_Type = Integer32
_MpsActualKeepAliveLifeTime_Object = MibTableColumn
mpsActualKeepAliveLifeTime = _MpsActualKeepAliveLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 3, 1, 6),
    _MpsActualKeepAliveLifeTime_Type()
)
mpsActualKeepAliveLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsActualKeepAliveLifeTime.setStatus("mandatory")


class _MpsActualInitialRetryTime_Type(Integer32):
    """Custom type mpsActualInitialRetryTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_MpsActualInitialRetryTime_Type.__name__ = "Integer32"
_MpsActualInitialRetryTime_Object = MibTableColumn
mpsActualInitialRetryTime = _MpsActualInitialRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 3, 1, 7),
    _MpsActualInitialRetryTime_Type()
)
mpsActualInitialRetryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsActualInitialRetryTime.setStatus("mandatory")


class _MpsActualRetryTimeMaximum_Type(Integer32):
    """Custom type mpsActualRetryTimeMaximum based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_MpsActualRetryTimeMaximum_Type.__name__ = "Integer32"
_MpsActualRetryTimeMaximum_Object = MibTableColumn
mpsActualRetryTimeMaximum = _MpsActualRetryTimeMaximum_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 3, 1, 8),
    _MpsActualRetryTimeMaximum_Type()
)
mpsActualRetryTimeMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsActualRetryTimeMaximum.setStatus("mandatory")


class _MpsActualGiveupTime_Type(Integer32):
    """Custom type mpsActualGiveupTime based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_MpsActualGiveupTime_Type.__name__ = "Integer32"
_MpsActualGiveupTime_Object = MibTableColumn
mpsActualGiveupTime = _MpsActualGiveupTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 3, 1, 9),
    _MpsActualGiveupTime_Type()
)
mpsActualGiveupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsActualGiveupTime.setStatus("mandatory")


class _MpsActualDefaultHoldingTime_Type(Integer32):
    """Custom type mpsActualDefaultHoldingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_MpsActualDefaultHoldingTime_Type.__name__ = "Integer32"
_MpsActualDefaultHoldingTime_Object = MibTableColumn
mpsActualDefaultHoldingTime = _MpsActualDefaultHoldingTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 3, 1, 10),
    _MpsActualDefaultHoldingTime_Type()
)
mpsActualDefaultHoldingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsActualDefaultHoldingTime.setStatus("mandatory")
_MpsStatisticsTable_Object = MibTable
mpsStatisticsTable = _MpsStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    mpsStatisticsTable.setStatus("mandatory")
_MpsStatisticsEntry_Object = MibTableRow
mpsStatisticsEntry = _MpsStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 4, 1)
)
mpsStatisticsEntry.setIndexNames(
    (0, "MPOA-MIB", "mpsIndex"),
)
if mibBuilder.loadTexts:
    mpsStatisticsEntry.setStatus("mandatory")
_MpsStatRxMpoaResolveRequests_Type = Counter32
_MpsStatRxMpoaResolveRequests_Object = MibTableColumn
mpsStatRxMpoaResolveRequests = _MpsStatRxMpoaResolveRequests_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 4, 1, 1),
    _MpsStatRxMpoaResolveRequests_Type()
)
mpsStatRxMpoaResolveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsStatRxMpoaResolveRequests.setStatus("mandatory")
_MpsStatTxMpoaResolveReplyAcks_Type = Counter32
_MpsStatTxMpoaResolveReplyAcks_Object = MibTableColumn
mpsStatTxMpoaResolveReplyAcks = _MpsStatTxMpoaResolveReplyAcks_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 4, 1, 2),
    _MpsStatTxMpoaResolveReplyAcks_Type()
)
mpsStatTxMpoaResolveReplyAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsStatTxMpoaResolveReplyAcks.setStatus("mandatory")
_MpsStatTxMpoaResolveReplyInsufECResources_Type = Counter32
_MpsStatTxMpoaResolveReplyInsufECResources_Object = MibTableColumn
mpsStatTxMpoaResolveReplyInsufECResources = _MpsStatTxMpoaResolveReplyInsufECResources_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 4, 1, 3),
    _MpsStatTxMpoaResolveReplyInsufECResources_Type()
)
mpsStatTxMpoaResolveReplyInsufECResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsStatTxMpoaResolveReplyInsufECResources.setStatus("mandatory")
_MpsStatTxMpoaResolveReplyInsufSCResources_Type = Counter32
_MpsStatTxMpoaResolveReplyInsufSCResources_Object = MibTableColumn
mpsStatTxMpoaResolveReplyInsufSCResources = _MpsStatTxMpoaResolveReplyInsufSCResources_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 4, 1, 4),
    _MpsStatTxMpoaResolveReplyInsufSCResources_Type()
)
mpsStatTxMpoaResolveReplyInsufSCResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsStatTxMpoaResolveReplyInsufSCResources.setStatus("mandatory")
_MpsStatTxMpoaResolveReplyInsufEitherResources_Type = Counter32
_MpsStatTxMpoaResolveReplyInsufEitherResources_Object = MibTableColumn
mpsStatTxMpoaResolveReplyInsufEitherResources = _MpsStatTxMpoaResolveReplyInsufEitherResources_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 4, 1, 5),
    _MpsStatTxMpoaResolveReplyInsufEitherResources_Type()
)
mpsStatTxMpoaResolveReplyInsufEitherResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsStatTxMpoaResolveReplyInsufEitherResources.setStatus("mandatory")
_MpsStatTxMpoaResolveReplyUnsupportedInetProt_Type = Counter32
_MpsStatTxMpoaResolveReplyUnsupportedInetProt_Object = MibTableColumn
mpsStatTxMpoaResolveReplyUnsupportedInetProt = _MpsStatTxMpoaResolveReplyUnsupportedInetProt_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 4, 1, 6),
    _MpsStatTxMpoaResolveReplyUnsupportedInetProt_Type()
)
mpsStatTxMpoaResolveReplyUnsupportedInetProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsStatTxMpoaResolveReplyUnsupportedInetProt.setStatus("mandatory")
_MpsStatTxMpoaResolveReplyUnsupportedMacEncaps_Type = Counter32
_MpsStatTxMpoaResolveReplyUnsupportedMacEncaps_Object = MibTableColumn
mpsStatTxMpoaResolveReplyUnsupportedMacEncaps = _MpsStatTxMpoaResolveReplyUnsupportedMacEncaps_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 4, 1, 7),
    _MpsStatTxMpoaResolveReplyUnsupportedMacEncaps_Type()
)
mpsStatTxMpoaResolveReplyUnsupportedMacEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsStatTxMpoaResolveReplyUnsupportedMacEncaps.setStatus("mandatory")
_MpsStatTxMpoaResolveReplyUnspecifiedOther_Type = Counter32
_MpsStatTxMpoaResolveReplyUnspecifiedOther_Object = MibTableColumn
mpsStatTxMpoaResolveReplyUnspecifiedOther = _MpsStatTxMpoaResolveReplyUnspecifiedOther_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 4, 1, 8),
    _MpsStatTxMpoaResolveReplyUnspecifiedOther_Type()
)
mpsStatTxMpoaResolveReplyUnspecifiedOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsStatTxMpoaResolveReplyUnspecifiedOther.setStatus("mandatory")
_MpsStatTxMpoaResolveReplyOther_Type = Counter32
_MpsStatTxMpoaResolveReplyOther_Object = MibTableColumn
mpsStatTxMpoaResolveReplyOther = _MpsStatTxMpoaResolveReplyOther_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 4, 1, 9),
    _MpsStatTxMpoaResolveReplyOther_Type()
)
mpsStatTxMpoaResolveReplyOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsStatTxMpoaResolveReplyOther.setStatus("mandatory")
_MpsStatGiveupTimeExpireds_Type = Counter32
_MpsStatGiveupTimeExpireds_Object = MibTableColumn
mpsStatGiveupTimeExpireds = _MpsStatGiveupTimeExpireds_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 4, 1, 10),
    _MpsStatGiveupTimeExpireds_Type()
)
mpsStatGiveupTimeExpireds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsStatGiveupTimeExpireds.setStatus("mandatory")
_MpsStatTxMpoaImpRequests_Type = Counter32
_MpsStatTxMpoaImpRequests_Object = MibTableColumn
mpsStatTxMpoaImpRequests = _MpsStatTxMpoaImpRequests_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 4, 1, 11),
    _MpsStatTxMpoaImpRequests_Type()
)
mpsStatTxMpoaImpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsStatTxMpoaImpRequests.setStatus("mandatory")
_MpsStatRxMpoaImpReplyAcks_Type = Counter32
_MpsStatRxMpoaImpReplyAcks_Object = MibTableColumn
mpsStatRxMpoaImpReplyAcks = _MpsStatRxMpoaImpReplyAcks_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 4, 1, 12),
    _MpsStatRxMpoaImpReplyAcks_Type()
)
mpsStatRxMpoaImpReplyAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsStatRxMpoaImpReplyAcks.setStatus("mandatory")
_MpsStatRxMpoaImpReplyInsufECResources_Type = Counter32
_MpsStatRxMpoaImpReplyInsufECResources_Object = MibTableColumn
mpsStatRxMpoaImpReplyInsufECResources = _MpsStatRxMpoaImpReplyInsufECResources_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 4, 1, 13),
    _MpsStatRxMpoaImpReplyInsufECResources_Type()
)
mpsStatRxMpoaImpReplyInsufECResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsStatRxMpoaImpReplyInsufECResources.setStatus("mandatory")
_MpsStatRxMpoaImpReplyInsufSCResources_Type = Counter32
_MpsStatRxMpoaImpReplyInsufSCResources_Object = MibTableColumn
mpsStatRxMpoaImpReplyInsufSCResources = _MpsStatRxMpoaImpReplyInsufSCResources_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 4, 1, 14),
    _MpsStatRxMpoaImpReplyInsufSCResources_Type()
)
mpsStatRxMpoaImpReplyInsufSCResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsStatRxMpoaImpReplyInsufSCResources.setStatus("mandatory")
_MpsStatRxMpoaImpReplyInsufEitherResources_Type = Counter32
_MpsStatRxMpoaImpReplyInsufEitherResources_Object = MibTableColumn
mpsStatRxMpoaImpReplyInsufEitherResources = _MpsStatRxMpoaImpReplyInsufEitherResources_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 4, 1, 15),
    _MpsStatRxMpoaImpReplyInsufEitherResources_Type()
)
mpsStatRxMpoaImpReplyInsufEitherResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsStatRxMpoaImpReplyInsufEitherResources.setStatus("mandatory")
_MpsStatRxMpoaImpReplyUnsupportedInetProt_Type = Counter32
_MpsStatRxMpoaImpReplyUnsupportedInetProt_Object = MibTableColumn
mpsStatRxMpoaImpReplyUnsupportedInetProt = _MpsStatRxMpoaImpReplyUnsupportedInetProt_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 4, 1, 16),
    _MpsStatRxMpoaImpReplyUnsupportedInetProt_Type()
)
mpsStatRxMpoaImpReplyUnsupportedInetProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsStatRxMpoaImpReplyUnsupportedInetProt.setStatus("mandatory")
_MpsStatRxMpoaImpReplyUnsupportedMacEncaps_Type = Counter32
_MpsStatRxMpoaImpReplyUnsupportedMacEncaps_Object = MibTableColumn
mpsStatRxMpoaImpReplyUnsupportedMacEncaps = _MpsStatRxMpoaImpReplyUnsupportedMacEncaps_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 4, 1, 17),
    _MpsStatRxMpoaImpReplyUnsupportedMacEncaps_Type()
)
mpsStatRxMpoaImpReplyUnsupportedMacEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsStatRxMpoaImpReplyUnsupportedMacEncaps.setStatus("mandatory")
_MpsStatRxMpoaImpReplyUnspecifiedOther_Type = Counter32
_MpsStatRxMpoaImpReplyUnspecifiedOther_Object = MibTableColumn
mpsStatRxMpoaImpReplyUnspecifiedOther = _MpsStatRxMpoaImpReplyUnspecifiedOther_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 4, 1, 18),
    _MpsStatRxMpoaImpReplyUnspecifiedOther_Type()
)
mpsStatRxMpoaImpReplyUnspecifiedOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsStatRxMpoaImpReplyUnspecifiedOther.setStatus("mandatory")
_MpsStatRxMpoaImpReplyOther_Type = Counter32
_MpsStatRxMpoaImpReplyOther_Object = MibTableColumn
mpsStatRxMpoaImpReplyOther = _MpsStatRxMpoaImpReplyOther_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 4, 1, 19),
    _MpsStatRxMpoaImpReplyOther_Type()
)
mpsStatRxMpoaImpReplyOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsStatRxMpoaImpReplyOther.setStatus("mandatory")
_MpsStatRxMpoaEgressCachePurgeRequests_Type = Counter32
_MpsStatRxMpoaEgressCachePurgeRequests_Object = MibTableColumn
mpsStatRxMpoaEgressCachePurgeRequests = _MpsStatRxMpoaEgressCachePurgeRequests_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 4, 1, 20),
    _MpsStatRxMpoaEgressCachePurgeRequests_Type()
)
mpsStatRxMpoaEgressCachePurgeRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsStatRxMpoaEgressCachePurgeRequests.setStatus("mandatory")
_MpsStatTxMpoaEgressCachePurgeReplies_Type = Counter32
_MpsStatTxMpoaEgressCachePurgeReplies_Object = MibTableColumn
mpsStatTxMpoaEgressCachePurgeReplies = _MpsStatTxMpoaEgressCachePurgeReplies_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 4, 1, 21),
    _MpsStatTxMpoaEgressCachePurgeReplies_Type()
)
mpsStatTxMpoaEgressCachePurgeReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsStatTxMpoaEgressCachePurgeReplies.setStatus("mandatory")
_MpsStatTxMpoaTriggers_Type = Counter32
_MpsStatTxMpoaTriggers_Object = MibTableColumn
mpsStatTxMpoaTriggers = _MpsStatTxMpoaTriggers_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 4, 1, 22),
    _MpsStatTxMpoaTriggers_Type()
)
mpsStatTxMpoaTriggers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsStatTxMpoaTriggers.setStatus("mandatory")
_MpsStatTxNhrpResolveRequests_Type = Counter32
_MpsStatTxNhrpResolveRequests_Object = MibTableColumn
mpsStatTxNhrpResolveRequests = _MpsStatTxNhrpResolveRequests_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 4, 1, 23),
    _MpsStatTxNhrpResolveRequests_Type()
)
mpsStatTxNhrpResolveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsStatTxNhrpResolveRequests.setStatus("mandatory")
_MpsStatRxNhrpResolveReplies_Type = Counter32
_MpsStatRxNhrpResolveReplies_Object = MibTableColumn
mpsStatRxNhrpResolveReplies = _MpsStatRxNhrpResolveReplies_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 4, 1, 24),
    _MpsStatRxNhrpResolveReplies_Type()
)
mpsStatRxNhrpResolveReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsStatRxNhrpResolveReplies.setStatus("mandatory")
_MpsStatRxNhrpResolveRequests_Type = Counter32
_MpsStatRxNhrpResolveRequests_Object = MibTableColumn
mpsStatRxNhrpResolveRequests = _MpsStatRxNhrpResolveRequests_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 4, 1, 25),
    _MpsStatRxNhrpResolveRequests_Type()
)
mpsStatRxNhrpResolveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsStatRxNhrpResolveRequests.setStatus("mandatory")
_MpsStatTxNhrpResolveReplies_Type = Counter32
_MpsStatTxNhrpResolveReplies_Object = MibTableColumn
mpsStatTxNhrpResolveReplies = _MpsStatTxNhrpResolveReplies_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 4, 1, 26),
    _MpsStatTxNhrpResolveReplies_Type()
)
mpsStatTxNhrpResolveReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsStatTxNhrpResolveReplies.setStatus("mandatory")
_MpsProtocolTable_Object = MibTable
mpsProtocolTable = _MpsProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    mpsProtocolTable.setStatus("mandatory")
_MpsProtocolEntry_Object = MibTableRow
mpsProtocolEntry = _MpsProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 5, 1)
)
mpsProtocolEntry.setIndexNames(
    (0, "MPOA-MIB", "mpsIndex"),
    (0, "MPOA-MIB", "mpsInternetworkLayerProtocol"),
)
if mibBuilder.loadTexts:
    mpsProtocolEntry.setStatus("mandatory")
_MpsInternetworkLayerProtocol_Type = InternetworkAddrType
_MpsInternetworkLayerProtocol_Object = MibTableColumn
mpsInternetworkLayerProtocol = _MpsInternetworkLayerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 5, 1, 1),
    _MpsInternetworkLayerProtocol_Type()
)
mpsInternetworkLayerProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsInternetworkLayerProtocol.setStatus("mandatory")
_MpsLECSValue_Type = TruthValue
_MpsLECSValue_Object = MibTableColumn
mpsLECSValue = _MpsLECSValue_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 5, 1, 2),
    _MpsLECSValue_Type()
)
mpsLECSValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsLECSValue.setStatus("mandatory")
_MpsProtocolRowStatus_Type = RowStatus
_MpsProtocolRowStatus_Object = MibTableColumn
mpsProtocolRowStatus = _MpsProtocolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 5, 1, 3),
    _MpsProtocolRowStatus_Type()
)
mpsProtocolRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpsProtocolRowStatus.setStatus("mandatory")
_MpsMappingTable_Object = MibTable
mpsMappingTable = _MpsMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 6)
)
if mibBuilder.loadTexts:
    mpsMappingTable.setStatus("mandatory")
_MpsMappingEntry_Object = MibTableRow
mpsMappingEntry = _MpsMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 6, 1)
)
mpsMappingEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"),
)
if mibBuilder.loadTexts:
    mpsMappingEntry.setStatus("mandatory")
_MpsMappingRowStatus_Type = RowStatus
_MpsMappingRowStatus_Object = MibTableColumn
mpsMappingRowStatus = _MpsMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 6, 1, 1),
    _MpsMappingRowStatus_Type()
)
mpsMappingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpsMappingRowStatus.setStatus("mandatory")
_MpsMappingIndex_Type = MpsIndex
_MpsMappingIndex_Object = MibTableColumn
mpsMappingIndex = _MpsMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 6, 1, 2),
    _MpsMappingIndex_Type()
)
mpsMappingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsMappingIndex.setStatus("mandatory")
_MpsIngressCacheTable_Object = MibTable
mpsIngressCacheTable = _MpsIngressCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 7)
)
if mibBuilder.loadTexts:
    mpsIngressCacheTable.setStatus("mandatory")
_MpsIngressCacheEntry_Object = MibTableRow
mpsIngressCacheEntry = _MpsIngressCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 7, 1)
)
mpsIngressCacheEntry.setIndexNames(
    (0, "MPOA-MIB", "mpsIngressCacheDestInternetworkAddrType"),
    (0, "MPOA-MIB", "mpsIngressCacheDestAddr"),
    (0, "MPOA-MIB", "mpsIndex"),
    (0, "MPOA-MIB", "mpsMpcIndex"),
)
if mibBuilder.loadTexts:
    mpsIngressCacheEntry.setStatus("mandatory")
_MpsIngressCacheDestInternetworkAddrType_Type = InternetworkAddrType
_MpsIngressCacheDestInternetworkAddrType_Object = MibTableColumn
mpsIngressCacheDestInternetworkAddrType = _MpsIngressCacheDestInternetworkAddrType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 7, 1, 1),
    _MpsIngressCacheDestInternetworkAddrType_Type()
)
mpsIngressCacheDestInternetworkAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsIngressCacheDestInternetworkAddrType.setStatus("mandatory")
_MpsIngressCacheDestAddr_Type = InternetworkAddr
_MpsIngressCacheDestAddr_Object = MibTableColumn
mpsIngressCacheDestAddr = _MpsIngressCacheDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 7, 1, 2),
    _MpsIngressCacheDestAddr_Type()
)
mpsIngressCacheDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsIngressCacheDestAddr.setStatus("mandatory")
_MpsIngressCachePrefixLen_Type = Integer32
_MpsIngressCachePrefixLen_Object = MibTableColumn
mpsIngressCachePrefixLen = _MpsIngressCachePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 7, 1, 3),
    _MpsIngressCachePrefixLen_Type()
)
mpsIngressCachePrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsIngressCachePrefixLen.setStatus("mandatory")


class _MpsIngressCacheEntryState_Type(Integer32):
    """Custom type mpsIngressCacheEntryState based on Integer32"""
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
        *(("doesNotExist", 1),
          ("inactive", 2),
          ("active", 3),
          ("negative", 4))
    )


_MpsIngressCacheEntryState_Type.__name__ = "Integer32"
_MpsIngressCacheEntryState_Object = MibTableColumn
mpsIngressCacheEntryState = _MpsIngressCacheEntryState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 7, 1, 4),
    _MpsIngressCacheEntryState_Type()
)
mpsIngressCacheEntryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsIngressCacheEntryState.setStatus("mandatory")
_MpsIngressCacheSrcInternetworkAddrType_Type = InternetworkAddrType
_MpsIngressCacheSrcInternetworkAddrType_Object = MibTableColumn
mpsIngressCacheSrcInternetworkAddrType = _MpsIngressCacheSrcInternetworkAddrType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 7, 1, 5),
    _MpsIngressCacheSrcInternetworkAddrType_Type()
)
mpsIngressCacheSrcInternetworkAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsIngressCacheSrcInternetworkAddrType.setStatus("mandatory")
_MpsIngressCacheSrcAddr_Type = InternetworkAddr
_MpsIngressCacheSrcAddr_Object = MibTableColumn
mpsIngressCacheSrcAddr = _MpsIngressCacheSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 7, 1, 6),
    _MpsIngressCacheSrcAddr_Type()
)
mpsIngressCacheSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsIngressCacheSrcAddr.setStatus("mandatory")
_MpsIngressCacheSourceMpcCtrlAtmAddr_Type = AtmAddr
_MpsIngressCacheSourceMpcCtrlAtmAddr_Object = MibTableColumn
mpsIngressCacheSourceMpcCtrlAtmAddr = _MpsIngressCacheSourceMpcCtrlAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 7, 1, 7),
    _MpsIngressCacheSourceMpcCtrlAtmAddr_Type()
)
mpsIngressCacheSourceMpcCtrlAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsIngressCacheSourceMpcCtrlAtmAddr.setStatus("mandatory")
_MpsIngressCacheResolvedAtmAddr_Type = AtmAddr
_MpsIngressCacheResolvedAtmAddr_Object = MibTableColumn
mpsIngressCacheResolvedAtmAddr = _MpsIngressCacheResolvedAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 7, 1, 8),
    _MpsIngressCacheResolvedAtmAddr_Type()
)
mpsIngressCacheResolvedAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsIngressCacheResolvedAtmAddr.setStatus("mandatory")
_MpsIngressCacheHoldTime_Type = TimeInterval
_MpsIngressCacheHoldTime_Object = MibTableColumn
mpsIngressCacheHoldTime = _MpsIngressCacheHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 7, 1, 9),
    _MpsIngressCacheHoldTime_Type()
)
mpsIngressCacheHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsIngressCacheHoldTime.setStatus("mandatory")
_MpsIngressCacheMpoaRequestId_Type = Integer32
_MpsIngressCacheMpoaRequestId_Object = MibTableColumn
mpsIngressCacheMpoaRequestId = _MpsIngressCacheMpoaRequestId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 7, 1, 10),
    _MpsIngressCacheMpoaRequestId_Type()
)
mpsIngressCacheMpoaRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsIngressCacheMpoaRequestId.setStatus("mandatory")
_MpsIngressCacheNhrpRequestId_Type = Integer32
_MpsIngressCacheNhrpRequestId_Object = MibTableColumn
mpsIngressCacheNhrpRequestId = _MpsIngressCacheNhrpRequestId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 7, 1, 11),
    _MpsIngressCacheNhrpRequestId_Type()
)
mpsIngressCacheNhrpRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsIngressCacheNhrpRequestId.setStatus("mandatory")


class _MpsIngressCacheServiceCategory_Type(Integer32):
    """Custom type mpsIngressCacheServiceCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpsIngressCacheServiceCategory_Type.__name__ = "Integer32"
_MpsIngressCacheServiceCategory_Object = MibTableColumn
mpsIngressCacheServiceCategory = _MpsIngressCacheServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 7, 1, 12),
    _MpsIngressCacheServiceCategory_Type()
)
mpsIngressCacheServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsIngressCacheServiceCategory.setStatus("mandatory")
_MpsEgressCacheTable_Object = MibTable
mpsEgressCacheTable = _MpsEgressCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 8)
)
if mibBuilder.loadTexts:
    mpsEgressCacheTable.setStatus("mandatory")
_MpsEgressCacheEntry_Object = MibTableRow
mpsEgressCacheEntry = _MpsEgressCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 8, 1)
)
mpsEgressCacheEntry.setIndexNames(
    (0, "MPOA-MIB", "mpsEgressCacheId"),
    (0, "MPOA-MIB", "mpsIndex"),
    (0, "MPOA-MIB", "mpsMpcIndex"),
)
if mibBuilder.loadTexts:
    mpsEgressCacheEntry.setStatus("mandatory")
_MpsEgressCacheId_Type = Integer32
_MpsEgressCacheId_Object = MibTableColumn
mpsEgressCacheId = _MpsEgressCacheId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 8, 1, 1),
    _MpsEgressCacheId_Type()
)
mpsEgressCacheId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsEgressCacheId.setStatus("mandatory")
_MpsEgressCacheDestInternetworkAddrType_Type = InternetworkAddrType
_MpsEgressCacheDestInternetworkAddrType_Object = MibTableColumn
mpsEgressCacheDestInternetworkAddrType = _MpsEgressCacheDestInternetworkAddrType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 8, 1, 2),
    _MpsEgressCacheDestInternetworkAddrType_Type()
)
mpsEgressCacheDestInternetworkAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsEgressCacheDestInternetworkAddrType.setStatus("mandatory")
_MpsEgressCacheDestAddr_Type = InternetworkAddr
_MpsEgressCacheDestAddr_Object = MibTableColumn
mpsEgressCacheDestAddr = _MpsEgressCacheDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 8, 1, 3),
    _MpsEgressCacheDestAddr_Type()
)
mpsEgressCacheDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsEgressCacheDestAddr.setStatus("mandatory")


class _MpsEgressCachePrefixLen_Type(Integer32):
    """Custom type mpsEgressCachePrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MpsEgressCachePrefixLen_Type.__name__ = "Integer32"
_MpsEgressCachePrefixLen_Object = MibTableColumn
mpsEgressCachePrefixLen = _MpsEgressCachePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 8, 1, 4),
    _MpsEgressCachePrefixLen_Type()
)
mpsEgressCachePrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsEgressCachePrefixLen.setStatus("mandatory")
_MpsEgressCacheHoldTime_Type = TimeInterval
_MpsEgressCacheHoldTime_Object = MibTableColumn
mpsEgressCacheHoldTime = _MpsEgressCacheHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 8, 1, 5),
    _MpsEgressCacheHoldTime_Type()
)
mpsEgressCacheHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsEgressCacheHoldTime.setStatus("mandatory")


class _MpsEgressCacheEntryState_Type(Integer32):
    """Custom type mpsEgressCacheEntryState based on Integer32"""
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
        *(("doesNotExist", 1),
          ("inactive", 2),
          ("active", 3),
          ("negative", 4))
    )


_MpsEgressCacheEntryState_Type.__name__ = "Integer32"
_MpsEgressCacheEntryState_Object = MibTableColumn
mpsEgressCacheEntryState = _MpsEgressCacheEntryState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 8, 1, 6),
    _MpsEgressCacheEntryState_Type()
)
mpsEgressCacheEntryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsEgressCacheEntryState.setStatus("mandatory")


class _MpsEgressCacheDataLinkHeader_Type(OctetString):
    """Custom type mpsEgressCacheDataLinkHeader based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpsEgressCacheDataLinkHeader_Type.__name__ = "OctetString"
_MpsEgressCacheDataLinkHeader_Object = MibTableColumn
mpsEgressCacheDataLinkHeader = _MpsEgressCacheDataLinkHeader_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 8, 1, 7),
    _MpsEgressCacheDataLinkHeader_Type()
)
mpsEgressCacheDataLinkHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsEgressCacheDataLinkHeader.setStatus("mandatory")
_MpsEgressCacheElanId_Type = Integer32
_MpsEgressCacheElanId_Object = MibTableColumn
mpsEgressCacheElanId = _MpsEgressCacheElanId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 8, 1, 8),
    _MpsEgressCacheElanId_Type()
)
mpsEgressCacheElanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsEgressCacheElanId.setStatus("mandatory")
_MpsEgressCacheSourceClientAtmAddr_Type = AtmAddr
_MpsEgressCacheSourceClientAtmAddr_Object = MibTableColumn
mpsEgressCacheSourceClientAtmAddr = _MpsEgressCacheSourceClientAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 8, 1, 9),
    _MpsEgressCacheSourceClientAtmAddr_Type()
)
mpsEgressCacheSourceClientAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsEgressCacheSourceClientAtmAddr.setStatus("mandatory")
_MpsEgressCacheNhrpRequestId_Type = Integer32
_MpsEgressCacheNhrpRequestId_Object = MibTableColumn
mpsEgressCacheNhrpRequestId = _MpsEgressCacheNhrpRequestId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 8, 1, 10),
    _MpsEgressCacheNhrpRequestId_Type()
)
mpsEgressCacheNhrpRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsEgressCacheNhrpRequestId.setStatus("mandatory")
_MpsEgressCacheMpoaRequestId_Type = Integer32
_MpsEgressCacheMpoaRequestId_Object = MibTableColumn
mpsEgressCacheMpoaRequestId = _MpsEgressCacheMpoaRequestId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 8, 1, 11),
    _MpsEgressCacheMpoaRequestId_Type()
)
mpsEgressCacheMpoaRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsEgressCacheMpoaRequestId.setStatus("mandatory")


class _MpsEgressCacheServiceCategory_Type(Integer32):
    """Custom type mpsEgressCacheServiceCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpsEgressCacheServiceCategory_Type.__name__ = "Integer32"
_MpsEgressCacheServiceCategory_Object = MibTableColumn
mpsEgressCacheServiceCategory = _MpsEgressCacheServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 8, 1, 12),
    _MpsEgressCacheServiceCategory_Type()
)
mpsEgressCacheServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsEgressCacheServiceCategory.setStatus("mandatory")
_MpsEgressCacheNextHopInternetworkAddrType_Type = InternetworkAddrType
_MpsEgressCacheNextHopInternetworkAddrType_Object = MibTableColumn
mpsEgressCacheNextHopInternetworkAddrType = _MpsEgressCacheNextHopInternetworkAddrType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 8, 1, 13),
    _MpsEgressCacheNextHopInternetworkAddrType_Type()
)
mpsEgressCacheNextHopInternetworkAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsEgressCacheNextHopInternetworkAddrType.setStatus("mandatory")
_MpsEgressCacheNextHopAddr_Type = InternetworkAddr
_MpsEgressCacheNextHopAddr_Object = MibTableColumn
mpsEgressCacheNextHopAddr = _MpsEgressCacheNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 8, 1, 14),
    _MpsEgressCacheNextHopAddr_Type()
)
mpsEgressCacheNextHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsEgressCacheNextHopAddr.setStatus("mandatory")
_MpsMpcTable_Object = MibTable
mpsMpcTable = _MpsMpcTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 9)
)
if mibBuilder.loadTexts:
    mpsMpcTable.setStatus("mandatory")
_MpsMpcEntry_Object = MibTableRow
mpsMpcEntry = _MpsMpcEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 9, 1)
)
mpsMpcEntry.setIndexNames(
    (0, "MPOA-MIB", "mpsIndex"),
    (0, "MPOA-MIB", "mpsMpcIndex"),
)
if mibBuilder.loadTexts:
    mpsMpcEntry.setStatus("mandatory")
_MpsMpcIndex_Type = MpcIndex
_MpsMpcIndex_Object = MibTableColumn
mpsMpcIndex = _MpsMpcIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 9, 1, 1),
    _MpsMpcIndex_Type()
)
mpsMpcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsMpcIndex.setStatus("mandatory")
_MpsMpcCtrlAtmAddr_Type = AtmAddr
_MpsMpcCtrlAtmAddr_Object = MibTableColumn
mpsMpcCtrlAtmAddr = _MpsMpcCtrlAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 3, 9, 1, 2),
    _MpsMpcCtrlAtmAddr_Type()
)
mpsMpcCtrlAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpsMpcCtrlAtmAddr.setStatus("mandatory")
_MpoaMIBConformance_ObjectIdentity = ObjectIdentity
mpoaMIBConformance = _MpoaMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2)
)
_MpoaMIBGroups_ObjectIdentity = ObjectIdentity
mpoaMIBGroups = _MpoaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 1)
)
_MpoaDeviceTypeGroup_ObjectIdentity = ObjectIdentity
mpoaDeviceTypeGroup = _MpoaDeviceTypeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 1, 1)
)
_MpoaDeviceTypeMpsMacGroup_ObjectIdentity = ObjectIdentity
mpoaDeviceTypeMpsMacGroup = _MpoaDeviceTypeMpsMacGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 1, 2)
)
_MpcConfigGroup_ObjectIdentity = ObjectIdentity
mpcConfigGroup = _MpcConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 1, 3)
)
_MpcActualGroup_ObjectIdentity = ObjectIdentity
mpcActualGroup = _MpcActualGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 1, 4)
)
_MpcDataAtmAddressGroup_ObjectIdentity = ObjectIdentity
mpcDataAtmAddressGroup = _MpcDataAtmAddressGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 1, 5)
)
_MpcStatisticsGroup_ObjectIdentity = ObjectIdentity
mpcStatisticsGroup = _MpcStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 1, 6)
)
_MpcProtocolGroup_ObjectIdentity = ObjectIdentity
mpcProtocolGroup = _MpcProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 1, 7)
)
_MpcMappingGroup_ObjectIdentity = ObjectIdentity
mpcMappingGroup = _MpcMappingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 1, 8)
)
_MpcMpsGroup_ObjectIdentity = ObjectIdentity
mpcMpsGroup = _MpcMpsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 1, 9)
)
_MpcMpsMacAddressGroup_ObjectIdentity = ObjectIdentity
mpcMpsMacAddressGroup = _MpcMpsMacAddressGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 1, 10)
)
_MpcIngressCacheTotalPacketGroup_ObjectIdentity = ObjectIdentity
mpcIngressCacheTotalPacketGroup = _MpcIngressCacheTotalPacketGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 1, 11)
)
_MpcIngressCacheTotalOctetGroup_ObjectIdentity = ObjectIdentity
mpcIngressCacheTotalOctetGroup = _MpcIngressCacheTotalOctetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 1, 12)
)
_MpcIngressCacheGroup_ObjectIdentity = ObjectIdentity
mpcIngressCacheGroup = _MpcIngressCacheGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 1, 13)
)
_MpcEgressCacheTotalPacketGroup_ObjectIdentity = ObjectIdentity
mpcEgressCacheTotalPacketGroup = _MpcEgressCacheTotalPacketGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 1, 14)
)
_MpcEgressCacheTotalOctetGroup_ObjectIdentity = ObjectIdentity
mpcEgressCacheTotalOctetGroup = _MpcEgressCacheTotalOctetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 1, 15)
)
_MpcEgressCacheGroup_ObjectIdentity = ObjectIdentity
mpcEgressCacheGroup = _MpcEgressCacheGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 1, 16)
)
_MpsConfigGroup_ObjectIdentity = ObjectIdentity
mpsConfigGroup = _MpsConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 1, 17)
)
_MpsActualGroup_ObjectIdentity = ObjectIdentity
mpsActualGroup = _MpsActualGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 1, 18)
)
_MpsStatisticsGroup_ObjectIdentity = ObjectIdentity
mpsStatisticsGroup = _MpsStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 1, 19)
)
_MpsProtocolGroup_ObjectIdentity = ObjectIdentity
mpsProtocolGroup = _MpsProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 1, 20)
)
_MpsMappingGroup_ObjectIdentity = ObjectIdentity
mpsMappingGroup = _MpsMappingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 1, 21)
)
_MpsMpcGroup_ObjectIdentity = ObjectIdentity
mpsMpcGroup = _MpsMpcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 1, 22)
)
_MpsIngressCacheGroup_ObjectIdentity = ObjectIdentity
mpsIngressCacheGroup = _MpsIngressCacheGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 1, 23)
)
_MpsEgressCacheGroup_ObjectIdentity = ObjectIdentity
mpsEgressCacheGroup = _MpsEgressCacheGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 1, 24)
)
_MpoaMIBCompliances_ObjectIdentity = ObjectIdentity
mpoaMIBCompliances = _MpoaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 2)
)
_MpoaMpcMibBasicCompliance_ObjectIdentity = ObjectIdentity
mpoaMpcMibBasicCompliance = _MpoaMpcMibBasicCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 2, 1)
)
_MpoaMpcMibAdvancedCompliance_ObjectIdentity = ObjectIdentity
mpoaMpcMibAdvancedCompliance = _MpoaMpcMibAdvancedCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 2, 2)
)
_MpoaMpcMibAdvancedPlusOctetsCompliance_ObjectIdentity = ObjectIdentity
mpoaMpcMibAdvancedPlusOctetsCompliance = _MpoaMpcMibAdvancedPlusOctetsCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 2, 3)
)
_MpoaMpsMibBasicCompliance_ObjectIdentity = ObjectIdentity
mpoaMpsMibBasicCompliance = _MpoaMpsMibBasicCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 2, 4)
)
_MpoaMpsMibAdvancedCompliance_ObjectIdentity = ObjectIdentity
mpoaMpsMibAdvancedCompliance = _MpoaMpsMibAdvancedCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 2, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPOA-MIB",
    **{"LecIndex": LecIndex,
       "AtmConfigAddr": AtmConfigAddr,
       "InternetworkAddrType": InternetworkAddrType,
       "InternetworkAddr": InternetworkAddr,
       "MpcIndex": MpcIndex,
       "MpsIndex": MpsIndex,
       "atmfMpoa": atmfMpoa,
       "mpoaMIB": mpoaMIB,
       "mpoaMIBObjects": mpoaMIBObjects,
       "mpoaCommonObjects": mpoaCommonObjects,
       "deviceTypeTable": deviceTypeTable,
       "deviceTypeEntry": deviceTypeEntry,
       "deviceTypeIndex": deviceTypeIndex,
       "deviceTypeLecIndex": deviceTypeLecIndex,
       "deviceTypeRemoteLecAtmAddress": deviceTypeRemoteLecAtmAddress,
       "deviceTypeType": deviceTypeType,
       "deviceTypeMpsAtmAddress": deviceTypeMpsAtmAddress,
       "deviceTypeMpcAtmAddress": deviceTypeMpcAtmAddress,
       "deviceTypeMpsMacAddressTable": deviceTypeMpsMacAddressTable,
       "deviceTypeMpsMacAddressEntry": deviceTypeMpsMacAddressEntry,
       "deviceTypeMpsMacAddress": deviceTypeMpsMacAddress,
       "mpcObjects": mpcObjects,
       "mpcNextIndex": mpcNextIndex,
       "mpcConfigTable": mpcConfigTable,
       "mpcConfigEntry": mpcConfigEntry,
       "mpcIndex": mpcIndex,
       "mpcRowStatus": mpcRowStatus,
       "mpcConfigMode": mpcConfigMode,
       "mpcCtrlAtmAddr": mpcCtrlAtmAddr,
       "mpcSCSetupFrameCount": mpcSCSetupFrameCount,
       "mpcSCSetupFrameTime": mpcSCSetupFrameTime,
       "mpcInitialRetryTime": mpcInitialRetryTime,
       "mpcRetryTimeMaximum": mpcRetryTimeMaximum,
       "mpcHoldDownTime": mpcHoldDownTime,
       "mpcActualTable": mpcActualTable,
       "mpcActualEntry": mpcActualEntry,
       "mpcActualState": mpcActualState,
       "mpcDiscontinuityTime": mpcDiscontinuityTime,
       "mpcActualConfigMode": mpcActualConfigMode,
       "mpcActualSCSetupFrameCount": mpcActualSCSetupFrameCount,
       "mpcActualSCSetupFrameTime": mpcActualSCSetupFrameTime,
       "mpcActualInitialRetryTime": mpcActualInitialRetryTime,
       "mpcActualRetryTimeMaximum": mpcActualRetryTimeMaximum,
       "mpcActualHoldDownTime": mpcActualHoldDownTime,
       "mpcDataAtmAddressTable": mpcDataAtmAddressTable,
       "mpcDataAtmAddressEntry": mpcDataAtmAddressEntry,
       "mpcDataAtmAddress": mpcDataAtmAddress,
       "mpcDataAtmAddressRowStatus": mpcDataAtmAddressRowStatus,
       "mpcStatisticsTable": mpcStatisticsTable,
       "mpcStatisticsEntry": mpcStatisticsEntry,
       "mpcStatTxMpoaResolveRequests": mpcStatTxMpoaResolveRequests,
       "mpcStatRxMpoaResolveReplyAcks": mpcStatRxMpoaResolveReplyAcks,
       "mpcStatRxMpoaResolveReplyInsufECResources": mpcStatRxMpoaResolveReplyInsufECResources,
       "mpcStatRxMpoaResolveReplyInsufSCResources": mpcStatRxMpoaResolveReplyInsufSCResources,
       "mpcStatRxMpoaResolveReplyInsufEitherResources": mpcStatRxMpoaResolveReplyInsufEitherResources,
       "mpcStatRxMpoaResolveReplyUnsupportedInetProt": mpcStatRxMpoaResolveReplyUnsupportedInetProt,
       "mpcStatRxMpoaResolveReplyUnsupportedMacEncaps": mpcStatRxMpoaResolveReplyUnsupportedMacEncaps,
       "mpcStatRxMpoaResolveReplyUnspecifiedOther": mpcStatRxMpoaResolveReplyUnspecifiedOther,
       "mpcStatRxMpoaImpRequests": mpcStatRxMpoaImpRequests,
       "mpcStatTxMpoaImpReplyAcks": mpcStatTxMpoaImpReplyAcks,
       "mpcStatTxMpoaImpReplyInsufECResources": mpcStatTxMpoaImpReplyInsufECResources,
       "mpcStatTxMpoaImpReplyInsufSCResources": mpcStatTxMpoaImpReplyInsufSCResources,
       "mpcStatTxMpoaImpReplyInsufEitherResources": mpcStatTxMpoaImpReplyInsufEitherResources,
       "mpcStatTxMpoaImpReplyUnsupportedInetProt": mpcStatTxMpoaImpReplyUnsupportedInetProt,
       "mpcStatTxMpoaImpReplyUnsupportedMacEncaps": mpcStatTxMpoaImpReplyUnsupportedMacEncaps,
       "mpcStatTxMpoaImpReplyUnspecifiedOther": mpcStatTxMpoaImpReplyUnspecifiedOther,
       "mpcStatTxMpoaEgressCachePurgeRequests": mpcStatTxMpoaEgressCachePurgeRequests,
       "mpcStatRxMpoaEgressCachePurgeReplies": mpcStatRxMpoaEgressCachePurgeReplies,
       "mpcStatRxMpoaKeepAlives": mpcStatRxMpoaKeepAlives,
       "mpcStatRxMpoaTriggers": mpcStatRxMpoaTriggers,
       "mpcStatRxMpoaDataPlanePurges": mpcStatRxMpoaDataPlanePurges,
       "mpcStatTxMpoaDataPlanePurges": mpcStatTxMpoaDataPlanePurges,
       "mpcStatRxNhrpPurgeRequests": mpcStatRxNhrpPurgeRequests,
       "mpcStatTxNhrpPurgeReplies": mpcStatTxNhrpPurgeReplies,
       "mpcStatRxErrUnrecognizedExtensions": mpcStatRxErrUnrecognizedExtensions,
       "mpcStatRxErrLoopDetecteds": mpcStatRxErrLoopDetecteds,
       "mpcStatRxErrProtoAddrUnreachables": mpcStatRxErrProtoAddrUnreachables,
       "mpcStatRxErrProtoErrors": mpcStatRxErrProtoErrors,
       "mpcStatRxErrSduSizeExceededs": mpcStatRxErrSduSizeExceededs,
       "mpcStatRxErrInvalidExtensions": mpcStatRxErrInvalidExtensions,
       "mpcStatRxErrInvalidReplies": mpcStatRxErrInvalidReplies,
       "mpcStatRxErrAuthenticationFailures": mpcStatRxErrAuthenticationFailures,
       "mpcStatRxErrHopCountExceededs": mpcStatRxErrHopCountExceededs,
       "mpcProtocolTable": mpcProtocolTable,
       "mpcProtocolEntry": mpcProtocolEntry,
       "mpcFlowDetectProtocol": mpcFlowDetectProtocol,
       "mpcLECSValue": mpcLECSValue,
       "mpcProtocolRowStatus": mpcProtocolRowStatus,
       "mpcMappingTable": mpcMappingTable,
       "mpcMappingEntry": mpcMappingEntry,
       "mpcMappingRowStatus": mpcMappingRowStatus,
       "mpcMappingIndex": mpcMappingIndex,
       "mpcMpsTable": mpcMpsTable,
       "mpcMpsEntry": mpcMpsEntry,
       "mpcMpsIndex": mpcMpsIndex,
       "mpcMpsAtmAddr": mpcMpsAtmAddr,
       "mpcMpsMacAddressTable": mpcMpsMacAddressTable,
       "mpcMpsMacAddressEntry": mpcMpsMacAddressEntry,
       "mpcLecIndex": mpcLecIndex,
       "mpcMpsMacAddress": mpcMpsMacAddress,
       "mpcIngressCacheTxTotalPackets": mpcIngressCacheTxTotalPackets,
       "mpcIngressCacheTxTotalOctets": mpcIngressCacheTxTotalOctets,
       "mpcIngressCacheTable": mpcIngressCacheTable,
       "mpcIngressCacheEntry": mpcIngressCacheEntry,
       "mpcIngressCacheDestInetworkAddrType": mpcIngressCacheDestInetworkAddrType,
       "mpcIngressCacheDestAddr": mpcIngressCacheDestAddr,
       "mpcIngressCachePrefixLen": mpcIngressCachePrefixLen,
       "mpcIngressCacheDestAtmAddr": mpcIngressCacheDestAtmAddr,
       "mpcIngressCacheSrcAtmAddr": mpcIngressCacheSrcAtmAddr,
       "mpcIngressCacheEntryState": mpcIngressCacheEntryState,
       "mpcIngressCacheEgressCacheTagValid": mpcIngressCacheEgressCacheTagValid,
       "mpcIngressCacheEgressCacheTag": mpcIngressCacheEgressCacheTag,
       "mpcIngressCacheLastNhrpCieCode": mpcIngressCacheLastNhrpCieCode,
       "mpcIngressCacheSigErrCode": mpcIngressCacheSigErrCode,
       "mpcIngressCacheRetries": mpcIngressCacheRetries,
       "mpcIngressCacheTimeUntilNextResolutionRequest": mpcIngressCacheTimeUntilNextResolutionRequest,
       "mpcIngressCacheHoldingTime": mpcIngressCacheHoldingTime,
       "mpcIngressCacheServiceCategory": mpcIngressCacheServiceCategory,
       "mpcEgressCacheRxTotalPackets": mpcEgressCacheRxTotalPackets,
       "mpcEgressCacheRxTotalOctets": mpcEgressCacheRxTotalOctets,
       "mpcEgressCacheTable": mpcEgressCacheTable,
       "mpcEgressCacheEntry": mpcEgressCacheEntry,
       "mpcEgressCacheId": mpcEgressCacheId,
       "mpcEgressCacheInetworkAddrType": mpcEgressCacheInetworkAddrType,
       "mpcEgressCacheIDestAddr": mpcEgressCacheIDestAddr,
       "mpcEgressCachePrefixLen": mpcEgressCachePrefixLen,
       "mpcEgressCacheEntryState": mpcEgressCacheEntryState,
       "mpcEgressCacheEgressCacheTagValid": mpcEgressCacheEgressCacheTagValid,
       "mpcEgressCacheEgressCacheTag": mpcEgressCacheEgressCacheTag,
       "mpcEgressCacheHoldTime": mpcEgressCacheHoldTime,
       "mpcEgressCacheDataLinkHeader": mpcEgressCacheDataLinkHeader,
       "mpcEgressCacheIngressMpcDataAtmAddr": mpcEgressCacheIngressMpcDataAtmAddr,
       "mpcEgressCacheLecIndex": mpcEgressCacheLecIndex,
       "mpcEgressCacheServiceCategory": mpcEgressCacheServiceCategory,
       "mpsObjects": mpsObjects,
       "mpsNextIndex": mpsNextIndex,
       "mpsConfigTable": mpsConfigTable,
       "mpsConfigEntry": mpsConfigEntry,
       "mpsIndex": mpsIndex,
       "mpsRowStatus": mpsRowStatus,
       "mpsConfigMode": mpsConfigMode,
       "mpsCtrlAtmAddr": mpsCtrlAtmAddr,
       "mpsKeepAliveTime": mpsKeepAliveTime,
       "mpsKeepAliveLifeTime": mpsKeepAliveLifeTime,
       "mpsInitialRetryTime": mpsInitialRetryTime,
       "mpsRetryTimeMaximum": mpsRetryTimeMaximum,
       "mpsGiveupTime": mpsGiveupTime,
       "mpsDefaultHoldingTime": mpsDefaultHoldingTime,
       "mpsActualTable": mpsActualTable,
       "mpsActualEntry": mpsActualEntry,
       "mpsActualState": mpsActualState,
       "mpsDiscontinuityTime": mpsDiscontinuityTime,
       "mpsActualConfigMode": mpsActualConfigMode,
       "mpsActualKeepAlive": mpsActualKeepAlive,
       "mpsActualKeepAliveLifeTime": mpsActualKeepAliveLifeTime,
       "mpsActualInitialRetryTime": mpsActualInitialRetryTime,
       "mpsActualRetryTimeMaximum": mpsActualRetryTimeMaximum,
       "mpsActualGiveupTime": mpsActualGiveupTime,
       "mpsActualDefaultHoldingTime": mpsActualDefaultHoldingTime,
       "mpsStatisticsTable": mpsStatisticsTable,
       "mpsStatisticsEntry": mpsStatisticsEntry,
       "mpsStatRxMpoaResolveRequests": mpsStatRxMpoaResolveRequests,
       "mpsStatTxMpoaResolveReplyAcks": mpsStatTxMpoaResolveReplyAcks,
       "mpsStatTxMpoaResolveReplyInsufECResources": mpsStatTxMpoaResolveReplyInsufECResources,
       "mpsStatTxMpoaResolveReplyInsufSCResources": mpsStatTxMpoaResolveReplyInsufSCResources,
       "mpsStatTxMpoaResolveReplyInsufEitherResources": mpsStatTxMpoaResolveReplyInsufEitherResources,
       "mpsStatTxMpoaResolveReplyUnsupportedInetProt": mpsStatTxMpoaResolveReplyUnsupportedInetProt,
       "mpsStatTxMpoaResolveReplyUnsupportedMacEncaps": mpsStatTxMpoaResolveReplyUnsupportedMacEncaps,
       "mpsStatTxMpoaResolveReplyUnspecifiedOther": mpsStatTxMpoaResolveReplyUnspecifiedOther,
       "mpsStatTxMpoaResolveReplyOther": mpsStatTxMpoaResolveReplyOther,
       "mpsStatGiveupTimeExpireds": mpsStatGiveupTimeExpireds,
       "mpsStatTxMpoaImpRequests": mpsStatTxMpoaImpRequests,
       "mpsStatRxMpoaImpReplyAcks": mpsStatRxMpoaImpReplyAcks,
       "mpsStatRxMpoaImpReplyInsufECResources": mpsStatRxMpoaImpReplyInsufECResources,
       "mpsStatRxMpoaImpReplyInsufSCResources": mpsStatRxMpoaImpReplyInsufSCResources,
       "mpsStatRxMpoaImpReplyInsufEitherResources": mpsStatRxMpoaImpReplyInsufEitherResources,
       "mpsStatRxMpoaImpReplyUnsupportedInetProt": mpsStatRxMpoaImpReplyUnsupportedInetProt,
       "mpsStatRxMpoaImpReplyUnsupportedMacEncaps": mpsStatRxMpoaImpReplyUnsupportedMacEncaps,
       "mpsStatRxMpoaImpReplyUnspecifiedOther": mpsStatRxMpoaImpReplyUnspecifiedOther,
       "mpsStatRxMpoaImpReplyOther": mpsStatRxMpoaImpReplyOther,
       "mpsStatRxMpoaEgressCachePurgeRequests": mpsStatRxMpoaEgressCachePurgeRequests,
       "mpsStatTxMpoaEgressCachePurgeReplies": mpsStatTxMpoaEgressCachePurgeReplies,
       "mpsStatTxMpoaTriggers": mpsStatTxMpoaTriggers,
       "mpsStatTxNhrpResolveRequests": mpsStatTxNhrpResolveRequests,
       "mpsStatRxNhrpResolveReplies": mpsStatRxNhrpResolveReplies,
       "mpsStatRxNhrpResolveRequests": mpsStatRxNhrpResolveRequests,
       "mpsStatTxNhrpResolveReplies": mpsStatTxNhrpResolveReplies,
       "mpsProtocolTable": mpsProtocolTable,
       "mpsProtocolEntry": mpsProtocolEntry,
       "mpsInternetworkLayerProtocol": mpsInternetworkLayerProtocol,
       "mpsLECSValue": mpsLECSValue,
       "mpsProtocolRowStatus": mpsProtocolRowStatus,
       "mpsMappingTable": mpsMappingTable,
       "mpsMappingEntry": mpsMappingEntry,
       "mpsMappingRowStatus": mpsMappingRowStatus,
       "mpsMappingIndex": mpsMappingIndex,
       "mpsIngressCacheTable": mpsIngressCacheTable,
       "mpsIngressCacheEntry": mpsIngressCacheEntry,
       "mpsIngressCacheDestInternetworkAddrType": mpsIngressCacheDestInternetworkAddrType,
       "mpsIngressCacheDestAddr": mpsIngressCacheDestAddr,
       "mpsIngressCachePrefixLen": mpsIngressCachePrefixLen,
       "mpsIngressCacheEntryState": mpsIngressCacheEntryState,
       "mpsIngressCacheSrcInternetworkAddrType": mpsIngressCacheSrcInternetworkAddrType,
       "mpsIngressCacheSrcAddr": mpsIngressCacheSrcAddr,
       "mpsIngressCacheSourceMpcCtrlAtmAddr": mpsIngressCacheSourceMpcCtrlAtmAddr,
       "mpsIngressCacheResolvedAtmAddr": mpsIngressCacheResolvedAtmAddr,
       "mpsIngressCacheHoldTime": mpsIngressCacheHoldTime,
       "mpsIngressCacheMpoaRequestId": mpsIngressCacheMpoaRequestId,
       "mpsIngressCacheNhrpRequestId": mpsIngressCacheNhrpRequestId,
       "mpsIngressCacheServiceCategory": mpsIngressCacheServiceCategory,
       "mpsEgressCacheTable": mpsEgressCacheTable,
       "mpsEgressCacheEntry": mpsEgressCacheEntry,
       "mpsEgressCacheId": mpsEgressCacheId,
       "mpsEgressCacheDestInternetworkAddrType": mpsEgressCacheDestInternetworkAddrType,
       "mpsEgressCacheDestAddr": mpsEgressCacheDestAddr,
       "mpsEgressCachePrefixLen": mpsEgressCachePrefixLen,
       "mpsEgressCacheHoldTime": mpsEgressCacheHoldTime,
       "mpsEgressCacheEntryState": mpsEgressCacheEntryState,
       "mpsEgressCacheDataLinkHeader": mpsEgressCacheDataLinkHeader,
       "mpsEgressCacheElanId": mpsEgressCacheElanId,
       "mpsEgressCacheSourceClientAtmAddr": mpsEgressCacheSourceClientAtmAddr,
       "mpsEgressCacheNhrpRequestId": mpsEgressCacheNhrpRequestId,
       "mpsEgressCacheMpoaRequestId": mpsEgressCacheMpoaRequestId,
       "mpsEgressCacheServiceCategory": mpsEgressCacheServiceCategory,
       "mpsEgressCacheNextHopInternetworkAddrType": mpsEgressCacheNextHopInternetworkAddrType,
       "mpsEgressCacheNextHopAddr": mpsEgressCacheNextHopAddr,
       "mpsMpcTable": mpsMpcTable,
       "mpsMpcEntry": mpsMpcEntry,
       "mpsMpcIndex": mpsMpcIndex,
       "mpsMpcCtrlAtmAddr": mpsMpcCtrlAtmAddr,
       "mpoaMIBConformance": mpoaMIBConformance,
       "mpoaMIBGroups": mpoaMIBGroups,
       "mpoaDeviceTypeGroup": mpoaDeviceTypeGroup,
       "mpoaDeviceTypeMpsMacGroup": mpoaDeviceTypeMpsMacGroup,
       "mpcConfigGroup": mpcConfigGroup,
       "mpcActualGroup": mpcActualGroup,
       "mpcDataAtmAddressGroup": mpcDataAtmAddressGroup,
       "mpcStatisticsGroup": mpcStatisticsGroup,
       "mpcProtocolGroup": mpcProtocolGroup,
       "mpcMappingGroup": mpcMappingGroup,
       "mpcMpsGroup": mpcMpsGroup,
       "mpcMpsMacAddressGroup": mpcMpsMacAddressGroup,
       "mpcIngressCacheTotalPacketGroup": mpcIngressCacheTotalPacketGroup,
       "mpcIngressCacheTotalOctetGroup": mpcIngressCacheTotalOctetGroup,
       "mpcIngressCacheGroup": mpcIngressCacheGroup,
       "mpcEgressCacheTotalPacketGroup": mpcEgressCacheTotalPacketGroup,
       "mpcEgressCacheTotalOctetGroup": mpcEgressCacheTotalOctetGroup,
       "mpcEgressCacheGroup": mpcEgressCacheGroup,
       "mpsConfigGroup": mpsConfigGroup,
       "mpsActualGroup": mpsActualGroup,
       "mpsStatisticsGroup": mpsStatisticsGroup,
       "mpsProtocolGroup": mpsProtocolGroup,
       "mpsMappingGroup": mpsMappingGroup,
       "mpsMpcGroup": mpsMpcGroup,
       "mpsIngressCacheGroup": mpsIngressCacheGroup,
       "mpsEgressCacheGroup": mpsEgressCacheGroup,
       "mpoaMIBCompliances": mpoaMIBCompliances,
       "mpoaMpcMibBasicCompliance": mpoaMpcMibBasicCompliance,
       "mpoaMpcMibAdvancedCompliance": mpoaMpcMibAdvancedCompliance,
       "mpoaMpcMibAdvancedPlusOctetsCompliance": mpoaMpcMibAdvancedPlusOctetsCompliance,
       "mpoaMpsMibBasicCompliance": mpoaMpsMibBasicCompliance,
       "mpoaMpsMibAdvancedCompliance": mpoaMpsMibAdvancedCompliance}
)
