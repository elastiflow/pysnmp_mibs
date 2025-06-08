# SNMP MIB module (CIE1000-MSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CIE1000-MSTP-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 20:26:42 2025
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

(CIE1000DisplayString,
 CIE1000InterfaceIndex,
 CIE1000Unsigned16,
 CIE1000Unsigned8,
 CIE1000VlanListQuarter) = mibBuilder.importSymbols(
    "CIE1000-TC",
    "CIE1000DisplayString",
    "CIE1000InterfaceIndex",
    "CIE1000Unsigned16",
    "CIE1000Unsigned8",
    "CIE1000VlanListQuarter")

(cie1000SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCO-IE1000-MIB",
    "cie1000SwitchMgmt")

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

cie1000MstpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20)
)
if mibBuilder.loadTexts:
    cie1000MstpMib.setRevisions(
        ("2015-11-13 00:00",
         "2015-11-04 00:00",
         "2015-09-29 00:00",
         "2014-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CIE1000MSTPForceVersion(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stp", 0),
          ("rstp", 2),
          ("mstp", 3))
    )



class CIE1000MstpPoint2Point(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceTrue", 0),
          ("forceFalse", 1),
          ("auto", 2))
    )



class CIE1000MstpPortState(TextualConvention, Integer32):
    status = "current"
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
        *(("disabled", 0),
          ("discarding", 1),
          ("learning", 2),
          ("forwarding", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Cie1000MstpMibObjects_ObjectIdentity = ObjectIdentity
cie1000MstpMibObjects = _Cie1000MstpMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1)
)
_Cie1000MstpConfig_ObjectIdentity = ObjectIdentity
cie1000MstpConfig = _Cie1000MstpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2)
)
_Cie1000MstpConfigBridgeParams_ObjectIdentity = ObjectIdentity
cie1000MstpConfigBridgeParams = _Cie1000MstpConfigBridgeParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 1)
)
_Cie1000MstpConfigBridgeParamsBridgeMaxAge_Type = Unsigned32
_Cie1000MstpConfigBridgeParamsBridgeMaxAge_Object = MibScalar
cie1000MstpConfigBridgeParamsBridgeMaxAge = _Cie1000MstpConfigBridgeParamsBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 1, 1),
    _Cie1000MstpConfigBridgeParamsBridgeMaxAge_Type()
)
cie1000MstpConfigBridgeParamsBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigBridgeParamsBridgeMaxAge.setStatus("current")


class _Cie1000MstpConfigBridgeParamsBridgeHelloTime_Type(Unsigned32):
    """Custom type cie1000MstpConfigBridgeParamsBridgeHelloTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Cie1000MstpConfigBridgeParamsBridgeHelloTime_Type.__name__ = "Unsigned32"
_Cie1000MstpConfigBridgeParamsBridgeHelloTime_Object = MibScalar
cie1000MstpConfigBridgeParamsBridgeHelloTime = _Cie1000MstpConfigBridgeParamsBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 1, 2),
    _Cie1000MstpConfigBridgeParamsBridgeHelloTime_Type()
)
cie1000MstpConfigBridgeParamsBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigBridgeParamsBridgeHelloTime.setStatus("current")


class _Cie1000MstpConfigBridgeParamsBridgeForwardDelay_Type(Unsigned32):
    """Custom type cie1000MstpConfigBridgeParamsBridgeForwardDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_Cie1000MstpConfigBridgeParamsBridgeForwardDelay_Type.__name__ = "Unsigned32"
_Cie1000MstpConfigBridgeParamsBridgeForwardDelay_Object = MibScalar
cie1000MstpConfigBridgeParamsBridgeForwardDelay = _Cie1000MstpConfigBridgeParamsBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 1, 3),
    _Cie1000MstpConfigBridgeParamsBridgeForwardDelay_Type()
)
cie1000MstpConfigBridgeParamsBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigBridgeParamsBridgeForwardDelay.setStatus("current")
_Cie1000MstpConfigBridgeParamsForceVersion_Type = CIE1000MSTPForceVersion
_Cie1000MstpConfigBridgeParamsForceVersion_Object = MibScalar
cie1000MstpConfigBridgeParamsForceVersion = _Cie1000MstpConfigBridgeParamsForceVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 1, 4),
    _Cie1000MstpConfigBridgeParamsForceVersion_Type()
)
cie1000MstpConfigBridgeParamsForceVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigBridgeParamsForceVersion.setStatus("current")


class _Cie1000MstpConfigBridgeParamsTxHoldCount_Type(Unsigned32):
    """Custom type cie1000MstpConfigBridgeParamsTxHoldCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Cie1000MstpConfigBridgeParamsTxHoldCount_Type.__name__ = "Unsigned32"
_Cie1000MstpConfigBridgeParamsTxHoldCount_Object = MibScalar
cie1000MstpConfigBridgeParamsTxHoldCount = _Cie1000MstpConfigBridgeParamsTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 1, 5),
    _Cie1000MstpConfigBridgeParamsTxHoldCount_Type()
)
cie1000MstpConfigBridgeParamsTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigBridgeParamsTxHoldCount.setStatus("current")


class _Cie1000MstpConfigBridgeParamsMaxHops_Type(CIE1000Unsigned8):
    """Custom type cie1000MstpConfigBridgeParamsMaxHops based on CIE1000Unsigned8"""
    subtypeSpec = CIE1000Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_Cie1000MstpConfigBridgeParamsMaxHops_Type.__name__ = "CIE1000Unsigned8"
_Cie1000MstpConfigBridgeParamsMaxHops_Object = MibScalar
cie1000MstpConfigBridgeParamsMaxHops = _Cie1000MstpConfigBridgeParamsMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 1, 6),
    _Cie1000MstpConfigBridgeParamsMaxHops_Type()
)
cie1000MstpConfigBridgeParamsMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigBridgeParamsMaxHops.setStatus("current")
_Cie1000MstpConfigBridgeParamsBpduFiltering_Type = TruthValue
_Cie1000MstpConfigBridgeParamsBpduFiltering_Object = MibScalar
cie1000MstpConfigBridgeParamsBpduFiltering = _Cie1000MstpConfigBridgeParamsBpduFiltering_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 1, 7),
    _Cie1000MstpConfigBridgeParamsBpduFiltering_Type()
)
cie1000MstpConfigBridgeParamsBpduFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigBridgeParamsBpduFiltering.setStatus("current")
_Cie1000MstpConfigBridgeParamsBpduGuard_Type = TruthValue
_Cie1000MstpConfigBridgeParamsBpduGuard_Object = MibScalar
cie1000MstpConfigBridgeParamsBpduGuard = _Cie1000MstpConfigBridgeParamsBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 1, 8),
    _Cie1000MstpConfigBridgeParamsBpduGuard_Type()
)
cie1000MstpConfigBridgeParamsBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigBridgeParamsBpduGuard.setStatus("current")
_Cie1000MstpConfigBridgeParamsErrorRecoveryDelay_Type = Unsigned32
_Cie1000MstpConfigBridgeParamsErrorRecoveryDelay_Object = MibScalar
cie1000MstpConfigBridgeParamsErrorRecoveryDelay = _Cie1000MstpConfigBridgeParamsErrorRecoveryDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 1, 9),
    _Cie1000MstpConfigBridgeParamsErrorRecoveryDelay_Type()
)
cie1000MstpConfigBridgeParamsErrorRecoveryDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigBridgeParamsErrorRecoveryDelay.setStatus("current")
_Cie1000MstpConfigMstiParamTable_Object = MibTable
cie1000MstpConfigMstiParamTable = _Cie1000MstpConfigMstiParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiParamTable.setStatus("current")
_Cie1000MstpConfigMstiParamEntry_Object = MibTableRow
cie1000MstpConfigMstiParamEntry = _Cie1000MstpConfigMstiParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 2, 1)
)
cie1000MstpConfigMstiParamEntry.setIndexNames(
    (0, "CIE1000-MSTP-MIB", "cie1000MstpConfigMstiParamInstance"),
)
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiParamEntry.setStatus("current")


class _Cie1000MstpConfigMstiParamInstance_Type(Integer32):
    """Custom type cie1000MstpConfigMstiParamInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cie1000MstpConfigMstiParamInstance_Type.__name__ = "Integer32"
_Cie1000MstpConfigMstiParamInstance_Object = MibTableColumn
cie1000MstpConfigMstiParamInstance = _Cie1000MstpConfigMstiParamInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 2, 1, 1),
    _Cie1000MstpConfigMstiParamInstance_Type()
)
cie1000MstpConfigMstiParamInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiParamInstance.setStatus("current")
_Cie1000MstpConfigMstiParamPriority_Type = CIE1000Unsigned8
_Cie1000MstpConfigMstiParamPriority_Object = MibTableColumn
cie1000MstpConfigMstiParamPriority = _Cie1000MstpConfigMstiParamPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 2, 1, 2),
    _Cie1000MstpConfigMstiParamPriority_Type()
)
cie1000MstpConfigMstiParamPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiParamPriority.setStatus("current")
_Cie1000MstpConfigMstiConfig_ObjectIdentity = ObjectIdentity
cie1000MstpConfigMstiConfig = _Cie1000MstpConfigMstiConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 3)
)
_Cie1000MstpConfigMstiConfigId_ObjectIdentity = ObjectIdentity
cie1000MstpConfigMstiConfigId = _Cie1000MstpConfigMstiConfigId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 3, 1)
)


class _Cie1000MstpConfigMstiConfigIdName_Type(CIE1000DisplayString):
    """Custom type cie1000MstpConfigMstiConfigIdName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Cie1000MstpConfigMstiConfigIdName_Type.__name__ = "CIE1000DisplayString"
_Cie1000MstpConfigMstiConfigIdName_Object = MibScalar
cie1000MstpConfigMstiConfigIdName = _Cie1000MstpConfigMstiConfigIdName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 3, 1, 1),
    _Cie1000MstpConfigMstiConfigIdName_Type()
)
cie1000MstpConfigMstiConfigIdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiConfigIdName.setStatus("current")
_Cie1000MstpConfigMstiConfigIdRevision_Type = CIE1000Unsigned16
_Cie1000MstpConfigMstiConfigIdRevision_Object = MibScalar
cie1000MstpConfigMstiConfigIdRevision = _Cie1000MstpConfigMstiConfigIdRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 3, 1, 2),
    _Cie1000MstpConfigMstiConfigIdRevision_Type()
)
cie1000MstpConfigMstiConfigIdRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiConfigIdRevision.setStatus("current")
_Cie1000MstpConfigMstiConfigTable_Object = MibTable
cie1000MstpConfigMstiConfigTable = _Cie1000MstpConfigMstiConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiConfigTable.setStatus("current")
_Cie1000MstpConfigMstiConfigEntry_Object = MibTableRow
cie1000MstpConfigMstiConfigEntry = _Cie1000MstpConfigMstiConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 3, 2, 1)
)
cie1000MstpConfigMstiConfigEntry.setIndexNames(
    (0, "CIE1000-MSTP-MIB", "cie1000MstpConfigMstiConfigVid"),
)
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiConfigEntry.setStatus("current")


class _Cie1000MstpConfigMstiConfigVid_Type(Integer32):
    """Custom type cie1000MstpConfigMstiConfigVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Cie1000MstpConfigMstiConfigVid_Type.__name__ = "Integer32"
_Cie1000MstpConfigMstiConfigVid_Object = MibTableColumn
cie1000MstpConfigMstiConfigVid = _Cie1000MstpConfigMstiConfigVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 3, 2, 1, 1),
    _Cie1000MstpConfigMstiConfigVid_Type()
)
cie1000MstpConfigMstiConfigVid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiConfigVid.setStatus("current")
_Cie1000MstpConfigMstiConfigMstid_Type = CIE1000Unsigned8
_Cie1000MstpConfigMstiConfigMstid_Object = MibTableColumn
cie1000MstpConfigMstiConfigMstid = _Cie1000MstpConfigMstiConfigMstid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 3, 2, 1, 2),
    _Cie1000MstpConfigMstiConfigMstid_Type()
)
cie1000MstpConfigMstiConfigMstid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiConfigMstid.setStatus("current")
_Cie1000MstpConfigMstiConfigVlanBitmapTable_Object = MibTable
cie1000MstpConfigMstiConfigVlanBitmapTable = _Cie1000MstpConfigMstiConfigVlanBitmapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiConfigVlanBitmapTable.setStatus("current")
_Cie1000MstpConfigMstiConfigVlanBitmapEntry_Object = MibTableRow
cie1000MstpConfigMstiConfigVlanBitmapEntry = _Cie1000MstpConfigMstiConfigVlanBitmapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 3, 3, 1)
)
cie1000MstpConfigMstiConfigVlanBitmapEntry.setIndexNames(
    (0, "CIE1000-MSTP-MIB", "cie1000MstpConfigMstiConfigVlanBitmapMstiValue"),
)
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiConfigVlanBitmapEntry.setStatus("current")


class _Cie1000MstpConfigMstiConfigVlanBitmapMstiValue_Type(Integer32):
    """Custom type cie1000MstpConfigMstiConfigVlanBitmapMstiValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Cie1000MstpConfigMstiConfigVlanBitmapMstiValue_Type.__name__ = "Integer32"
_Cie1000MstpConfigMstiConfigVlanBitmapMstiValue_Object = MibTableColumn
cie1000MstpConfigMstiConfigVlanBitmapMstiValue = _Cie1000MstpConfigMstiConfigVlanBitmapMstiValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 3, 3, 1, 1),
    _Cie1000MstpConfigMstiConfigVlanBitmapMstiValue_Type()
)
cie1000MstpConfigMstiConfigVlanBitmapMstiValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiConfigVlanBitmapMstiValue.setStatus("current")
_Cie1000MstpConfigMstiConfigVlanBitmapAccessVlans0To1K_Type = CIE1000VlanListQuarter
_Cie1000MstpConfigMstiConfigVlanBitmapAccessVlans0To1K_Object = MibTableColumn
cie1000MstpConfigMstiConfigVlanBitmapAccessVlans0To1K = _Cie1000MstpConfigMstiConfigVlanBitmapAccessVlans0To1K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 3, 3, 1, 2),
    _Cie1000MstpConfigMstiConfigVlanBitmapAccessVlans0To1K_Type()
)
cie1000MstpConfigMstiConfigVlanBitmapAccessVlans0To1K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiConfigVlanBitmapAccessVlans0To1K.setStatus("current")
_Cie1000MstpConfigMstiConfigVlanBitmapAccessVlans1KTo2K_Type = CIE1000VlanListQuarter
_Cie1000MstpConfigMstiConfigVlanBitmapAccessVlans1KTo2K_Object = MibTableColumn
cie1000MstpConfigMstiConfigVlanBitmapAccessVlans1KTo2K = _Cie1000MstpConfigMstiConfigVlanBitmapAccessVlans1KTo2K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 3, 3, 1, 3),
    _Cie1000MstpConfigMstiConfigVlanBitmapAccessVlans1KTo2K_Type()
)
cie1000MstpConfigMstiConfigVlanBitmapAccessVlans1KTo2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiConfigVlanBitmapAccessVlans1KTo2K.setStatus("current")
_Cie1000MstpConfigMstiConfigVlanBitmapAccessVlans2KTo3K_Type = CIE1000VlanListQuarter
_Cie1000MstpConfigMstiConfigVlanBitmapAccessVlans2KTo3K_Object = MibTableColumn
cie1000MstpConfigMstiConfigVlanBitmapAccessVlans2KTo3K = _Cie1000MstpConfigMstiConfigVlanBitmapAccessVlans2KTo3K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 3, 3, 1, 4),
    _Cie1000MstpConfigMstiConfigVlanBitmapAccessVlans2KTo3K_Type()
)
cie1000MstpConfigMstiConfigVlanBitmapAccessVlans2KTo3K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiConfigVlanBitmapAccessVlans2KTo3K.setStatus("current")
_Cie1000MstpConfigMstiConfigVlanBitmapAccessVlans3KTo4K_Type = CIE1000VlanListQuarter
_Cie1000MstpConfigMstiConfigVlanBitmapAccessVlans3KTo4K_Object = MibTableColumn
cie1000MstpConfigMstiConfigVlanBitmapAccessVlans3KTo4K = _Cie1000MstpConfigMstiConfigVlanBitmapAccessVlans3KTo4K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 3, 3, 1, 5),
    _Cie1000MstpConfigMstiConfigVlanBitmapAccessVlans3KTo4K_Type()
)
cie1000MstpConfigMstiConfigVlanBitmapAccessVlans3KTo4K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiConfigVlanBitmapAccessVlans3KTo4K.setStatus("current")
_Cie1000MstpConfigCistInterfaceParamTable_Object = MibTable
cie1000MstpConfigCistInterfaceParamTable = _Cie1000MstpConfigCistInterfaceParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cie1000MstpConfigCistInterfaceParamTable.setStatus("current")
_Cie1000MstpConfigCistInterfaceParamEntry_Object = MibTableRow
cie1000MstpConfigCistInterfaceParamEntry = _Cie1000MstpConfigCistInterfaceParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 4, 1)
)
cie1000MstpConfigCistInterfaceParamEntry.setIndexNames(
    (0, "CIE1000-MSTP-MIB", "cie1000MstpConfigCistInterfaceParamInterfaceNo"),
)
if mibBuilder.loadTexts:
    cie1000MstpConfigCistInterfaceParamEntry.setStatus("current")
_Cie1000MstpConfigCistInterfaceParamInterfaceNo_Type = CIE1000InterfaceIndex
_Cie1000MstpConfigCistInterfaceParamInterfaceNo_Object = MibTableColumn
cie1000MstpConfigCistInterfaceParamInterfaceNo = _Cie1000MstpConfigCistInterfaceParamInterfaceNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 4, 1, 1),
    _Cie1000MstpConfigCistInterfaceParamInterfaceNo_Type()
)
cie1000MstpConfigCistInterfaceParamInterfaceNo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000MstpConfigCistInterfaceParamInterfaceNo.setStatus("current")
_Cie1000MstpConfigCistInterfaceParamEnable_Type = TruthValue
_Cie1000MstpConfigCistInterfaceParamEnable_Object = MibTableColumn
cie1000MstpConfigCistInterfaceParamEnable = _Cie1000MstpConfigCistInterfaceParamEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 4, 1, 2),
    _Cie1000MstpConfigCistInterfaceParamEnable_Type()
)
cie1000MstpConfigCistInterfaceParamEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigCistInterfaceParamEnable.setStatus("current")
_Cie1000MstpConfigCistInterfaceParamAdminEdgePort_Type = TruthValue
_Cie1000MstpConfigCistInterfaceParamAdminEdgePort_Object = MibTableColumn
cie1000MstpConfigCistInterfaceParamAdminEdgePort = _Cie1000MstpConfigCistInterfaceParamAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 4, 1, 3),
    _Cie1000MstpConfigCistInterfaceParamAdminEdgePort_Type()
)
cie1000MstpConfigCistInterfaceParamAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigCistInterfaceParamAdminEdgePort.setStatus("current")
_Cie1000MstpConfigCistInterfaceParamAdminAutoEdgePort_Type = TruthValue
_Cie1000MstpConfigCistInterfaceParamAdminAutoEdgePort_Object = MibTableColumn
cie1000MstpConfigCistInterfaceParamAdminAutoEdgePort = _Cie1000MstpConfigCistInterfaceParamAdminAutoEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 4, 1, 4),
    _Cie1000MstpConfigCistInterfaceParamAdminAutoEdgePort_Type()
)
cie1000MstpConfigCistInterfaceParamAdminAutoEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigCistInterfaceParamAdminAutoEdgePort.setStatus("current")
_Cie1000MstpConfigCistInterfaceParamAdminPointToPointMAC_Type = CIE1000MstpPoint2Point
_Cie1000MstpConfigCistInterfaceParamAdminPointToPointMAC_Object = MibTableColumn
cie1000MstpConfigCistInterfaceParamAdminPointToPointMAC = _Cie1000MstpConfigCistInterfaceParamAdminPointToPointMAC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 4, 1, 5),
    _Cie1000MstpConfigCistInterfaceParamAdminPointToPointMAC_Type()
)
cie1000MstpConfigCistInterfaceParamAdminPointToPointMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigCistInterfaceParamAdminPointToPointMAC.setStatus("current")
_Cie1000MstpConfigCistInterfaceParamRestrictedRole_Type = TruthValue
_Cie1000MstpConfigCistInterfaceParamRestrictedRole_Object = MibTableColumn
cie1000MstpConfigCistInterfaceParamRestrictedRole = _Cie1000MstpConfigCistInterfaceParamRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 4, 1, 6),
    _Cie1000MstpConfigCistInterfaceParamRestrictedRole_Type()
)
cie1000MstpConfigCistInterfaceParamRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigCistInterfaceParamRestrictedRole.setStatus("current")
_Cie1000MstpConfigCistInterfaceParamRestrictedTcn_Type = TruthValue
_Cie1000MstpConfigCistInterfaceParamRestrictedTcn_Object = MibTableColumn
cie1000MstpConfigCistInterfaceParamRestrictedTcn = _Cie1000MstpConfigCistInterfaceParamRestrictedTcn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 4, 1, 7),
    _Cie1000MstpConfigCistInterfaceParamRestrictedTcn_Type()
)
cie1000MstpConfigCistInterfaceParamRestrictedTcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigCistInterfaceParamRestrictedTcn.setStatus("current")
_Cie1000MstpConfigCistInterfaceParamBpduGuard_Type = TruthValue
_Cie1000MstpConfigCistInterfaceParamBpduGuard_Object = MibTableColumn
cie1000MstpConfigCistInterfaceParamBpduGuard = _Cie1000MstpConfigCistInterfaceParamBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 4, 1, 8),
    _Cie1000MstpConfigCistInterfaceParamBpduGuard_Type()
)
cie1000MstpConfigCistInterfaceParamBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigCistInterfaceParamBpduGuard.setStatus("current")
_Cie1000MstpConfigAggrParams_ObjectIdentity = ObjectIdentity
cie1000MstpConfigAggrParams = _Cie1000MstpConfigAggrParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 5)
)
_Cie1000MstpConfigAggrParamsEnable_Type = TruthValue
_Cie1000MstpConfigAggrParamsEnable_Object = MibScalar
cie1000MstpConfigAggrParamsEnable = _Cie1000MstpConfigAggrParamsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 5, 1),
    _Cie1000MstpConfigAggrParamsEnable_Type()
)
cie1000MstpConfigAggrParamsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigAggrParamsEnable.setStatus("current")
_Cie1000MstpConfigAggrParamsAdminEdgePort_Type = TruthValue
_Cie1000MstpConfigAggrParamsAdminEdgePort_Object = MibScalar
cie1000MstpConfigAggrParamsAdminEdgePort = _Cie1000MstpConfigAggrParamsAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 5, 2),
    _Cie1000MstpConfigAggrParamsAdminEdgePort_Type()
)
cie1000MstpConfigAggrParamsAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigAggrParamsAdminEdgePort.setStatus("current")
_Cie1000MstpConfigAggrParamsAdminAutoEdgePort_Type = TruthValue
_Cie1000MstpConfigAggrParamsAdminAutoEdgePort_Object = MibScalar
cie1000MstpConfigAggrParamsAdminAutoEdgePort = _Cie1000MstpConfigAggrParamsAdminAutoEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 5, 3),
    _Cie1000MstpConfigAggrParamsAdminAutoEdgePort_Type()
)
cie1000MstpConfigAggrParamsAdminAutoEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigAggrParamsAdminAutoEdgePort.setStatus("current")
_Cie1000MstpConfigAggrParamsAdminPointToPointMAC_Type = CIE1000MstpPoint2Point
_Cie1000MstpConfigAggrParamsAdminPointToPointMAC_Object = MibScalar
cie1000MstpConfigAggrParamsAdminPointToPointMAC = _Cie1000MstpConfigAggrParamsAdminPointToPointMAC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 5, 4),
    _Cie1000MstpConfigAggrParamsAdminPointToPointMAC_Type()
)
cie1000MstpConfigAggrParamsAdminPointToPointMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigAggrParamsAdminPointToPointMAC.setStatus("current")
_Cie1000MstpConfigAggrParamsRestrictedRole_Type = TruthValue
_Cie1000MstpConfigAggrParamsRestrictedRole_Object = MibScalar
cie1000MstpConfigAggrParamsRestrictedRole = _Cie1000MstpConfigAggrParamsRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 5, 5),
    _Cie1000MstpConfigAggrParamsRestrictedRole_Type()
)
cie1000MstpConfigAggrParamsRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigAggrParamsRestrictedRole.setStatus("current")
_Cie1000MstpConfigAggrParamsRestrictedTcn_Type = TruthValue
_Cie1000MstpConfigAggrParamsRestrictedTcn_Object = MibScalar
cie1000MstpConfigAggrParamsRestrictedTcn = _Cie1000MstpConfigAggrParamsRestrictedTcn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 5, 6),
    _Cie1000MstpConfigAggrParamsRestrictedTcn_Type()
)
cie1000MstpConfigAggrParamsRestrictedTcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigAggrParamsRestrictedTcn.setStatus("current")
_Cie1000MstpConfigAggrParamsBpduGuard_Type = TruthValue
_Cie1000MstpConfigAggrParamsBpduGuard_Object = MibScalar
cie1000MstpConfigAggrParamsBpduGuard = _Cie1000MstpConfigAggrParamsBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 5, 7),
    _Cie1000MstpConfigAggrParamsBpduGuard_Type()
)
cie1000MstpConfigAggrParamsBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigAggrParamsBpduGuard.setStatus("current")
_Cie1000MstpConfigMstiInterfaceParamTable_Object = MibTable
cie1000MstpConfigMstiInterfaceParamTable = _Cie1000MstpConfigMstiInterfaceParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiInterfaceParamTable.setStatus("current")
_Cie1000MstpConfigMstiInterfaceParamEntry_Object = MibTableRow
cie1000MstpConfigMstiInterfaceParamEntry = _Cie1000MstpConfigMstiInterfaceParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 6, 1)
)
cie1000MstpConfigMstiInterfaceParamEntry.setIndexNames(
    (0, "CIE1000-MSTP-MIB", "cie1000MstpConfigMstiInterfaceParamInterfaceNo"),
    (0, "CIE1000-MSTP-MIB", "cie1000MstpConfigMstiInterfaceParamInstance"),
)
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiInterfaceParamEntry.setStatus("current")
_Cie1000MstpConfigMstiInterfaceParamInterfaceNo_Type = CIE1000InterfaceIndex
_Cie1000MstpConfigMstiInterfaceParamInterfaceNo_Object = MibTableColumn
cie1000MstpConfigMstiInterfaceParamInterfaceNo = _Cie1000MstpConfigMstiInterfaceParamInterfaceNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 6, 1, 1),
    _Cie1000MstpConfigMstiInterfaceParamInterfaceNo_Type()
)
cie1000MstpConfigMstiInterfaceParamInterfaceNo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiInterfaceParamInterfaceNo.setStatus("current")


class _Cie1000MstpConfigMstiInterfaceParamInstance_Type(Integer32):
    """Custom type cie1000MstpConfigMstiInterfaceParamInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cie1000MstpConfigMstiInterfaceParamInstance_Type.__name__ = "Integer32"
_Cie1000MstpConfigMstiInterfaceParamInstance_Object = MibTableColumn
cie1000MstpConfigMstiInterfaceParamInstance = _Cie1000MstpConfigMstiInterfaceParamInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 6, 1, 2),
    _Cie1000MstpConfigMstiInterfaceParamInstance_Type()
)
cie1000MstpConfigMstiInterfaceParamInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiInterfaceParamInstance.setStatus("current")
_Cie1000MstpConfigMstiInterfaceParamAdminPathCost_Type = Unsigned32
_Cie1000MstpConfigMstiInterfaceParamAdminPathCost_Object = MibTableColumn
cie1000MstpConfigMstiInterfaceParamAdminPathCost = _Cie1000MstpConfigMstiInterfaceParamAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 6, 1, 3),
    _Cie1000MstpConfigMstiInterfaceParamAdminPathCost_Type()
)
cie1000MstpConfigMstiInterfaceParamAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiInterfaceParamAdminPathCost.setStatus("current")
_Cie1000MstpConfigMstiInterfaceParamAdminPortPriority_Type = CIE1000Unsigned8
_Cie1000MstpConfigMstiInterfaceParamAdminPortPriority_Object = MibTableColumn
cie1000MstpConfigMstiInterfaceParamAdminPortPriority = _Cie1000MstpConfigMstiInterfaceParamAdminPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 6, 1, 4),
    _Cie1000MstpConfigMstiInterfaceParamAdminPortPriority_Type()
)
cie1000MstpConfigMstiInterfaceParamAdminPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiInterfaceParamAdminPortPriority.setStatus("current")
_Cie1000MstpConfigMstiAggrParamTable_Object = MibTable
cie1000MstpConfigMstiAggrParamTable = _Cie1000MstpConfigMstiAggrParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 7)
)
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiAggrParamTable.setStatus("current")
_Cie1000MstpConfigMstiAggrParamEntry_Object = MibTableRow
cie1000MstpConfigMstiAggrParamEntry = _Cie1000MstpConfigMstiAggrParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 7, 1)
)
cie1000MstpConfigMstiAggrParamEntry.setIndexNames(
    (0, "CIE1000-MSTP-MIB", "cie1000MstpConfigMstiAggrParamInstance"),
)
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiAggrParamEntry.setStatus("current")


class _Cie1000MstpConfigMstiAggrParamInstance_Type(Integer32):
    """Custom type cie1000MstpConfigMstiAggrParamInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cie1000MstpConfigMstiAggrParamInstance_Type.__name__ = "Integer32"
_Cie1000MstpConfigMstiAggrParamInstance_Object = MibTableColumn
cie1000MstpConfigMstiAggrParamInstance = _Cie1000MstpConfigMstiAggrParamInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 7, 1, 1),
    _Cie1000MstpConfigMstiAggrParamInstance_Type()
)
cie1000MstpConfigMstiAggrParamInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiAggrParamInstance.setStatus("current")
_Cie1000MstpConfigMstiAggrParamAdminPathCost_Type = Unsigned32
_Cie1000MstpConfigMstiAggrParamAdminPathCost_Object = MibTableColumn
cie1000MstpConfigMstiAggrParamAdminPathCost = _Cie1000MstpConfigMstiAggrParamAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 7, 1, 3),
    _Cie1000MstpConfigMstiAggrParamAdminPathCost_Type()
)
cie1000MstpConfigMstiAggrParamAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiAggrParamAdminPathCost.setStatus("current")
_Cie1000MstpConfigMstiAggrParamAdminPortPriority_Type = CIE1000Unsigned8
_Cie1000MstpConfigMstiAggrParamAdminPortPriority_Object = MibTableColumn
cie1000MstpConfigMstiAggrParamAdminPortPriority = _Cie1000MstpConfigMstiAggrParamAdminPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 2, 7, 1, 4),
    _Cie1000MstpConfigMstiAggrParamAdminPortPriority_Type()
)
cie1000MstpConfigMstiAggrParamAdminPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiAggrParamAdminPortPriority.setStatus("current")
_Cie1000MstpStatus_ObjectIdentity = ObjectIdentity
cie1000MstpStatus = _Cie1000MstpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3)
)
_Cie1000MstpStatusBridgeTable_Object = MibTable
cie1000MstpStatusBridgeTable = _Cie1000MstpStatusBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cie1000MstpStatusBridgeTable.setStatus("current")
_Cie1000MstpStatusBridgeEntry_Object = MibTableRow
cie1000MstpStatusBridgeEntry = _Cie1000MstpStatusBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 1, 1)
)
cie1000MstpStatusBridgeEntry.setIndexNames(
    (0, "CIE1000-MSTP-MIB", "cie1000MstpStatusBridgeInstance"),
)
if mibBuilder.loadTexts:
    cie1000MstpStatusBridgeEntry.setStatus("current")


class _Cie1000MstpStatusBridgeInstance_Type(Integer32):
    """Custom type cie1000MstpStatusBridgeInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cie1000MstpStatusBridgeInstance_Type.__name__ = "Integer32"
_Cie1000MstpStatusBridgeInstance_Object = MibTableColumn
cie1000MstpStatusBridgeInstance = _Cie1000MstpStatusBridgeInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 1, 1, 1),
    _Cie1000MstpStatusBridgeInstance_Type()
)
cie1000MstpStatusBridgeInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000MstpStatusBridgeInstance.setStatus("current")


class _Cie1000MstpStatusBridgeBridgeId_Type(OctetString):
    """Custom type cie1000MstpStatusBridgeBridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_Cie1000MstpStatusBridgeBridgeId_Type.__name__ = "OctetString"
_Cie1000MstpStatusBridgeBridgeId_Object = MibTableColumn
cie1000MstpStatusBridgeBridgeId = _Cie1000MstpStatusBridgeBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 1, 1, 2),
    _Cie1000MstpStatusBridgeBridgeId_Type()
)
cie1000MstpStatusBridgeBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusBridgeBridgeId.setStatus("current")
_Cie1000MstpStatusBridgeTimeSinceTopologyChange_Type = Unsigned32
_Cie1000MstpStatusBridgeTimeSinceTopologyChange_Object = MibTableColumn
cie1000MstpStatusBridgeTimeSinceTopologyChange = _Cie1000MstpStatusBridgeTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 1, 1, 3),
    _Cie1000MstpStatusBridgeTimeSinceTopologyChange_Type()
)
cie1000MstpStatusBridgeTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusBridgeTimeSinceTopologyChange.setStatus("current")
_Cie1000MstpStatusBridgeTopologyChangeCount_Type = Unsigned32
_Cie1000MstpStatusBridgeTopologyChangeCount_Object = MibTableColumn
cie1000MstpStatusBridgeTopologyChangeCount = _Cie1000MstpStatusBridgeTopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 1, 1, 4),
    _Cie1000MstpStatusBridgeTopologyChangeCount_Type()
)
cie1000MstpStatusBridgeTopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusBridgeTopologyChangeCount.setStatus("current")
_Cie1000MstpStatusBridgeTopologyChange_Type = TruthValue
_Cie1000MstpStatusBridgeTopologyChange_Object = MibTableColumn
cie1000MstpStatusBridgeTopologyChange = _Cie1000MstpStatusBridgeTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 1, 1, 5),
    _Cie1000MstpStatusBridgeTopologyChange_Type()
)
cie1000MstpStatusBridgeTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusBridgeTopologyChange.setStatus("current")


class _Cie1000MstpStatusBridgeDesignatedRoot_Type(OctetString):
    """Custom type cie1000MstpStatusBridgeDesignatedRoot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_Cie1000MstpStatusBridgeDesignatedRoot_Type.__name__ = "OctetString"
_Cie1000MstpStatusBridgeDesignatedRoot_Object = MibTableColumn
cie1000MstpStatusBridgeDesignatedRoot = _Cie1000MstpStatusBridgeDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 1, 1, 6),
    _Cie1000MstpStatusBridgeDesignatedRoot_Type()
)
cie1000MstpStatusBridgeDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusBridgeDesignatedRoot.setStatus("current")
_Cie1000MstpStatusBridgeRootPathCost_Type = Unsigned32
_Cie1000MstpStatusBridgeRootPathCost_Object = MibTableColumn
cie1000MstpStatusBridgeRootPathCost = _Cie1000MstpStatusBridgeRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 1, 1, 7),
    _Cie1000MstpStatusBridgeRootPathCost_Type()
)
cie1000MstpStatusBridgeRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusBridgeRootPathCost.setStatus("current")
_Cie1000MstpStatusBridgeRootPort_Type = Unsigned32
_Cie1000MstpStatusBridgeRootPort_Object = MibTableColumn
cie1000MstpStatusBridgeRootPort = _Cie1000MstpStatusBridgeRootPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 1, 1, 8),
    _Cie1000MstpStatusBridgeRootPort_Type()
)
cie1000MstpStatusBridgeRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusBridgeRootPort.setStatus("current")
_Cie1000MstpStatusBridgeMaxAge_Type = Unsigned32
_Cie1000MstpStatusBridgeMaxAge_Object = MibTableColumn
cie1000MstpStatusBridgeMaxAge = _Cie1000MstpStatusBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 1, 1, 9),
    _Cie1000MstpStatusBridgeMaxAge_Type()
)
cie1000MstpStatusBridgeMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusBridgeMaxAge.setStatus("current")
_Cie1000MstpStatusBridgeForwardDelay_Type = Unsigned32
_Cie1000MstpStatusBridgeForwardDelay_Object = MibTableColumn
cie1000MstpStatusBridgeForwardDelay = _Cie1000MstpStatusBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 1, 1, 10),
    _Cie1000MstpStatusBridgeForwardDelay_Type()
)
cie1000MstpStatusBridgeForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusBridgeForwardDelay.setStatus("current")
_Cie1000MstpStatusBridgeBridgeMaxAge_Type = Unsigned32
_Cie1000MstpStatusBridgeBridgeMaxAge_Object = MibTableColumn
cie1000MstpStatusBridgeBridgeMaxAge = _Cie1000MstpStatusBridgeBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 1, 1, 11),
    _Cie1000MstpStatusBridgeBridgeMaxAge_Type()
)
cie1000MstpStatusBridgeBridgeMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusBridgeBridgeMaxAge.setStatus("current")
_Cie1000MstpStatusBridgeBridgeHelloTime_Type = Unsigned32
_Cie1000MstpStatusBridgeBridgeHelloTime_Object = MibTableColumn
cie1000MstpStatusBridgeBridgeHelloTime = _Cie1000MstpStatusBridgeBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 1, 1, 12),
    _Cie1000MstpStatusBridgeBridgeHelloTime_Type()
)
cie1000MstpStatusBridgeBridgeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusBridgeBridgeHelloTime.setStatus("current")
_Cie1000MstpStatusBridgeBridgeForwardDelay_Type = Unsigned32
_Cie1000MstpStatusBridgeBridgeForwardDelay_Object = MibTableColumn
cie1000MstpStatusBridgeBridgeForwardDelay = _Cie1000MstpStatusBridgeBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 1, 1, 13),
    _Cie1000MstpStatusBridgeBridgeForwardDelay_Type()
)
cie1000MstpStatusBridgeBridgeForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusBridgeBridgeForwardDelay.setStatus("current")
_Cie1000MstpStatusBridgeTxHoldCount_Type = Unsigned32
_Cie1000MstpStatusBridgeTxHoldCount_Object = MibTableColumn
cie1000MstpStatusBridgeTxHoldCount = _Cie1000MstpStatusBridgeTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 1, 1, 14),
    _Cie1000MstpStatusBridgeTxHoldCount_Type()
)
cie1000MstpStatusBridgeTxHoldCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusBridgeTxHoldCount.setStatus("current")
_Cie1000MstpStatusBridgeForceVersion_Type = CIE1000MSTPForceVersion
_Cie1000MstpStatusBridgeForceVersion_Object = MibTableColumn
cie1000MstpStatusBridgeForceVersion = _Cie1000MstpStatusBridgeForceVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 1, 1, 15),
    _Cie1000MstpStatusBridgeForceVersion_Type()
)
cie1000MstpStatusBridgeForceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusBridgeForceVersion.setStatus("current")


class _Cie1000MstpStatusBridgeCistRegionalRoot_Type(OctetString):
    """Custom type cie1000MstpStatusBridgeCistRegionalRoot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_Cie1000MstpStatusBridgeCistRegionalRoot_Type.__name__ = "OctetString"
_Cie1000MstpStatusBridgeCistRegionalRoot_Object = MibTableColumn
cie1000MstpStatusBridgeCistRegionalRoot = _Cie1000MstpStatusBridgeCistRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 1, 1, 16),
    _Cie1000MstpStatusBridgeCistRegionalRoot_Type()
)
cie1000MstpStatusBridgeCistRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusBridgeCistRegionalRoot.setStatus("current")
_Cie1000MstpStatusBridgeCistInternalPathCost_Type = Unsigned32
_Cie1000MstpStatusBridgeCistInternalPathCost_Object = MibTableColumn
cie1000MstpStatusBridgeCistInternalPathCost = _Cie1000MstpStatusBridgeCistInternalPathCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 1, 1, 17),
    _Cie1000MstpStatusBridgeCistInternalPathCost_Type()
)
cie1000MstpStatusBridgeCistInternalPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusBridgeCistInternalPathCost.setStatus("current")
_Cie1000MstpStatusBridgeMaxHops_Type = CIE1000Unsigned8
_Cie1000MstpStatusBridgeMaxHops_Object = MibTableColumn
cie1000MstpStatusBridgeMaxHops = _Cie1000MstpStatusBridgeMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 1, 1, 18),
    _Cie1000MstpStatusBridgeMaxHops_Type()
)
cie1000MstpStatusBridgeMaxHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusBridgeMaxHops.setStatus("current")
_Cie1000MstpStatusInterfaceTable_Object = MibTable
cie1000MstpStatusInterfaceTable = _Cie1000MstpStatusInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceTable.setStatus("current")
_Cie1000MstpStatusInterfaceEntry_Object = MibTableRow
cie1000MstpStatusInterfaceEntry = _Cie1000MstpStatusInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 2, 1)
)
cie1000MstpStatusInterfaceEntry.setIndexNames(
    (0, "CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceInterfaceNo"),
    (0, "CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceInstance"),
)
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceEntry.setStatus("current")
_Cie1000MstpStatusInterfaceInterfaceNo_Type = CIE1000InterfaceIndex
_Cie1000MstpStatusInterfaceInterfaceNo_Object = MibTableColumn
cie1000MstpStatusInterfaceInterfaceNo = _Cie1000MstpStatusInterfaceInterfaceNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 2, 1, 1),
    _Cie1000MstpStatusInterfaceInterfaceNo_Type()
)
cie1000MstpStatusInterfaceInterfaceNo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceInterfaceNo.setStatus("current")


class _Cie1000MstpStatusInterfaceInstance_Type(Integer32):
    """Custom type cie1000MstpStatusInterfaceInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cie1000MstpStatusInterfaceInstance_Type.__name__ = "Integer32"
_Cie1000MstpStatusInterfaceInstance_Object = MibTableColumn
cie1000MstpStatusInterfaceInstance = _Cie1000MstpStatusInterfaceInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 2, 1, 2),
    _Cie1000MstpStatusInterfaceInstance_Type()
)
cie1000MstpStatusInterfaceInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceInstance.setStatus("current")
_Cie1000MstpStatusInterfaceEnabled_Type = TruthValue
_Cie1000MstpStatusInterfaceEnabled_Object = MibTableColumn
cie1000MstpStatusInterfaceEnabled = _Cie1000MstpStatusInterfaceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 2, 1, 3),
    _Cie1000MstpStatusInterfaceEnabled_Type()
)
cie1000MstpStatusInterfaceEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceEnabled.setStatus("current")
_Cie1000MstpStatusInterfaceActive_Type = TruthValue
_Cie1000MstpStatusInterfaceActive_Object = MibTableColumn
cie1000MstpStatusInterfaceActive = _Cie1000MstpStatusInterfaceActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 2, 1, 4),
    _Cie1000MstpStatusInterfaceActive_Type()
)
cie1000MstpStatusInterfaceActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceActive.setStatus("current")
_Cie1000MstpStatusInterfaceParentPort_Type = Unsigned32
_Cie1000MstpStatusInterfaceParentPort_Object = MibTableColumn
cie1000MstpStatusInterfaceParentPort = _Cie1000MstpStatusInterfaceParentPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 2, 1, 5),
    _Cie1000MstpStatusInterfaceParentPort_Type()
)
cie1000MstpStatusInterfaceParentPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceParentPort.setStatus("current")
_Cie1000MstpStatusInterfaceUpTime_Type = Unsigned32
_Cie1000MstpStatusInterfaceUpTime_Object = MibTableColumn
cie1000MstpStatusInterfaceUpTime = _Cie1000MstpStatusInterfaceUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 2, 1, 6),
    _Cie1000MstpStatusInterfaceUpTime_Type()
)
cie1000MstpStatusInterfaceUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceUpTime.setStatus("current")
_Cie1000MstpStatusInterfacePortState_Type = CIE1000MstpPortState
_Cie1000MstpStatusInterfacePortState_Object = MibTableColumn
cie1000MstpStatusInterfacePortState = _Cie1000MstpStatusInterfacePortState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 2, 1, 7),
    _Cie1000MstpStatusInterfacePortState_Type()
)
cie1000MstpStatusInterfacePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfacePortState.setStatus("current")


class _Cie1000MstpStatusInterfacePortId_Type(OctetString):
    """Custom type cie1000MstpStatusInterfacePortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixedLength = 2


_Cie1000MstpStatusInterfacePortId_Type.__name__ = "OctetString"
_Cie1000MstpStatusInterfacePortId_Object = MibTableColumn
cie1000MstpStatusInterfacePortId = _Cie1000MstpStatusInterfacePortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 2, 1, 8),
    _Cie1000MstpStatusInterfacePortId_Type()
)
cie1000MstpStatusInterfacePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfacePortId.setStatus("current")
_Cie1000MstpStatusInterfacePathCost_Type = Unsigned32
_Cie1000MstpStatusInterfacePathCost_Object = MibTableColumn
cie1000MstpStatusInterfacePathCost = _Cie1000MstpStatusInterfacePathCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 2, 1, 9),
    _Cie1000MstpStatusInterfacePathCost_Type()
)
cie1000MstpStatusInterfacePathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfacePathCost.setStatus("current")


class _Cie1000MstpStatusInterfaceDesignatedRoot_Type(OctetString):
    """Custom type cie1000MstpStatusInterfaceDesignatedRoot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_Cie1000MstpStatusInterfaceDesignatedRoot_Type.__name__ = "OctetString"
_Cie1000MstpStatusInterfaceDesignatedRoot_Object = MibTableColumn
cie1000MstpStatusInterfaceDesignatedRoot = _Cie1000MstpStatusInterfaceDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 2, 1, 10),
    _Cie1000MstpStatusInterfaceDesignatedRoot_Type()
)
cie1000MstpStatusInterfaceDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceDesignatedRoot.setStatus("current")
_Cie1000MstpStatusInterfaceDesignatedCost_Type = Unsigned32
_Cie1000MstpStatusInterfaceDesignatedCost_Object = MibTableColumn
cie1000MstpStatusInterfaceDesignatedCost = _Cie1000MstpStatusInterfaceDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 2, 1, 11),
    _Cie1000MstpStatusInterfaceDesignatedCost_Type()
)
cie1000MstpStatusInterfaceDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceDesignatedCost.setStatus("current")


class _Cie1000MstpStatusInterfaceDesignatedBridge_Type(OctetString):
    """Custom type cie1000MstpStatusInterfaceDesignatedBridge based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_Cie1000MstpStatusInterfaceDesignatedBridge_Type.__name__ = "OctetString"
_Cie1000MstpStatusInterfaceDesignatedBridge_Object = MibTableColumn
cie1000MstpStatusInterfaceDesignatedBridge = _Cie1000MstpStatusInterfaceDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 2, 1, 12),
    _Cie1000MstpStatusInterfaceDesignatedBridge_Type()
)
cie1000MstpStatusInterfaceDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceDesignatedBridge.setStatus("current")


class _Cie1000MstpStatusInterfaceDesignatedPort_Type(OctetString):
    """Custom type cie1000MstpStatusInterfaceDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixedLength = 2


_Cie1000MstpStatusInterfaceDesignatedPort_Type.__name__ = "OctetString"
_Cie1000MstpStatusInterfaceDesignatedPort_Object = MibTableColumn
cie1000MstpStatusInterfaceDesignatedPort = _Cie1000MstpStatusInterfaceDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 2, 1, 13),
    _Cie1000MstpStatusInterfaceDesignatedPort_Type()
)
cie1000MstpStatusInterfaceDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceDesignatedPort.setStatus("current")
_Cie1000MstpStatusInterfaceTcAck_Type = TruthValue
_Cie1000MstpStatusInterfaceTcAck_Object = MibTableColumn
cie1000MstpStatusInterfaceTcAck = _Cie1000MstpStatusInterfaceTcAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 2, 1, 14),
    _Cie1000MstpStatusInterfaceTcAck_Type()
)
cie1000MstpStatusInterfaceTcAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceTcAck.setStatus("current")
_Cie1000MstpStatusInterfaceHelloTime_Type = Unsigned32
_Cie1000MstpStatusInterfaceHelloTime_Object = MibTableColumn
cie1000MstpStatusInterfaceHelloTime = _Cie1000MstpStatusInterfaceHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 2, 1, 15),
    _Cie1000MstpStatusInterfaceHelloTime_Type()
)
cie1000MstpStatusInterfaceHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceHelloTime.setStatus("current")
_Cie1000MstpStatusInterfaceAdminEdgePort_Type = TruthValue
_Cie1000MstpStatusInterfaceAdminEdgePort_Object = MibTableColumn
cie1000MstpStatusInterfaceAdminEdgePort = _Cie1000MstpStatusInterfaceAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 2, 1, 16),
    _Cie1000MstpStatusInterfaceAdminEdgePort_Type()
)
cie1000MstpStatusInterfaceAdminEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceAdminEdgePort.setStatus("current")
_Cie1000MstpStatusInterfaceOperEdgePort_Type = TruthValue
_Cie1000MstpStatusInterfaceOperEdgePort_Object = MibTableColumn
cie1000MstpStatusInterfaceOperEdgePort = _Cie1000MstpStatusInterfaceOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 2, 1, 17),
    _Cie1000MstpStatusInterfaceOperEdgePort_Type()
)
cie1000MstpStatusInterfaceOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceOperEdgePort.setStatus("current")
_Cie1000MstpStatusInterfaceAutoEdgePort_Type = TruthValue
_Cie1000MstpStatusInterfaceAutoEdgePort_Object = MibTableColumn
cie1000MstpStatusInterfaceAutoEdgePort = _Cie1000MstpStatusInterfaceAutoEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 2, 1, 18),
    _Cie1000MstpStatusInterfaceAutoEdgePort_Type()
)
cie1000MstpStatusInterfaceAutoEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceAutoEdgePort.setStatus("current")
_Cie1000MstpStatusInterfaceMacOperational_Type = TruthValue
_Cie1000MstpStatusInterfaceMacOperational_Object = MibTableColumn
cie1000MstpStatusInterfaceMacOperational = _Cie1000MstpStatusInterfaceMacOperational_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 2, 1, 19),
    _Cie1000MstpStatusInterfaceMacOperational_Type()
)
cie1000MstpStatusInterfaceMacOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceMacOperational.setStatus("current")
_Cie1000MstpStatusInterfaceAdminPointToPointMAC_Type = CIE1000MstpPoint2Point
_Cie1000MstpStatusInterfaceAdminPointToPointMAC_Object = MibTableColumn
cie1000MstpStatusInterfaceAdminPointToPointMAC = _Cie1000MstpStatusInterfaceAdminPointToPointMAC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 2, 1, 20),
    _Cie1000MstpStatusInterfaceAdminPointToPointMAC_Type()
)
cie1000MstpStatusInterfaceAdminPointToPointMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceAdminPointToPointMAC.setStatus("current")
_Cie1000MstpStatusInterfaceOperPointToPointMAC_Type = TruthValue
_Cie1000MstpStatusInterfaceOperPointToPointMAC_Object = MibTableColumn
cie1000MstpStatusInterfaceOperPointToPointMAC = _Cie1000MstpStatusInterfaceOperPointToPointMAC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 2, 1, 21),
    _Cie1000MstpStatusInterfaceOperPointToPointMAC_Type()
)
cie1000MstpStatusInterfaceOperPointToPointMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceOperPointToPointMAC.setStatus("current")
_Cie1000MstpStatusInterfaceRestrictedRole_Type = TruthValue
_Cie1000MstpStatusInterfaceRestrictedRole_Object = MibTableColumn
cie1000MstpStatusInterfaceRestrictedRole = _Cie1000MstpStatusInterfaceRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 2, 1, 22),
    _Cie1000MstpStatusInterfaceRestrictedRole_Type()
)
cie1000MstpStatusInterfaceRestrictedRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceRestrictedRole.setStatus("current")
_Cie1000MstpStatusInterfaceRestrictedTcn_Type = TruthValue
_Cie1000MstpStatusInterfaceRestrictedTcn_Object = MibTableColumn
cie1000MstpStatusInterfaceRestrictedTcn = _Cie1000MstpStatusInterfaceRestrictedTcn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 2, 1, 23),
    _Cie1000MstpStatusInterfaceRestrictedTcn_Type()
)
cie1000MstpStatusInterfaceRestrictedTcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceRestrictedTcn.setStatus("current")


class _Cie1000MstpStatusInterfacePortRole_Type(CIE1000DisplayString):
    """Custom type cie1000MstpStatusInterfacePortRole based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cie1000MstpStatusInterfacePortRole_Type.__name__ = "CIE1000DisplayString"
_Cie1000MstpStatusInterfacePortRole_Object = MibTableColumn
cie1000MstpStatusInterfacePortRole = _Cie1000MstpStatusInterfacePortRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 2, 1, 24),
    _Cie1000MstpStatusInterfacePortRole_Type()
)
cie1000MstpStatusInterfacePortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfacePortRole.setStatus("current")
_Cie1000MstpStatusInterfaceDisputed_Type = TruthValue
_Cie1000MstpStatusInterfaceDisputed_Object = MibTableColumn
cie1000MstpStatusInterfaceDisputed = _Cie1000MstpStatusInterfaceDisputed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 2, 1, 25),
    _Cie1000MstpStatusInterfaceDisputed_Type()
)
cie1000MstpStatusInterfaceDisputed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceDisputed.setStatus("current")
_Cie1000MstpStatusInterfaceStatisticsTable_Object = MibTable
cie1000MstpStatusInterfaceStatisticsTable = _Cie1000MstpStatusInterfaceStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceStatisticsTable.setStatus("current")
_Cie1000MstpStatusInterfaceStatisticsEntry_Object = MibTableRow
cie1000MstpStatusInterfaceStatisticsEntry = _Cie1000MstpStatusInterfaceStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 3, 1)
)
cie1000MstpStatusInterfaceStatisticsEntry.setIndexNames(
    (0, "CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceStatisticsInterfaceNo"),
)
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceStatisticsEntry.setStatus("current")
_Cie1000MstpStatusInterfaceStatisticsInterfaceNo_Type = CIE1000InterfaceIndex
_Cie1000MstpStatusInterfaceStatisticsInterfaceNo_Object = MibTableColumn
cie1000MstpStatusInterfaceStatisticsInterfaceNo = _Cie1000MstpStatusInterfaceStatisticsInterfaceNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 3, 1, 1),
    _Cie1000MstpStatusInterfaceStatisticsInterfaceNo_Type()
)
cie1000MstpStatusInterfaceStatisticsInterfaceNo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceStatisticsInterfaceNo.setStatus("current")
_Cie1000MstpStatusInterfaceStatisticsStpFrameXmits_Type = Unsigned32
_Cie1000MstpStatusInterfaceStatisticsStpFrameXmits_Object = MibTableColumn
cie1000MstpStatusInterfaceStatisticsStpFrameXmits = _Cie1000MstpStatusInterfaceStatisticsStpFrameXmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 3, 1, 2),
    _Cie1000MstpStatusInterfaceStatisticsStpFrameXmits_Type()
)
cie1000MstpStatusInterfaceStatisticsStpFrameXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceStatisticsStpFrameXmits.setStatus("current")
_Cie1000MstpStatusInterfaceStatisticsStpFrameReceived_Type = Unsigned32
_Cie1000MstpStatusInterfaceStatisticsStpFrameReceived_Object = MibTableColumn
cie1000MstpStatusInterfaceStatisticsStpFrameReceived = _Cie1000MstpStatusInterfaceStatisticsStpFrameReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 3, 1, 3),
    _Cie1000MstpStatusInterfaceStatisticsStpFrameReceived_Type()
)
cie1000MstpStatusInterfaceStatisticsStpFrameReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceStatisticsStpFrameReceived.setStatus("current")
_Cie1000MstpStatusInterfaceStatisticsRstpFrameXmits_Type = Unsigned32
_Cie1000MstpStatusInterfaceStatisticsRstpFrameXmits_Object = MibTableColumn
cie1000MstpStatusInterfaceStatisticsRstpFrameXmits = _Cie1000MstpStatusInterfaceStatisticsRstpFrameXmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 3, 1, 4),
    _Cie1000MstpStatusInterfaceStatisticsRstpFrameXmits_Type()
)
cie1000MstpStatusInterfaceStatisticsRstpFrameXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceStatisticsRstpFrameXmits.setStatus("current")
_Cie1000MstpStatusInterfaceStatisticsRstpFrameReceived_Type = Unsigned32
_Cie1000MstpStatusInterfaceStatisticsRstpFrameReceived_Object = MibTableColumn
cie1000MstpStatusInterfaceStatisticsRstpFrameReceived = _Cie1000MstpStatusInterfaceStatisticsRstpFrameReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 3, 1, 5),
    _Cie1000MstpStatusInterfaceStatisticsRstpFrameReceived_Type()
)
cie1000MstpStatusInterfaceStatisticsRstpFrameReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceStatisticsRstpFrameReceived.setStatus("current")
_Cie1000MstpStatusInterfaceStatisticsMstpFrameXmits_Type = Unsigned32
_Cie1000MstpStatusInterfaceStatisticsMstpFrameXmits_Object = MibTableColumn
cie1000MstpStatusInterfaceStatisticsMstpFrameXmits = _Cie1000MstpStatusInterfaceStatisticsMstpFrameXmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 3, 1, 6),
    _Cie1000MstpStatusInterfaceStatisticsMstpFrameXmits_Type()
)
cie1000MstpStatusInterfaceStatisticsMstpFrameXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceStatisticsMstpFrameXmits.setStatus("current")
_Cie1000MstpStatusInterfaceStatisticsMstpFrameReceived_Type = Unsigned32
_Cie1000MstpStatusInterfaceStatisticsMstpFrameReceived_Object = MibTableColumn
cie1000MstpStatusInterfaceStatisticsMstpFrameReceived = _Cie1000MstpStatusInterfaceStatisticsMstpFrameReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 3, 1, 7),
    _Cie1000MstpStatusInterfaceStatisticsMstpFrameReceived_Type()
)
cie1000MstpStatusInterfaceStatisticsMstpFrameReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceStatisticsMstpFrameReceived.setStatus("current")
_Cie1000MstpStatusInterfaceStatisticsUnknownFramesReceived_Type = Unsigned32
_Cie1000MstpStatusInterfaceStatisticsUnknownFramesReceived_Object = MibTableColumn
cie1000MstpStatusInterfaceStatisticsUnknownFramesReceived = _Cie1000MstpStatusInterfaceStatisticsUnknownFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 3, 1, 8),
    _Cie1000MstpStatusInterfaceStatisticsUnknownFramesReceived_Type()
)
cie1000MstpStatusInterfaceStatisticsUnknownFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceStatisticsUnknownFramesReceived.setStatus("current")
_Cie1000MstpStatusInterfaceStatisticsIllegalFrameReceived_Type = Unsigned32
_Cie1000MstpStatusInterfaceStatisticsIllegalFrameReceived_Object = MibTableColumn
cie1000MstpStatusInterfaceStatisticsIllegalFrameReceived = _Cie1000MstpStatusInterfaceStatisticsIllegalFrameReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 3, 1, 9),
    _Cie1000MstpStatusInterfaceStatisticsIllegalFrameReceived_Type()
)
cie1000MstpStatusInterfaceStatisticsIllegalFrameReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceStatisticsIllegalFrameReceived.setStatus("current")
_Cie1000MstpStatusInterfaceStatisticsTcnFrameXmits_Type = Unsigned32
_Cie1000MstpStatusInterfaceStatisticsTcnFrameXmits_Object = MibTableColumn
cie1000MstpStatusInterfaceStatisticsTcnFrameXmits = _Cie1000MstpStatusInterfaceStatisticsTcnFrameXmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 3, 1, 10),
    _Cie1000MstpStatusInterfaceStatisticsTcnFrameXmits_Type()
)
cie1000MstpStatusInterfaceStatisticsTcnFrameXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceStatisticsTcnFrameXmits.setStatus("current")
_Cie1000MstpStatusInterfaceStatisticsTcnFrameReceived_Type = Unsigned32
_Cie1000MstpStatusInterfaceStatisticsTcnFrameReceived_Object = MibTableColumn
cie1000MstpStatusInterfaceStatisticsTcnFrameReceived = _Cie1000MstpStatusInterfaceStatisticsTcnFrameReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 1, 3, 3, 1, 11),
    _Cie1000MstpStatusInterfaceStatisticsTcnFrameReceived_Type()
)
cie1000MstpStatusInterfaceStatisticsTcnFrameReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceStatisticsTcnFrameReceived.setStatus("current")
_Cie1000MstpMibConformance_ObjectIdentity = ObjectIdentity
cie1000MstpMibConformance = _Cie1000MstpMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 2)
)
_Cie1000MstpMibCompliances_ObjectIdentity = ObjectIdentity
cie1000MstpMibCompliances = _Cie1000MstpMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 2, 1)
)
_Cie1000MstpMibGroups_ObjectIdentity = ObjectIdentity
cie1000MstpMibGroups = _Cie1000MstpMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 2, 2)
)

# Managed Objects groups

cie1000MstpConfigBridgeParamsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 2, 2, 1)
)
cie1000MstpConfigBridgeParamsInfoGroup.setObjects(
      *(("CIE1000-MSTP-MIB", "cie1000MstpConfigBridgeParamsBridgeMaxAge"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigBridgeParamsBridgeHelloTime"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigBridgeParamsBridgeForwardDelay"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigBridgeParamsForceVersion"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigBridgeParamsTxHoldCount"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigBridgeParamsMaxHops"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigBridgeParamsBpduFiltering"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigBridgeParamsBpduGuard"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigBridgeParamsErrorRecoveryDelay"))
)
if mibBuilder.loadTexts:
    cie1000MstpConfigBridgeParamsInfoGroup.setStatus("current")

cie1000MstpConfigMstiParamTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 2, 2, 2)
)
cie1000MstpConfigMstiParamTableInfoGroup.setObjects(
      *(("CIE1000-MSTP-MIB", "cie1000MstpConfigMstiParamInstance"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigMstiParamPriority"))
)
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiParamTableInfoGroup.setStatus("current")

cie1000MstpConfigMstiConfigIdInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 2, 2, 3)
)
cie1000MstpConfigMstiConfigIdInfoGroup.setObjects(
      *(("CIE1000-MSTP-MIB", "cie1000MstpConfigMstiConfigIdName"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigMstiConfigIdRevision"))
)
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiConfigIdInfoGroup.setStatus("current")

cie1000MstpConfigMstiConfigTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 2, 2, 4)
)
cie1000MstpConfigMstiConfigTableInfoGroup.setObjects(
      *(("CIE1000-MSTP-MIB", "cie1000MstpConfigMstiConfigVid"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigMstiConfigMstid"))
)
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiConfigTableInfoGroup.setStatus("current")

cie1000MstpConfigMstiConfigVlanBitmapTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 2, 2, 5)
)
cie1000MstpConfigMstiConfigVlanBitmapTableInfoGroup.setObjects(
      *(("CIE1000-MSTP-MIB", "cie1000MstpConfigMstiConfigVlanBitmapMstiValue"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigMstiConfigVlanBitmapAccessVlans0To1K"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigMstiConfigVlanBitmapAccessVlans1KTo2K"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigMstiConfigVlanBitmapAccessVlans2KTo3K"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigMstiConfigVlanBitmapAccessVlans3KTo4K"))
)
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiConfigVlanBitmapTableInfoGroup.setStatus("current")

cie1000MstpConfigCistInterfaceParamTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 2, 2, 6)
)
cie1000MstpConfigCistInterfaceParamTableInfoGroup.setObjects(
      *(("CIE1000-MSTP-MIB", "cie1000MstpConfigCistInterfaceParamInterfaceNo"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigCistInterfaceParamEnable"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigCistInterfaceParamAdminEdgePort"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigCistInterfaceParamAdminAutoEdgePort"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigCistInterfaceParamAdminPointToPointMAC"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigCistInterfaceParamRestrictedRole"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigCistInterfaceParamRestrictedTcn"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigCistInterfaceParamBpduGuard"))
)
if mibBuilder.loadTexts:
    cie1000MstpConfigCistInterfaceParamTableInfoGroup.setStatus("current")

cie1000MstpConfigAggrParamsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 2, 2, 7)
)
cie1000MstpConfigAggrParamsInfoGroup.setObjects(
      *(("CIE1000-MSTP-MIB", "cie1000MstpConfigAggrParamsEnable"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigAggrParamsAdminEdgePort"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigAggrParamsAdminAutoEdgePort"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigAggrParamsAdminPointToPointMAC"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigAggrParamsRestrictedRole"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigAggrParamsRestrictedTcn"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigAggrParamsBpduGuard"))
)
if mibBuilder.loadTexts:
    cie1000MstpConfigAggrParamsInfoGroup.setStatus("current")

cie1000MstpConfigMstiInterfaceParamTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 2, 2, 8)
)
cie1000MstpConfigMstiInterfaceParamTableInfoGroup.setObjects(
      *(("CIE1000-MSTP-MIB", "cie1000MstpConfigMstiInterfaceParamInterfaceNo"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigMstiInterfaceParamInstance"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigMstiInterfaceParamAdminPathCost"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigMstiInterfaceParamAdminPortPriority"))
)
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiInterfaceParamTableInfoGroup.setStatus("current")

cie1000MstpConfigMstiAggrParamTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 2, 2, 9)
)
cie1000MstpConfigMstiAggrParamTableInfoGroup.setObjects(
      *(("CIE1000-MSTP-MIB", "cie1000MstpConfigMstiAggrParamInstance"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigMstiAggrParamAdminPathCost"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigMstiAggrParamAdminPortPriority"))
)
if mibBuilder.loadTexts:
    cie1000MstpConfigMstiAggrParamTableInfoGroup.setStatus("current")

cie1000MstpStatusBridgeTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 2, 2, 10)
)
cie1000MstpStatusBridgeTableInfoGroup.setObjects(
      *(("CIE1000-MSTP-MIB", "cie1000MstpStatusBridgeInstance"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusBridgeBridgeId"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusBridgeTimeSinceTopologyChange"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusBridgeTopologyChangeCount"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusBridgeTopologyChange"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusBridgeDesignatedRoot"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusBridgeRootPathCost"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusBridgeRootPort"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusBridgeMaxAge"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusBridgeForwardDelay"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusBridgeBridgeMaxAge"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusBridgeBridgeHelloTime"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusBridgeBridgeForwardDelay"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusBridgeTxHoldCount"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusBridgeForceVersion"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusBridgeCistRegionalRoot"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusBridgeCistInternalPathCost"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusBridgeMaxHops"))
)
if mibBuilder.loadTexts:
    cie1000MstpStatusBridgeTableInfoGroup.setStatus("current")

cie1000MstpStatusInterfaceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 2, 2, 11)
)
cie1000MstpStatusInterfaceTableInfoGroup.setObjects(
      *(("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceInterfaceNo"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceInstance"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceEnabled"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceActive"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceParentPort"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceUpTime"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfacePortState"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfacePortId"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfacePathCost"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceDesignatedRoot"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceDesignatedCost"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceDesignatedBridge"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceDesignatedPort"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceTcAck"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceHelloTime"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceAdminEdgePort"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceOperEdgePort"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceAutoEdgePort"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceMacOperational"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceAdminPointToPointMAC"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceOperPointToPointMAC"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceRestrictedRole"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceRestrictedTcn"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfacePortRole"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceDisputed"))
)
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceTableInfoGroup.setStatus("current")

cie1000MstpStatusInterfaceStatisticsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 2, 2, 12)
)
cie1000MstpStatusInterfaceStatisticsTableInfoGroup.setObjects(
      *(("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceStatisticsInterfaceNo"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceStatisticsStpFrameXmits"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceStatisticsStpFrameReceived"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceStatisticsRstpFrameXmits"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceStatisticsRstpFrameReceived"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceStatisticsMstpFrameXmits"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceStatisticsMstpFrameReceived"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceStatisticsUnknownFramesReceived"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceStatisticsIllegalFrameReceived"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceStatisticsTcnFrameXmits"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceStatisticsTcnFrameReceived"))
)
if mibBuilder.loadTexts:
    cie1000MstpStatusInterfaceStatisticsTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cie1000MstpMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 20, 2, 1, 1)
)
cie1000MstpMibCompliance.setObjects(
      *(("CIE1000-MSTP-MIB", "cie1000MstpConfigBridgeParamsInfoGroup"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigMstiParamTableInfoGroup"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigMstiConfigIdInfoGroup"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigMstiConfigTableInfoGroup"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigMstiConfigVlanBitmapTableInfoGroup"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigCistInterfaceParamTableInfoGroup"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigAggrParamsInfoGroup"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigMstiInterfaceParamTableInfoGroup"),
        ("CIE1000-MSTP-MIB", "cie1000MstpConfigMstiAggrParamTableInfoGroup"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusBridgeTableInfoGroup"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceTableInfoGroup"),
        ("CIE1000-MSTP-MIB", "cie1000MstpStatusInterfaceStatisticsTableInfoGroup"))
)
if mibBuilder.loadTexts:
    cie1000MstpMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIE1000-MSTP-MIB",
    **{"CIE1000MSTPForceVersion": CIE1000MSTPForceVersion,
       "CIE1000MstpPoint2Point": CIE1000MstpPoint2Point,
       "CIE1000MstpPortState": CIE1000MstpPortState,
       "cie1000MstpMib": cie1000MstpMib,
       "cie1000MstpMibObjects": cie1000MstpMibObjects,
       "cie1000MstpConfig": cie1000MstpConfig,
       "cie1000MstpConfigBridgeParams": cie1000MstpConfigBridgeParams,
       "cie1000MstpConfigBridgeParamsBridgeMaxAge": cie1000MstpConfigBridgeParamsBridgeMaxAge,
       "cie1000MstpConfigBridgeParamsBridgeHelloTime": cie1000MstpConfigBridgeParamsBridgeHelloTime,
       "cie1000MstpConfigBridgeParamsBridgeForwardDelay": cie1000MstpConfigBridgeParamsBridgeForwardDelay,
       "cie1000MstpConfigBridgeParamsForceVersion": cie1000MstpConfigBridgeParamsForceVersion,
       "cie1000MstpConfigBridgeParamsTxHoldCount": cie1000MstpConfigBridgeParamsTxHoldCount,
       "cie1000MstpConfigBridgeParamsMaxHops": cie1000MstpConfigBridgeParamsMaxHops,
       "cie1000MstpConfigBridgeParamsBpduFiltering": cie1000MstpConfigBridgeParamsBpduFiltering,
       "cie1000MstpConfigBridgeParamsBpduGuard": cie1000MstpConfigBridgeParamsBpduGuard,
       "cie1000MstpConfigBridgeParamsErrorRecoveryDelay": cie1000MstpConfigBridgeParamsErrorRecoveryDelay,
       "cie1000MstpConfigMstiParamTable": cie1000MstpConfigMstiParamTable,
       "cie1000MstpConfigMstiParamEntry": cie1000MstpConfigMstiParamEntry,
       "cie1000MstpConfigMstiParamInstance": cie1000MstpConfigMstiParamInstance,
       "cie1000MstpConfigMstiParamPriority": cie1000MstpConfigMstiParamPriority,
       "cie1000MstpConfigMstiConfig": cie1000MstpConfigMstiConfig,
       "cie1000MstpConfigMstiConfigId": cie1000MstpConfigMstiConfigId,
       "cie1000MstpConfigMstiConfigIdName": cie1000MstpConfigMstiConfigIdName,
       "cie1000MstpConfigMstiConfigIdRevision": cie1000MstpConfigMstiConfigIdRevision,
       "cie1000MstpConfigMstiConfigTable": cie1000MstpConfigMstiConfigTable,
       "cie1000MstpConfigMstiConfigEntry": cie1000MstpConfigMstiConfigEntry,
       "cie1000MstpConfigMstiConfigVid": cie1000MstpConfigMstiConfigVid,
       "cie1000MstpConfigMstiConfigMstid": cie1000MstpConfigMstiConfigMstid,
       "cie1000MstpConfigMstiConfigVlanBitmapTable": cie1000MstpConfigMstiConfigVlanBitmapTable,
       "cie1000MstpConfigMstiConfigVlanBitmapEntry": cie1000MstpConfigMstiConfigVlanBitmapEntry,
       "cie1000MstpConfigMstiConfigVlanBitmapMstiValue": cie1000MstpConfigMstiConfigVlanBitmapMstiValue,
       "cie1000MstpConfigMstiConfigVlanBitmapAccessVlans0To1K": cie1000MstpConfigMstiConfigVlanBitmapAccessVlans0To1K,
       "cie1000MstpConfigMstiConfigVlanBitmapAccessVlans1KTo2K": cie1000MstpConfigMstiConfigVlanBitmapAccessVlans1KTo2K,
       "cie1000MstpConfigMstiConfigVlanBitmapAccessVlans2KTo3K": cie1000MstpConfigMstiConfigVlanBitmapAccessVlans2KTo3K,
       "cie1000MstpConfigMstiConfigVlanBitmapAccessVlans3KTo4K": cie1000MstpConfigMstiConfigVlanBitmapAccessVlans3KTo4K,
       "cie1000MstpConfigCistInterfaceParamTable": cie1000MstpConfigCistInterfaceParamTable,
       "cie1000MstpConfigCistInterfaceParamEntry": cie1000MstpConfigCistInterfaceParamEntry,
       "cie1000MstpConfigCistInterfaceParamInterfaceNo": cie1000MstpConfigCistInterfaceParamInterfaceNo,
       "cie1000MstpConfigCistInterfaceParamEnable": cie1000MstpConfigCistInterfaceParamEnable,
       "cie1000MstpConfigCistInterfaceParamAdminEdgePort": cie1000MstpConfigCistInterfaceParamAdminEdgePort,
       "cie1000MstpConfigCistInterfaceParamAdminAutoEdgePort": cie1000MstpConfigCistInterfaceParamAdminAutoEdgePort,
       "cie1000MstpConfigCistInterfaceParamAdminPointToPointMAC": cie1000MstpConfigCistInterfaceParamAdminPointToPointMAC,
       "cie1000MstpConfigCistInterfaceParamRestrictedRole": cie1000MstpConfigCistInterfaceParamRestrictedRole,
       "cie1000MstpConfigCistInterfaceParamRestrictedTcn": cie1000MstpConfigCistInterfaceParamRestrictedTcn,
       "cie1000MstpConfigCistInterfaceParamBpduGuard": cie1000MstpConfigCistInterfaceParamBpduGuard,
       "cie1000MstpConfigAggrParams": cie1000MstpConfigAggrParams,
       "cie1000MstpConfigAggrParamsEnable": cie1000MstpConfigAggrParamsEnable,
       "cie1000MstpConfigAggrParamsAdminEdgePort": cie1000MstpConfigAggrParamsAdminEdgePort,
       "cie1000MstpConfigAggrParamsAdminAutoEdgePort": cie1000MstpConfigAggrParamsAdminAutoEdgePort,
       "cie1000MstpConfigAggrParamsAdminPointToPointMAC": cie1000MstpConfigAggrParamsAdminPointToPointMAC,
       "cie1000MstpConfigAggrParamsRestrictedRole": cie1000MstpConfigAggrParamsRestrictedRole,
       "cie1000MstpConfigAggrParamsRestrictedTcn": cie1000MstpConfigAggrParamsRestrictedTcn,
       "cie1000MstpConfigAggrParamsBpduGuard": cie1000MstpConfigAggrParamsBpduGuard,
       "cie1000MstpConfigMstiInterfaceParamTable": cie1000MstpConfigMstiInterfaceParamTable,
       "cie1000MstpConfigMstiInterfaceParamEntry": cie1000MstpConfigMstiInterfaceParamEntry,
       "cie1000MstpConfigMstiInterfaceParamInterfaceNo": cie1000MstpConfigMstiInterfaceParamInterfaceNo,
       "cie1000MstpConfigMstiInterfaceParamInstance": cie1000MstpConfigMstiInterfaceParamInstance,
       "cie1000MstpConfigMstiInterfaceParamAdminPathCost": cie1000MstpConfigMstiInterfaceParamAdminPathCost,
       "cie1000MstpConfigMstiInterfaceParamAdminPortPriority": cie1000MstpConfigMstiInterfaceParamAdminPortPriority,
       "cie1000MstpConfigMstiAggrParamTable": cie1000MstpConfigMstiAggrParamTable,
       "cie1000MstpConfigMstiAggrParamEntry": cie1000MstpConfigMstiAggrParamEntry,
       "cie1000MstpConfigMstiAggrParamInstance": cie1000MstpConfigMstiAggrParamInstance,
       "cie1000MstpConfigMstiAggrParamAdminPathCost": cie1000MstpConfigMstiAggrParamAdminPathCost,
       "cie1000MstpConfigMstiAggrParamAdminPortPriority": cie1000MstpConfigMstiAggrParamAdminPortPriority,
       "cie1000MstpStatus": cie1000MstpStatus,
       "cie1000MstpStatusBridgeTable": cie1000MstpStatusBridgeTable,
       "cie1000MstpStatusBridgeEntry": cie1000MstpStatusBridgeEntry,
       "cie1000MstpStatusBridgeInstance": cie1000MstpStatusBridgeInstance,
       "cie1000MstpStatusBridgeBridgeId": cie1000MstpStatusBridgeBridgeId,
       "cie1000MstpStatusBridgeTimeSinceTopologyChange": cie1000MstpStatusBridgeTimeSinceTopologyChange,
       "cie1000MstpStatusBridgeTopologyChangeCount": cie1000MstpStatusBridgeTopologyChangeCount,
       "cie1000MstpStatusBridgeTopologyChange": cie1000MstpStatusBridgeTopologyChange,
       "cie1000MstpStatusBridgeDesignatedRoot": cie1000MstpStatusBridgeDesignatedRoot,
       "cie1000MstpStatusBridgeRootPathCost": cie1000MstpStatusBridgeRootPathCost,
       "cie1000MstpStatusBridgeRootPort": cie1000MstpStatusBridgeRootPort,
       "cie1000MstpStatusBridgeMaxAge": cie1000MstpStatusBridgeMaxAge,
       "cie1000MstpStatusBridgeForwardDelay": cie1000MstpStatusBridgeForwardDelay,
       "cie1000MstpStatusBridgeBridgeMaxAge": cie1000MstpStatusBridgeBridgeMaxAge,
       "cie1000MstpStatusBridgeBridgeHelloTime": cie1000MstpStatusBridgeBridgeHelloTime,
       "cie1000MstpStatusBridgeBridgeForwardDelay": cie1000MstpStatusBridgeBridgeForwardDelay,
       "cie1000MstpStatusBridgeTxHoldCount": cie1000MstpStatusBridgeTxHoldCount,
       "cie1000MstpStatusBridgeForceVersion": cie1000MstpStatusBridgeForceVersion,
       "cie1000MstpStatusBridgeCistRegionalRoot": cie1000MstpStatusBridgeCistRegionalRoot,
       "cie1000MstpStatusBridgeCistInternalPathCost": cie1000MstpStatusBridgeCistInternalPathCost,
       "cie1000MstpStatusBridgeMaxHops": cie1000MstpStatusBridgeMaxHops,
       "cie1000MstpStatusInterfaceTable": cie1000MstpStatusInterfaceTable,
       "cie1000MstpStatusInterfaceEntry": cie1000MstpStatusInterfaceEntry,
       "cie1000MstpStatusInterfaceInterfaceNo": cie1000MstpStatusInterfaceInterfaceNo,
       "cie1000MstpStatusInterfaceInstance": cie1000MstpStatusInterfaceInstance,
       "cie1000MstpStatusInterfaceEnabled": cie1000MstpStatusInterfaceEnabled,
       "cie1000MstpStatusInterfaceActive": cie1000MstpStatusInterfaceActive,
       "cie1000MstpStatusInterfaceParentPort": cie1000MstpStatusInterfaceParentPort,
       "cie1000MstpStatusInterfaceUpTime": cie1000MstpStatusInterfaceUpTime,
       "cie1000MstpStatusInterfacePortState": cie1000MstpStatusInterfacePortState,
       "cie1000MstpStatusInterfacePortId": cie1000MstpStatusInterfacePortId,
       "cie1000MstpStatusInterfacePathCost": cie1000MstpStatusInterfacePathCost,
       "cie1000MstpStatusInterfaceDesignatedRoot": cie1000MstpStatusInterfaceDesignatedRoot,
       "cie1000MstpStatusInterfaceDesignatedCost": cie1000MstpStatusInterfaceDesignatedCost,
       "cie1000MstpStatusInterfaceDesignatedBridge": cie1000MstpStatusInterfaceDesignatedBridge,
       "cie1000MstpStatusInterfaceDesignatedPort": cie1000MstpStatusInterfaceDesignatedPort,
       "cie1000MstpStatusInterfaceTcAck": cie1000MstpStatusInterfaceTcAck,
       "cie1000MstpStatusInterfaceHelloTime": cie1000MstpStatusInterfaceHelloTime,
       "cie1000MstpStatusInterfaceAdminEdgePort": cie1000MstpStatusInterfaceAdminEdgePort,
       "cie1000MstpStatusInterfaceOperEdgePort": cie1000MstpStatusInterfaceOperEdgePort,
       "cie1000MstpStatusInterfaceAutoEdgePort": cie1000MstpStatusInterfaceAutoEdgePort,
       "cie1000MstpStatusInterfaceMacOperational": cie1000MstpStatusInterfaceMacOperational,
       "cie1000MstpStatusInterfaceAdminPointToPointMAC": cie1000MstpStatusInterfaceAdminPointToPointMAC,
       "cie1000MstpStatusInterfaceOperPointToPointMAC": cie1000MstpStatusInterfaceOperPointToPointMAC,
       "cie1000MstpStatusInterfaceRestrictedRole": cie1000MstpStatusInterfaceRestrictedRole,
       "cie1000MstpStatusInterfaceRestrictedTcn": cie1000MstpStatusInterfaceRestrictedTcn,
       "cie1000MstpStatusInterfacePortRole": cie1000MstpStatusInterfacePortRole,
       "cie1000MstpStatusInterfaceDisputed": cie1000MstpStatusInterfaceDisputed,
       "cie1000MstpStatusInterfaceStatisticsTable": cie1000MstpStatusInterfaceStatisticsTable,
       "cie1000MstpStatusInterfaceStatisticsEntry": cie1000MstpStatusInterfaceStatisticsEntry,
       "cie1000MstpStatusInterfaceStatisticsInterfaceNo": cie1000MstpStatusInterfaceStatisticsInterfaceNo,
       "cie1000MstpStatusInterfaceStatisticsStpFrameXmits": cie1000MstpStatusInterfaceStatisticsStpFrameXmits,
       "cie1000MstpStatusInterfaceStatisticsStpFrameReceived": cie1000MstpStatusInterfaceStatisticsStpFrameReceived,
       "cie1000MstpStatusInterfaceStatisticsRstpFrameXmits": cie1000MstpStatusInterfaceStatisticsRstpFrameXmits,
       "cie1000MstpStatusInterfaceStatisticsRstpFrameReceived": cie1000MstpStatusInterfaceStatisticsRstpFrameReceived,
       "cie1000MstpStatusInterfaceStatisticsMstpFrameXmits": cie1000MstpStatusInterfaceStatisticsMstpFrameXmits,
       "cie1000MstpStatusInterfaceStatisticsMstpFrameReceived": cie1000MstpStatusInterfaceStatisticsMstpFrameReceived,
       "cie1000MstpStatusInterfaceStatisticsUnknownFramesReceived": cie1000MstpStatusInterfaceStatisticsUnknownFramesReceived,
       "cie1000MstpStatusInterfaceStatisticsIllegalFrameReceived": cie1000MstpStatusInterfaceStatisticsIllegalFrameReceived,
       "cie1000MstpStatusInterfaceStatisticsTcnFrameXmits": cie1000MstpStatusInterfaceStatisticsTcnFrameXmits,
       "cie1000MstpStatusInterfaceStatisticsTcnFrameReceived": cie1000MstpStatusInterfaceStatisticsTcnFrameReceived,
       "cie1000MstpMibConformance": cie1000MstpMibConformance,
       "cie1000MstpMibCompliances": cie1000MstpMibCompliances,
       "cie1000MstpMibCompliance": cie1000MstpMibCompliance,
       "cie1000MstpMibGroups": cie1000MstpMibGroups,
       "cie1000MstpConfigBridgeParamsInfoGroup": cie1000MstpConfigBridgeParamsInfoGroup,
       "cie1000MstpConfigMstiParamTableInfoGroup": cie1000MstpConfigMstiParamTableInfoGroup,
       "cie1000MstpConfigMstiConfigIdInfoGroup": cie1000MstpConfigMstiConfigIdInfoGroup,
       "cie1000MstpConfigMstiConfigTableInfoGroup": cie1000MstpConfigMstiConfigTableInfoGroup,
       "cie1000MstpConfigMstiConfigVlanBitmapTableInfoGroup": cie1000MstpConfigMstiConfigVlanBitmapTableInfoGroup,
       "cie1000MstpConfigCistInterfaceParamTableInfoGroup": cie1000MstpConfigCistInterfaceParamTableInfoGroup,
       "cie1000MstpConfigAggrParamsInfoGroup": cie1000MstpConfigAggrParamsInfoGroup,
       "cie1000MstpConfigMstiInterfaceParamTableInfoGroup": cie1000MstpConfigMstiInterfaceParamTableInfoGroup,
       "cie1000MstpConfigMstiAggrParamTableInfoGroup": cie1000MstpConfigMstiAggrParamTableInfoGroup,
       "cie1000MstpStatusBridgeTableInfoGroup": cie1000MstpStatusBridgeTableInfoGroup,
       "cie1000MstpStatusInterfaceTableInfoGroup": cie1000MstpStatusInterfaceTableInfoGroup,
       "cie1000MstpStatusInterfaceStatisticsTableInfoGroup": cie1000MstpStatusInterfaceStatisticsTableInfoGroup}
)
