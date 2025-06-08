# SNMP MIB module (WWP-LEOS-SYSTEM-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/wwp_6141/WWP-LEOS-SYSTEM-CONTROL-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:32:50 2025
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

(dot1dStpPort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dStpPort")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpModules,
 wwpModulesLeos) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosSysCtrlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 25)
)
if mibBuilder.loadTexts:
    wwpLeosSysCtrlMIB.setRevisions(
        ("2013-04-23 00:00",
         "2006-03-15 18:55",
         "2001-04-03 17:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpLeosSysCtrlMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosSysCtrlMIBObjects = _WwpLeosSysCtrlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 25, 1)
)
_WwpLeosSysCtrl_ObjectIdentity = ObjectIdentity
wwpLeosSysCtrl = _WwpLeosSysCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 25, 1, 1)
)


class _WwpLeosSysCtrlBridgeRstpEnable_Type(TruthValue):
    """Custom type wwpLeosSysCtrlBridgeRstpEnable based on TruthValue"""
    defaultValue = 2


_WwpLeosSysCtrlBridgeRstpEnable_Type.__name__ = "TruthValue"
_WwpLeosSysCtrlBridgeRstpEnable_Object = MibScalar
wwpLeosSysCtrlBridgeRstpEnable = _WwpLeosSysCtrlBridgeRstpEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 25, 1, 1, 1),
    _WwpLeosSysCtrlBridgeRstpEnable_Type()
)
wwpLeosSysCtrlBridgeRstpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSysCtrlBridgeRstpEnable.setStatus("current")


class _WwpLeosSysCtrlLacpEnable_Type(TruthValue):
    """Custom type wwpLeosSysCtrlLacpEnable based on TruthValue"""
    defaultValue = 1


_WwpLeosSysCtrlLacpEnable_Type.__name__ = "TruthValue"
_WwpLeosSysCtrlLacpEnable_Object = MibScalar
wwpLeosSysCtrlLacpEnable = _WwpLeosSysCtrlLacpEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 25, 1, 1, 2),
    _WwpLeosSysCtrlLacpEnable_Type()
)
wwpLeosSysCtrlLacpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSysCtrlLacpEnable.setStatus("current")


class _WwpLeosSysCtrlLldpState_Type(Integer32):
    """Custom type wwpLeosSysCtrlLldpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_WwpLeosSysCtrlLldpState_Type.__name__ = "Integer32"
_WwpLeosSysCtrlLldpState_Object = MibScalar
wwpLeosSysCtrlLldpState = _WwpLeosSysCtrlLldpState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 25, 1, 1, 3),
    _WwpLeosSysCtrlLldpState_Type()
)
wwpLeosSysCtrlLldpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSysCtrlLldpState.setStatus("current")
_WwpLeosSysCtrlLldpExt_ObjectIdentity = ObjectIdentity
wwpLeosSysCtrlLldpExt = _WwpLeosSysCtrlLldpExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 25, 1, 2)
)
_WwpLeosSysCtrlLldpDaMac_Type = MacAddress
_WwpLeosSysCtrlLldpDaMac_Object = MibScalar
wwpLeosSysCtrlLldpDaMac = _WwpLeosSysCtrlLldpDaMac_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 25, 1, 2, 1),
    _WwpLeosSysCtrlLldpDaMac_Type()
)
wwpLeosSysCtrlLldpDaMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSysCtrlLldpDaMac.setStatus("current")


class _WwpLeosSysCtrlLldpEthType_Type(Integer32):
    """Custom type wwpLeosSysCtrlLldpEthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosSysCtrlLldpEthType_Type.__name__ = "Integer32"
_WwpLeosSysCtrlLldpEthType_Object = MibScalar
wwpLeosSysCtrlLldpEthType = _WwpLeosSysCtrlLldpEthType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 25, 1, 2, 2),
    _WwpLeosSysCtrlLldpEthType_Type()
)
wwpLeosSysCtrlLldpEthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSysCtrlLldpEthType.setStatus("current")
_WwpLeosSysCtrlMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosSysCtrlMIBNotificationPrefix = _WwpLeosSysCtrlMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 25, 2)
)
_WwpLeosSysCtrlMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosSysCtrlMIBNotifications = _WwpLeosSysCtrlMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 25, 2, 0)
)
_WwpLeosSysCtrlMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosSysCtrlMIBConformance = _WwpLeosSysCtrlMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 25, 3)
)
_WwpLeosSysCtrlMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosSysCtrlMIBCompliances = _WwpLeosSysCtrlMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 25, 3, 1)
)
_WwpLeosSysCtrlMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosSysCtrlMIBGroups = _WwpLeosSysCtrlMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 25, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-SYSTEM-CONTROL-MIB",
    **{"wwpLeosSysCtrlMIB": wwpLeosSysCtrlMIB,
       "wwpLeosSysCtrlMIBObjects": wwpLeosSysCtrlMIBObjects,
       "wwpLeosSysCtrl": wwpLeosSysCtrl,
       "wwpLeosSysCtrlBridgeRstpEnable": wwpLeosSysCtrlBridgeRstpEnable,
       "wwpLeosSysCtrlLacpEnable": wwpLeosSysCtrlLacpEnable,
       "wwpLeosSysCtrlLldpState": wwpLeosSysCtrlLldpState,
       "wwpLeosSysCtrlLldpExt": wwpLeosSysCtrlLldpExt,
       "wwpLeosSysCtrlLldpDaMac": wwpLeosSysCtrlLldpDaMac,
       "wwpLeosSysCtrlLldpEthType": wwpLeosSysCtrlLldpEthType,
       "wwpLeosSysCtrlMIBNotificationPrefix": wwpLeosSysCtrlMIBNotificationPrefix,
       "wwpLeosSysCtrlMIBNotifications": wwpLeosSysCtrlMIBNotifications,
       "wwpLeosSysCtrlMIBConformance": wwpLeosSysCtrlMIBConformance,
       "wwpLeosSysCtrlMIBCompliances": wwpLeosSysCtrlMIBCompliances,
       "wwpLeosSysCtrlMIBGroups": wwpLeosSysCtrlMIBGroups}
)
