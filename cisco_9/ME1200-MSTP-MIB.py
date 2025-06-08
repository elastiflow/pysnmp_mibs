# SNMP MIB module (ME1200-MSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-MSTP-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:31 2025
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

(me1200SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCOME1200-MIB",
    "me1200SwitchMgmt")

(ME1200DisplayString,
 ME1200InterfaceIndex,
 ME1200Unsigned16,
 ME1200Unsigned8) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200DisplayString",
    "ME1200InterfaceIndex",
    "ME1200Unsigned16",
    "ME1200Unsigned8")

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

me1200MstpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20)
)
if mibBuilder.loadTexts:
    me1200MstpMib.setRevisions(
        ("2014-03-28 00:00",
         "2014-03-11 00:00",
         "2014-02-18 00:00",
         "2014-02-10 00:00",
         "2014-01-29 00:00",
         "2013-11-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200MSTPForceVersion(TextualConvention, Integer32):
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



class ME1200Point2Point(TextualConvention, Integer32):
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



class ME1200PortState(TextualConvention, Integer32):
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

_Me1200Mstp_ObjectIdentity = ObjectIdentity
me1200Mstp = _Me1200Mstp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1)
)
_Me1200MstpConfig_ObjectIdentity = ObjectIdentity
me1200MstpConfig = _Me1200MstpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2)
)
_Me1200MstpBridgeParams_ObjectIdentity = ObjectIdentity
me1200MstpBridgeParams = _Me1200MstpBridgeParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 1)
)
_Me1200MstpBridgeParamsBridgeMaxAge_Type = Unsigned32
_Me1200MstpBridgeParamsBridgeMaxAge_Object = MibScalar
me1200MstpBridgeParamsBridgeMaxAge = _Me1200MstpBridgeParamsBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 1, 1),
    _Me1200MstpBridgeParamsBridgeMaxAge_Type()
)
me1200MstpBridgeParamsBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpBridgeParamsBridgeMaxAge.setStatus("current")
_Me1200MstpBridgeParamsBridgeHelloTime_Type = Unsigned32
_Me1200MstpBridgeParamsBridgeHelloTime_Object = MibScalar
me1200MstpBridgeParamsBridgeHelloTime = _Me1200MstpBridgeParamsBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 1, 2),
    _Me1200MstpBridgeParamsBridgeHelloTime_Type()
)
me1200MstpBridgeParamsBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpBridgeParamsBridgeHelloTime.setStatus("current")
_Me1200MstpBridgeParamsBridgeForwardDelay_Type = Unsigned32
_Me1200MstpBridgeParamsBridgeForwardDelay_Object = MibScalar
me1200MstpBridgeParamsBridgeForwardDelay = _Me1200MstpBridgeParamsBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 1, 3),
    _Me1200MstpBridgeParamsBridgeForwardDelay_Type()
)
me1200MstpBridgeParamsBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpBridgeParamsBridgeForwardDelay.setStatus("current")
_Me1200MstpBridgeParamsForceVersion_Type = ME1200MSTPForceVersion
_Me1200MstpBridgeParamsForceVersion_Object = MibScalar
me1200MstpBridgeParamsForceVersion = _Me1200MstpBridgeParamsForceVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 1, 4),
    _Me1200MstpBridgeParamsForceVersion_Type()
)
me1200MstpBridgeParamsForceVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpBridgeParamsForceVersion.setStatus("current")
_Me1200MstpBridgeParamsTxHoldCount_Type = Unsigned32
_Me1200MstpBridgeParamsTxHoldCount_Object = MibScalar
me1200MstpBridgeParamsTxHoldCount = _Me1200MstpBridgeParamsTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 1, 5),
    _Me1200MstpBridgeParamsTxHoldCount_Type()
)
me1200MstpBridgeParamsTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpBridgeParamsTxHoldCount.setStatus("current")
_Me1200MstpBridgeParamsMaxHops_Type = ME1200Unsigned8
_Me1200MstpBridgeParamsMaxHops_Object = MibScalar
me1200MstpBridgeParamsMaxHops = _Me1200MstpBridgeParamsMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 1, 6),
    _Me1200MstpBridgeParamsMaxHops_Type()
)
me1200MstpBridgeParamsMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpBridgeParamsMaxHops.setStatus("current")
_Me1200MstpBridgeParamsBpduFiltering_Type = TruthValue
_Me1200MstpBridgeParamsBpduFiltering_Object = MibScalar
me1200MstpBridgeParamsBpduFiltering = _Me1200MstpBridgeParamsBpduFiltering_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 1, 7),
    _Me1200MstpBridgeParamsBpduFiltering_Type()
)
me1200MstpBridgeParamsBpduFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpBridgeParamsBpduFiltering.setStatus("current")
_Me1200MstpBridgeParamsBpduGuard_Type = TruthValue
_Me1200MstpBridgeParamsBpduGuard_Object = MibScalar
me1200MstpBridgeParamsBpduGuard = _Me1200MstpBridgeParamsBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 1, 8),
    _Me1200MstpBridgeParamsBpduGuard_Type()
)
me1200MstpBridgeParamsBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpBridgeParamsBpduGuard.setStatus("current")
_Me1200MstpBridgeParamsErrorRecoveryDelay_Type = Unsigned32
_Me1200MstpBridgeParamsErrorRecoveryDelay_Object = MibScalar
me1200MstpBridgeParamsErrorRecoveryDelay = _Me1200MstpBridgeParamsErrorRecoveryDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 1, 9),
    _Me1200MstpBridgeParamsErrorRecoveryDelay_Type()
)
me1200MstpBridgeParamsErrorRecoveryDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpBridgeParamsErrorRecoveryDelay.setStatus("current")
_Me1200MstpMstiParamTable_Object = MibTable
me1200MstpMstiParamTable = _Me1200MstpMstiParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 2)
)
if mibBuilder.loadTexts:
    me1200MstpMstiParamTable.setStatus("current")
_Me1200MstpMstiParamEntry_Object = MibTableRow
me1200MstpMstiParamEntry = _Me1200MstpMstiParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 2, 1)
)
me1200MstpMstiParamEntry.setIndexNames(
    (0, "ME1200-MSTP-MIB", "me1200MstpMstiParamInstance"),
)
if mibBuilder.loadTexts:
    me1200MstpMstiParamEntry.setStatus("current")


class _Me1200MstpMstiParamInstance_Type(Integer32):
    """Custom type me1200MstpMstiParamInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Me1200MstpMstiParamInstance_Type.__name__ = "Integer32"
_Me1200MstpMstiParamInstance_Object = MibTableColumn
me1200MstpMstiParamInstance = _Me1200MstpMstiParamInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 2, 1, 1),
    _Me1200MstpMstiParamInstance_Type()
)
me1200MstpMstiParamInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200MstpMstiParamInstance.setStatus("current")
_Me1200MstpMstiParamPriority_Type = ME1200Unsigned8
_Me1200MstpMstiParamPriority_Object = MibTableColumn
me1200MstpMstiParamPriority = _Me1200MstpMstiParamPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 2, 1, 2),
    _Me1200MstpMstiParamPriority_Type()
)
me1200MstpMstiParamPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpMstiParamPriority.setStatus("current")
_Me1200MstpMstiConfig_ObjectIdentity = ObjectIdentity
me1200MstpMstiConfig = _Me1200MstpMstiConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 3)
)
_Me1200MstpMstiConfigId_ObjectIdentity = ObjectIdentity
me1200MstpMstiConfigId = _Me1200MstpMstiConfigId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 3, 1)
)


class _Me1200MstpMstiConfigIdName_Type(ME1200DisplayString):
    """Custom type me1200MstpMstiConfigIdName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Me1200MstpMstiConfigIdName_Type.__name__ = "ME1200DisplayString"
_Me1200MstpMstiConfigIdName_Object = MibScalar
me1200MstpMstiConfigIdName = _Me1200MstpMstiConfigIdName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 3, 1, 1),
    _Me1200MstpMstiConfigIdName_Type()
)
me1200MstpMstiConfigIdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpMstiConfigIdName.setStatus("current")
_Me1200MstpMstiConfigIdRevision_Type = ME1200Unsigned16
_Me1200MstpMstiConfigIdRevision_Object = MibScalar
me1200MstpMstiConfigIdRevision = _Me1200MstpMstiConfigIdRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 3, 1, 2),
    _Me1200MstpMstiConfigIdRevision_Type()
)
me1200MstpMstiConfigIdRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpMstiConfigIdRevision.setStatus("current")
_Me1200MstpMstiConfigTable_Object = MibTable
me1200MstpMstiConfigTable = _Me1200MstpMstiConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    me1200MstpMstiConfigTable.setStatus("current")
_Me1200MstpMstiConfigEntry_Object = MibTableRow
me1200MstpMstiConfigEntry = _Me1200MstpMstiConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 3, 2, 1)
)
me1200MstpMstiConfigEntry.setIndexNames(
    (0, "ME1200-MSTP-MIB", "me1200MstpMstiConfigVid"),
)
if mibBuilder.loadTexts:
    me1200MstpMstiConfigEntry.setStatus("current")


class _Me1200MstpMstiConfigVid_Type(Integer32):
    """Custom type me1200MstpMstiConfigVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Me1200MstpMstiConfigVid_Type.__name__ = "Integer32"
_Me1200MstpMstiConfigVid_Object = MibTableColumn
me1200MstpMstiConfigVid = _Me1200MstpMstiConfigVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 3, 2, 1, 1),
    _Me1200MstpMstiConfigVid_Type()
)
me1200MstpMstiConfigVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200MstpMstiConfigVid.setStatus("current")
_Me1200MstpMstiConfigMstid_Type = ME1200Unsigned8
_Me1200MstpMstiConfigMstid_Object = MibTableColumn
me1200MstpMstiConfigMstid = _Me1200MstpMstiConfigMstid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 3, 2, 1, 2),
    _Me1200MstpMstiConfigMstid_Type()
)
me1200MstpMstiConfigMstid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpMstiConfigMstid.setStatus("current")
_Me1200MstpCistInterfaceParamTable_Object = MibTable
me1200MstpCistInterfaceParamTable = _Me1200MstpCistInterfaceParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 4)
)
if mibBuilder.loadTexts:
    me1200MstpCistInterfaceParamTable.setStatus("current")
_Me1200MstpCistInterfaceParamEntry_Object = MibTableRow
me1200MstpCistInterfaceParamEntry = _Me1200MstpCistInterfaceParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 4, 1)
)
me1200MstpCistInterfaceParamEntry.setIndexNames(
    (0, "ME1200-MSTP-MIB", "me1200MstpCistInterfaceParamInterfaceNo"),
)
if mibBuilder.loadTexts:
    me1200MstpCistInterfaceParamEntry.setStatus("current")
_Me1200MstpCistInterfaceParamInterfaceNo_Type = ME1200InterfaceIndex
_Me1200MstpCistInterfaceParamInterfaceNo_Object = MibTableColumn
me1200MstpCistInterfaceParamInterfaceNo = _Me1200MstpCistInterfaceParamInterfaceNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 4, 1, 1),
    _Me1200MstpCistInterfaceParamInterfaceNo_Type()
)
me1200MstpCistInterfaceParamInterfaceNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200MstpCistInterfaceParamInterfaceNo.setStatus("current")
_Me1200MstpCistInterfaceParamEnable_Type = TruthValue
_Me1200MstpCistInterfaceParamEnable_Object = MibTableColumn
me1200MstpCistInterfaceParamEnable = _Me1200MstpCistInterfaceParamEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 4, 1, 2),
    _Me1200MstpCistInterfaceParamEnable_Type()
)
me1200MstpCistInterfaceParamEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpCistInterfaceParamEnable.setStatus("current")
_Me1200MstpCistInterfaceParamAdminEdgePort_Type = TruthValue
_Me1200MstpCistInterfaceParamAdminEdgePort_Object = MibTableColumn
me1200MstpCistInterfaceParamAdminEdgePort = _Me1200MstpCistInterfaceParamAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 4, 1, 3),
    _Me1200MstpCistInterfaceParamAdminEdgePort_Type()
)
me1200MstpCistInterfaceParamAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpCistInterfaceParamAdminEdgePort.setStatus("current")
_Me1200MstpCistInterfaceParamAdminAutoEdgePort_Type = TruthValue
_Me1200MstpCistInterfaceParamAdminAutoEdgePort_Object = MibTableColumn
me1200MstpCistInterfaceParamAdminAutoEdgePort = _Me1200MstpCistInterfaceParamAdminAutoEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 4, 1, 4),
    _Me1200MstpCistInterfaceParamAdminAutoEdgePort_Type()
)
me1200MstpCistInterfaceParamAdminAutoEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpCistInterfaceParamAdminAutoEdgePort.setStatus("current")
_Me1200MstpCistInterfaceParamAdminPointToPointMAC_Type = ME1200Point2Point
_Me1200MstpCistInterfaceParamAdminPointToPointMAC_Object = MibTableColumn
me1200MstpCistInterfaceParamAdminPointToPointMAC = _Me1200MstpCistInterfaceParamAdminPointToPointMAC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 4, 1, 5),
    _Me1200MstpCistInterfaceParamAdminPointToPointMAC_Type()
)
me1200MstpCistInterfaceParamAdminPointToPointMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpCistInterfaceParamAdminPointToPointMAC.setStatus("current")
_Me1200MstpCistInterfaceParamRestrictedRole_Type = TruthValue
_Me1200MstpCistInterfaceParamRestrictedRole_Object = MibTableColumn
me1200MstpCistInterfaceParamRestrictedRole = _Me1200MstpCistInterfaceParamRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 4, 1, 6),
    _Me1200MstpCistInterfaceParamRestrictedRole_Type()
)
me1200MstpCistInterfaceParamRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpCistInterfaceParamRestrictedRole.setStatus("current")
_Me1200MstpCistInterfaceParamRestrictedTcn_Type = TruthValue
_Me1200MstpCistInterfaceParamRestrictedTcn_Object = MibTableColumn
me1200MstpCistInterfaceParamRestrictedTcn = _Me1200MstpCistInterfaceParamRestrictedTcn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 4, 1, 7),
    _Me1200MstpCistInterfaceParamRestrictedTcn_Type()
)
me1200MstpCistInterfaceParamRestrictedTcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpCistInterfaceParamRestrictedTcn.setStatus("current")
_Me1200MstpCistInterfaceParamBpduGuard_Type = TruthValue
_Me1200MstpCistInterfaceParamBpduGuard_Object = MibTableColumn
me1200MstpCistInterfaceParamBpduGuard = _Me1200MstpCistInterfaceParamBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 4, 1, 8),
    _Me1200MstpCistInterfaceParamBpduGuard_Type()
)
me1200MstpCistInterfaceParamBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpCistInterfaceParamBpduGuard.setStatus("current")
_Me1200MstpAggrParams_ObjectIdentity = ObjectIdentity
me1200MstpAggrParams = _Me1200MstpAggrParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 5)
)
_Me1200MstpAggrParamsEnable_Type = TruthValue
_Me1200MstpAggrParamsEnable_Object = MibScalar
me1200MstpAggrParamsEnable = _Me1200MstpAggrParamsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 5, 1),
    _Me1200MstpAggrParamsEnable_Type()
)
me1200MstpAggrParamsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpAggrParamsEnable.setStatus("current")
_Me1200MstpAggrParamsAdminEdgePort_Type = TruthValue
_Me1200MstpAggrParamsAdminEdgePort_Object = MibScalar
me1200MstpAggrParamsAdminEdgePort = _Me1200MstpAggrParamsAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 5, 2),
    _Me1200MstpAggrParamsAdminEdgePort_Type()
)
me1200MstpAggrParamsAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpAggrParamsAdminEdgePort.setStatus("current")
_Me1200MstpAggrParamsAdminAutoEdgePort_Type = TruthValue
_Me1200MstpAggrParamsAdminAutoEdgePort_Object = MibScalar
me1200MstpAggrParamsAdminAutoEdgePort = _Me1200MstpAggrParamsAdminAutoEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 5, 3),
    _Me1200MstpAggrParamsAdminAutoEdgePort_Type()
)
me1200MstpAggrParamsAdminAutoEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpAggrParamsAdminAutoEdgePort.setStatus("current")
_Me1200MstpAggrParamsAdminPointToPointMAC_Type = ME1200Point2Point
_Me1200MstpAggrParamsAdminPointToPointMAC_Object = MibScalar
me1200MstpAggrParamsAdminPointToPointMAC = _Me1200MstpAggrParamsAdminPointToPointMAC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 5, 4),
    _Me1200MstpAggrParamsAdminPointToPointMAC_Type()
)
me1200MstpAggrParamsAdminPointToPointMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpAggrParamsAdminPointToPointMAC.setStatus("current")
_Me1200MstpAggrParamsRestrictedRole_Type = TruthValue
_Me1200MstpAggrParamsRestrictedRole_Object = MibScalar
me1200MstpAggrParamsRestrictedRole = _Me1200MstpAggrParamsRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 5, 5),
    _Me1200MstpAggrParamsRestrictedRole_Type()
)
me1200MstpAggrParamsRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpAggrParamsRestrictedRole.setStatus("current")
_Me1200MstpAggrParamsRestrictedTcn_Type = TruthValue
_Me1200MstpAggrParamsRestrictedTcn_Object = MibScalar
me1200MstpAggrParamsRestrictedTcn = _Me1200MstpAggrParamsRestrictedTcn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 5, 6),
    _Me1200MstpAggrParamsRestrictedTcn_Type()
)
me1200MstpAggrParamsRestrictedTcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpAggrParamsRestrictedTcn.setStatus("current")
_Me1200MstpAggrParamsBpduGuard_Type = TruthValue
_Me1200MstpAggrParamsBpduGuard_Object = MibScalar
me1200MstpAggrParamsBpduGuard = _Me1200MstpAggrParamsBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 5, 7),
    _Me1200MstpAggrParamsBpduGuard_Type()
)
me1200MstpAggrParamsBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpAggrParamsBpduGuard.setStatus("current")
_Me1200MstpMstiInterfaceParamTable_Object = MibTable
me1200MstpMstiInterfaceParamTable = _Me1200MstpMstiInterfaceParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 6)
)
if mibBuilder.loadTexts:
    me1200MstpMstiInterfaceParamTable.setStatus("current")
_Me1200MstpMstiInterfaceParamEntry_Object = MibTableRow
me1200MstpMstiInterfaceParamEntry = _Me1200MstpMstiInterfaceParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 6, 1)
)
me1200MstpMstiInterfaceParamEntry.setIndexNames(
    (0, "ME1200-MSTP-MIB", "me1200MstpMstiInterfaceParamInterfaceNo"),
    (0, "ME1200-MSTP-MIB", "me1200MstpMstiInterfaceParamInstance"),
)
if mibBuilder.loadTexts:
    me1200MstpMstiInterfaceParamEntry.setStatus("current")
_Me1200MstpMstiInterfaceParamInterfaceNo_Type = ME1200InterfaceIndex
_Me1200MstpMstiInterfaceParamInterfaceNo_Object = MibTableColumn
me1200MstpMstiInterfaceParamInterfaceNo = _Me1200MstpMstiInterfaceParamInterfaceNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 6, 1, 1),
    _Me1200MstpMstiInterfaceParamInterfaceNo_Type()
)
me1200MstpMstiInterfaceParamInterfaceNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200MstpMstiInterfaceParamInterfaceNo.setStatus("current")


class _Me1200MstpMstiInterfaceParamInstance_Type(Integer32):
    """Custom type me1200MstpMstiInterfaceParamInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Me1200MstpMstiInterfaceParamInstance_Type.__name__ = "Integer32"
_Me1200MstpMstiInterfaceParamInstance_Object = MibTableColumn
me1200MstpMstiInterfaceParamInstance = _Me1200MstpMstiInterfaceParamInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 6, 1, 2),
    _Me1200MstpMstiInterfaceParamInstance_Type()
)
me1200MstpMstiInterfaceParamInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200MstpMstiInterfaceParamInstance.setStatus("current")
_Me1200MstpMstiInterfaceParamAdminPathCost_Type = Unsigned32
_Me1200MstpMstiInterfaceParamAdminPathCost_Object = MibTableColumn
me1200MstpMstiInterfaceParamAdminPathCost = _Me1200MstpMstiInterfaceParamAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 6, 1, 3),
    _Me1200MstpMstiInterfaceParamAdminPathCost_Type()
)
me1200MstpMstiInterfaceParamAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpMstiInterfaceParamAdminPathCost.setStatus("current")
_Me1200MstpMstiInterfaceParamAdminPortPriority_Type = ME1200Unsigned8
_Me1200MstpMstiInterfaceParamAdminPortPriority_Object = MibTableColumn
me1200MstpMstiInterfaceParamAdminPortPriority = _Me1200MstpMstiInterfaceParamAdminPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 6, 1, 4),
    _Me1200MstpMstiInterfaceParamAdminPortPriority_Type()
)
me1200MstpMstiInterfaceParamAdminPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpMstiInterfaceParamAdminPortPriority.setStatus("current")
_Me1200MstpMstiAggrParamTable_Object = MibTable
me1200MstpMstiAggrParamTable = _Me1200MstpMstiAggrParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 7)
)
if mibBuilder.loadTexts:
    me1200MstpMstiAggrParamTable.setStatus("current")
_Me1200MstpMstiAggrParamEntry_Object = MibTableRow
me1200MstpMstiAggrParamEntry = _Me1200MstpMstiAggrParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 7, 1)
)
me1200MstpMstiAggrParamEntry.setIndexNames(
    (0, "ME1200-MSTP-MIB", "me1200MstpMstiAggrParamInstance"),
)
if mibBuilder.loadTexts:
    me1200MstpMstiAggrParamEntry.setStatus("current")


class _Me1200MstpMstiAggrParamInstance_Type(Integer32):
    """Custom type me1200MstpMstiAggrParamInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Me1200MstpMstiAggrParamInstance_Type.__name__ = "Integer32"
_Me1200MstpMstiAggrParamInstance_Object = MibTableColumn
me1200MstpMstiAggrParamInstance = _Me1200MstpMstiAggrParamInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 7, 1, 1),
    _Me1200MstpMstiAggrParamInstance_Type()
)
me1200MstpMstiAggrParamInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200MstpMstiAggrParamInstance.setStatus("current")
_Me1200MstpMstiAggrParamAdminPathCost_Type = Unsigned32
_Me1200MstpMstiAggrParamAdminPathCost_Object = MibTableColumn
me1200MstpMstiAggrParamAdminPathCost = _Me1200MstpMstiAggrParamAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 7, 1, 3),
    _Me1200MstpMstiAggrParamAdminPathCost_Type()
)
me1200MstpMstiAggrParamAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpMstiAggrParamAdminPathCost.setStatus("current")
_Me1200MstpMstiAggrParamAdminPortPriority_Type = ME1200Unsigned8
_Me1200MstpMstiAggrParamAdminPortPriority_Object = MibTableColumn
me1200MstpMstiAggrParamAdminPortPriority = _Me1200MstpMstiAggrParamAdminPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 2, 7, 1, 4),
    _Me1200MstpMstiAggrParamAdminPortPriority_Type()
)
me1200MstpMstiAggrParamAdminPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200MstpMstiAggrParamAdminPortPriority.setStatus("current")
_Me1200MstpStatus_ObjectIdentity = ObjectIdentity
me1200MstpStatus = _Me1200MstpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3)
)
_Me1200MstpBridgeStatusTable_Object = MibTable
me1200MstpBridgeStatusTable = _Me1200MstpBridgeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 1)
)
if mibBuilder.loadTexts:
    me1200MstpBridgeStatusTable.setStatus("current")
_Me1200MstpBridgeStatusEntry_Object = MibTableRow
me1200MstpBridgeStatusEntry = _Me1200MstpBridgeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 1, 1)
)
me1200MstpBridgeStatusEntry.setIndexNames(
    (0, "ME1200-MSTP-MIB", "me1200MstpBridgeStatusInstance"),
)
if mibBuilder.loadTexts:
    me1200MstpBridgeStatusEntry.setStatus("current")


class _Me1200MstpBridgeStatusInstance_Type(Integer32):
    """Custom type me1200MstpBridgeStatusInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Me1200MstpBridgeStatusInstance_Type.__name__ = "Integer32"
_Me1200MstpBridgeStatusInstance_Object = MibTableColumn
me1200MstpBridgeStatusInstance = _Me1200MstpBridgeStatusInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 1, 1, 1),
    _Me1200MstpBridgeStatusInstance_Type()
)
me1200MstpBridgeStatusInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200MstpBridgeStatusInstance.setStatus("current")


class _Me1200MstpBridgeStatusBridgeId_Type(OctetString):
    """Custom type me1200MstpBridgeStatusBridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_Me1200MstpBridgeStatusBridgeId_Type.__name__ = "OctetString"
_Me1200MstpBridgeStatusBridgeId_Object = MibTableColumn
me1200MstpBridgeStatusBridgeId = _Me1200MstpBridgeStatusBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 1, 1, 2),
    _Me1200MstpBridgeStatusBridgeId_Type()
)
me1200MstpBridgeStatusBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpBridgeStatusBridgeId.setStatus("current")
_Me1200MstpBridgeStatusTimeSinceTopologyChange_Type = Unsigned32
_Me1200MstpBridgeStatusTimeSinceTopologyChange_Object = MibTableColumn
me1200MstpBridgeStatusTimeSinceTopologyChange = _Me1200MstpBridgeStatusTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 1, 1, 3),
    _Me1200MstpBridgeStatusTimeSinceTopologyChange_Type()
)
me1200MstpBridgeStatusTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpBridgeStatusTimeSinceTopologyChange.setStatus("current")
_Me1200MstpBridgeStatusTopologyChangeCount_Type = Unsigned32
_Me1200MstpBridgeStatusTopologyChangeCount_Object = MibTableColumn
me1200MstpBridgeStatusTopologyChangeCount = _Me1200MstpBridgeStatusTopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 1, 1, 4),
    _Me1200MstpBridgeStatusTopologyChangeCount_Type()
)
me1200MstpBridgeStatusTopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpBridgeStatusTopologyChangeCount.setStatus("current")
_Me1200MstpBridgeStatusTopologyChange_Type = TruthValue
_Me1200MstpBridgeStatusTopologyChange_Object = MibTableColumn
me1200MstpBridgeStatusTopologyChange = _Me1200MstpBridgeStatusTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 1, 1, 5),
    _Me1200MstpBridgeStatusTopologyChange_Type()
)
me1200MstpBridgeStatusTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpBridgeStatusTopologyChange.setStatus("current")


class _Me1200MstpBridgeStatusDesignatedRoot_Type(OctetString):
    """Custom type me1200MstpBridgeStatusDesignatedRoot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_Me1200MstpBridgeStatusDesignatedRoot_Type.__name__ = "OctetString"
_Me1200MstpBridgeStatusDesignatedRoot_Object = MibTableColumn
me1200MstpBridgeStatusDesignatedRoot = _Me1200MstpBridgeStatusDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 1, 1, 6),
    _Me1200MstpBridgeStatusDesignatedRoot_Type()
)
me1200MstpBridgeStatusDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpBridgeStatusDesignatedRoot.setStatus("current")
_Me1200MstpBridgeStatusRootPathCost_Type = Unsigned32
_Me1200MstpBridgeStatusRootPathCost_Object = MibTableColumn
me1200MstpBridgeStatusRootPathCost = _Me1200MstpBridgeStatusRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 1, 1, 7),
    _Me1200MstpBridgeStatusRootPathCost_Type()
)
me1200MstpBridgeStatusRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpBridgeStatusRootPathCost.setStatus("current")
_Me1200MstpBridgeStatusRootPort_Type = Unsigned32
_Me1200MstpBridgeStatusRootPort_Object = MibTableColumn
me1200MstpBridgeStatusRootPort = _Me1200MstpBridgeStatusRootPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 1, 1, 8),
    _Me1200MstpBridgeStatusRootPort_Type()
)
me1200MstpBridgeStatusRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpBridgeStatusRootPort.setStatus("current")
_Me1200MstpBridgeStatusMaxAge_Type = Unsigned32
_Me1200MstpBridgeStatusMaxAge_Object = MibTableColumn
me1200MstpBridgeStatusMaxAge = _Me1200MstpBridgeStatusMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 1, 1, 9),
    _Me1200MstpBridgeStatusMaxAge_Type()
)
me1200MstpBridgeStatusMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpBridgeStatusMaxAge.setStatus("current")
_Me1200MstpBridgeStatusForwardDelay_Type = Unsigned32
_Me1200MstpBridgeStatusForwardDelay_Object = MibTableColumn
me1200MstpBridgeStatusForwardDelay = _Me1200MstpBridgeStatusForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 1, 1, 10),
    _Me1200MstpBridgeStatusForwardDelay_Type()
)
me1200MstpBridgeStatusForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpBridgeStatusForwardDelay.setStatus("current")
_Me1200MstpBridgeStatusBridgeMaxAge_Type = Unsigned32
_Me1200MstpBridgeStatusBridgeMaxAge_Object = MibTableColumn
me1200MstpBridgeStatusBridgeMaxAge = _Me1200MstpBridgeStatusBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 1, 1, 11),
    _Me1200MstpBridgeStatusBridgeMaxAge_Type()
)
me1200MstpBridgeStatusBridgeMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpBridgeStatusBridgeMaxAge.setStatus("current")
_Me1200MstpBridgeStatusBridgeHelloTime_Type = Unsigned32
_Me1200MstpBridgeStatusBridgeHelloTime_Object = MibTableColumn
me1200MstpBridgeStatusBridgeHelloTime = _Me1200MstpBridgeStatusBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 1, 1, 12),
    _Me1200MstpBridgeStatusBridgeHelloTime_Type()
)
me1200MstpBridgeStatusBridgeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpBridgeStatusBridgeHelloTime.setStatus("current")
_Me1200MstpBridgeStatusBridgeForwardDelay_Type = Unsigned32
_Me1200MstpBridgeStatusBridgeForwardDelay_Object = MibTableColumn
me1200MstpBridgeStatusBridgeForwardDelay = _Me1200MstpBridgeStatusBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 1, 1, 13),
    _Me1200MstpBridgeStatusBridgeForwardDelay_Type()
)
me1200MstpBridgeStatusBridgeForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpBridgeStatusBridgeForwardDelay.setStatus("current")
_Me1200MstpBridgeStatusTxHoldCount_Type = Unsigned32
_Me1200MstpBridgeStatusTxHoldCount_Object = MibTableColumn
me1200MstpBridgeStatusTxHoldCount = _Me1200MstpBridgeStatusTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 1, 1, 14),
    _Me1200MstpBridgeStatusTxHoldCount_Type()
)
me1200MstpBridgeStatusTxHoldCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpBridgeStatusTxHoldCount.setStatus("current")
_Me1200MstpBridgeStatusForceVersion_Type = ME1200MSTPForceVersion
_Me1200MstpBridgeStatusForceVersion_Object = MibTableColumn
me1200MstpBridgeStatusForceVersion = _Me1200MstpBridgeStatusForceVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 1, 1, 15),
    _Me1200MstpBridgeStatusForceVersion_Type()
)
me1200MstpBridgeStatusForceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpBridgeStatusForceVersion.setStatus("current")


class _Me1200MstpBridgeStatusCistRegionalRoot_Type(OctetString):
    """Custom type me1200MstpBridgeStatusCistRegionalRoot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_Me1200MstpBridgeStatusCistRegionalRoot_Type.__name__ = "OctetString"
_Me1200MstpBridgeStatusCistRegionalRoot_Object = MibTableColumn
me1200MstpBridgeStatusCistRegionalRoot = _Me1200MstpBridgeStatusCistRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 1, 1, 16),
    _Me1200MstpBridgeStatusCistRegionalRoot_Type()
)
me1200MstpBridgeStatusCistRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpBridgeStatusCistRegionalRoot.setStatus("current")
_Me1200MstpBridgeStatusCistInternalPathCost_Type = Unsigned32
_Me1200MstpBridgeStatusCistInternalPathCost_Object = MibTableColumn
me1200MstpBridgeStatusCistInternalPathCost = _Me1200MstpBridgeStatusCistInternalPathCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 1, 1, 17),
    _Me1200MstpBridgeStatusCistInternalPathCost_Type()
)
me1200MstpBridgeStatusCistInternalPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpBridgeStatusCistInternalPathCost.setStatus("current")
_Me1200MstpBridgeStatusMaxHops_Type = ME1200Unsigned8
_Me1200MstpBridgeStatusMaxHops_Object = MibTableColumn
me1200MstpBridgeStatusMaxHops = _Me1200MstpBridgeStatusMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 1, 1, 18),
    _Me1200MstpBridgeStatusMaxHops_Type()
)
me1200MstpBridgeStatusMaxHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpBridgeStatusMaxHops.setStatus("current")
_Me1200MstpInterfaceStatusTable_Object = MibTable
me1200MstpInterfaceStatusTable = _Me1200MstpInterfaceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 2)
)
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatusTable.setStatus("current")
_Me1200MstpInterfaceStatusEntry_Object = MibTableRow
me1200MstpInterfaceStatusEntry = _Me1200MstpInterfaceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 2, 1)
)
me1200MstpInterfaceStatusEntry.setIndexNames(
    (0, "ME1200-MSTP-MIB", "me1200MstpInterfaceStatusInterfaceNo"),
    (0, "ME1200-MSTP-MIB", "me1200MstpInterfaceStatusInstance"),
)
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatusEntry.setStatus("current")
_Me1200MstpInterfaceStatusInterfaceNo_Type = ME1200InterfaceIndex
_Me1200MstpInterfaceStatusInterfaceNo_Object = MibTableColumn
me1200MstpInterfaceStatusInterfaceNo = _Me1200MstpInterfaceStatusInterfaceNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 2, 1, 1),
    _Me1200MstpInterfaceStatusInterfaceNo_Type()
)
me1200MstpInterfaceStatusInterfaceNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatusInterfaceNo.setStatus("current")


class _Me1200MstpInterfaceStatusInstance_Type(Integer32):
    """Custom type me1200MstpInterfaceStatusInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Me1200MstpInterfaceStatusInstance_Type.__name__ = "Integer32"
_Me1200MstpInterfaceStatusInstance_Object = MibTableColumn
me1200MstpInterfaceStatusInstance = _Me1200MstpInterfaceStatusInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 2, 1, 2),
    _Me1200MstpInterfaceStatusInstance_Type()
)
me1200MstpInterfaceStatusInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatusInstance.setStatus("current")
_Me1200MstpInterfaceStatusEnabled_Type = TruthValue
_Me1200MstpInterfaceStatusEnabled_Object = MibTableColumn
me1200MstpInterfaceStatusEnabled = _Me1200MstpInterfaceStatusEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 2, 1, 3),
    _Me1200MstpInterfaceStatusEnabled_Type()
)
me1200MstpInterfaceStatusEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatusEnabled.setStatus("current")
_Me1200MstpInterfaceStatusActive_Type = TruthValue
_Me1200MstpInterfaceStatusActive_Object = MibTableColumn
me1200MstpInterfaceStatusActive = _Me1200MstpInterfaceStatusActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 2, 1, 4),
    _Me1200MstpInterfaceStatusActive_Type()
)
me1200MstpInterfaceStatusActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatusActive.setStatus("current")
_Me1200MstpInterfaceStatusParentPort_Type = Unsigned32
_Me1200MstpInterfaceStatusParentPort_Object = MibTableColumn
me1200MstpInterfaceStatusParentPort = _Me1200MstpInterfaceStatusParentPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 2, 1, 5),
    _Me1200MstpInterfaceStatusParentPort_Type()
)
me1200MstpInterfaceStatusParentPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatusParentPort.setStatus("current")
_Me1200MstpInterfaceStatusUpTime_Type = Unsigned32
_Me1200MstpInterfaceStatusUpTime_Object = MibTableColumn
me1200MstpInterfaceStatusUpTime = _Me1200MstpInterfaceStatusUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 2, 1, 6),
    _Me1200MstpInterfaceStatusUpTime_Type()
)
me1200MstpInterfaceStatusUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatusUpTime.setStatus("current")
_Me1200MstpInterfaceStatusPortState_Type = ME1200PortState
_Me1200MstpInterfaceStatusPortState_Object = MibTableColumn
me1200MstpInterfaceStatusPortState = _Me1200MstpInterfaceStatusPortState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 2, 1, 7),
    _Me1200MstpInterfaceStatusPortState_Type()
)
me1200MstpInterfaceStatusPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatusPortState.setStatus("current")


class _Me1200MstpInterfaceStatusPortId_Type(OctetString):
    """Custom type me1200MstpInterfaceStatusPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixedLength = 2


_Me1200MstpInterfaceStatusPortId_Type.__name__ = "OctetString"
_Me1200MstpInterfaceStatusPortId_Object = MibTableColumn
me1200MstpInterfaceStatusPortId = _Me1200MstpInterfaceStatusPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 2, 1, 8),
    _Me1200MstpInterfaceStatusPortId_Type()
)
me1200MstpInterfaceStatusPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatusPortId.setStatus("current")
_Me1200MstpInterfaceStatusPathCost_Type = Unsigned32
_Me1200MstpInterfaceStatusPathCost_Object = MibTableColumn
me1200MstpInterfaceStatusPathCost = _Me1200MstpInterfaceStatusPathCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 2, 1, 9),
    _Me1200MstpInterfaceStatusPathCost_Type()
)
me1200MstpInterfaceStatusPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatusPathCost.setStatus("current")


class _Me1200MstpInterfaceStatusDesignatedRoot_Type(OctetString):
    """Custom type me1200MstpInterfaceStatusDesignatedRoot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_Me1200MstpInterfaceStatusDesignatedRoot_Type.__name__ = "OctetString"
_Me1200MstpInterfaceStatusDesignatedRoot_Object = MibTableColumn
me1200MstpInterfaceStatusDesignatedRoot = _Me1200MstpInterfaceStatusDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 2, 1, 10),
    _Me1200MstpInterfaceStatusDesignatedRoot_Type()
)
me1200MstpInterfaceStatusDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatusDesignatedRoot.setStatus("current")
_Me1200MstpInterfaceStatusDesignatedCost_Type = Unsigned32
_Me1200MstpInterfaceStatusDesignatedCost_Object = MibTableColumn
me1200MstpInterfaceStatusDesignatedCost = _Me1200MstpInterfaceStatusDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 2, 1, 11),
    _Me1200MstpInterfaceStatusDesignatedCost_Type()
)
me1200MstpInterfaceStatusDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatusDesignatedCost.setStatus("current")


class _Me1200MstpInterfaceStatusDesignatedBridge_Type(OctetString):
    """Custom type me1200MstpInterfaceStatusDesignatedBridge based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_Me1200MstpInterfaceStatusDesignatedBridge_Type.__name__ = "OctetString"
_Me1200MstpInterfaceStatusDesignatedBridge_Object = MibTableColumn
me1200MstpInterfaceStatusDesignatedBridge = _Me1200MstpInterfaceStatusDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 2, 1, 12),
    _Me1200MstpInterfaceStatusDesignatedBridge_Type()
)
me1200MstpInterfaceStatusDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatusDesignatedBridge.setStatus("current")


class _Me1200MstpInterfaceStatusDesignatedPort_Type(OctetString):
    """Custom type me1200MstpInterfaceStatusDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixedLength = 2


_Me1200MstpInterfaceStatusDesignatedPort_Type.__name__ = "OctetString"
_Me1200MstpInterfaceStatusDesignatedPort_Object = MibTableColumn
me1200MstpInterfaceStatusDesignatedPort = _Me1200MstpInterfaceStatusDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 2, 1, 13),
    _Me1200MstpInterfaceStatusDesignatedPort_Type()
)
me1200MstpInterfaceStatusDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatusDesignatedPort.setStatus("current")
_Me1200MstpInterfaceStatusTcAck_Type = TruthValue
_Me1200MstpInterfaceStatusTcAck_Object = MibTableColumn
me1200MstpInterfaceStatusTcAck = _Me1200MstpInterfaceStatusTcAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 2, 1, 14),
    _Me1200MstpInterfaceStatusTcAck_Type()
)
me1200MstpInterfaceStatusTcAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatusTcAck.setStatus("current")
_Me1200MstpInterfaceStatusHelloTime_Type = Unsigned32
_Me1200MstpInterfaceStatusHelloTime_Object = MibTableColumn
me1200MstpInterfaceStatusHelloTime = _Me1200MstpInterfaceStatusHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 2, 1, 15),
    _Me1200MstpInterfaceStatusHelloTime_Type()
)
me1200MstpInterfaceStatusHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatusHelloTime.setStatus("current")
_Me1200MstpInterfaceStatusAdminEdgePort_Type = TruthValue
_Me1200MstpInterfaceStatusAdminEdgePort_Object = MibTableColumn
me1200MstpInterfaceStatusAdminEdgePort = _Me1200MstpInterfaceStatusAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 2, 1, 16),
    _Me1200MstpInterfaceStatusAdminEdgePort_Type()
)
me1200MstpInterfaceStatusAdminEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatusAdminEdgePort.setStatus("current")
_Me1200MstpInterfaceStatusOperEdgePort_Type = TruthValue
_Me1200MstpInterfaceStatusOperEdgePort_Object = MibTableColumn
me1200MstpInterfaceStatusOperEdgePort = _Me1200MstpInterfaceStatusOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 2, 1, 17),
    _Me1200MstpInterfaceStatusOperEdgePort_Type()
)
me1200MstpInterfaceStatusOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatusOperEdgePort.setStatus("current")
_Me1200MstpInterfaceStatusAutoEdgePort_Type = TruthValue
_Me1200MstpInterfaceStatusAutoEdgePort_Object = MibTableColumn
me1200MstpInterfaceStatusAutoEdgePort = _Me1200MstpInterfaceStatusAutoEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 2, 1, 18),
    _Me1200MstpInterfaceStatusAutoEdgePort_Type()
)
me1200MstpInterfaceStatusAutoEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatusAutoEdgePort.setStatus("current")
_Me1200MstpInterfaceStatusMacOperational_Type = TruthValue
_Me1200MstpInterfaceStatusMacOperational_Object = MibTableColumn
me1200MstpInterfaceStatusMacOperational = _Me1200MstpInterfaceStatusMacOperational_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 2, 1, 19),
    _Me1200MstpInterfaceStatusMacOperational_Type()
)
me1200MstpInterfaceStatusMacOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatusMacOperational.setStatus("current")
_Me1200MstpInterfaceStatusAdminPointToPointMAC_Type = ME1200Point2Point
_Me1200MstpInterfaceStatusAdminPointToPointMAC_Object = MibTableColumn
me1200MstpInterfaceStatusAdminPointToPointMAC = _Me1200MstpInterfaceStatusAdminPointToPointMAC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 2, 1, 20),
    _Me1200MstpInterfaceStatusAdminPointToPointMAC_Type()
)
me1200MstpInterfaceStatusAdminPointToPointMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatusAdminPointToPointMAC.setStatus("current")
_Me1200MstpInterfaceStatusOperPointToPointMAC_Type = TruthValue
_Me1200MstpInterfaceStatusOperPointToPointMAC_Object = MibTableColumn
me1200MstpInterfaceStatusOperPointToPointMAC = _Me1200MstpInterfaceStatusOperPointToPointMAC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 2, 1, 21),
    _Me1200MstpInterfaceStatusOperPointToPointMAC_Type()
)
me1200MstpInterfaceStatusOperPointToPointMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatusOperPointToPointMAC.setStatus("current")
_Me1200MstpInterfaceStatusRestrictedRole_Type = TruthValue
_Me1200MstpInterfaceStatusRestrictedRole_Object = MibTableColumn
me1200MstpInterfaceStatusRestrictedRole = _Me1200MstpInterfaceStatusRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 2, 1, 22),
    _Me1200MstpInterfaceStatusRestrictedRole_Type()
)
me1200MstpInterfaceStatusRestrictedRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatusRestrictedRole.setStatus("current")
_Me1200MstpInterfaceStatusRestrictedTcn_Type = TruthValue
_Me1200MstpInterfaceStatusRestrictedTcn_Object = MibTableColumn
me1200MstpInterfaceStatusRestrictedTcn = _Me1200MstpInterfaceStatusRestrictedTcn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 2, 1, 23),
    _Me1200MstpInterfaceStatusRestrictedTcn_Type()
)
me1200MstpInterfaceStatusRestrictedTcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatusRestrictedTcn.setStatus("current")


class _Me1200MstpInterfaceStatusPortRole_Type(ME1200DisplayString):
    """Custom type me1200MstpInterfaceStatusPortRole based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Me1200MstpInterfaceStatusPortRole_Type.__name__ = "ME1200DisplayString"
_Me1200MstpInterfaceStatusPortRole_Object = MibTableColumn
me1200MstpInterfaceStatusPortRole = _Me1200MstpInterfaceStatusPortRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 2, 1, 24),
    _Me1200MstpInterfaceStatusPortRole_Type()
)
me1200MstpInterfaceStatusPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatusPortRole.setStatus("current")
_Me1200MstpInterfaceStatusDisputed_Type = TruthValue
_Me1200MstpInterfaceStatusDisputed_Object = MibTableColumn
me1200MstpInterfaceStatusDisputed = _Me1200MstpInterfaceStatusDisputed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 2, 1, 25),
    _Me1200MstpInterfaceStatusDisputed_Type()
)
me1200MstpInterfaceStatusDisputed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatusDisputed.setStatus("current")
_Me1200MstpInterfaceStatisticsTable_Object = MibTable
me1200MstpInterfaceStatisticsTable = _Me1200MstpInterfaceStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 3)
)
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatisticsTable.setStatus("current")
_Me1200MstpInterfaceStatisticsEntry_Object = MibTableRow
me1200MstpInterfaceStatisticsEntry = _Me1200MstpInterfaceStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 3, 1)
)
me1200MstpInterfaceStatisticsEntry.setIndexNames(
    (0, "ME1200-MSTP-MIB", "me1200MstpInterfaceStatisticsInterfaceNo"),
)
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatisticsEntry.setStatus("current")
_Me1200MstpInterfaceStatisticsInterfaceNo_Type = ME1200InterfaceIndex
_Me1200MstpInterfaceStatisticsInterfaceNo_Object = MibTableColumn
me1200MstpInterfaceStatisticsInterfaceNo = _Me1200MstpInterfaceStatisticsInterfaceNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 3, 1, 1),
    _Me1200MstpInterfaceStatisticsInterfaceNo_Type()
)
me1200MstpInterfaceStatisticsInterfaceNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatisticsInterfaceNo.setStatus("current")
_Me1200MstpInterfaceStatisticsStpFrameXmits_Type = Unsigned32
_Me1200MstpInterfaceStatisticsStpFrameXmits_Object = MibTableColumn
me1200MstpInterfaceStatisticsStpFrameXmits = _Me1200MstpInterfaceStatisticsStpFrameXmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 3, 1, 2),
    _Me1200MstpInterfaceStatisticsStpFrameXmits_Type()
)
me1200MstpInterfaceStatisticsStpFrameXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatisticsStpFrameXmits.setStatus("current")
_Me1200MstpInterfaceStatisticsStpFrameReceived_Type = Unsigned32
_Me1200MstpInterfaceStatisticsStpFrameReceived_Object = MibTableColumn
me1200MstpInterfaceStatisticsStpFrameReceived = _Me1200MstpInterfaceStatisticsStpFrameReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 3, 1, 3),
    _Me1200MstpInterfaceStatisticsStpFrameReceived_Type()
)
me1200MstpInterfaceStatisticsStpFrameReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatisticsStpFrameReceived.setStatus("current")
_Me1200MstpInterfaceStatisticsRstpFrameXmits_Type = Unsigned32
_Me1200MstpInterfaceStatisticsRstpFrameXmits_Object = MibTableColumn
me1200MstpInterfaceStatisticsRstpFrameXmits = _Me1200MstpInterfaceStatisticsRstpFrameXmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 3, 1, 4),
    _Me1200MstpInterfaceStatisticsRstpFrameXmits_Type()
)
me1200MstpInterfaceStatisticsRstpFrameXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatisticsRstpFrameXmits.setStatus("current")
_Me1200MstpInterfaceStatisticsRstpFrameReceived_Type = Unsigned32
_Me1200MstpInterfaceStatisticsRstpFrameReceived_Object = MibTableColumn
me1200MstpInterfaceStatisticsRstpFrameReceived = _Me1200MstpInterfaceStatisticsRstpFrameReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 3, 1, 5),
    _Me1200MstpInterfaceStatisticsRstpFrameReceived_Type()
)
me1200MstpInterfaceStatisticsRstpFrameReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatisticsRstpFrameReceived.setStatus("current")
_Me1200MstpInterfaceStatisticsMstpFrameXmits_Type = Unsigned32
_Me1200MstpInterfaceStatisticsMstpFrameXmits_Object = MibTableColumn
me1200MstpInterfaceStatisticsMstpFrameXmits = _Me1200MstpInterfaceStatisticsMstpFrameXmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 3, 1, 6),
    _Me1200MstpInterfaceStatisticsMstpFrameXmits_Type()
)
me1200MstpInterfaceStatisticsMstpFrameXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatisticsMstpFrameXmits.setStatus("current")
_Me1200MstpInterfaceStatisticsMstpFrameReceived_Type = Unsigned32
_Me1200MstpInterfaceStatisticsMstpFrameReceived_Object = MibTableColumn
me1200MstpInterfaceStatisticsMstpFrameReceived = _Me1200MstpInterfaceStatisticsMstpFrameReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 3, 1, 7),
    _Me1200MstpInterfaceStatisticsMstpFrameReceived_Type()
)
me1200MstpInterfaceStatisticsMstpFrameReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatisticsMstpFrameReceived.setStatus("current")
_Me1200MstpInterfaceStatisticsUnknownFramesReceived_Type = Unsigned32
_Me1200MstpInterfaceStatisticsUnknownFramesReceived_Object = MibTableColumn
me1200MstpInterfaceStatisticsUnknownFramesReceived = _Me1200MstpInterfaceStatisticsUnknownFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 3, 1, 8),
    _Me1200MstpInterfaceStatisticsUnknownFramesReceived_Type()
)
me1200MstpInterfaceStatisticsUnknownFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatisticsUnknownFramesReceived.setStatus("current")
_Me1200MstpInterfaceStatisticsIllegalFrameReceived_Type = Unsigned32
_Me1200MstpInterfaceStatisticsIllegalFrameReceived_Object = MibTableColumn
me1200MstpInterfaceStatisticsIllegalFrameReceived = _Me1200MstpInterfaceStatisticsIllegalFrameReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 1, 3, 3, 1, 9),
    _Me1200MstpInterfaceStatisticsIllegalFrameReceived_Type()
)
me1200MstpInterfaceStatisticsIllegalFrameReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatisticsIllegalFrameReceived.setStatus("current")
_Me1200MstpMibConformance_ObjectIdentity = ObjectIdentity
me1200MstpMibConformance = _Me1200MstpMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 3)
)
_Me1200MstpMibCompliances_ObjectIdentity = ObjectIdentity
me1200MstpMibCompliances = _Me1200MstpMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 3, 1)
)
_Me1200MstpMibGroups_ObjectIdentity = ObjectIdentity
me1200MstpMibGroups = _Me1200MstpMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 3, 2)
)

# Managed Objects groups

me1200MstpBridgeParamsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 3, 2, 1)
)
me1200MstpBridgeParamsInfoGroup.setObjects(
      *(("ME1200-MSTP-MIB", "me1200MstpBridgeParamsBridgeMaxAge"),
        ("ME1200-MSTP-MIB", "me1200MstpBridgeParamsBridgeHelloTime"),
        ("ME1200-MSTP-MIB", "me1200MstpBridgeParamsBridgeForwardDelay"),
        ("ME1200-MSTP-MIB", "me1200MstpBridgeParamsForceVersion"),
        ("ME1200-MSTP-MIB", "me1200MstpBridgeParamsTxHoldCount"),
        ("ME1200-MSTP-MIB", "me1200MstpBridgeParamsMaxHops"),
        ("ME1200-MSTP-MIB", "me1200MstpBridgeParamsBpduFiltering"),
        ("ME1200-MSTP-MIB", "me1200MstpBridgeParamsBpduGuard"),
        ("ME1200-MSTP-MIB", "me1200MstpBridgeParamsErrorRecoveryDelay"))
)
if mibBuilder.loadTexts:
    me1200MstpBridgeParamsInfoGroup.setStatus("current")

me1200MstpMstiParamTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 3, 2, 2)
)
me1200MstpMstiParamTableInfoGroup.setObjects(
    ("ME1200-MSTP-MIB", "me1200MstpMstiParamPriority")
)
if mibBuilder.loadTexts:
    me1200MstpMstiParamTableInfoGroup.setStatus("current")

me1200MstpMstiConfigIdInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 3, 2, 3)
)
me1200MstpMstiConfigIdInfoGroup.setObjects(
      *(("ME1200-MSTP-MIB", "me1200MstpMstiConfigIdName"),
        ("ME1200-MSTP-MIB", "me1200MstpMstiConfigIdRevision"))
)
if mibBuilder.loadTexts:
    me1200MstpMstiConfigIdInfoGroup.setStatus("current")

me1200MstpMstiConfigTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 3, 2, 4)
)
me1200MstpMstiConfigTableInfoGroup.setObjects(
    ("ME1200-MSTP-MIB", "me1200MstpMstiConfigMstid")
)
if mibBuilder.loadTexts:
    me1200MstpMstiConfigTableInfoGroup.setStatus("current")

me1200MstpCistInterfaceParamTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 3, 2, 5)
)
me1200MstpCistInterfaceParamTableInfoGroup.setObjects(
      *(("ME1200-MSTP-MIB", "me1200MstpCistInterfaceParamEnable"),
        ("ME1200-MSTP-MIB", "me1200MstpCistInterfaceParamAdminEdgePort"),
        ("ME1200-MSTP-MIB", "me1200MstpCistInterfaceParamAdminAutoEdgePort"),
        ("ME1200-MSTP-MIB", "me1200MstpCistInterfaceParamAdminPointToPointMAC"),
        ("ME1200-MSTP-MIB", "me1200MstpCistInterfaceParamRestrictedRole"),
        ("ME1200-MSTP-MIB", "me1200MstpCistInterfaceParamRestrictedTcn"),
        ("ME1200-MSTP-MIB", "me1200MstpCistInterfaceParamBpduGuard"))
)
if mibBuilder.loadTexts:
    me1200MstpCistInterfaceParamTableInfoGroup.setStatus("current")

me1200MstpAggrParamsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 3, 2, 6)
)
me1200MstpAggrParamsInfoGroup.setObjects(
      *(("ME1200-MSTP-MIB", "me1200MstpAggrParamsEnable"),
        ("ME1200-MSTP-MIB", "me1200MstpAggrParamsAdminEdgePort"),
        ("ME1200-MSTP-MIB", "me1200MstpAggrParamsAdminAutoEdgePort"),
        ("ME1200-MSTP-MIB", "me1200MstpAggrParamsAdminPointToPointMAC"),
        ("ME1200-MSTP-MIB", "me1200MstpAggrParamsRestrictedRole"),
        ("ME1200-MSTP-MIB", "me1200MstpAggrParamsRestrictedTcn"),
        ("ME1200-MSTP-MIB", "me1200MstpAggrParamsBpduGuard"))
)
if mibBuilder.loadTexts:
    me1200MstpAggrParamsInfoGroup.setStatus("current")

me1200MstpMstiInterfaceParamTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 3, 2, 7)
)
me1200MstpMstiInterfaceParamTableInfoGroup.setObjects(
      *(("ME1200-MSTP-MIB", "me1200MstpMstiInterfaceParamAdminPathCost"),
        ("ME1200-MSTP-MIB", "me1200MstpMstiInterfaceParamAdminPortPriority"))
)
if mibBuilder.loadTexts:
    me1200MstpMstiInterfaceParamTableInfoGroup.setStatus("current")

me1200MstpMstiAggrParamTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 3, 2, 8)
)
me1200MstpMstiAggrParamTableInfoGroup.setObjects(
      *(("ME1200-MSTP-MIB", "me1200MstpMstiAggrParamAdminPathCost"),
        ("ME1200-MSTP-MIB", "me1200MstpMstiAggrParamAdminPortPriority"))
)
if mibBuilder.loadTexts:
    me1200MstpMstiAggrParamTableInfoGroup.setStatus("current")

me1200MstpBridgeStatusTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 3, 2, 9)
)
me1200MstpBridgeStatusTableInfoGroup.setObjects(
      *(("ME1200-MSTP-MIB", "me1200MstpBridgeStatusBridgeId"),
        ("ME1200-MSTP-MIB", "me1200MstpBridgeStatusTimeSinceTopologyChange"),
        ("ME1200-MSTP-MIB", "me1200MstpBridgeStatusTopologyChangeCount"),
        ("ME1200-MSTP-MIB", "me1200MstpBridgeStatusTopologyChange"),
        ("ME1200-MSTP-MIB", "me1200MstpBridgeStatusDesignatedRoot"),
        ("ME1200-MSTP-MIB", "me1200MstpBridgeStatusRootPathCost"),
        ("ME1200-MSTP-MIB", "me1200MstpBridgeStatusRootPort"),
        ("ME1200-MSTP-MIB", "me1200MstpBridgeStatusMaxAge"),
        ("ME1200-MSTP-MIB", "me1200MstpBridgeStatusForwardDelay"),
        ("ME1200-MSTP-MIB", "me1200MstpBridgeStatusBridgeMaxAge"),
        ("ME1200-MSTP-MIB", "me1200MstpBridgeStatusBridgeHelloTime"),
        ("ME1200-MSTP-MIB", "me1200MstpBridgeStatusBridgeForwardDelay"),
        ("ME1200-MSTP-MIB", "me1200MstpBridgeStatusTxHoldCount"),
        ("ME1200-MSTP-MIB", "me1200MstpBridgeStatusForceVersion"),
        ("ME1200-MSTP-MIB", "me1200MstpBridgeStatusCistRegionalRoot"),
        ("ME1200-MSTP-MIB", "me1200MstpBridgeStatusCistInternalPathCost"),
        ("ME1200-MSTP-MIB", "me1200MstpBridgeStatusMaxHops"))
)
if mibBuilder.loadTexts:
    me1200MstpBridgeStatusTableInfoGroup.setStatus("current")

me1200MstpInterfaceStatusTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 3, 2, 10)
)
me1200MstpInterfaceStatusTableInfoGroup.setObjects(
      *(("ME1200-MSTP-MIB", "me1200MstpInterfaceStatusEnabled"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatusActive"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatusParentPort"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatusUpTime"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatusPortState"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatusPortId"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatusPathCost"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatusDesignatedRoot"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatusDesignatedCost"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatusDesignatedBridge"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatusDesignatedPort"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatusTcAck"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatusHelloTime"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatusAdminEdgePort"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatusOperEdgePort"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatusAutoEdgePort"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatusMacOperational"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatusAdminPointToPointMAC"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatusOperPointToPointMAC"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatusRestrictedRole"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatusRestrictedTcn"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatusPortRole"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatusDisputed"))
)
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatusTableInfoGroup.setStatus("current")

me1200MstpInterfaceStatisticsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 3, 2, 11)
)
me1200MstpInterfaceStatisticsTableInfoGroup.setObjects(
      *(("ME1200-MSTP-MIB", "me1200MstpInterfaceStatisticsStpFrameXmits"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatisticsStpFrameReceived"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatisticsRstpFrameXmits"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatisticsRstpFrameReceived"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatisticsMstpFrameXmits"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatisticsMstpFrameReceived"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatisticsUnknownFramesReceived"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatisticsIllegalFrameReceived"))
)
if mibBuilder.loadTexts:
    me1200MstpInterfaceStatisticsTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200MstpMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 20, 3, 1, 1)
)
me1200MstpMibCompliance.setObjects(
      *(("ME1200-MSTP-MIB", "me1200MstpBridgeParamsInfoGroup"),
        ("ME1200-MSTP-MIB", "me1200MstpMstiParamTableInfoGroup"),
        ("ME1200-MSTP-MIB", "me1200MstpMstiConfigIdInfoGroup"),
        ("ME1200-MSTP-MIB", "me1200MstpMstiConfigTableInfoGroup"),
        ("ME1200-MSTP-MIB", "me1200MstpCistInterfaceParamTableInfoGroup"),
        ("ME1200-MSTP-MIB", "me1200MstpAggrParamsInfoGroup"),
        ("ME1200-MSTP-MIB", "me1200MstpMstiInterfaceParamTableInfoGroup"),
        ("ME1200-MSTP-MIB", "me1200MstpMstiAggrParamTableInfoGroup"),
        ("ME1200-MSTP-MIB", "me1200MstpBridgeStatusTableInfoGroup"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatusTableInfoGroup"),
        ("ME1200-MSTP-MIB", "me1200MstpInterfaceStatisticsTableInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200MstpMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-MSTP-MIB",
    **{"ME1200MSTPForceVersion": ME1200MSTPForceVersion,
       "ME1200Point2Point": ME1200Point2Point,
       "ME1200PortState": ME1200PortState,
       "me1200MstpMib": me1200MstpMib,
       "me1200Mstp": me1200Mstp,
       "me1200MstpConfig": me1200MstpConfig,
       "me1200MstpBridgeParams": me1200MstpBridgeParams,
       "me1200MstpBridgeParamsBridgeMaxAge": me1200MstpBridgeParamsBridgeMaxAge,
       "me1200MstpBridgeParamsBridgeHelloTime": me1200MstpBridgeParamsBridgeHelloTime,
       "me1200MstpBridgeParamsBridgeForwardDelay": me1200MstpBridgeParamsBridgeForwardDelay,
       "me1200MstpBridgeParamsForceVersion": me1200MstpBridgeParamsForceVersion,
       "me1200MstpBridgeParamsTxHoldCount": me1200MstpBridgeParamsTxHoldCount,
       "me1200MstpBridgeParamsMaxHops": me1200MstpBridgeParamsMaxHops,
       "me1200MstpBridgeParamsBpduFiltering": me1200MstpBridgeParamsBpduFiltering,
       "me1200MstpBridgeParamsBpduGuard": me1200MstpBridgeParamsBpduGuard,
       "me1200MstpBridgeParamsErrorRecoveryDelay": me1200MstpBridgeParamsErrorRecoveryDelay,
       "me1200MstpMstiParamTable": me1200MstpMstiParamTable,
       "me1200MstpMstiParamEntry": me1200MstpMstiParamEntry,
       "me1200MstpMstiParamInstance": me1200MstpMstiParamInstance,
       "me1200MstpMstiParamPriority": me1200MstpMstiParamPriority,
       "me1200MstpMstiConfig": me1200MstpMstiConfig,
       "me1200MstpMstiConfigId": me1200MstpMstiConfigId,
       "me1200MstpMstiConfigIdName": me1200MstpMstiConfigIdName,
       "me1200MstpMstiConfigIdRevision": me1200MstpMstiConfigIdRevision,
       "me1200MstpMstiConfigTable": me1200MstpMstiConfigTable,
       "me1200MstpMstiConfigEntry": me1200MstpMstiConfigEntry,
       "me1200MstpMstiConfigVid": me1200MstpMstiConfigVid,
       "me1200MstpMstiConfigMstid": me1200MstpMstiConfigMstid,
       "me1200MstpCistInterfaceParamTable": me1200MstpCistInterfaceParamTable,
       "me1200MstpCistInterfaceParamEntry": me1200MstpCistInterfaceParamEntry,
       "me1200MstpCistInterfaceParamInterfaceNo": me1200MstpCistInterfaceParamInterfaceNo,
       "me1200MstpCistInterfaceParamEnable": me1200MstpCistInterfaceParamEnable,
       "me1200MstpCistInterfaceParamAdminEdgePort": me1200MstpCistInterfaceParamAdminEdgePort,
       "me1200MstpCistInterfaceParamAdminAutoEdgePort": me1200MstpCistInterfaceParamAdminAutoEdgePort,
       "me1200MstpCistInterfaceParamAdminPointToPointMAC": me1200MstpCistInterfaceParamAdminPointToPointMAC,
       "me1200MstpCistInterfaceParamRestrictedRole": me1200MstpCistInterfaceParamRestrictedRole,
       "me1200MstpCistInterfaceParamRestrictedTcn": me1200MstpCistInterfaceParamRestrictedTcn,
       "me1200MstpCistInterfaceParamBpduGuard": me1200MstpCistInterfaceParamBpduGuard,
       "me1200MstpAggrParams": me1200MstpAggrParams,
       "me1200MstpAggrParamsEnable": me1200MstpAggrParamsEnable,
       "me1200MstpAggrParamsAdminEdgePort": me1200MstpAggrParamsAdminEdgePort,
       "me1200MstpAggrParamsAdminAutoEdgePort": me1200MstpAggrParamsAdminAutoEdgePort,
       "me1200MstpAggrParamsAdminPointToPointMAC": me1200MstpAggrParamsAdminPointToPointMAC,
       "me1200MstpAggrParamsRestrictedRole": me1200MstpAggrParamsRestrictedRole,
       "me1200MstpAggrParamsRestrictedTcn": me1200MstpAggrParamsRestrictedTcn,
       "me1200MstpAggrParamsBpduGuard": me1200MstpAggrParamsBpduGuard,
       "me1200MstpMstiInterfaceParamTable": me1200MstpMstiInterfaceParamTable,
       "me1200MstpMstiInterfaceParamEntry": me1200MstpMstiInterfaceParamEntry,
       "me1200MstpMstiInterfaceParamInterfaceNo": me1200MstpMstiInterfaceParamInterfaceNo,
       "me1200MstpMstiInterfaceParamInstance": me1200MstpMstiInterfaceParamInstance,
       "me1200MstpMstiInterfaceParamAdminPathCost": me1200MstpMstiInterfaceParamAdminPathCost,
       "me1200MstpMstiInterfaceParamAdminPortPriority": me1200MstpMstiInterfaceParamAdminPortPriority,
       "me1200MstpMstiAggrParamTable": me1200MstpMstiAggrParamTable,
       "me1200MstpMstiAggrParamEntry": me1200MstpMstiAggrParamEntry,
       "me1200MstpMstiAggrParamInstance": me1200MstpMstiAggrParamInstance,
       "me1200MstpMstiAggrParamAdminPathCost": me1200MstpMstiAggrParamAdminPathCost,
       "me1200MstpMstiAggrParamAdminPortPriority": me1200MstpMstiAggrParamAdminPortPriority,
       "me1200MstpStatus": me1200MstpStatus,
       "me1200MstpBridgeStatusTable": me1200MstpBridgeStatusTable,
       "me1200MstpBridgeStatusEntry": me1200MstpBridgeStatusEntry,
       "me1200MstpBridgeStatusInstance": me1200MstpBridgeStatusInstance,
       "me1200MstpBridgeStatusBridgeId": me1200MstpBridgeStatusBridgeId,
       "me1200MstpBridgeStatusTimeSinceTopologyChange": me1200MstpBridgeStatusTimeSinceTopologyChange,
       "me1200MstpBridgeStatusTopologyChangeCount": me1200MstpBridgeStatusTopologyChangeCount,
       "me1200MstpBridgeStatusTopologyChange": me1200MstpBridgeStatusTopologyChange,
       "me1200MstpBridgeStatusDesignatedRoot": me1200MstpBridgeStatusDesignatedRoot,
       "me1200MstpBridgeStatusRootPathCost": me1200MstpBridgeStatusRootPathCost,
       "me1200MstpBridgeStatusRootPort": me1200MstpBridgeStatusRootPort,
       "me1200MstpBridgeStatusMaxAge": me1200MstpBridgeStatusMaxAge,
       "me1200MstpBridgeStatusForwardDelay": me1200MstpBridgeStatusForwardDelay,
       "me1200MstpBridgeStatusBridgeMaxAge": me1200MstpBridgeStatusBridgeMaxAge,
       "me1200MstpBridgeStatusBridgeHelloTime": me1200MstpBridgeStatusBridgeHelloTime,
       "me1200MstpBridgeStatusBridgeForwardDelay": me1200MstpBridgeStatusBridgeForwardDelay,
       "me1200MstpBridgeStatusTxHoldCount": me1200MstpBridgeStatusTxHoldCount,
       "me1200MstpBridgeStatusForceVersion": me1200MstpBridgeStatusForceVersion,
       "me1200MstpBridgeStatusCistRegionalRoot": me1200MstpBridgeStatusCistRegionalRoot,
       "me1200MstpBridgeStatusCistInternalPathCost": me1200MstpBridgeStatusCistInternalPathCost,
       "me1200MstpBridgeStatusMaxHops": me1200MstpBridgeStatusMaxHops,
       "me1200MstpInterfaceStatusTable": me1200MstpInterfaceStatusTable,
       "me1200MstpInterfaceStatusEntry": me1200MstpInterfaceStatusEntry,
       "me1200MstpInterfaceStatusInterfaceNo": me1200MstpInterfaceStatusInterfaceNo,
       "me1200MstpInterfaceStatusInstance": me1200MstpInterfaceStatusInstance,
       "me1200MstpInterfaceStatusEnabled": me1200MstpInterfaceStatusEnabled,
       "me1200MstpInterfaceStatusActive": me1200MstpInterfaceStatusActive,
       "me1200MstpInterfaceStatusParentPort": me1200MstpInterfaceStatusParentPort,
       "me1200MstpInterfaceStatusUpTime": me1200MstpInterfaceStatusUpTime,
       "me1200MstpInterfaceStatusPortState": me1200MstpInterfaceStatusPortState,
       "me1200MstpInterfaceStatusPortId": me1200MstpInterfaceStatusPortId,
       "me1200MstpInterfaceStatusPathCost": me1200MstpInterfaceStatusPathCost,
       "me1200MstpInterfaceStatusDesignatedRoot": me1200MstpInterfaceStatusDesignatedRoot,
       "me1200MstpInterfaceStatusDesignatedCost": me1200MstpInterfaceStatusDesignatedCost,
       "me1200MstpInterfaceStatusDesignatedBridge": me1200MstpInterfaceStatusDesignatedBridge,
       "me1200MstpInterfaceStatusDesignatedPort": me1200MstpInterfaceStatusDesignatedPort,
       "me1200MstpInterfaceStatusTcAck": me1200MstpInterfaceStatusTcAck,
       "me1200MstpInterfaceStatusHelloTime": me1200MstpInterfaceStatusHelloTime,
       "me1200MstpInterfaceStatusAdminEdgePort": me1200MstpInterfaceStatusAdminEdgePort,
       "me1200MstpInterfaceStatusOperEdgePort": me1200MstpInterfaceStatusOperEdgePort,
       "me1200MstpInterfaceStatusAutoEdgePort": me1200MstpInterfaceStatusAutoEdgePort,
       "me1200MstpInterfaceStatusMacOperational": me1200MstpInterfaceStatusMacOperational,
       "me1200MstpInterfaceStatusAdminPointToPointMAC": me1200MstpInterfaceStatusAdminPointToPointMAC,
       "me1200MstpInterfaceStatusOperPointToPointMAC": me1200MstpInterfaceStatusOperPointToPointMAC,
       "me1200MstpInterfaceStatusRestrictedRole": me1200MstpInterfaceStatusRestrictedRole,
       "me1200MstpInterfaceStatusRestrictedTcn": me1200MstpInterfaceStatusRestrictedTcn,
       "me1200MstpInterfaceStatusPortRole": me1200MstpInterfaceStatusPortRole,
       "me1200MstpInterfaceStatusDisputed": me1200MstpInterfaceStatusDisputed,
       "me1200MstpInterfaceStatisticsTable": me1200MstpInterfaceStatisticsTable,
       "me1200MstpInterfaceStatisticsEntry": me1200MstpInterfaceStatisticsEntry,
       "me1200MstpInterfaceStatisticsInterfaceNo": me1200MstpInterfaceStatisticsInterfaceNo,
       "me1200MstpInterfaceStatisticsStpFrameXmits": me1200MstpInterfaceStatisticsStpFrameXmits,
       "me1200MstpInterfaceStatisticsStpFrameReceived": me1200MstpInterfaceStatisticsStpFrameReceived,
       "me1200MstpInterfaceStatisticsRstpFrameXmits": me1200MstpInterfaceStatisticsRstpFrameXmits,
       "me1200MstpInterfaceStatisticsRstpFrameReceived": me1200MstpInterfaceStatisticsRstpFrameReceived,
       "me1200MstpInterfaceStatisticsMstpFrameXmits": me1200MstpInterfaceStatisticsMstpFrameXmits,
       "me1200MstpInterfaceStatisticsMstpFrameReceived": me1200MstpInterfaceStatisticsMstpFrameReceived,
       "me1200MstpInterfaceStatisticsUnknownFramesReceived": me1200MstpInterfaceStatisticsUnknownFramesReceived,
       "me1200MstpInterfaceStatisticsIllegalFrameReceived": me1200MstpInterfaceStatisticsIllegalFrameReceived,
       "me1200MstpMibConformance": me1200MstpMibConformance,
       "me1200MstpMibCompliances": me1200MstpMibCompliances,
       "me1200MstpMibCompliance": me1200MstpMibCompliance,
       "me1200MstpMibGroups": me1200MstpMibGroups,
       "me1200MstpBridgeParamsInfoGroup": me1200MstpBridgeParamsInfoGroup,
       "me1200MstpMstiParamTableInfoGroup": me1200MstpMstiParamTableInfoGroup,
       "me1200MstpMstiConfigIdInfoGroup": me1200MstpMstiConfigIdInfoGroup,
       "me1200MstpMstiConfigTableInfoGroup": me1200MstpMstiConfigTableInfoGroup,
       "me1200MstpCistInterfaceParamTableInfoGroup": me1200MstpCistInterfaceParamTableInfoGroup,
       "me1200MstpAggrParamsInfoGroup": me1200MstpAggrParamsInfoGroup,
       "me1200MstpMstiInterfaceParamTableInfoGroup": me1200MstpMstiInterfaceParamTableInfoGroup,
       "me1200MstpMstiAggrParamTableInfoGroup": me1200MstpMstiAggrParamTableInfoGroup,
       "me1200MstpBridgeStatusTableInfoGroup": me1200MstpBridgeStatusTableInfoGroup,
       "me1200MstpInterfaceStatusTableInfoGroup": me1200MstpInterfaceStatusTableInfoGroup,
       "me1200MstpInterfaceStatisticsTableInfoGroup": me1200MstpInterfaceStatisticsTableInfoGroup}
)
