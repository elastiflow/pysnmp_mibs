# SNMP MIB module (CISCO-IPSEC-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-IPSEC-TC.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:31:29 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoIPsecTc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 422)
)
if mibBuilder.loadTexts:
    ciscoIPsecTc.setRevisions(
        ("2004-07-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CCryptoMD5Hash(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixedLength = 16



class CIKEIsakmpDoi(TextualConvention, Integer32):
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
        *(("isakmpDoiUnknown", 1),
          ("isakmpDoiOther", 2),
          ("isakmpDoiIPsec", 3),
          ("isakmpDoiFcsp", 4),
          ("isakmpDoiCps", 5),
          ("isakmpDoiFcCtAuth", 6))
    )



class CIKELifetime(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )



class CIKELifesize(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2560, 4294967295),
    )



class CIPsecEncryptionKeySize(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class CIPsecControlProtocol(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("cpUnknown", 1),
          ("cpAll", 2),
          ("cpOther", 3),
          ("cpManual", 4),
          ("cpIkev1", 5),
          ("cpIkev2", 6),
          ("cpKink", 7),
          ("cpPhoturis", 8))
    )



class CIPsecProtocol(TextualConvention, Integer32):
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
        *(("ipsecProtUnknown", 1),
          ("ipsecProtAh", 2),
          ("ipsecProtEsp", 3),
          ("ipsecProtIPcomp", 4))
    )



class CIPsecPhase1PeerIdentityType(TextualConvention, Integer32):
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("idOther", 1),
          ("idIpv4Addr", 2),
          ("idFqdn", 3),
          ("idDn", 4),
          ("idIpv6Addr", 5),
          ("idUserFqdn", 6),
          ("idIpv4AddrSubnet", 7),
          ("idIpv6AddrSubnet", 8),
          ("idIpv4AddrRange", 9),
          ("idIpv6AddrRange", 10),
          ("idDerAsn1Gn", 11),
          ("idKeyId", 12),
          ("idWwn", 13))
    )



class CIPsecIkeNegoMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mainMode", 1),
          ("aggressiveMode", 2))
    )



class CIPsecIkeHashAlgorithm(TextualConvention, Integer32):
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
        *(("none", 1),
          ("other", 2),
          ("md5", 3),
          ("sha", 4),
          ("tiger", 5),
          ("sha256", 6),
          ("sha384", 7),
          ("sha512", 8),
          ("aesMac", 9))
    )



class CIPsecIkeAuthMethod(TextualConvention, Integer32):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("preSharedKey", 2),
          ("rsaSignature", 3),
          ("rsaEncryption", 4),
          ("revRsaEncryption", 5),
          ("dssSignature", 6),
          ("elGamalEncryption", 7),
          ("revElGamalEncryption", 8),
          ("ecsdaSignature", 9),
          ("gssApiV1", 10),
          ("gssApiV2", 11))
    )



class CIPsecDiffHellmanGrp(TextualConvention, Integer32):
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("notDH", 2),
          ("modp768", 3),
          ("modp1024", 4),
          ("ec2nGP155", 5),
          ("ec2nGP185", 6),
          ("modp1536", 7),
          ("ec2nGF163", 8),
          ("ec2nGF283", 9),
          ("ec2nGF409", 10),
          ("ec2nGF571", 11),
          ("modp2048", 12))
    )



class CIPsecEncapMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("encapTunnel", 1),
          ("encapTransport", 2))
    )



class CIPsecTransform(TextualConvention, Integer32):
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
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("xformNONE", 1),
          ("xformOTHER", 2),
          ("xformAhRFC1829", 3),
          ("xformAhMD5", 4),
          ("xformAhSHA1", 5),
          ("xformEspNULL", 6),
          ("xformEspDES", 7),
          ("xformEsp3DES", 8),
          ("xformEspAES128", 9),
          ("xformEspAES192", 10),
          ("xformEspAES256", 11),
          ("xformEspMD5", 12),
          ("xformEspSHA1", 13),
          ("xformCompLZS", 14),
          ("xformEspAESCtr128", 15),
          ("xformEspAESCtr192", 16),
          ("xformEspAESCtr256", 17),
          ("xformEspRc5", 18),
          ("xformEspIdea", 19),
          ("xformEspCast", 20),
          ("xformEspTwofish", 21),
          ("xformEspBlowfish", 22),
          ("xformEsp3idea", 23),
          ("xformEspRc4", 24),
          ("xformEspDesMac", 25),
          ("xformEspHmacSha256", 26),
          ("xformEspHmacSha384", 27),
          ("xformEspHmacSha512", 28),
          ("xformEspRipemd", 29),
          ("xformAHDesMac", 30),
          ("xformAHHmacSha256", 31),
          ("xformAHHmacSha384", 32),
          ("xformAHHmacSha512", 33),
          ("xformAHRipemd", 34),
          ("xformEspAESXCbcMac", 35),
          ("xformAHAESXCbcMac", 36))
    )



class CIPsecSecuritySuite(TextualConvention, Integer32):
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
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("suiteOther", 1),
          ("suiteConfEsp", 2),
          ("suiteIntegEsp", 3),
          ("suiteIntegAh", 4),
          ("suiteConfComp", 5),
          ("suiteIntegEspComp", 6),
          ("suiteIntegAhComp", 7),
          ("suiteConfAh", 8),
          ("suiteConfAhComp", 9),
          ("suiteIntegEspAh", 10),
          ("suiteIntegEspAhComp", 11),
          ("suiteConfIntegEsp", 12),
          ("suiteConfIntegEspComp", 13),
          ("suiteConfIntegEspAh", 14),
          ("suiteConfIntegEspAhComp", 15))
    )



class CIPsecNATTraversalMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("natEncapNone", 1),
          ("natEncapOther", 2),
          ("natEncapIPsecOverUdp", 3),
          ("natEncapIPsecOverTcp", 4),
          ("natEncapNATT", 5))
    )



class CIPsecEncryptAlgorithm(TextualConvention, Integer32):
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
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("other", 2),
          ("espDes", 3),
          ("esp3des", 4),
          ("espRc5", 5),
          ("espIdea", 6),
          ("espCast", 7),
          ("espTwofish", 8),
          ("espBlowfish", 9),
          ("esp3idea", 10),
          ("espRc4", 11),
          ("espNull", 12),
          ("espAes128", 13),
          ("espAes192", 14),
          ("espAes256", 15),
          ("espAesCtr128", 16),
          ("espAesCtr192", 17),
          ("espAesCtr256", 18))
    )



class CIPsecSpi(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "x"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 4294967295),
    )



class CIPsecAuthAlgorithm(TextualConvention, Integer32):
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
        *(("none", 1),
          ("other", 2),
          ("hmacMd5", 3),
          ("hmacSha", 4),
          ("desMac", 5),
          ("hmacSha256", 6),
          ("hmacSha384", 7),
          ("hmacSha512", 8),
          ("ripemd", 9))
    )



class CIPsecCompAlgorithm(TextualConvention, Integer32):
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
        *(("none", 1),
          ("other", 2),
          ("compOui", 3),
          ("compDeflate", 4),
          ("compLzs", 5),
          ("compLzjh", 6))
    )



class CIPsecEndPtType(TextualConvention, Integer32):
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("idIpv4Addr", 2),
          ("idIpv4AddrRange", 3),
          ("idIpv4AddrSubnet", 4),
          ("idFqdn", 5),
          ("idUserFqdn", 6),
          ("idIpv6Addr", 7),
          ("idIpv6AddrRange", 8),
          ("idIpv6AddrSubnet", 9),
          ("idDerAsn1Dn", 10),
          ("idDerAsn1Gn", 11),
          ("idKeyId", 12))
    )



class CIPsecPhase2SaDirection(TextualConvention, Integer32):
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
        *(("saDirectionUnknown", 1),
          ("saDirectionIn", 2),
          ("saDirectionOut", 3))
    )



class CIPsecPhase1TunnelIndex(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class CIPsecPhase1TunnelIndexOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class CIPsecPhase2TunnelIndex(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class CIPsecPmtu(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(68, 1500),
    )



class CIPsecLifetime(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 86400),
    )



class CIPsecLifesize(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2560, 4294967295),
    )



class CIPsecTunnelIdleTime(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 86400),
    )



class CIPsecNumCryptoMaps(TextualConvention, Gauge32):
    status = "current"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class CIPsecTunnelStatus(TextualConvention, Integer32):
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
        *(("initializePhase1", 1),
          ("awaitXauth", 2),
          ("awaitCommit", 3),
          ("active", 4),
          ("destroy", 5),
          ("rekey", 6))
    )



class CIPsecCryptomapType(TextualConvention, Integer32):
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
        *(("cryptomapTypeNONE", 1),
          ("cryptomapTypeMANUAL", 2),
          ("cryptomapTypeISAKMP", 3),
          ("cryptomapTypeCET", 4),
          ("cryptomapTypeDYNAMIC", 5),
          ("cryptomapTypeDYNAMICDISCOVERY", 6))
    )



class CIPsecCryptomapSetBindStatus(TextualConvention, Integer32):
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
        *(("unknown", 1),
          ("attached", 2),
          ("detached", 3))
    )



class CIPsecIkePRFAlgorithm(TextualConvention, Integer32):
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
        *(("none", 1),
          ("other", 2),
          ("prfHmacMd5", 3),
          ("prfHmacSha1", 4))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IPSEC-TC",
    **{"CCryptoMD5Hash": CCryptoMD5Hash,
       "CIKEIsakmpDoi": CIKEIsakmpDoi,
       "CIKELifetime": CIKELifetime,
       "CIKELifesize": CIKELifesize,
       "CIPsecEncryptionKeySize": CIPsecEncryptionKeySize,
       "CIPsecControlProtocol": CIPsecControlProtocol,
       "CIPsecProtocol": CIPsecProtocol,
       "CIPsecPhase1PeerIdentityType": CIPsecPhase1PeerIdentityType,
       "CIPsecIkeNegoMode": CIPsecIkeNegoMode,
       "CIPsecIkeHashAlgorithm": CIPsecIkeHashAlgorithm,
       "CIPsecIkeAuthMethod": CIPsecIkeAuthMethod,
       "CIPsecDiffHellmanGrp": CIPsecDiffHellmanGrp,
       "CIPsecEncapMode": CIPsecEncapMode,
       "CIPsecTransform": CIPsecTransform,
       "CIPsecSecuritySuite": CIPsecSecuritySuite,
       "CIPsecNATTraversalMode": CIPsecNATTraversalMode,
       "CIPsecEncryptAlgorithm": CIPsecEncryptAlgorithm,
       "CIPsecSpi": CIPsecSpi,
       "CIPsecAuthAlgorithm": CIPsecAuthAlgorithm,
       "CIPsecCompAlgorithm": CIPsecCompAlgorithm,
       "CIPsecEndPtType": CIPsecEndPtType,
       "CIPsecPhase2SaDirection": CIPsecPhase2SaDirection,
       "CIPsecPhase1TunnelIndex": CIPsecPhase1TunnelIndex,
       "CIPsecPhase1TunnelIndexOrZero": CIPsecPhase1TunnelIndexOrZero,
       "CIPsecPhase2TunnelIndex": CIPsecPhase2TunnelIndex,
       "CIPsecPmtu": CIPsecPmtu,
       "CIPsecLifetime": CIPsecLifetime,
       "CIPsecLifesize": CIPsecLifesize,
       "CIPsecTunnelIdleTime": CIPsecTunnelIdleTime,
       "CIPsecNumCryptoMaps": CIPsecNumCryptoMaps,
       "CIPsecTunnelStatus": CIPsecTunnelStatus,
       "CIPsecCryptomapType": CIPsecCryptomapType,
       "CIPsecCryptomapSetBindStatus": CIPsecCryptomapSetBindStatus,
       "CIPsecIkePRFAlgorithm": CIPsecIkePRFAlgorithm,
       "ciscoIPsecTc": ciscoIPsecTc}
)
