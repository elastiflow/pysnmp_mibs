# SNMP MIB module (CL-PW-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cablelabs_4491/CL-PW-TC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:37:34 2025
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

(clabProjDocsis,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjDocsis")

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

teaPwTcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 17)
)
if mibBuilder.loadTexts:
    teaPwTcMIB.setRevisions(
        ("2006-11-08 14:00",
         "2005-11-11 17:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TeaPwGroupID(TextualConvention, Unsigned32):
    status = "current"


class TeaPwIDType(TextualConvention, Unsigned32):
    status = "current"


class TeaPwIndexType(TextualConvention, Unsigned32):
    status = "current"


class TeaPwVlanCfg(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4097),
    )



class TeaPwOperStatusTC(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("dormant", 5),
          ("notPresent", 6),
          ("lowerLayerDown", 7))
    )



class TeaPwPsnTypeTC(TextualConvention, Integer32):
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
        *(("mpls", 1),
          ("l2tp", 2),
          ("ip", 3),
          ("mplsOverIp", 4),
          ("gre", 5),
          ("other", 6))
    )



class TeaPwTypeTC(TextualConvention, Integer32):
    status = "current"
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
              25)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("frameRelayDlci", 1),
          ("atmAal5SduVcc", 2),
          ("atmTransparent", 3),
          ("ethernetTagged", 4),
          ("ethernet", 5),
          ("hdlc", 6),
          ("ppp", 7),
          ("cem", 8),
          ("atmCellNto1Vcc", 9),
          ("atmCellNto1Vpc", 10),
          ("ipLayer2Transport", 11),
          ("atmCell1to1Vcc", 12),
          ("atmCell1to1Vpc", 13),
          ("atmAal5PduVcc", 14),
          ("frameRelayPortMode", 15),
          ("cep", 16),
          ("e1Satop", 17),
          ("t1Satop", 18),
          ("e3Satop", 19),
          ("t3Satop", 20),
          ("basicCesPsn", 21),
          ("basicTdmIp", 22),
          ("tdmCasCesPsn", 23),
          ("tdmCasTdmIp", 24),
          ("frDlci", 25))
    )



class TeaPwAttachmentIdentifierType(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class TeaPwCwStatusTC(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("waitingForNextMsg", 1),
          ("sentWrongBitErrorCode", 2),
          ("rxWithdrawWithWrongBitErrorCode", 3),
          ("illegalReceivedBit", 4),
          ("cwPresent", 5),
          ("cwNotPresent", 6),
          ("notYetKnown", 7))
    )



class TeaPwCapabilities(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        ("pwStatusIndication", 0)
    )


class TeaPwStatus(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("pwNotForwarding", 0),
          ("customerFacingPwRxFault", 1),
          ("customerFacingPwTxFault", 2),
          ("psnFacingPwRxFault", 3),
          ("psnFacingPwTxFault", 4))
    )


class TeaPwFragSize(TextualConvention, Unsigned32):
    status = "current"


class TeaPwFragStatus(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("noFrag", 0),
          ("cfgFragGreaterThanPsnMtu", 1),
          ("cfgFragButRemoteIncapable", 2),
          ("remoteFragCapable", 3),
          ("fragEnabled", 4))
    )


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CL-PW-TC-MIB",
    **{"TeaPwGroupID": TeaPwGroupID,
       "TeaPwIDType": TeaPwIDType,
       "TeaPwIndexType": TeaPwIndexType,
       "TeaPwVlanCfg": TeaPwVlanCfg,
       "TeaPwOperStatusTC": TeaPwOperStatusTC,
       "TeaPwPsnTypeTC": TeaPwPsnTypeTC,
       "TeaPwTypeTC": TeaPwTypeTC,
       "TeaPwAttachmentIdentifierType": TeaPwAttachmentIdentifierType,
       "TeaPwCwStatusTC": TeaPwCwStatusTC,
       "TeaPwCapabilities": TeaPwCapabilities,
       "TeaPwStatus": TeaPwStatus,
       "TeaPwFragSize": TeaPwFragSize,
       "TeaPwFragStatus": TeaPwFragStatus,
       "teaPwTcMIB": teaPwTcMIB}
)
