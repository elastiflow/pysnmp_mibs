# SNMP MIB module (TROPIC-EXPRSCALARS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-EXPRSCALARS.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:04:18 2025
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

(tnExprScalarsMIB,
 tropicExprModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnExprScalarsMIB",
    "tropicExprModules")

(AluWdmEnabledDisabled,) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "AluWdmEnabledDisabled")


# MODULE-IDENTITY

tnExprScalarsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 5, 3)
)
if mibBuilder.loadTexts:
    tnExprScalarsMibModule.setRevisions(
        ("2009-02-27 12:00",
         "2009-03-03 12:00",
         "2009-06-11 12:00",
         "2009-07-22 12:00",
         "2010-06-22 12:00",
         "2011-08-12 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnExprScalarsConf_ObjectIdentity = ObjectIdentity
tnExprScalarsConf = _TnExprScalarsConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 1)
)
_TnExprScalarsGroups_ObjectIdentity = ObjectIdentity
tnExprScalarsGroups = _TnExprScalarsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 1, 1)
)
_TnExprScalarsCompliances_ObjectIdentity = ObjectIdentity
tnExprScalarsCompliances = _TnExprScalarsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 1, 2)
)
_TnExprScalarsObjs_ObjectIdentity = ObjectIdentity
tnExprScalarsObjs = _TnExprScalarsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 2)
)
_TnExprSysBasics_ObjectIdentity = ObjectIdentity
tnExprSysBasics = _TnExprSysBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 2, 1)
)


class _TnSysLastRequestWebCliSourceIP_Type(SnmpAdminString):
    """Custom type tnSysLastRequestWebCliSourceIP based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnSysLastRequestWebCliSourceIP_Type.__name__ = "SnmpAdminString"
_TnSysLastRequestWebCliSourceIP_Object = MibScalar
tnSysLastRequestWebCliSourceIP = _TnSysLastRequestWebCliSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 2, 1, 1),
    _TnSysLastRequestWebCliSourceIP_Type()
)
tnSysLastRequestWebCliSourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysLastRequestWebCliSourceIP.setStatus("current")
_TnExprSysFeatures_ObjectIdentity = ObjectIdentity
tnExprSysFeatures = _TnExprSysFeatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 2, 2)
)
_TnExprContinuityTest_ObjectIdentity = ObjectIdentity
tnExprContinuityTest = _TnExprContinuityTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 2, 3)
)
_TnContinuityTestEnabled_Type = TruthValue
_TnContinuityTestEnabled_Object = MibScalar
tnContinuityTestEnabled = _TnContinuityTestEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 2, 3, 1),
    _TnContinuityTestEnabled_Type()
)
tnContinuityTestEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnContinuityTestEnabled.setStatus("current")
_TnContinuityTestSource_Type = Integer32
_TnContinuityTestSource_Object = MibScalar
tnContinuityTestSource = _TnContinuityTestSource_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 2, 3, 2),
    _TnContinuityTestSource_Type()
)
tnContinuityTestSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnContinuityTestSource.setStatus("current")
_TnContinuityTestDestination_Type = Integer32
_TnContinuityTestDestination_Object = MibScalar
tnContinuityTestDestination = _TnContinuityTestDestination_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 2, 3, 3),
    _TnContinuityTestDestination_Type()
)
tnContinuityTestDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnContinuityTestDestination.setStatus("current")
_TnContinuityTestTransponderPort_Type = Integer32
_TnContinuityTestTransponderPort_Object = MibScalar
tnContinuityTestTransponderPort = _TnContinuityTestTransponderPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 2, 3, 4),
    _TnContinuityTestTransponderPort_Type()
)
tnContinuityTestTransponderPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnContinuityTestTransponderPort.setStatus("current")
_TnContinuityTestTargetPower_Type = Integer32
_TnContinuityTestTargetPower_Object = MibScalar
tnContinuityTestTargetPower = _TnContinuityTestTargetPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 2, 3, 5),
    _TnContinuityTestTargetPower_Type()
)
tnContinuityTestTargetPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnContinuityTestTargetPower.setStatus("current")
if mibBuilder.loadTexts:
    tnContinuityTestTargetPower.setUnits("mBm")
_TnContinuityTestIngressPower_Type = Integer32
_TnContinuityTestIngressPower_Object = MibScalar
tnContinuityTestIngressPower = _TnContinuityTestIngressPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 2, 3, 6),
    _TnContinuityTestIngressPower_Type()
)
tnContinuityTestIngressPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnContinuityTestIngressPower.setStatus("current")
if mibBuilder.loadTexts:
    tnContinuityTestIngressPower.setUnits("mBm")
_TnContinuityTestEgressPower_Type = Integer32
_TnContinuityTestEgressPower_Object = MibScalar
tnContinuityTestEgressPower = _TnContinuityTestEgressPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 2, 3, 7),
    _TnContinuityTestEgressPower_Type()
)
tnContinuityTestEgressPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnContinuityTestEgressPower.setStatus("current")
if mibBuilder.loadTexts:
    tnContinuityTestEgressPower.setUnits("mBm")
_TnExprSysRadiusServers_ObjectIdentity = ObjectIdentity
tnExprSysRadiusServers = _TnExprSysRadiusServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 2, 4)
)
_TnSysRadiusServerTable_Object = MibTable
tnSysRadiusServerTable = _TnSysRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 2, 4, 1)
)
if mibBuilder.loadTexts:
    tnSysRadiusServerTable.setStatus("current")
_TnSysRadiusServerEntry_Object = MibTableRow
tnSysRadiusServerEntry = _TnSysRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 2, 4, 1, 1)
)
tnSysRadiusServerEntry.setIndexNames(
    (0, "TROPIC-EXPRSCALARS", "tnSysRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    tnSysRadiusServerEntry.setStatus("current")
_TnSysRadiusServerIndex_Type = Unsigned32
_TnSysRadiusServerIndex_Object = MibTableColumn
tnSysRadiusServerIndex = _TnSysRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 2, 4, 1, 1, 1),
    _TnSysRadiusServerIndex_Type()
)
tnSysRadiusServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSysRadiusServerIndex.setStatus("current")
_TnSysRadiusServerIpAddress_Type = IpAddress
_TnSysRadiusServerIpAddress_Object = MibTableColumn
tnSysRadiusServerIpAddress = _TnSysRadiusServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 2, 4, 1, 1, 2),
    _TnSysRadiusServerIpAddress_Type()
)
tnSysRadiusServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysRadiusServerIpAddress.setStatus("current")
_TnSysRadiusServerIpPort_Type = Unsigned32
_TnSysRadiusServerIpPort_Object = MibTableColumn
tnSysRadiusServerIpPort = _TnSysRadiusServerIpPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 2, 4, 1, 1, 3),
    _TnSysRadiusServerIpPort_Type()
)
tnSysRadiusServerIpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysRadiusServerIpPort.setStatus("current")


class _TnSysRadiusServerSharedSecret_Type(SnmpAdminString):
    """Custom type tnSysRadiusServerSharedSecret based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysRadiusServerSharedSecret_Type.__name__ = "SnmpAdminString"
_TnSysRadiusServerSharedSecret_Object = MibTableColumn
tnSysRadiusServerSharedSecret = _TnSysRadiusServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 2, 4, 1, 1, 4),
    _TnSysRadiusServerSharedSecret_Type()
)
tnSysRadiusServerSharedSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysRadiusServerSharedSecret.setStatus("current")
_TnSysRadiusServerStatus_Type = AluWdmEnabledDisabled
_TnSysRadiusServerStatus_Object = MibTableColumn
tnSysRadiusServerStatus = _TnSysRadiusServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 2, 4, 1, 1, 5),
    _TnSysRadiusServerStatus_Type()
)
tnSysRadiusServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysRadiusServerStatus.setStatus("current")
_TnSysRadiusServerRowStatus_Type = RowStatus
_TnSysRadiusServerRowStatus_Object = MibTableColumn
tnSysRadiusServerRowStatus = _TnSysRadiusServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 2, 4, 1, 1, 6),
    _TnSysRadiusServerRowStatus_Type()
)
tnSysRadiusServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSysRadiusServerRowStatus.setStatus("current")
_TnExprSysRadius_ObjectIdentity = ObjectIdentity
tnExprSysRadius = _TnExprSysRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 2, 5)
)
_TnSysRadiusTimeout_Type = Unsigned32
_TnSysRadiusTimeout_Object = MibScalar
tnSysRadiusTimeout = _TnSysRadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 2, 5, 1),
    _TnSysRadiusTimeout_Type()
)
tnSysRadiusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysRadiusTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tnSysRadiusTimeout.setUnits("seconds")
_TnSysRadiusRetries_Type = Unsigned32
_TnSysRadiusRetries_Object = MibScalar
tnSysRadiusRetries = _TnSysRadiusRetries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 2, 5, 2),
    _TnSysRadiusRetries_Type()
)
tnSysRadiusRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysRadiusRetries.setStatus("current")


class _TnSysAuthenOrder_Type(Integer32):
    """Custom type tnSysAuthenOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("radius", 2),
          ("radiusThenLocal", 3))
    )


_TnSysAuthenOrder_Type.__name__ = "Integer32"
_TnSysAuthenOrder_Object = MibScalar
tnSysAuthenOrder = _TnSysAuthenOrder_Object(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 2, 5, 3),
    _TnSysAuthenOrder_Type()
)
tnSysAuthenOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSysAuthenOrder.setStatus("current")

# Managed Objects groups

tnExprSysBasicsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 1, 1, 1)
)
tnExprSysBasicsGroup.setObjects(
    ("TROPIC-EXPRSCALARS", "tnSysLastRequestWebCliSourceIP")
)
if mibBuilder.loadTexts:
    tnExprSysBasicsGroup.setStatus("current")

tnExprContinuityTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 1, 1, 3)
)
tnExprContinuityTestGroup.setObjects(
      *(("TROPIC-EXPRSCALARS", "tnContinuityTestEnabled"),
        ("TROPIC-EXPRSCALARS", "tnContinuityTestSource"),
        ("TROPIC-EXPRSCALARS", "tnContinuityTestDestination"),
        ("TROPIC-EXPRSCALARS", "tnContinuityTestTransponderPort"),
        ("TROPIC-EXPRSCALARS", "tnContinuityTestTargetPower"),
        ("TROPIC-EXPRSCALARS", "tnContinuityTestIngressPower"),
        ("TROPIC-EXPRSCALARS", "tnContinuityTestEgressPower"))
)
if mibBuilder.loadTexts:
    tnExprContinuityTestGroup.setStatus("current")

tnExprSysRadiusServersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 1, 1, 4)
)
tnExprSysRadiusServersGroup.setObjects(
      *(("TROPIC-EXPRSCALARS", "tnSysRadiusServerIpAddress"),
        ("TROPIC-EXPRSCALARS", "tnSysRadiusServerIpPort"),
        ("TROPIC-EXPRSCALARS", "tnSysRadiusServerSharedSecret"),
        ("TROPIC-EXPRSCALARS", "tnSysRadiusServerStatus"),
        ("TROPIC-EXPRSCALARS", "tnSysRadiusServerRowStatus"))
)
if mibBuilder.loadTexts:
    tnExprSysRadiusServersGroup.setStatus("current")

tnExprSysRadiusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 1, 1, 5)
)
tnExprSysRadiusGroup.setObjects(
      *(("TROPIC-EXPRSCALARS", "tnSysRadiusTimeout"),
        ("TROPIC-EXPRSCALARS", "tnSysRadiusRetries"),
        ("TROPIC-EXPRSCALARS", "tnSysAuthenOrder"))
)
if mibBuilder.loadTexts:
    tnExprSysRadiusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnExprScalarsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 4, 3, 1, 2, 1)
)
tnExprScalarsCompliance.setObjects(
      *(("TROPIC-EXPRSCALARS", "tnExprSysBasicsGroup"),
        ("TROPIC-EXPRSCALARS", "tnExprContinuityTestGroup"),
        ("TROPIC-EXPRSCALARS", "tnExprSysRadiusServersGroup"),
        ("TROPIC-EXPRSCALARS", "tnExprSysRadiusGroup"))
)
if mibBuilder.loadTexts:
    tnExprScalarsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-EXPRSCALARS",
    **{"tnExprScalarsMibModule": tnExprScalarsMibModule,
       "tnExprScalarsConf": tnExprScalarsConf,
       "tnExprScalarsGroups": tnExprScalarsGroups,
       "tnExprSysBasicsGroup": tnExprSysBasicsGroup,
       "tnExprContinuityTestGroup": tnExprContinuityTestGroup,
       "tnExprSysRadiusServersGroup": tnExprSysRadiusServersGroup,
       "tnExprSysRadiusGroup": tnExprSysRadiusGroup,
       "tnExprScalarsCompliances": tnExprScalarsCompliances,
       "tnExprScalarsCompliance": tnExprScalarsCompliance,
       "tnExprScalarsObjs": tnExprScalarsObjs,
       "tnExprSysBasics": tnExprSysBasics,
       "tnSysLastRequestWebCliSourceIP": tnSysLastRequestWebCliSourceIP,
       "tnExprSysFeatures": tnExprSysFeatures,
       "tnExprContinuityTest": tnExprContinuityTest,
       "tnContinuityTestEnabled": tnContinuityTestEnabled,
       "tnContinuityTestSource": tnContinuityTestSource,
       "tnContinuityTestDestination": tnContinuityTestDestination,
       "tnContinuityTestTransponderPort": tnContinuityTestTransponderPort,
       "tnContinuityTestTargetPower": tnContinuityTestTargetPower,
       "tnContinuityTestIngressPower": tnContinuityTestIngressPower,
       "tnContinuityTestEgressPower": tnContinuityTestEgressPower,
       "tnExprSysRadiusServers": tnExprSysRadiusServers,
       "tnSysRadiusServerTable": tnSysRadiusServerTable,
       "tnSysRadiusServerEntry": tnSysRadiusServerEntry,
       "tnSysRadiusServerIndex": tnSysRadiusServerIndex,
       "tnSysRadiusServerIpAddress": tnSysRadiusServerIpAddress,
       "tnSysRadiusServerIpPort": tnSysRadiusServerIpPort,
       "tnSysRadiusServerSharedSecret": tnSysRadiusServerSharedSecret,
       "tnSysRadiusServerStatus": tnSysRadiusServerStatus,
       "tnSysRadiusServerRowStatus": tnSysRadiusServerRowStatus,
       "tnExprSysRadius": tnExprSysRadius,
       "tnSysRadiusTimeout": tnSysRadiusTimeout,
       "tnSysRadiusRetries": tnSysRadiusRetries,
       "tnSysAuthenOrder": tnSysAuthenOrder}
)
