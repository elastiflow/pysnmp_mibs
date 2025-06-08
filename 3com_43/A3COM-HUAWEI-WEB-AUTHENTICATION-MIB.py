# SNMP MIB module (A3COM-HUAWEI-WEB-AUTHENTICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/3com_43/A3COM-HUAWEI-WEB-AUTHENTICATION-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:00:33 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

(ifDescr,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

h3cWebAuthentication = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 93)
)
if mibBuilder.loadTexts:
    h3cWebAuthentication.setRevisions(
        ("2008-06-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cWaTrapObjects_ObjectIdentity = ObjectIdentity
h3cWaTrapObjects = _H3cWaTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 93, 1)
)
_H3cWaVlanID_Type = Integer32
_H3cWaVlanID_Object = MibScalar
h3cWaVlanID = _H3cWaVlanID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 93, 1, 1),
    _H3cWaVlanID_Type()
)
h3cWaVlanID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cWaVlanID.setStatus("current")


class _H3cWaReasonCode_Type(Integer32):
    """Custom type h3cWaReasonCode based on Integer32"""
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
        *(("globalNumberMax", 1),
          ("configNumberMax", 2),
          ("portNumberMax", 3),
          ("invalidUsername", 4),
          ("authFail", 5),
          ("setACLFail", 6),
          ("changeVlanFail", 7),
          ("other", 8),
          ("onlineOverTime", 9),
          ("noTransferData", 10),
          ("cutOperation", 11),
          ("portDisabled", 12),
          ("portDown", 13),
          ("userLogout", 14),
          ("vlanChanged", 15),
          ("vlanDelted", 16))
    )


_H3cWaReasonCode_Type.__name__ = "Integer32"
_H3cWaReasonCode_Object = MibScalar
h3cWaReasonCode = _H3cWaReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 93, 1, 2),
    _H3cWaReasonCode_Type()
)
h3cWaReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cWaReasonCode.setStatus("current")


class _H3cWaActionCode_Type(Integer32):
    """Custom type h3cWaActionCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_H3cWaActionCode_Type.__name__ = "Integer32"
_H3cWaActionCode_Object = MibScalar
h3cWaActionCode = _H3cWaActionCode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 93, 1, 3),
    _H3cWaActionCode_Type()
)
h3cWaActionCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cWaActionCode.setStatus("current")
_H3cWaClientMacAddr_Type = MacAddress
_H3cWaClientMacAddr_Object = MibScalar
h3cWaClientMacAddr = _H3cWaClientMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 93, 1, 4),
    _H3cWaClientMacAddr_Type()
)
h3cWaClientMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cWaClientMacAddr.setStatus("current")
_H3cWaTrap_ObjectIdentity = ObjectIdentity
h3cWaTrap = _H3cWaTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 93, 2)
)
_H3cWaTrapPrefix_ObjectIdentity = ObjectIdentity
h3cWaTrapPrefix = _H3cWaTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 93, 2, 0)
)

# Managed Objects groups


# Notification objects

h3cWaClientLogon = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 93, 2, 0, 1)
)
h3cWaClientLogon.setObjects(
      *(("A3COM-HUAWEI-WEB-AUTHENTICATION-MIB", "h3cWaClientMacAddr"),
        ("IF-MIB", "ifDescr"),
        ("A3COM-HUAWEI-WEB-AUTHENTICATION-MIB", "h3cWaVlanID"))
)
if mibBuilder.loadTexts:
    h3cWaClientLogon.setStatus(
        "current"
    )

h3cWaClientLogonFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 93, 2, 0, 2)
)
h3cWaClientLogonFail.setObjects(
      *(("A3COM-HUAWEI-WEB-AUTHENTICATION-MIB", "h3cWaClientMacAddr"),
        ("IF-MIB", "ifDescr"),
        ("A3COM-HUAWEI-WEB-AUTHENTICATION-MIB", "h3cWaVlanID"),
        ("A3COM-HUAWEI-WEB-AUTHENTICATION-MIB", "h3cWaReasonCode"))
)
if mibBuilder.loadTexts:
    h3cWaClientLogonFail.setStatus(
        "current"
    )

h3cWaClientLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 93, 2, 0, 3)
)
h3cWaClientLogout.setObjects(
      *(("A3COM-HUAWEI-WEB-AUTHENTICATION-MIB", "h3cWaClientMacAddr"),
        ("IF-MIB", "ifDescr"),
        ("A3COM-HUAWEI-WEB-AUTHENTICATION-MIB", "h3cWaVlanID"),
        ("A3COM-HUAWEI-WEB-AUTHENTICATION-MIB", "h3cWaReasonCode"))
)
if mibBuilder.loadTexts:
    h3cWaClientLogout.setStatus(
        "current"
    )

h3cWaSysAction = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 93, 2, 0, 4)
)
h3cWaSysAction.setObjects(
    ("A3COM-HUAWEI-WEB-AUTHENTICATION-MIB", "h3cWaActionCode")
)
if mibBuilder.loadTexts:
    h3cWaSysAction.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-WEB-AUTHENTICATION-MIB",
    **{"h3cWebAuthentication": h3cWebAuthentication,
       "h3cWaTrapObjects": h3cWaTrapObjects,
       "h3cWaVlanID": h3cWaVlanID,
       "h3cWaReasonCode": h3cWaReasonCode,
       "h3cWaActionCode": h3cWaActionCode,
       "h3cWaClientMacAddr": h3cWaClientMacAddr,
       "h3cWaTrap": h3cWaTrap,
       "h3cWaTrapPrefix": h3cWaTrapPrefix,
       "h3cWaClientLogon": h3cWaClientLogon,
       "h3cWaClientLogonFail": h3cWaClientLogonFail,
       "h3cWaClientLogout": h3cWaClientLogout,
       "h3cWaSysAction": h3cWaSysAction}
)
