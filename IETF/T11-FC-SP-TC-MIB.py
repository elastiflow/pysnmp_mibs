# SNMP MIB module (T11-FC-SP-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/T11-FC-SP-TC-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 13:42:56 2025
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

t11FcTcMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 175)
)
if mibBuilder.loadTexts:
    t11FcTcMIB.setRevisions(
        ("2008-08-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class T11FcSpPolicyHashFormat(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixedLength = 4



class T11FcSpPolicyHashValue(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class T11FcSpHashCalculationStatus(TextualConvention, Integer32):
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
        *(("calculate", 1),
          ("correct", 2),
          ("stale", 3))
    )



class T11FcSpAuthRejectReasonCode(TextualConvention, Integer32):
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
        *(("authFailure", 1),
          ("logicalError", 2),
          ("logicalBusy", 3),
          ("authILSNotSupported", 4),
          ("authELSNotSupported", 5),
          ("notLoggedIn", 6))
    )



class T11FcSpAuthRejReasonCodeExp(TextualConvention, Integer32):
    status = "current"
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("authMechanismNotUsable", 1),
          ("dhGroupNotUsable", 2),
          ("hashFunctionNotUsable", 3),
          ("authTransactionAlreadyStarted", 4),
          ("authenticationFailed", 5),
          ("incorrectPayload", 6),
          ("incorrectAuthProtocolMessage", 7),
          ("restartAuthProtocol", 8),
          ("authConcatNotSupported", 9),
          ("unsupportedProtocolVersion", 10),
          ("logicalBusy", 11),
          ("authILSNotSupported", 12),
          ("authELSNotSupported", 13),
          ("notLoggedIn", 14))
    )



class T11FcSpHashFunctions(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("md5", 0),
          ("sha1", 1))
    )


class T11FcSpSignFunctions(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        ("rsaSha1", 0)
    )


class T11FcSpDhGroups(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("null", 0),
          ("group1024", 1),
          ("group1280", 2),
          ("group1536", 3),
          ("group2048", 4),
          ("group3072", 5),
          ("group4096", 6),
          ("group6144", 7),
          ("group8192", 8))
    )


class T11FcSpPolicyObjectType(TextualConvention, Integer32):
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
        *(("summary", 1),
          ("switchMemberList", 2),
          ("nodeMemberList", 3),
          ("switchConnectivity", 4),
          ("ipMgmtList", 5),
          ("attribute", 6))
    )



class T11FcSpPolicyNameType(TextualConvention, Integer32):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("nodeName", 1),
          ("restrictedNodeName", 2),
          ("portName", 3),
          ("restrictedPortName", 4),
          ("wildcard", 5),
          ("restrictedWildcard", 6),
          ("alphaNumericName", 7),
          ("ipv6AddressRange", 8),
          ("ipv4AddressRange", 9))
    )



class T11FcSpPolicyName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



class T11FcSpAlphaNumName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



class T11FcSpAlphaNumNameOrAbsent(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class T11FcSaDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2))
    )



class T11FcSpiIndex(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class T11FcSpPrecedence(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class T11FcRoutingControl(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1



class T11FcSpType(TextualConvention, OctetString):
    status = "current"
    displayHint = "2x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixedLength = 2



class T11FcSpTransforms(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("encrNull", 0),
          ("encrAesCbc", 1),
          ("encrAesCtr", 2),
          ("encrAesGcm", 3),
          ("encr3Des", 4),
          ("prfHmacMd5", 5),
          ("prfHmacSha1", 6),
          ("prfAesCbc", 7),
          ("authHmacMd5L96", 8),
          ("authHmacSha1L96", 9),
          ("authHmacMd5L128", 10),
          ("authHmacSha1L160", 11),
          ("encrNullAuthAesGmac", 12),
          ("dhGroups1024bit", 13),
          ("dhGroups2048bit", 14))
    )


class T11FcSpSecurityProtocolId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("espHeader", 1),
          ("ctAuth", 2))
    )



class T11FcSpLifetimeLeft(TextualConvention, Unsigned32):
    status = "current"


class T11FcSpLifetimeLeftUnits(TextualConvention, Integer32):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("seconds", 1),
          ("kiloBytes", 2),
          ("megaBytes", 3),
          ("gigaBytes", 4),
          ("teraBytes", 5),
          ("petaBytes", 6),
          ("exaBytes", 7),
          ("zettaBytes", 8),
          ("yottaBytes", 9))
    )



# MIB Managed Objects in the order of their OIDs

_T11FcSpIdentities_ObjectIdentity = ObjectIdentity
t11FcSpIdentities = _T11FcSpIdentities_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1)
)
_T11FcSpAlgorithms_ObjectIdentity = ObjectIdentity
t11FcSpAlgorithms = _T11FcSpAlgorithms_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1, 1)
)
_T11FcSpEncryptAlgorithms_ObjectIdentity = ObjectIdentity
t11FcSpEncryptAlgorithms = _T11FcSpEncryptAlgorithms_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1, 1, 1)
)
_T11FcSpEncrNull_ObjectIdentity = ObjectIdentity
t11FcSpEncrNull = _T11FcSpEncrNull_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    t11FcSpEncrNull.setStatus("current")
_T11FcSpEncrAesCbc_ObjectIdentity = ObjectIdentity
t11FcSpEncrAesCbc = _T11FcSpEncrAesCbc_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    t11FcSpEncrAesCbc.setStatus("current")
_T11FcSpEncrAesCtr_ObjectIdentity = ObjectIdentity
t11FcSpEncrAesCtr = _T11FcSpEncrAesCtr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    t11FcSpEncrAesCtr.setStatus("current")
_T11FcSpEncrAesGcm_ObjectIdentity = ObjectIdentity
t11FcSpEncrAesGcm = _T11FcSpEncrAesGcm_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    t11FcSpEncrAesGcm.setStatus("current")
_T11FcSpEncr3Des_ObjectIdentity = ObjectIdentity
t11FcSpEncr3Des = _T11FcSpEncr3Des_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    t11FcSpEncr3Des.setStatus("current")
_T11FcSpEncrNullAuthAesGmac_ObjectIdentity = ObjectIdentity
t11FcSpEncrNullAuthAesGmac = _T11FcSpEncrNullAuthAesGmac_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    t11FcSpEncrNullAuthAesGmac.setStatus("current")
_T11FcSpAuthAlgorithms_ObjectIdentity = ObjectIdentity
t11FcSpAuthAlgorithms = _T11FcSpAuthAlgorithms_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1, 1, 2)
)
_T11FcSpAuthNull_ObjectIdentity = ObjectIdentity
t11FcSpAuthNull = _T11FcSpAuthNull_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    t11FcSpAuthNull.setStatus("current")
_T11FcSpAuthHmacMd5L96_ObjectIdentity = ObjectIdentity
t11FcSpAuthHmacMd5L96 = _T11FcSpAuthHmacMd5L96_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    t11FcSpAuthHmacMd5L96.setStatus("current")
_T11FcSpAuthHmacSha1L96_ObjectIdentity = ObjectIdentity
t11FcSpAuthHmacSha1L96 = _T11FcSpAuthHmacSha1L96_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    t11FcSpAuthHmacSha1L96.setStatus("current")
_T11FcSpAuthHmacMd5L128_ObjectIdentity = ObjectIdentity
t11FcSpAuthHmacMd5L128 = _T11FcSpAuthHmacMd5L128_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    t11FcSpAuthHmacMd5L128.setStatus("current")
_T11FcSpAuthHmacSha1L160_ObjectIdentity = ObjectIdentity
t11FcSpAuthHmacSha1L160 = _T11FcSpAuthHmacSha1L160_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    t11FcSpAuthHmacSha1L160.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "T11-FC-SP-TC-MIB",
    **{"T11FcSpPolicyHashFormat": T11FcSpPolicyHashFormat,
       "T11FcSpPolicyHashValue": T11FcSpPolicyHashValue,
       "T11FcSpHashCalculationStatus": T11FcSpHashCalculationStatus,
       "T11FcSpAuthRejectReasonCode": T11FcSpAuthRejectReasonCode,
       "T11FcSpAuthRejReasonCodeExp": T11FcSpAuthRejReasonCodeExp,
       "T11FcSpHashFunctions": T11FcSpHashFunctions,
       "T11FcSpSignFunctions": T11FcSpSignFunctions,
       "T11FcSpDhGroups": T11FcSpDhGroups,
       "T11FcSpPolicyObjectType": T11FcSpPolicyObjectType,
       "T11FcSpPolicyNameType": T11FcSpPolicyNameType,
       "T11FcSpPolicyName": T11FcSpPolicyName,
       "T11FcSpAlphaNumName": T11FcSpAlphaNumName,
       "T11FcSpAlphaNumNameOrAbsent": T11FcSpAlphaNumNameOrAbsent,
       "T11FcSaDirection": T11FcSaDirection,
       "T11FcSpiIndex": T11FcSpiIndex,
       "T11FcSpPrecedence": T11FcSpPrecedence,
       "T11FcRoutingControl": T11FcRoutingControl,
       "T11FcSpType": T11FcSpType,
       "T11FcSpTransforms": T11FcSpTransforms,
       "T11FcSpSecurityProtocolId": T11FcSpSecurityProtocolId,
       "T11FcSpLifetimeLeft": T11FcSpLifetimeLeft,
       "T11FcSpLifetimeLeftUnits": T11FcSpLifetimeLeftUnits,
       "t11FcTcMIB": t11FcTcMIB,
       "t11FcSpIdentities": t11FcSpIdentities,
       "t11FcSpAlgorithms": t11FcSpAlgorithms,
       "t11FcSpEncryptAlgorithms": t11FcSpEncryptAlgorithms,
       "t11FcSpEncrNull": t11FcSpEncrNull,
       "t11FcSpEncrAesCbc": t11FcSpEncrAesCbc,
       "t11FcSpEncrAesCtr": t11FcSpEncrAesCtr,
       "t11FcSpEncrAesGcm": t11FcSpEncrAesGcm,
       "t11FcSpEncr3Des": t11FcSpEncr3Des,
       "t11FcSpEncrNullAuthAesGmac": t11FcSpEncrNullAuthAesGmac,
       "t11FcSpAuthAlgorithms": t11FcSpAuthAlgorithms,
       "t11FcSpAuthNull": t11FcSpAuthNull,
       "t11FcSpAuthHmacMd5L96": t11FcSpAuthHmacMd5L96,
       "t11FcSpAuthHmacSha1L96": t11FcSpAuthHmacSha1L96,
       "t11FcSpAuthHmacMd5L128": t11FcSpAuthHmacMd5L128,
       "t11FcSpAuthHmacSha1L160": t11FcSpAuthHmacSha1L160}
)
